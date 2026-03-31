# MTZ_Transfer_Pricing_Aba_Exportacao

- **Fonte:** MTZ_Transfer_Pricing_Aba_Exportacao.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 272 KB

---

# Módulo \- Transfer Pricing \- Aba Exportação \- Lei 12\.715/12 – IN 1\.312/12

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

MFS\-651

Atualização Legal, implementação do Método PECEX de acordo com as regras estabelecidas pela IN 1\.312/12

Esse documento contempla as regras definidas para o Cálculo do Preço Praticado para atendimento a Lei 12\.715/12 e IN 1\.312/2012 do produto Transfer Pricing/Mastersaf\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Link: __Res\. Exportações:__

Nesta opção: “__Res\. Exportações__” \(disponível no lado esquerdo superior da Aba Exportações\), o sistema deve possibilitar a demonstração, por Produto, dos métodos de cálculos processados, os valores de:  
   
__Exposição Fiscal__ \- Diferença entre o Preço Parâmetro e o Preço Praticado\.Quantidade Vendida \- Quantidade vendida do produto, para clientes não vinculados, de acordo com os Documentos Fiscais\.   
__Custo de Aquisição__ \- É a média aritmética ponderada dos preços pelos quais a empresa efetivamente comprou ou vendeu um determinado produto, durante o ano\-calendário\. É calculado, obrigatoriamente, produto a produto\.   
__Preço Parâmetro__ \- É a média aritmética ponderada de preços praticados em operações entre empresas independentes coletados e ajustados, conforme método definido em lei, escolhido pelo contribuinte\. Também deve ser calculado, produto a produto\.

Ao clicar neste link, devera aparecer uma tela inicial, e constará uma linha com as seguintes informações:

__Resumo de Cálculo de Preços de Transferência de Exportações__

__Ano de referência__: __2011__

Ambas deverão estar em “negrito” e o ano “2011” esta citado apenas como exemplo, pois no sistema devera ser processado o ano definido para o cálculo disponível na Aba Cadastros 🡪 Define ano de referência\.

 

__Nesta tela também deverá conter os seguintes Campos/CheckBox/ComboBox/Botões:__

Empresa  
Pesquisar

Fechar Ano de Referencia

Total de Exposição Fiscal em função dos métodos de Exportações

Ações

Empresa

Exposição Fiscal dos Métodos Selecionados

Data

OS3645

__RN01__

Parâmetro “__Empresa__”: Este parâmetro foi desenvolvido com as seguintes opções de filtro, para possibilitar ao usuário a visualização dos resultados somente para uma empresa específica a que foi submetido o cálculo do Transfer Pricing\.

Campo “__CNPJ”: __Se preenchido, o usuário poderá pesquisar a empresa a qual deseja visualizar os resultados dos cálculos\.__ __

Campo “__Razão Social__”: Se preenchido, o usuário poderá pesquisar a empresa a qual deseja visualizar os resultados dos cálculos\.

Campo “__Pesquisar__”\. Ao clicar neste campo, o sistema retorna os dados referente aos campos acima se preenchidos\.

Caso nenhum dos campos deste parâmetro tenha sido preenchido, o sistema possibilitará a visualização dos resultados para todas as empresas previamente cadastradas, as quais tenha sido submetido o cálculo do Transfer Pricing\.

OS3645

__RN02__

Campo “__Fechar Ano de Referência__”: Neste campo, o sistema disponibiliza a possibilidade de executar o encerramento dos Cálculos de Preços de Transferência, com o objetivo de "fechar" o ano em que foi realizado o cálculo, não permitindo que usuários alterem dados e realizem novos cálculos\.

OS3645

__RN03__

Linha “__Total de Exposição Fiscal em função dos métodos de Exportações__” Nesta linha o sistema informa o resultado em  Reais \(R$\) da exposição fiscal somados todos os produtos a que foram submetidos o cálculo do Transfer Pricing\.

OS3645

__RN04__

Coluna “__Ações__”: Nesta opção o sistema disponibiliza a lista para pesquisa através do ícone \(Lupa\) a possibilidade de visualizar os resultados no detalhe dos cálculos a que foram submetidos os produtos, conforme citado na RN00\.

OS3645

__RN05__

Coluna “__Empresa__”: Lista das empresas previamente cadastradas as quais foram submetidos os cálculos de Transfer Pricing

OS3645

__RN06__

Coluna “__Exposição Fiscal dos Métodos Selecionados__” Lista contendo os resultados em Reais \(R$\) por empresa da exposição fiscal somados todos os produtos a que foram submetidos o cálculo do Transfer Pricing\.

OS3645

__RN07__

Coluna “__Data__”: Lista de informação da data e hora que foi processado o cálculo do Transfer Pricing por empresa

OS3645

__RN08__

__Regra para visualização e analise do Cálculo detalhado\.__

 A visualização dos resultados do cálculo no detalhe, é disponibilizado através do ícone \(Lupa\) da coluna “__Ações__”, conforme “__RN04__”\. 

Através desta opção, o sistema disponibilizará uma nova tela contendo os seguintes __Campos/CheckBox/ComboBox/Botões__:

Pesquisar

Empresa

Produto

Método 

Mostrar apenas produtos com exposição Fiscal

Mostrar apenas os métodos selecionados \(menor Exposição Fiscal\)

Mostrar apenas Produtos com crítica de cálculos

OS3645

__RN09__

Botão: “__Pesquisar__” A finalidade este campo é para que o sistema retorne as informações de acordo com as opções definidas a partir da “__RN10__” até a “__RN15__”\.

Caso o usuário clique nesta opção sem aderir nenhuma das opções citadas nas RNs 10 á 15, o sistema ira disponibilizar as informações dos resultados de todos os produtos que foram submetidos ao calculo do Transfer Pricing\. 

OS3645

__RN10__

Parâmetro “__Empresa__”: Este parâmetro foi desenvolvido com as seguintes opções de filtro, para possibilitar ao usuário a visualização dos resultados somente para uma empresa específica a que foi submetido o cálculo do Transfer Pricing\.

Campo “__CNPJ”: __Se preenchido, o usuário poderá pesquisar a empresa a qual deseja visualizar os resultados dos cálculos\.__ __

Campo “__Razão Social__”: Este campo já retornará preenchido, devido o usuário já ter selecionado e empresa na tela anterior através do ícone \(Lupa\) da tela anterior\.

Campo “__Pesquisar__”\. Ao clicar neste campo, o sistema retorna os dados referente ao preenchimento do campo “__CNPJ__”\.\.

OS3645

__RN11__

Parâmetro “__Produto__”: Campo desenvolvido para identificar o produto que o usuário deseja ver os resultados calculados, a ser consultado na seguinte composição, e possibilidades de filtros:

Campo: “Empresa ou estabelecimento” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

Campo: “Código”   
  
Se preenchido: O sistema deverá possibilitar a visualização dos cálculos somente do Produto que contém o código informado\.

  
Campo: “Descrição” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

OS3645

__RN12__

Lista de opções “__Método__”: Através desta opção, o sistema disponibiliza ao usuário a visualização do resultado de um método específico, podendo ser:

- Todos\(as\)
- CAP
- Pvex
- PVA
- PVV
- PCEX
- Produtos com operações de entrada/saída de vinculadas que não foram marcados

MFS\-651

__RN13__

Aba __Exportações__:

Criação dos Links \(menus\) com o título “__PECEX__” e com as seguintes descrições:

__“Notas Fiscais”__

__“Produtos Similares”__

__“Cotação em Bolsa”__

MFS\-651

__RN14__

Ao clicar na “lupa” em ações, nesta tela o sistema também disponibiliza a visualização referente o método utilizado no cálculo da seguinte maneira:

__Calcular utilizando os métodos \(Exportação\): __Esta linha estará destacada em “negrito” e sua finalidade é apenas como título da tela\.

Calcula CAP

Calcula PVEx

Calcula PVA

Calcula PVV

Calcula PECEX

Esta informação é ilustrada através de um ChekBox, em que vem “flegado” como default o método utilizado durante o processo de cálculo definido pelo usuário\.

MFS\-651

__RN15__

__No Link \(menu\) “Notas Fiscais” deverá conter os seguintes Campos/CheckBox/ComboBox/Botões:__

__Deverá seguir o mesmo padrão da tela de notas fiscais dos métodos existentes\. Ex: CAP >> Notas Fiscais__

MFS\-651

__RN16__

__Adicionar: __Quando selecionado o usuário será direcionado para tela de parametrização de “Ajustes por Diferença de Condições de Negócios em Notas Fiscais”

MFS\-651

__RN17__

__Detalhe de ajustes por Diferença de Condições de Negócios em Notas Fiscais__

\*Os campos deverão seguir o mesmo padrão de telas existentes\. Ex: Detalhe de ajustes por Diferença de Condições de Negócios em Notas Fiscais\. \(Aba Exportações, Menu Notas Fiscais\)

Para cada registro \(diário\) deverá existir um __*Sub\-Menu *__para inserção dos dados pertinentes aos ajustes permitimos pela IN 1\.312/12, os campos são:

__Item\(0 para todo o documento\);__

__Diferença por;__

__Valor da diferença; __

__Indicador Econômico; __

__Documento;__

__Tipo; __

__Data de emissão;__

MFS\-651

__RN18__

__“Item\(0 para todo o documento\)” – __ informar o número do item do Documento Fiscal para o qual se está realizando este ajuste\. Caso o ajuste de valor deva se refletir para toda a nota fiscal, independente do item, deve\-se informar 0 \(Zero\)\.

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN19__

“__Diferença por__” – selecionar o tipo de situação diferenciada, que cabe ajuste de valores, no qual se enquadra este documento fiscal, se por: 

- Prazo de Pagamento; 
- Quantidades negociadas; 
- Influências Climáticas 
- Obrigação por Garantia de Funcionalidade ou Aplicabilidade
- Obrigação pela Promoção
- Obrigação de Fiscalização de Qualidade e Higiene
- Custos de Intermediação de Compra e Venda
- Acondicionamento; 
- Valor do Prêmio;
- Frete; 
- Seguro;
- Variação de Commodities 
- Risco de Crédito
- Similaridade

Prazo de Pagamento será apresentado como default

Os dados pertinentes aos ajustes citados acima, deverão ser excluídos/adicionados no resultado de apuração do preço parâmetro do método PECEX\.

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN20__

“__Valor da diferença__” – Informar o valor da diferença de preço\.

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN21__

“__Indicador Econômico__” \- Informar o indicador econômico\. Ex: Taxa SELIC

MFS\-651

__RN22__

“__Documento__” – Informar o documento de comprovação do ajuste realizado

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN23__

“__Tipo__” – Informar o tipo de documento de comprovação

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN24__

“__Data de emissão__” – Informar a data de emissão do documento comprobatório

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN25__

__No Link \(menu\) “Produtos Similares” deverá conter os seguintes Campos/CheckBox/ComboBox/Botões:__

__Deverá seguir o mesmo padrão da tela de “Produtos Similares” dos métodos existentes\. Ex: PVex >> Produtos Similares__

MFS\-651

__RN26__

__No Link \(menu\) “Cotação em Bolsa – Commodities” deverá conter os seguintes Campos/CheckBox/ComboBox/Botões:__

No menu: Exportações >> PECEX \(Criação de Link com as seguintes descrição\):

__Cotação em Bolsa – Commodities__

\*Os campos deverão seguir o mesmo padrão de telas existentes\.

Para atendimento à IN 1312/12 deverá ser criada uma nova tela para inserção, visualização e edição das informações pertinentes aos valores de cotação de commodities contendo os seguintes campos:

__Produto__

__Data__

MFS\-651

__RN27__

Parâmetro “__Produto__”: Visualizar a cotação do produto a ser consultado na seguinte composição, e possibilidades de filtros:

Campo: “Empresa ou estabelecimento” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

Campo: “Código”   
  
Se preenchido: O sistema deverá possibilitar a visualização somente o custo do Produto que contém o código informado, previamente cadastrado/Integrado que poderá ser utilizado como filtro\.

  
Campo: “Descrição” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

MFS\-651

__RN28__

Para o parâmetro “__Data”: __Validade do período em se compões o Produto\.

Opção para obter a visualização das datas de validades da composição do Produto Acabado previamente cadastrados/interados através do preenchimento do ComboBox “Período”:

Se o ComboBox “Período” não estiver preenchido, o sistema deverá possibilitar a visualização de todas os componentes previamente cadastrados/integrados que poderão ser utilizadas como filtro\.

Se o ComboBox “Período” estiver preenchido com as opções do título “Corrente”, o sistema deverá preencher automaticamente os campos “De” e “a” de acordo com as respectivas opões “Semana Corrente”, “Mês Corrente”, “Trimestre Corrente”, “Semestre Corrente”, e “Ano Corrente”, e possibilitar a visualização somente dos componentes cadastrados/Integrados que poderão ser utilizadas como filtro\.

Se o ComboBox “Período” estiver preenchido com as opções do título “Passada”, o sistema deverá preencher automaticamente os campos “De” e “a” de acordo com as respectivas opões “Semana Passada”, “Mês Passado”, “Trimestre Passado” “Semestre Passado”, e “Ano Passado”, e possibilitar a visualização somente dos componentes previamente cadastrados/Integrados que poderão ser utilizadas como filtro\.

Se o ComboBox “Período” estiver preenchido com as opções do título “Próximo”, o sistema deverá preencher automaticamente os campos “De” e “a” de acordo com as respectivas datas “Próxima Semana”, “ Próximo Mês”, “Próximo Trimestre ”, “Próximo Semestre”, e “Próximo Ano”, e possibilitar a visualização somente dos componentes previamente cadastrados/Integrados que poderão ser utilizadas como filtro\.

Opção para obter a visualização dos componentes previamente cadastrados/integrados através do preenchimento dos campos “De” e “a”:

Este campo devera ser preenchido somente quando o usuário não optar por nenhuma das opções de preenchimento do ComboBox “Período”

Se o usuário digitar um período nos campos “De” e “a”, ex: dd/mm/aaaa, o sistema deverá possibilitar a visualização dos componentes previamente cadastrados/integrados somente do período escolhido que será utilizado como filtro\.

MFS\-651

__RN29__

Para o botão “__Filtrar__” o sistema deverá trazer somente as cotações de acordo com os filtros utilizados\. Caso não seja utilizado nenhum filtro o sistema ira carregar todas as cotações previamente cadastras/integradas no sistema\.

MFS\-651

__RN30__

__Botão Adicionar: __Quando selecionado o usuário será direcionado para tela de parametrização de Detalhes de Cotação de Commodities\.

MFS\-651

__RN31__

__Detalhes de Cotação de Commodities__

\*Os campos deverão seguir o mesmo padrão de telas existentes\.

Para cada registro \(por produto\) deverá existir um __*Sub\-Menu *__para inserção dos dados correspondentes aos valores de cotação e moeda, os campos são:

__Produto__

__Data__

__Preço__

__Moeda__

__Unidade__

MFS\-651

__RN32__

“__Produto__”: Visualizar o detalhe do preço do produto a ser consultado na seguinte composição, e possibilidades de filtros:

Campo: “Empresa ou estabelecimento” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

Campo: “Código”   
  
Se preenchido: O sistema deverá possibilitar a visualização somente o custo do Produto que contém o código informado, previamente cadastrado/Integrado que poderá ser utilizado como filtro\.

  
Campo: “Descrição” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN33__

__“Data”: __Informar a data para inclusão dos dados de detalhe de preços\.

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN34__

__“Preço”: __Informar o preço obtido através de instituição de pesquisa para inclusão dos dados de detalhe de preços\. 

MFS\-651

__RN35__

“__Moeda__”: Serão listadas as moedas, conforme cadastro na Aba “Cadastro” menu “Moedas”

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN36__

“__Unidade__”: Serão listadas as unidades, conforme cadastro na Aba “Cadastro” menu “Unidade”

MFS\-651

__RN37__

No menu: Exportações >> Res\. Exportações \(Ao selecionar o resultado de cálculo para um produto controlado pelo __PECEX e clicar na lupa existente no lado esquerdo da tela__\):

Deve\-se apresentar o resultado somente do produto em análise a exemplo do que já ocorre com os demais métodos;

MFS\-651

__RN40__

No menu: Exportações >> Res\. Exportações \(Ao selecionar o resultado de cálculo para um produto controlado pelo __PECEX e clicar na lupa existente ao lado da informação “Operação Sujeita a Arbitramento Artigo 14”__\):

Deve\-se apresentar o resultado de apuração da operação, respeitando as regras a seguir:

__Regra para verificação da Operação Sujeita a Arbitramento:__

Nesta opção, o sistema deverá disponibilizar as seguintes informações para visualização e análise do usuário:

__Detalhes do Cálculo do Artigo 14 IN 243 \(Operação Sujeita a Arbitramento\)__

__Ano de referência: 2013__

Ambas deverão estar em “negrito” e o ano “2013” esta citado apenas como exemplo, pois no sistema deverá apresentar o ano definido para o cálculo disponível na Aba Cadastros 🡪 Define ano de referência\.

Na mesma tela, o sistema deverá disponibilizar as informações abaixo, em que serão apresentadas apenas como cabeçalho, para o usuário identificar o processo calculado detalhadamente:

“__Cód Empresa__”: Código da empresa definido pelo usuário no cadastro\.

“__Empresa__”: Nome da empresa cadastrada para cálculo do Transfer Pricing

“__Código do produto__”: Código do produto ao qual o usuário pretende visualizar o cálculo detalhado\.

“__Produto__”: Descrição do produto\.

“__Unidade__”: Código da unidade do produto definida pelo usuário no cadastro\.

Operação Sujeita a Arbitramento __SIM__

Operação sujeita a Arbitramento = SE Preço Médio de Venda no Mercado Externo Vinculado < 90% do Preço Médio de Venda no Mercado Interno \(deverá ser aplicado os métodos de cálculo\), caso a empresa não tenha sido dispensada no teste de Safe Harbour

Abaixo, o sistema devera disponibilizar a visualização dos valores das seguintes informações do cálculo que foram executadas através da Aba “__Processar Cálculo__”, conforme as RNs descritas no documento “do documento__ __“__MTZ \-  Transfer Pricing \- Operacao Sujeita ao Arbitramento\.docx”\. __

![](data:image/png;base64,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)

MFS\-651

__RN38__

No menu: Exportações >> Res\. Exportações \(Ao selecionar o resultado de cálculo para um produto controlado pelo __PECEX e clicar na lupa existente ao lado da informação “preço praticado”__\):

Deve\-se apresentar o resultado de apuração do preço praticado, respeitando as regras a seguir:

__Regra para verificação do Preço Praticado:__

Nesta opção, o sistema deverá disponibilizar as seguintes informações para visualização e análise do usuário:

__Detalhes do cálculo __

__Ano de referência: 2013__

Ambas deverão estar em “negrito” e o ano “2013” esta citado apenas como exemplo, pois no sistema deverá apresentar o ano definido para o cálculo disponível na Aba Cadastros 🡪 Define ano de referência\.

Na mesma tela, o sistema deverá disponibilizar as informações abaixo, em que serão apresentadas apenas como cabeçalho, para o usuário identificar o processo calculado detalhadamente:

“__Cód Empresa__”: Código da empresa definido pelo usuário no cadastro\.

“__Empresa__”: Nome da empresa cadastrada para cálculo do Transfer Pricing

“__Código do produto__”: Código do produto ao qual o usuário pretende visualizar o cálculo detalhado\.

“__Produto__”: Descrição do produto\.

“__Unidade__”: Código da unidade do produto definida pelo usuário no cadastro\.

“__Detalhe de__”: Preço Praticado

Abaixo, o sistema devera disponibilizar a visualização dos valores das seguintes informações do cálculo que foram executadas através da Aba “__Processar Cálculo__”, conforme as RNs descritas no documento “do documento__ __“__MTZ \- Transfer Pricing \- Preço Praticado \- Método PECEX\.docx__”__\.__ :

![](data:image/png;base64,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)

MFS\-651

__RN39__

No menu: Exportações >> Res\. Exportações \(Ao selecionar o resultado de cálculo para um produto controlado pelo __PECEX e clicar na lupa existente ao lado da informação “preço parâmetro”__\):

Deve\-se apresentar o resultado de apuração do preço parâmetro, respeitando as regras a seguir:

__Regra para verificação do Preço Parâmetro:__

Nesta opção, o sistema deverá disponibilizar as seguintes informações para visualização e análise do usuário:

__Detalhes do cálculo __

__Ano de referência: 2013__

Ambas deverão estar em “negrito” e o ano “2013” esta citado apenas como exemplo, pois no sistema deverá apresentar o ano definido para o cálculo disponível na Aba Cadastros 🡪 Define ano de referência\.

Na mesma tela, o sistema deverá disponibilizar as informações abaixo, em que serão apresentadas apenas como cabeçalho, para o usuário identificar o processo calculado detalhadamente:

“__Cód Empresa__”: Código da empresa definido pelo usuário no cadastro\.

“__Empresa__”: Nome da empresa cadastrada para cálculo do Transfer Pricing

“__Código do produto__”: Código do produto ao qual o usuário pretende visualizar o cálculo detalhado\.

“__Produto__”: Descrição do produto\.

“__Unidade__”: Código da unidade do produto definida pelo usuário no cadastro\.

“__Método__”: PECEX

Na sequência da mesma tela, o sistema devera disponibilizar a linha: __Resultado proveniente de: __

Abaixo, o sistema devera disponibilizar a visualização dos valores das seguintes informações do cálculo que foram executadas através da Aba “__Processar Cálculo__”, conforme as RNs descritas no documento “do documento__ __“__MTZ \- Transfer Pricing \- Preço Parâmetro \- Método PECEX\.docx__”__\.__ :

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAboAAAEtCAIAAADx9jIpAAAAAXNSR0IArs4c6QAAAAlwSFlzAAAOwwAADsQBiC4+owAAPBJJREFUeF7tnc1qHUmWx2/NE7RfoUzZwyBoBJoXMBiKarQpgWAGtKryyqCCrsUgEAwNBjOLKrDAK3etBDMgUG9EFwUCv8AIRINoRm7sV1C9Qc2Jz4zIPJFxIr9u3rz/XHS77o2PE/+IPHki8ur8Pvvtt99WuKAAFIACUCCnwD/lCnT+/udvP/v25+La3WoVd9OjwpQWTtlXD0lQFQpshwLGXf7jx3/9zF//+uM/hhw7tT1wi0NaV97WV3/+7c9fFVVbmgJFg0dhKLAcBXx0uffDB9qX0/Xh3/7nSYewcDmSYCRQAApAAU6B5mb8i3/+fVAwiDt9jEhbRHeZz8I9Y23/+I8f//37m5vvn1AF5YOjMLZyylWLf/jJdx50w7lv1dG3zhJnmw7kfjSf6kqNRpQFQXP0va3LjJTtIhigqEpNgUgDPuxm1eAmIppQVWBRYTxuWCgwNwWa7vLnv/y09y9fGDt//vbJ3/9kgk4Vdf67co4/f/uH1V/tZ3/9/d8zG/cv/vjfP+yZyFVtYb/44//aqr99+OFvfzB+i1r8m4tt//qN6Zlu/uDD1R9YR/DT6mvT2l9//722TV033//dfPrnr7hGvvjjn7756S/uUJUG+82f/kij5UaqWnNdfPhh9f1/xUexwio1BVK1gqdEU42keXNbTrAHCixaAeMKf9jzg/zG+ULyQtZ3Rd/ZskExVc7/p/+3+weV9xt95dnCNnWtsLb/j+jDuIhz1UGnqoDuJO4s0YgrHJRmRxp161t2jcqrhEbxtdwjpEWNeBGG6geVq0eRm89QeqYgPoICUECuQO3sku7sn/4zfNUT35dBgPj1X6odr/h5QtvMIDStO2NxM2zB3/+zDYmzzXz1HyZU/Pm/vl/9276r1RxptqEOVajNCWpVQfz/qtAZFxSAAkMoUNuM031GG1v3querr7/5yW6Yzf6YNs/mf1crekGsorO//Z/ZA7v/p91t06ybYMv+zdf2tbIv+cW/7PndcfSh89v/+PE/q/MBdtDhAUJQQLXMNWI25N+6jbgaDTPSjLxFVbwC2VqsGtlaZnpwdjnELYE2oEBSAbcZD3ZtZrttgqBwm24+Cj9xlarPvvnG7ZGrnbDdgLqdtzWlKhk0GXwYdsTtPZu7emNcvP0MrI0a0bWjT5ojbd+Ms+LwVdwJRErSeDPAiclNRG0Loaph6y3fV6EkFChW4DOqsZkPE9rY/+Xr0p9AbuZQYTUUgAJzUGC8v+qZw+hgAxSAAlBgMAU2N7ocTAI0BAWgABSQKIDoUqISykABKAAFVnCXWARQAApAAZECcJcimVAICkABKPDZw8MDVIACUGBzFfjd735Hxv/666/jDWGCLsYzvn/LZvh0IbrsLyZagAJQYCsUgLvcimnGIKEAFOivANxlfw3RAhSAAluhQOAur48fPXr29mPLsFWJ4+v+ulA7QzTDG/Lx7TN2GL7TQXpvNpLql6zs1mO3Wv1nJ9WCmn0z/x/fHreuk/FsQMtQYJ0KeHd5fXx49+rm/cvH3prq9nAfPT97uFgdMp6OubNHudm1SUH/9f9Wd/KLy4NoGA11aRRnz0WaKw8YXOGzpN5Ia7/yHkVmpR8TobXpBxINq/2xyHXw8e3V05sHNf+PHu3d7wfrpIfNqAoFGAXaFqjxSu5y67i6U6uVzZcMu+NqkQdxNz1zk1h3+fHt6/Ojk+geuL46P7q4ODq/isLJ59+9unvdCC2e7x+dR5/q9vZlTqlsxezu+v6pk7vd3bj645fvQ5df1jZTevcV+Qh7ndzvJcPvofstNJyWxh49JrypDzfcNBU2GhV//PJMLQ/y/HQJHzd9+kPdrVRAO6u909u2wR9d+HVu7nWKVU53zIcXO6cvKvfUKBk7S6ZWsilT07jLj79c3ta8m/KW+8+VH4z95eMvD1aXv9S37ORFw0+pvdWr75S3jAI0Pi51Twr3rX62vDUPkWaNnZOTndM3yoVTJ+o/vAJBV9wj5vDclgzi3uABJDgdUMG1mw3fCDvA2hBKeqxM8gbnNKTNfn1nsKrcd32MakHc3p7u+Y11EEFXItTFTNhQJuBWOgAMukQBWrcP9KyvBUHtLVTehh7nsSNqqcjWyjVl3OWn+5q3VIGb9neNuHH1+MnO7f2nuh2RF1WdHnypt/V6+OaigKe2kad7UN3n5mva5nkvd3t6v68/5MIY68Kv31weaI9sruvjvfsT19PBpXnEGD9i2z+q2ZzsvUVj6rs2+NQAuSHke2QNbtVQPTc+3O1aueumMz0+fvnu1a4JmpW6bOMkpo9VL3bUbHPF8sMpuVFQdggF4h1oIuQYoqM1tnFO50GykclLCofDvxkP/J3UXQf+8vrNqfOW2mXZwTVDbOWl/QlA6Il2TWiauPSBwLPXd6GLoGB45cWhnrRTUxFyfMIQtpjsXShd5ai5AXJDyPaYMrhFw3Zjsz2yExSZ8fzMPLOaNkgaL9QSxXsqYA5LomtZJyfVAJvhV6ydvKRcc9Zdqr252a7RpXxPc/fd7OHxS7tLDm82uscOV+6o4aIe38nNjEuqrm536o4wOKgY7XjNHFEE1owzwGi42S5UvC+ZIU7ubOOmkrBY1wlFvaEU2Ibo0mpFAdru3Ye2X/I4UeUlc9Ng3OXnT3eDI0oVHQZvOGgXvTKnhfpSW7+nn3Ptml1y3aN496ICwPhS3bo3ROrlUKJdpq/Gu2bVd7XVp22iOoYLhzVA78pnmCOK6GoZYOl4UwZnulA7gNO9+EXe9bH675TC4YlCs/GwFnlKc6LZXqxs+nKrEt93VWCR0aV6BthjdbcalSOioG7nCR35qY2tc1DVzpYraR78pi22Ft9UNRnGXSr36/1lY0dIwVz1wifYpzemVPuswzD+en6mf3mir6tVPbqkA7Gbg0sTxe7Ru60+77Sfn6ng3G+Ld1QMqI7p3Gcde/dBNrX8mn5JUzexfYA1hbLjZQ0WdKFOFr2SRoPDlYq+2R71fCqpaNmwjYe16AlBD8dssb7T19U9oN6yFHBvxvV9x/yS5/On1U1Ox+vmoCG4bSieeWd+4MOWVOdz7piMrcV+WEnsU2yQ1yV3kHVYVOxqHz8kWdYaTY+GVu+bJ++Xdfq1uLmbIP/FBF1MMi20nl+s3mW9XN2WZooNih926hu6ei1zgoWbZ5KZXXMn5pdD9IK87aXbmm1E91CgTIFP98FL6LKqujQSuHUQDVWgwIwUmCD0m6CLGQnaMAUJ3OY8O7ANCkCBOSoAtNkcZwU2QQEoMEMFkMBthpMCk6AAFJijAji7nOOswCYoIFdggoPFCbqQj3f6kji7nF5z9AgFoMBmK4DN+GbPH6yHAlBgMgXgLieTGh1BASiw2QqMD59Qv3cWJJPcGBkHSRM/SCOxZOZ35QVKj2DDxkziog1VfxYtTZefSFwe/JX2oqUqHRwLn0hBF5LwCderyYcS37Lq75lL/hCoExqhdNhhecZtzMiTxHOR9IYGfhElDc1pMgkSI2cEvh9aASZXdLoLykjRyOylSmfv9KGtHqO9VoyE6nA4+EQAXYjyufPwCTtYnlcxhhJDtjkhOaOb2dVchCmU47Zs9nRa5sV/ENvNKNSapQIMRUbZmXj+N/IRBmNqvdNnOfb6bitBpHDFWM5EV/hE2HeYq5uHT+jSDK/Cpt8zQVE4Z9W/gwx9tIOooREiegW3wVDtHLsExCzWKM+0mIycUQ3VgyWCtLuCnbRLodzgczDgjboyvnOnUjAdwRwU7OY34J7ZNhMZikyLBG3e0mQ465pGdf265zASKv+bBeQEyIpcrQR8YhUkLjs811nl3MXDJ5RfY3gVKv1ea1Zg2jpU6YMJc1BDI7BIidpcnK8MqMKDdIqZFtOQMziwRBm/IQTGhXCLlEpOGZWwdI8SSRkESJi81G5JeATI+tc8LChUoEGRaat/fcVkbw0qpO70QpuWVDz1ZjwkIN48fZ1/hdCBV6F0VJloKfWijmkc5qDSl0VK1OX3eWtV7KUeh+VMiynIGSxYQsRvqBLb+wx/q1UAt0iq5JShde+z+6p/x5fIhiWt+e0Zi9900G6mzq1R4Y3Ht2SP+bZHs9aRSn5IJMnd3olXQZZZZNb+VYpVVIiUiAJh+RxPSM6QG+VKVo+u5LlkoUrlNqDGJirggXS0w/NLxLx3jdN8V+Q6HH23TTQHn6iXp9dnJsu7vlj4RDuvomrQsTUcCsJSIjS+mnCZ9muPRmCREsnhqEzJCovRiWkxOjmDBUt0MrUuQJlKDfkGsWETnckCbY4pMi0D1NRpk3Y8eaUxMxugXAojMTh8QmsRQhfU6aL/KRALn2jnVThxDVImAlHQoMJk8ipvfIhGIDfaRErU58rvMshO/WzMMh7Y2R6bnMGCJbqZ2vCXApXSK3wYGzbgDtoCEyOKTMt41Q+IIkQfU7YNM7MBUvIYidnDJzrmexdOCGAYQqFQbLEKxPkvJBQZyV0TlVlKio2OzmgS+ITlF/A/hF3s4sXAoMA6FZBQZLJ/obBUzAzgE+tcmugbCqxfgQlCvwm6WL+OaQuQwG3OswPboAAUmKMCgE/McVZgExSAAjNUQPK7yxmaDZOgABSAAlMrAPjE1IqjPygwrAITHCxO0MWwmgzbGs4uh9UTrUEBKLB8BbAZX/4cY4RQAAoMogDc5SAyohEoAAWWr0ARfILk6JSVfmn8iQGXxYzytg84KjS1TgUAnxhNfRY+oXurEShsCrdsVvqN5E/URzvHHLlCCsVoK6W94cmRIWsa5/y7BXzCzVE2K91g8AlyenuK/eIvynTx+u1HbcgC+RN6XBLGw3rvlvlbuF590LtK0n1+1Ew1BPiEdV7BEhkMPsE8oCwLRve2QP5EfKMlGA9RfGcCUB4Cl2U5sBQKBiCRvP8DC3WGp1q20JylLnrOAipY+EcT+NFAhmQVgGcbRQHAJ3xoybElQs0Hg0+oPHc+zzI3qwvkT0RCqie0TW8VMh6qHKqUm/PuUPmc6iOF2NCP9TxPgqNQ0KHw3v2JDeZvDi5fNJ+G0YPRWsiYpM6Xq52BJ3+wJanJdkCFBGvx5ppkePdq18S+lOkvr8AorgKNrjRIIJeYzesE+ETxkhnyzfhG8yeCFJ/K2bj8ngHjgbT1QdPe6W3sYJ8p3I2ulGU5sBQKEWaDo1A0TWLbTxrfCqjIYy2+PHA5nSs9sgoUr1JU6KYA4BPddEvW4tylCh47IOA2nD8RnF3yCfhNUisbAAa8NlqTysH2ztqfB0g0KBQpk5rTLS9Zq5u3auAVieaGUwDwieG01C2x8AmT9jzm1F4fV/+9UP5EXlq/0XHwDL3zPd0xWdzNlWU5sBSKzgCJpklh+zRTflSM8bkRF1nlkSFZBXLd4vuuCgA+4ZSbEj6hnkp0gGZAEeY6XPn3bYvlT7QvUsq7uiJoZQTPUC8i6fzPfax+bZVlObAUChFmo2EfZ5I+SHREjxeXtg5bMn9TSuAfupUQGZJVIN8vSnRTAPAJr9ss4BNkjSRzfTzZHVO+C1dMuT3ChhdQTEIiWMAwt3sIgE+I57+jJ+oGnzC+kg7wPOgsZyf4EzmFRvg++BmRo72N0AuanKcCgE+0zAvgE/NctLAKCkylwATZ1SboYiq1uvSDBG5dVEMdKAAFtlkBwCe2efYxdigABQoUGPJn6gXdoigUgAJQYNMUAHxi02YM9kKBWIEJDhYn6GLOs4qzyznPDmyDAlBgjgpgMz7HWYFNUAAKzFABuMsZTgpMggJQYI4KAD4x5aywWVrl/Al5ySkHVetLbqS85BqHs4FdAz4x2qSx8Ak+6a22YanwCTU2Jqluf90jKgOpJ/6DqP5dRy3oRG9VlpTxXNUaxziwZJvZHOATbt6mg08E2cweHk7u94IbbaHwiRpuQ2XTmCOxp88tfHS0c9qedrhP66g7BwUAn6ic5QtKFabzLV6w634w+ERt3lVEGXa4QPiEXmVhGjb6y9ujc0MnCgMx/282Es1SGYKmGP5EIroVkyoC4kOcfM/N575KzEfJz+OLhV6kxtcKutC9tksUpFh+dEjJnPTFDzw7nDm4p5nZAPiE95aTwSeYJeDYMOar5cEnmKT98ZDrmkhYDg0qQ9UIy59IkCRUnnaTlNjnJOaYENRklbx45/4TdyPrNGsOUWcKsHgJDl/BIyWiknGv8uFwJSXDmZmvmoE5gE+MOwlDvhnfcPhEodA8iMKzHDgqg+9BzoeQkypUZljKu6lPEJ6fpY5IdebnIMBk8RJspyxSIirZ6LUPGEM2nMI527bigE8MPONCd6luixwyaZPhE0wWahry7tPPE3J3Zjm0TF9Rm00mhA3R9q9qVMhajzbA/FB9PBJeQj4ctqRwOAPfDgtrDvCJgSeUhU/U+lDL+e7Vd4rbZa7lwSdMMvDgxI/2ggGv+e6DQaxXzAnCPrrHR/ghOzueyuC/ZfkT9G07ScJ3xDEhKJCwgeUDcSqbvLHKMp0Q8dSeG7J4CRZfwSIlwg9pX197OSYcDjdw+XAGviE2uznAJ9z8TQmfCLCIFKu8fnrzEIK7FgmfMO+zPG5DjdluaA25KGJO0G63CaLgb7SQyuBLsPyJLEniakVwXn0xTAhaHo448YhIa+8qeFDTLhrRrvuUw0uw+AoWKRF+SM/UMBqXD4crWTKczfZwg1oP+AR3j1Gw5+4HtWe0kR9Lp+CRFb5Rn2JDjikohz10TPkuXEjl9mQalkshtHCTi0GM2c8e4BPiKeroiQCfaFHYpO9X4ST/exzx5GxsQeArNnbq1MaHVm/7ys3+KUEhY2Zj1AJ8YmOmCoZCgVEUmCC72gRdjCLNQI0igdtAQqIZKAAFtkYBwCe2ZqoxUCgABfopIPzdZb9OUBsKQAEosPkKAD6x+XOIEWy3AhMcLE7QxZznEGeXc54d2AYFoMAcFcBmfI6zApugABSYoQJwlzOcFJgEBaDAHBWQwydUepnihLnq987Fleaok/3hNv36V5CH3BQuHreg5S7S+GY7tK9Gwv3iuUNTQtPHa1lowAyLFWqi7lTpH1hEyf6roXe62Weo3NAmsfCJIDFrld5mqdgJP9gW90aJly8PVNLJ8E/nU1NhC9MflUvXrG0p+7cWucmvQUPqDru4fTMSO+a5UDS8CC2IlJxQme/Z9d+zzbh6wksN0QfgE07FCeETUVYvlzyRUjPcxcllg/lVOd4uKAX5VT1b9xBrYMQ21GPgaEXjbaHoUK7HnSePhUZQ2gnlYahdiXMVNpovRvc4pdawiYRVMuGblsnKN6dK2JHICq+j1K5LnJwCDHQ2il3/nVubriLgE5WzXBN8oprsBWIn6itZbXyOFQas+ptxlcxtpVLvxluccIsU/JthOTBtqm7rJX0jHWAMTEzRcHbRrjwco4+mXDjcNECBTW5v9V/Sqyi8ZbwdjGeJFOGHooON3YMv7RNNMAWNIWc8mm7S7z/8djcxs0F46uroePKtWVjPnkVilkBHmJZDywGf8N5yUviE9g5NMMvysBPMbXK+2teshxubeFxxe1T4KdmLsywH6qPepqY++GDwIo9taIcxqAyk3ltIYpnQnr2reLw6rDS4Cx2jHtItrxJb7ZpgLorCm6PoQJLgUBw866I2NOO/9XV47uJ/yRQ0h1xrub7+VaY6UkI9T5RlhPlwWwenpOdZJS2/Pb03Qr9/H4kppnTkNQF8QrL4u5dJvRkv24wsCzshA0iwmrMsB1Wy0WYptmFgGIO358lOZRv9210+itk7vW1ZXewomnXbjZezLuqWBJvxh5unr03ge2W3AsqJkvU+OXNuyFHjzPonr6YzVamnXPDI8DmQFdzp8pePK5bSoRp3iRabejYV665JFGzqd476YWK2R+qy8S5t2++YeLzwvL2759nImoP8kGiTsRODz1p/loPJnmWjO4cza4cxqKhf3arDXKwBwqY7GC9sOVNMZca1We/7T0GiL3L77VbIT7irdvqondPE7RLc9kgtKuPq4xzfVYA76Xn7MDM/YSsS+ERgzvKwE720bkApWJYD20UhtiEHYzAp3+PQ4Pq4e6jAojV4ioZ/+efgE426GeNZFAfLumibrOs3p/p9nHwKSqfeHjzcHFzucb+icHAnoeWhmEJKR75lwCfcpE4Ln+DPLpeInVAPd71VKf2dJAel4LAQ/F1ZiG3IwhhUfKBu5ODI+XB10oagSHuLBDdC4YyqzZyu3hxFB5IEi+JgWRd1k4OzSx2Q68CJw2mUesZq62q3r+p1DPWgYi+1KV8d+td+/k6xX0ea7J3uhPR6b0aIJJFTOvKaAD4RSPyODpvNUcR64BPkWeitQMsPbhqrsmOyd+HqLrdH2DCKQQGRArNYgYBPiOZKH0G8ffZi9a74wKEDfMIcsYh9pfl1BD1dO0Y4YgVQEApAgUoBwCdaVgPgE7hVoMB2KzBBdrUJupjzHCKB25xnB7ZBASgwRwUAn5jjrMAmKAAFZqjAIL+7nOG4YBIUgAJQYGAFAJ8YWFA0BwUmVmCCg8UJuphYtKLucHZZJBcKQwEoAAVW2IxjEUABKAAFRArAXYpkQiEoAAWggBA+0SkZ/WLIE1MvkygxZWG2ZZPcRv1B58e3x5RurPAKk3gWVt3G4rOUy2fjFMwI4BMCkaoiAviEytOwxeSJETkB2ZnqgIu4eko5KdXfND/au9/v9ifjWbOqAhncRUFL0xRl3NssPV4PNQCfcOKtBz5h/8Jya8kTPZbu5FUfvzxTLpLcbD2P7wimkKMZGncxgpVRkypdUYRP0bCGfZ3SbBEX4BOVs1wvfGIryRM16EKTGEGzE3IFaBdcBxIwnAOGjsACGDI4iga+IosxSKRdqpAGlJyp+XBOwCAp0Yvjnpk6Fe6CYSRkZWFBDjVtEwMMPR2rrS+g0kgFiUFViq1X3xlvKUBW2GYYuQSGTeGOAZ/wq3dN8Ikqr9k2kidq0IUU2MBzBUwKkna0A9sIB2CobrAEn6COr+CK5YkFbNepkfrlmMZdJHtslyXQzYMcVG+htqwOoR/Kmb2KHvpBQkIJsuKNPkdm5coaNoWzXOlM7uJY+frqzj0qWOtS9/s0Q5llL3n4RDYH0RaRJ5JggxpXoJVzwDbCwgZiP2AzWXoahBD8kGQhuNbZrpMjFaziZI9Z/EMD5KB6i7Vtp2IIzA78JWUUXln+Qh5Z4ZK1p2ZKiOsQ6DdcER/zAj4xjKj9f0i0ZeSJQcAGpY0I+QTCYsKV027ksLgLziQG5CAZYFZbSs27c6oCxZrjy1Zs0U1imFD2IYv5mBfwiWFkLYFPbC15wnMCBgEbsI2wAIZwink+QR78sMoSC9iu8yNN4y6yPeaXrgM5NEuyVAxfLG+2KqpKXV0rb+k3rrKKqnJqptoNyw95kBKATzgZp4VPMJO3peSJkBMwDNiAoyOwAIbKC5zpnwbp62p1ZD6XgR/yLAS+6zzCIYm7yDMSUq6hAXKoFWQ5DVGZvNnOXx4eRq/EZRW17B5qUM1F3rBBvGG2EcAnvETBPK0DPlGeZ79jpvfsmjAFyu0RNrx5xUjoN0/eZw+ZZz4wTGjHCQJ8QixcR5dUCp8AeUI8I5MWtIiPywP7Y5hJO0dnc1QA8ImWWQF8Yo5LFjZBgekUmCC72gRdTKdXeU9I4FauGWpAASiw3QoAPrHd84/RQwEoIFag/+8uxV2hIBSAAlBgkxUAfGKTZw+2Q4HVaoKDxQm6mPNM4uxyzrMD26AAFJijAtiMz3FWYBMUgAIzVADucoaTApOgABSYowJC+IQ3HRSKbrMo4UksLa93N6VQq68CgE/0VTBZn4VP6NJBhldHf6FPl0qhMAJVoJvRBG/hSRSjJkYz0jW8TvDG6INbaAeATwSr1+ZZUPwc5mLpFK3ICusuaznrVZXXCvrirptXdz75zSIpFMZbUo6aiwuVrWahtxKGtXQFAJ+onOVU8AlKm7pzYRE9pvcKK6D+48uDMIF/uAJNUiyTIMt+bqNUk5Q93G9W/w4CWXoOSHgPUZ/Hj46PNf+Qruo5wvAPaiSD+q3DGE9FmkwCAVkhHjvZ5aEOgQL1loOvpF2wzIMs5kEIWmhMBGPV0t3Pho0P8AnvLSeDT0SJALn1skgKBT2XTS7+CH9FTILLAxtmX+zcf1LeUzFqTNhNadW8fw7JCi2UAq9no2X/TUEXKeZBB/oFdV8bQgzeyEMsNsy1LNFcwCfGndXcm/EsfDIwb6MpFLzxTcBDnqyQoxQYxVh0hPlK3oWJ183loRSqiXL6RVTLDSFce1mIxbgLFa13UADwiQ6itVXh3GWYktmGL5S8PnttNIWiq/FZVUYt0Jl50Ae0MOqI0PiQCgA+MaSa1BYHn7B5iCsEZL3P5VEoFOTK7bDVLvvm1UrjXEKOAgVyJImcrNDOk2i27FWWdxHEkSpcFa4NOWiBGvTgjSKrhJag2MAKAD7hBJ0SPqGeShXuQL2puHv17uVja8ryKBQNup8mTtDbqibgQU5WaOdJNFv2d468i47MgwLQAsmgqBf0nJBbNbALQHNyBQCfCO4iDwlZB3zC21EOCeiY8l24SsrtETaMYlBgExQAfEI8Sx09USl8IvSVh6sLMRbGwhFOd058bCoeGgpCAShQrADgEy2SAT5RvJ5QAQosSoEJsqtN0MWcpwQJ3OY8O7ANCkCBOSoA+MQcZwU2QQEoMEMFcj9Tn6HJMAkKQAEosA4FAJ9Yh+roEwoMp8AEB4sTdDGcHsO3hLPL4TVFi1AACixbAWzGlz2/GB0UgAKDKQB3OZiUaAgKQIFlK1AEnwB5YtmLAaNbhAKAT4w2jSx8ogaN8f+5VPJEzNlIZKqvTwHADKMtSjTcQwHAJ5x42eSTQ8En0rO1VPJEkNEsSiPfY92iKhSYXAHAJypnORV8om2Sl0qeiMfcwFTUQRGlhIzJ7xt0uI0KAD7hveVk8AnVo07bZS/PmdGmLJI8EYzXpfm8Pb3f14QJyidCoIj7E4t5uzm4fPH2YwxmYAps482KMa9bAcAnxp2B1JvxMN22JJX6aqPJE0RruHDQS5dtaVeDe/SlMu/65wdBHnzKXDc32QLjTiJahwKsAoBPDLwwhvohUVd4g02Pv3+lI1kmgXshJmHniUtiPKxQWTOyBYa1B61BgbwCgE/kNSoqwcEn2htYHnkiK1iK1uCjzCKcQ7Y7FIACHRUAfMIJNyV8omWylkeeEKxMjtag+RQWzLAS4xwEnaEIFOiqAOATXrmA/bI++EQ56aFjvnfhgim3R9gwikGBDVEA8AnxRHV0Rt3gE4bTCvKEeHZQEApMrQDgEy2KAz4x9XJEf1BgXgpMkF1tgi7mpWlsDRK4zXl2YBsUgAJzVADwiTnOCmyCAlBghgoM9bvLGQ4NJkEBKAAFhlQA8Ikh1URbUGB6BSY4WJygi+l1k/eIs0u5VigJBaAAFFAKYDOOdQAFoAAUECkAdymSCYWgABSAAnCXWANQAApAAZECElYPED0iKVEICsxCAbB6zDSMB5+gnI7H9IfoNwa84Nk1JqHaUhE9oaCp/HGzWP8wAgqIFQCrxznL0eAT5Ihfnx+daF9p/eORypjr/zx8kYgeypF+eXDj0gI/XBydX+nHAy4osKkKgNVjZ05lTnMJvsl7rS5/+RjPKVsgV8tsxvOIjwUielTizoMvq2zCFES7x0OdzFOL7X0i4xCZ6f/d4PwEoEkm//Gm3piwe4YK5G/k0GiCABztO2RAYzQtt/wMRz6NScZdChAfy0P0UMLKndM9vQuPWblNMg9JFIaiWRpHwPkh56lOOUwMe7E6FGJ5p5l99LIwBQQ3cjXi66u7CrDCCJG65RemWclw+r4Z32hED8WT5jq5N25TB38seEc9iP1hRVbggPOjFnB1yrF/1OD8ZBtDASjQUQGwejoKl6rW010uBNFj/GZ1eAnwzsDLDM2tRYEtZvWMCZ8QID6Wh+gJDx7VYnYnOSx4J1SIpKgW/90Hc4SsYlLuUhVfvzVl1Dn87tPP13LnoNNtUEBwIxsZKM7Zye2W2Ft+Y1QcBT5hossa4kNlTdeo2OrNxAIRPeptf0BTf/T66Y151cOTed750i8u3ZpRr9zs8efV6ohdSfSAJzK52evvne5cmJ9q4YICYygAVk+gqo+tH/xNF7/eZQqQL3z53h7RMbeqz0hELpL8RepmLkfidKRiCNdQuT3ChiXF2qWStIAyUGA4BcDqEWt5ffzsw3flEUsRqweIHr2RfqYjRLqIV1SuuHhGURAK9FEArJ4W9Z6f9btzke+yz9JEXSiwfgUmSEY5QRfr1zFtgY8u4S7nPE2wDQrkFZjAl5kuPvvss7w1Syzx22+/mWGB1bPE6cWYoAAUGEGBnr+7HMEiNAkFoAAUmKUC2IzPclpgFBQQKzDZZvzXX38VG7WogmD1LGo6MRgoAAUmUACb8QlERhdQAAosQQG4yyXMIsYABaDABAqMBp9gbK//kbZ4eEHFYhAG22lnS8QmoyAUgAKLU8C7yzBnvf8Llgx8gvE64zoiylFBuSN9jnfJbARJfyXFUQYKQIE1K6ATbNeSnzuTglzbQaJaDsvDlwyHxsJ8Wgk/1l3GOevNX5mHSXB5+ITK3eOy7WgzdDPp/My9Z4EM6/dHTL0tQANQAAqMp4B2Vnunt209BOkVjTf4+DaB5WmUjJ0lUyvZlKnZDz5Rg2BUpIvgL6xt0t14/AyPocFsaN/OR88OEwWzKIjaRt7+1XeVbA1kiPHWPlqGAoUK6Ejt5tVuSbUcYIdvqwerR5Czns9EH/E8giRvVRYkGvvdYYyoSfIYAmZDu1xxC3zmtHoL5rTBQiBsFZAhSpYlys5fgXgHuky+KWWWNFeWfCUvKZzZvm/GA395/eZ0VaHC/Lw1I+skjyFgNrSbH7UgGylLjwAZQiYeSm2KAp6n4gGnFc51U8bQamc1wGYcFleUl5QL09ddUjZNAoS9oc1w6I9Myjc7Y1kQmNxalIQCUKBNgW2ILu34VSpkxzJoXxTykrnFZdwll7M+QizQcSphZnlugnrhc3Vdh3D6Nz5NKkN/HkMHFERYxZvU35KcvvgeCkypwCKjy+DXg9fHfgeuOGE7T+hVD4/l4UrSTPi22Fopwo+bwiZ8wr2lUaSE6ic7LHzCNqLhNofhK3FKUbpyBwxNKkN/HkPA4XgkREGEVbxJ/S2Z8lZAX1Bg6Qq4N+O3iunC/Jro86ceGLN3eWB/U8hiediSag/sjvzYWjzhx6s+GnxiunldK4hiumGiJyjAK4AUG+KV0RGJMyZ8Qmw7CkIBKAAFJlTg033wNrpDv0jg1kE0VIECM1IA0eXYk4EEbmMrjPahABRYmgKATyxtRjEeKAAFRlKg9+8uR7ILzUIBKAAFZqYAzi5nNiEwBwoUKoCzy0LBiovj7LJYMlSAAlBgyxXAZnzLFwCGDwWggFQBuEupUigHBaDAlisggU94iYrJD7MUV2chSGZrnqXJMAoKQIEZKJCCTwTuxPwRufrLdvr7ffpbcDbLXJQPOJ+IrtfI+/RFdV8/vXm4Obh8kUpvL7GtLT1+tj5rfz2VTKVyXNxl+UuXz/aPAlBgMAXmB4qQIyXkJZ1cLHwi0JJaVH/K/uCy5vEUCl1h1yXfVT515Oitc18WX7FuigVrf5Aq3+tNXtHo7y7K8ud4H1z5wW4DNAQFMgrMEhTB0iN6fljp0AqfsL4ywuNE+dMTelKKotv7T4qhQYiit2rva2OiIFCq/GnzwxIgRNCXzbEcpFmuGcAiMRSd4tjYqPfovvO0hUr9W50zRcfRjWF2sZ+VMuTN2QItjl4Pz0elyoiRH1pwKFutwBxBEXKkhLxkMMnGXXLwiU8mrmygxHgKRbhuQsBZyJO4Pt67P7FRkt8N04c+errYISdbBoTwfaVwF6EBqTLnq31t1s2r1eneVfVvlfVYZcirm62yPO2aANGmuAt66Wg/deRT5bvHi8oxWuWnb9ya9fIqHR2RPpSPVEZQfmZw4LbNn80tPbAc/yAvucY5Tb0Zvz09vN85ur38JcGvZEw24RZdVSI6tUP/7rktq5Lyek0ISaED0IgJ8fyMvI8ICMH1xeMuYqAFX8alMqYnwSr8tzacNbs+/KCXzvavSjfXTHnymBc7NA/hFKxxdaHrqRWYVXpgOf5BXnJqQeP+Uu6SYqezs7OHk/s98YauOo9LBjXRDd4HItLoS4K7kJRhZ2Mws33rAq2orArkSx5YunnKEL/eJYXe16jA3KJLK4Uc/yAvuQ6V0/AJbc3zM9o1xx4zTaHI2K+Trlep498+U/8O8Q+07aWPOgMhWnAX3jJJmdowWLOpjA6Omauz/UxbCkx8WntgXR+3PcDs2YaatSwnbx3rDX2Oq8Dao8s1gyLkSAl5yWDGmvCJ2nQ6PoO7+dooFDl/eaaO1uxLFWJb7NM2PcQ/PDq8IxpQNyBEO+7CGCYpw/ks1uwT8v0su7Ob/arfxtmllkf96MmecmjpDlcnmkXfLK9e9dCJpYrt1aac8B/incG49zBaX6QCswRFyJES8pLV7AnhE77CeKQHEv/Nk/cVHWiRKwyDggKDK7DQFBsdQRGDy0sNFsEnQl9J0cvgHs38vofeTvi3QmMMGW1CASiwQQr0BUWMMVQkcBtDVbQJBaZTYKHR5XQCZntCAresRCgABaAAFIgUAHwCCwIKQAEoIFIACdxEMqEQFIACUABnl1gDUGCzFcDZ5djzh7PLsRVG+1AACixNAWzGlzajGA8UgAIjKQB3OZKwaBYKQIGlKSCETywDO2EmTyW41JnZOlx96nboDlWgABSYkQIsfKLpFDYcOxFlyKexDP6HSTOaUZgCBTZOgTiRkkt10IRD1EEsXOATlIlyZVcZwJ08w8MnKuE3HTuxcUsIBkOBLVIgyJJoEkByxIggwffDw8WRz05b6RSkG1cJfYzDvL66c2QcSgdrKV1yIkXVeit8Ip6sGWMnQsRFkzBRY0UEsXOde8HSKfT23V6H516TEsLEFq16DBUKDKIAC4cIWiaOwl2VezzscueJydilsn2b6/mZT8FL+RjNZwPDJ5pjnil2ggxtJ0w0WRFmbA3uhc6X5ugY1aPp+LB6NjmtCe5QfTg6yW2Q9YdGtkCBmaYHFihfCJ+4fnO64zIZhq1Tht6nr21wQ8zX+rGbgtU4dyowql5kkDfj68ZOhIgL7QZ9Ts3bFkma3Au2blTMNSciTHSYDlSBAr0UWHt64G7Wl8InNPOPTWBGW0kHBGvSsU2A1OPNxSDuUoBSGIzfkOurM2HC+EoFBDMXnYzgggIbpsDmRpdWaAl8QvMMudCSbmEKOlXacXU9fnmyc2rwhHSpgzYKN/vR/jLwiWixzBY7UVvSLGGiyYpoci+onWZdVezKaq4wZ/oakjCxYTckzJ2zApsZXWrqjPVqv1ze6t0yC4fQZcglrmqhpf+hY3xTX53vEp/BBEIK5xr6ykHhEyEIwQ5lptiJ2uJlCRP0nGmyIprci0Tddx6ZcbWyIWd3wsSc7zXYBgXWosDnTysojd8ts3AI5floH/7O8lestRTGWBarQ6FaTosmsVBg+ZrCnMClaY82LnwC2Im1rCR0CgUyCmx9io3RMRWl8AlzqtfjjJSfcWAn4AugABToqcB0mAokcOs5VagOBdaswNZHl6PrjwRuo0uMDqAAFFiYAoBPLGxCMRwoAAXGUmCQ312OZRzahQJQAArMRwGcXc5nLmAJFOiiAM4uu6hWUgdnlyVqoSwUgAJQYLXCZhyrAApAASggUgDuUiQTCkEBKAAFhPAJL9TaKRQs/kHOhJCXnNva2FzL56Yk7IECHRVIwScehWnddZoT85fjLRQK9XUiv25H42y19aAj6rldOvN9koOPxtVPItSGApMq0Fi75SCH2F844ETkRGbzodPWustGSqTd3bvXbz/qUipt8e5uNRlJCoVK+0F/IO8S7F6sDrszxCad+1RnUda5wf8CdBZDhBFQoFAB7Rj3TqNUsl1ADjxegmVOrPnDSqAUfGLnxOWKo0RE6j8CTXkKhfa4JgOIuSi/z9G58bnhRtL/m41E1bfHLr2vfrik0REME6KEHlEnT+RXja4R4ZK0hU2bdVMMnUI/k9+a4T179uL01iRWVk3KLR8lgs8PHiWggFZAIwduXgUBVDeQQ0EtOShijJLBvBt3qZKDu6Sa3tvtH6k8j9dvLg/qaYtZCgXTBnExmmkmfecs6YG+PV/t6wD15tVKJfdMoyOaTAg5PUKRJ1zW5Ydm2mVjZJjFTvk0lbaNkrkpH0k+S2USdk8HZ/ODIyep71k6hedkvH//7tWuSXasAlcx94IviVsZCtSe0Y4vNfwp0vZK3fJmXG+6n72+O/jSB4wD68RTIpzjbs+rzDIhwpjObxfYkirRr/eGVJR168xm3OXTqyWx9w8b9YS4/OWjfgD5fM/hY8Pm5WOUbKohH+PAE4PmNlWBzUwPvDFqt/2QSCVvv2X5Qdzwwqzj9nuVtdNkM+a9w+CkhyJ6RFceBg20fXq7oJPklstLbswihKGDKbDx8InBlBiloXb4BD2ruDccLIXCZCwP3mVR2uOAqHH3wbw48vwG+jdLiWCHyaMjGkwItk2WHkEB37mFEFMl2jpLtywWH0n79z2uintCCOkU4biE3Isi3UZZM2h0vgqsJ7osAjn43yLKa623ZDDbxl2qfa8H0mTXQopCoX5ktKPfXeiLOELO2dK+fmW/8PwGlvTA9p1ARzBMCDk9gl5EqWNIj4z0PKTQgvrZpXrJQhGxOrBUm3J68++eDr6k/Vofc5JH1e3vne6Er8B8D+G45JbLdctOJApAgXIF3Jtx/ZrS3gAFIIcKFFGAf5C3P0bJSiOfYoN8vpCTJqFQyFsrn67Z1ZAIMjujYdBiFNioFBujgyLGmNZS+IS3QUihoBDIxpnB7nyMgaBNKAAFNkiB6UARY4iCBG5jqIo2ocB0CmxUdDmdLAP2hARuA4qJpqAAFNgKBQCf2IppxiChABTorwASuPXXEC1AASiwFQrg7HIrphmDXLACOLsce3Jxdjm2wmgfCkCBpSmAzfjSZhTjgQJQYCQF4C5HEhbNQgEosDQFiuATaydP9FG/G7zB1+pWXWawyWAp/at13+aYJskMRykosFUKpOET1Z/j+NuyhTwR8Cm0fvX/3nhRE9lGBhgX5T9WOejpT9AL/wJqPJMGGBWagAJiBRooiyqxUhREVJmx2fQ2Lq14LfYQ1vJNtkBhUvCJo6Od0xeWPhGOOkmeWK1aeBVi3baxIGXjUEk7yPkFqei3UQiMeQsVYFAWNvW2zhEeBBH0ccW2YRKlffyw0sm2dWbxO5duLFNLkXV0LU9+0NHLuwoKEc1JCj6x2ldJhCiZef3iyROqVIpXwcISQgyDduupUi6/kYu86qQH/xziQzMGUBH1Ja5lQ2xlZvBko09tCwzKYrAx2jmod9GO8djCWw9D3jwFGJRFyGVQucxUum3ar75JJPZyY3788sw5OWrBJtrN1qorpir4vN4NOdPwCZ1ezOHNgnosecJ8r5JINnkVKciExzDQk8JmkTQPlCPbW4oPEdIp9q4iUkVtfJRysyJA5Jr1ddla9lutisuzqZJ3mpzpKVMHGaN5aEUS7dx/CqdE0VMaz9XNu3VgcW8FlpAemEk0TiHOh7sABpM8tjLj97nVsrVUCnSdWtLk5qVgc3XRAjFsezOus1QyAWZ6ThO8Ch4yEWAYyvgQnk7xZMdnGCYn3jSrrFlXP4V8sN+rZ4J5iuhAXnOMkiiL/mOkTKQ6s3Jk1fOz2pTyCve++dDApimwnvTAw6oUpKyMkJMGbKUjKv6kUEVsZ+r7d6sXfg+Yq+UVU1GbAZP5u6lxQtr6QyIbYH6Qq8HwKvrAErryITIG92vWPUUobF9VHKPObXauGETDKmmxW0kuiJZPGkouR4ElRJcR54/2mk2YSzsz0aQ7d/iGam5ztVRoqfaKKjJRtxOdgNZ31+3wCQW/3Tk9PQ+XE0ueCGxieBVZyEQYfqv4WV+d+RDemG7YCbZWqIDZkB+7jbjQ1J5jDGkW9PirPfeyCi/HIWAkbQosIbqsxmd4qnoDF/InlENzEDD/48YQIEO8h1vtZFO1OAk55m29XBY+QbFURPJKkSeScyiBJYTh94tL15SED9F684TNeuhFFjvB14o6Up78/DxgDQtM7TnGkGbx6PAuJMZJFIaTgQKzVIBDWfj3vupNuPu5iMW96Fe/DvGiz6jsgRd5xgomQ/XMcRVfi1GCXljo0NIFPwYaU3/pUwqfGB+0sA3cim0Y4yxvzkUatcUpNiZCWXSDTwjJEx3WZPAbmerJ0aGdOVfZhjHOWX/YtjwFpkZZIIHb8tYQRrRdCmxxdDnRRCOB20RCoxsoAAUWowDgE4uZSgwECkCBcRVAArdx9UXrUAAKLEYBnF0uZioxkC1VAGeXY088zi7HVhjtQwEosDQFsBlf2oxiPFAACoykANzlSMKiWSgABZamQBF8gga/dv5EO3HBZBhQf1D98e0xk91YNH39oQ69W1DjSCSpavnKjq7HHLU13tIs+1VuBvIDGWe95fvtIaBogaHQpirAwifUYNh0vTpBEiU4ZrEy9WQoxewZkYZtxIWPb6+eUo4nMpD+4PN+P5ERudZNbLbyUWuHOpiEm2xu9fCrOEl+BfxpmaN2icPGmx6/pdnaV1rS41+os0+KQsT6/VpfEarI1NdZPjuPJTXSRr9lkBXRGrVu3mW2br9bJMwDaa+bVa668+KE21Y3TrbIK7nIyI66wYwICvO+qCoQLFH2QycsD5+ggVR53o3/qTps4U9EychasmyONK02n7LJylLQfWD2DPgPlEfKJh1uyJT8yqfYt6NumaOk9i39ujotzYZf6QnYvz89P329evfAMTUafbWQS7qMJTXIRr8dICuSxcuDEKqahcwDSZcbVoYlTCSwE9XQglTjOo+4zXLDECzCdNoBiyJQiSgTlJ+9lj+T/bCqxMEn9Jq6CBwHpbwJE6un+RP1KdPD8I7W74JU5HLsOETR073xQA5iP1MwiHrqMIZEQBw0IQt4qy4avTfBFYlOuy9elXwqyHUUNpT4yvrKyNPL58h10NJvsFy/PLAsgMYAgx61bFdPXx29OqE8rUx02ewrRS5R3aTGIpidmpXMGEshK3a+MxQ6FoTQtibamQfdV9Nsa7KECR47wY+hSs5t82PexKnTqJZLlMnmDlep1UxuONrDOMQF+2HQPwefCI22RePMmkn+xDntgv1FvkllHSPKkFpb9sHh7mkHkPCJkU1qO5su2QGNVFYln/c2Bi4wMAaOcsE2W9e/Mjvyp0zvTQJECq3BzHH9tIKH5TLqu7a4r2i7G6a58t22MEL45dfSb1ChpdnqKx1dnn1J1T5XWIxmxM71xZNLdNdsp/zs3J84CsfBZRPNx/VbCFmx863yddPV6jXNfHsQQih7IfNA7vRka0ze3mglWcIE+yFvQvb5QjkVn762zojmoGCz2TLmYd+MM5txlXBO0TDUPR2Y7OMn5YgVu0itZJ9dznlnJR95YO3EasAFFsbgF8ve6a0ZNNtsXY/K7EjUZu/CThN6j5C69fb08H7HCCi5Ws9lJA2UlAkiLFG1BLkkVZednQrnQivgNgIapW0oh6z4fN/aa6b2LE0QQmBDEfNApJ8uNMIak3deUpIlTKSwE42G9Qm0DQ0TvdK22j07b7hHZ4mxviznLhkfH6QvLu+G2muv1Mwub8vbR/n+lX5KZLbS5CuHZTBIei/pdIQnP4FIzs7OHk7u90SM8ioUnsEZbWNNMOSSlnXDzk43kkc5ZMW9CX2hzmbbAxcehBAMTMA8kN9zI6wxeedlJYN9WUWYYD+stys4ZdfgyH2z1aZNLvHLiqBjqZFw8Am9evQO2l7ky6OXDxn+RNyX3b+Sh99jWeo2j3wIV1ByqOTyLp+8emTSyURE32BhDE0GA9escFaZ3oWdJjqQPflbNiTJr2jjQfJGHrNojpTBso1QS7MFPab6SvwmgWuZmZ08raRFQClkxQbo2k+yb7GUliwIIbEqJMwD4YqlYrI1Jm9vgpLmvKwWKkYf1n7YpSBZmdDSLGdP2uFgFSGXwmO32A8DDXj4BImu7j93DKmCtuARmuZP1M8u1dqy6X5tFnh3S/uSLhtwCFegrO/6TVMtn3zESm/CGFgGA9escAkwvQs7FXbAF1PRSIXmjcq0fUWnxGrG3BOpmBGicVBxv+Fs2nZbmi3psWUgjChsy9zayCJAWvqVQlZs+NMenfMgBG6+ZcyDXgtqrpXdyVB09M5+GI1A78MjV2Dfv6rjF8XANS7GHQImYRVU4h29VzHf+xbZD6v+S+ETVJN8PcG9+xyd9m8hFJAUfvPkfR975ragSB/2BYERP/VVOIpuCmcbb2m2tMdsX344pS23z6aw32E7HXeBIcWGWF/yFbQvKD6J6gafMLcrxYMz8U3mUURPp/ZDX7GYcymo+Zv8aWTLV6F/6TZH7Y23TH2HVSEZyBjrTdJvh+HMZenAjlYF+sIqkMANCwwKbLYCiC7Hnj8kcBtbYbQPBaDA0hQAfGJpM4rxQAEoMJIC/w//nx9KEeuIbwAAAABJRU5ErkJggg==)

MFS\-651

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


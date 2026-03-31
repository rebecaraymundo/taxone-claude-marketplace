# MTZ_Transfer_Pricing_Aba_Importacao

- **Fonte:** MTZ_Transfer_Pricing_Aba_Importacao.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 205 KB

---

# Módulo \- Transfer Pricing \- Aba Importação \- Lei 12\.715/12 – IN 1\.312/12

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3645

Conversão da Medida Provisória Nº 563/12 na* *lei 12\.715/12  \- “Plano Brasil Maior” 

Esse documento contempla as regras definidas para atendimento a Lei 12\.715/12 do produto Transfer Pricing/Mastersaf\.

MFS\-651

Atualização Legal, implementação do Método PCI de acordo com as regras estabelecidas pela IN 1\.312/12

Esse documento contempla as regras definidas para o Cálculo do Preço Praticado para atendimento a Lei 12\.715/12 e IN 1\.312/2012 do produto Transfer Pricing/Mastersaf\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Link: __Res\. Importações:__

Nesta opção: “__Res\. Importações__” \(disponível no lado esquerdo superior da Aba Importações\), o sistema deve possibilitar a demonstração, por Produto, dos métodos de cálculos processados, os valores de:  
   
__Exposição Fiscal__ \- Diferença entre o Preço Parâmetro e o Preço Praticado\.Quantidade Vendida \- Quantidade vendida do produto, para clientes não vinculados, de acordo com os Documentos Fiscais\.   
__Custo de Aquisição__ \- É a média aritmética ponderada dos preços pelos quais a empresa efetivamente comprou ou vendeu um determinado produto, durante o ano\-calendário\. É calculado, obrigatoriamente, produto a produto\.   
__Preço Parâmetro__ \- É a média aritmética ponderada de preços praticados em operações entre empresas independentes coletados e ajustados, conforme método definido em lei, escolhido pelo contribuinte\. Também deve ser calculado, produto a produto\.

Ao clicar neste link, devera aparecer uma tela inicial, e constará uma linha com as seguintes informações:

__Resumo de Cálculo de Preços de Transferência de Importações__

__Ano de referência__: __2011__

Ambas deverão estar em “negrito” e o ano “2011” esta citado apenas como exemplo, pois no sistema devera ser processado o ano definido para o cálculo disponível na Aba Cadastros 🡪 Define ano de referência\.

 

__Nesta tela também deverá conter os seguintes Campos/CheckBox/ComboBox/Botões:__

Empresa  
Pesquisar

Fechar Ano de Referencia

Total de Exposição Fiscal em função dos métodos de Importações

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

Linha “__Total de Exposição Fiscal em função dos métodos de Importações__” Nesta linha o sistema informa o resultado em  Reais \(R$\) da exposição fiscal somados todos os produtos a que foram submetidos o cálculo do Transfer Pricing\.

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
- PRL Rev Lei 12\.715/123
- PRL Prod Lei 12\.715/123
- PRL Revenda
- PRL Produção IN243/2002
- PRL Produção – Lei 9\.959
- CPL
- PIC
- PCI
- Produtos com operações de entrada/saída de vinculadas que não foram marcados

OS3645/MFS\-651

__RN13__

Opção “__Mostrar apenas produtos com exposição Fiscal__” Quando selecionado o sistema ira disponibilizar a visualização dos resultados somente os valores de exposição fiscal > que 0,00\.

OS3645

__RN14__

Opção “__Mostrar apenas os métodos selecionados \(menor Exposição Fiscal\)__” Quando selecionado, o sistema ira disponibilizar apenas os resultados que contenha os métodos selecionados considerando valores de exposição fiscal aleatórias e de menor valor, não considerando os resultados de processos criticados\.

OS3645

__RN15__

Opção “__Mostrar apenas Produtos com crítica de cálculos__” Quando selecionado o sistrma ira disponibilizar apenas os resultados em que não foram calculados, informando a critica no processo\.

OS3645

__RN16__

Tópico “__Resumo de Cálculo de Preços de Transferência de Importações__” 

Caso o usuário clique no botão “__Pesquisar__” sem aderir nenhuma das opções citadas nas RNs, o sistema ira disponibilizar todas as informações dos resultados do calculo do Transfer Pricing\.

Nesta lista o sistema ira demonstrar os detalhes do Cálculo após processamento, em que constara na linha inicial a seguintes informações:

“__Total de Exposição Fiscal dos métodos de cálculo escolhidos listado abaixo:__” Ao lado direito desta linha o sistema ira informar o resultado da soma de todos os produtos em  Reais \(R$\) que houveram exposições fiscais\.

Em sequencia \(abaixo\), o sistema apresentara a visualização das seguintes colunas possibilitando ao usuário a visualização por produtos as informações do resultado do cálculo:

Ações

Empresa

Código

Produto 

Método 

Exposição Fiscal 

Quant 

Preço Praticado 

Preço Parâmetro

OS3645

__RN17__

Regra para visualização dos resultados detalhados do Cálculo\. 

Ao clicar no ícone \(Lupa\) da coluna Ações, o sistema deverá disponibilizar a próxima tela com as seguintes definições:

__Resumo de Cálculo de Preços de Transferência de Importações__

__Ano de referência__: __2011__

Ambas deverão estar em “negrito” e o ano “2011” esta citado apenas como exemplo, pois no sistema devera ser processado o ano definido para o cálculo disponível na Aba Cadastros 🡪 Define ano de referência\.

Campo “__Voltar__”

As informações abaixo serão apresentadas na tela apenas como cabeçalho, para o usuário identificar o processo calculado detalhadamente:

“__Cód Empresa__”: Código da empresa definido pelo usuário no cadastro\.

“__Empresa__”: Nome da empresa cadastrada para cálculo do Transfer Pricing

“__Cód, Produto__”: Código do produto ao qual o usuário pretende visualizar o cálculo detalhado

“__Unidade__”: Código da unidade do produto definida pelo usuário no cadastro\.

Ao lado direito das informações acima, o sistema ilustrará os seguintes ícones como legenda, para melhor orientar o usuário durante a análise dos cálculos processados:

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAATCAIAAADwLNHcAAAAAXNSR0IArs4c6QAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUATWljcm9zb2Z0IE9mZmljZX/tNXEAAAP3SURBVDhPVVRdbBRVFD537szusD9uaW3ZtkAtVkAbCqWItkbbYDSimDQQMaIPEptgMMZEE6s+9YnokxqpFQIiMb5QSLEP1cBSJNiG1tpixBbaFFLp2t3t/u/M7szcP+/WlOLJPNw5Od+95+f7DjBiCkGFNEcIIgQXheLZTjmGdAgmTMKkU3D5R6kM5ILKCHkgIi8oosRSVMEBsNAtBDqhoKiA4Gr4WsfF99bpquMzU3fZN+3HnqpuAcodVVFtADcoFLgM5EyAAhwIgIalK896Y72jsdDGspK57O2UwcIivZhNbSnfmI7nX3xs/5t1bwBSCTgad0kgkvnI16RRAOLQwUj/1VRI52nDaym4JJ6dSsQo8yZiKZaxjLU4eGjt+/sff4txwLggqAsxRhUFAVOA0b6FvvGFIY/foiieoUaMzthJOwe+PGTiaRH0lBoEg13eufm11oaDq0FFMnVFwSDzwMCRMzI/mNNMrObSdtgkGeYQvvoBoriywBtXPbG39vDrDQcCKjp5a7BUqBzyJpLIZeszLq3Tgw+qNGpF4vl42s5yWunY3iyZqcGbD9a/e7jmUHtJ+7bKrQkavRQN2abiBVm/EP/d0Nizs21rLcbGn4VpzIWfK1lsgOkGveyDps9aPc8YTmYoM3j65vFfpkZr9bprHcOK0FfeD5SLjLCmFhNrUi0VbNe0MJLMSoPryM7uZr3N0nLD9sXu693nJofSOb+wddk0EKDeyx/bvunw7L6KjmcrdgfXr++ffzI0+/0nz/VsoZuYiw4kLvT8fvS36Liq+qjjYX4KTLeU++pPM8Pt5gPJMxPGoF4w20p3HWn+/FFSST3OlcWfTv1x8nJ8NGlarhjVHWI7aXDARZIr+R99/qsa78Nh658TkW/PRX+s9jxUVVJv+5Qrd89+OfbF5TtDyEFeM6CZa7ZXNR9/6QTogLTSFfyOYJMV9y8WUmE0f2bh9M8L30XTM6Fo6NObXw+ZExZ3LMINzcvcyKPbLVVNglsMUdzV1bXcAotBIUGT1yOTGZaZy92apZMjt4cvRH41UnlmYV9uA0/5H6nc8HbrgW1lm2yxSuXZlflRTm1qnB8/f+zGqXE2ZqK8zjQ3Cxh2QTU0x0JC0XZUNH749DuvbH+5yPal1t+HX/LYItv/18APE2fv0L9vhKew14VjxO+qrq2sqwkE9jXs3lv/quaooEko2I7xP7xgUlUYJKMxjETGPu7tnPfMuYlaogQ793y0p+oFkMrVwOTMqyoEEAaxgidULgJNklGqGRU/TUp7SR1SmBRwcSkQRU5NTp0jqrtUpXi4x1/gyzXJZSLVqBC+xA61qG8pL7A5qFJoTPoYc2Fc5L3xLxD1RjV2e0qKAAAAAElFTkSuQmCC) : Método de cálculo escolhido\.

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAIAAABL1vtsAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAPdSURBVDhPnVRraBxVFN4a28S2UkpQihjF1hSsrSaigSARHz+KRgPBqtGKFI2Yqg3igzYNau0PwaqIghgUHzREWpSWQqxtOptEd+OjSdPO7uzsI7O7Zl/JJtnX7M7r3pl7PXfSulPoj+LhMnfuzD3f+c53z7ku+p9ZmFqUDcyeJkWImjAIMSmhsNZhYVJqwGAz+0jK8HRVIQj4EkSppmoUJhuKmWUqSK9QqlJs2d80Q2chANoABL0KoevE9iEU6LD4NisgBXCYuUJkiI4RQYTolMAfQIXdVQiFKrqdB/uHIAQqk+jMiWcnjnWUszkGAHwsXQMWsOUiQxbTmQggAldbEZrT5vjUxFshT3fe90bs7AG57IeIGi4s+7Itl8wBgUE6A3YQDNTzJDWdHnmqlP7OnB/4h3sh4nmnOB9mUtoIIOUVICxTNxhdBBFMtKjEBtPn35/3H4r59ij8Pv7wvXPiD4ANSoLqDgRnIssZaiAWzaWOhsYeWwp++PP3zb8MNJbDnbGxBxKBT9WKDCLBwdjHe9GqibD0lhMFJfP8wuTbkz/dv2ZNw81rNw0fbpbF9gtDd8XHPrYsA1EEwl8ZgtHANCsNSlJvQXx38njzqvp1Tbe0jw5vqiRao783zoUOYSAJwy6cZbustHQTlcShpHdHdGq3kewN/tXesvnOrdta/p65XZ69oxzZLHnaUlODwNNwYDgTQaYpZ859sOjdmQsekOdeyQhP9HQ1dD39UGRmQyG7Xs1viE+vFcZ3Ql1C1jpVCBSJqVUhYFnMnEoI/QlhN5b20nhvJtB58set33zWlkltKy1uLBbqFhZqUuL2UtwL58pSYQV7KRECzYTV6MhLi3905yIHC/49pVBnLtmaEVoC5x4ulLeoxRupcS0yV4R9Lu/wg9lkEBPWJyouuMAZzLIsTHBK+iLrfzMnvV6IvYqlZ5Tpe05+cuvw1zeU5+topQYbLkxXmaXrZ7i6o+/dDXWusP6lVYjAiZ4ov38p9rkcP5iNvVbJdESmWnd0NHVtfyQZrqeVlWppNTFrTbU2KbpGBzZSQGAlhhkEzPD888jj+eBHeuKrYqTHmN2F0k/K6WbvmZvc7vv00nUWXmnQ1RpdUVHqE5LL822jZhTtPjarcobFY6Hxvph7l+/XR/mRtgunmkJnbps9XS9MNPi5a0TOFfGsE7ga30it77fGrG/IroklUMBxqIRm+CNJ7/7zXN/Z0X6e6xdP7xO4l1Ncn8C9KI4/H3Lv5UefC7i7xYkv2aWE2G2mUdlRWs7WuYr3CmiBNUW9rM2uws+xBe41dvsQ/P9ZwD0LNy005r9AuOTR/IRrGwAAAABJRU5ErkJggg==): Avisos ou erros no cálculo por esse método

OS3645

__RN18__

Em sequência, o sistema disponibilizará a seguinte visualização, possibilitando ao usuário a verificação do cálculo processado somente do Preço Praticado e ou do Preço Parâmetro:

Ações:

Método:

Exposição Fiscal:

Margem de divergência \(%\):

Resultado da Operação:

Preço praticado:

Preço parâmetro:

Diferença:

Para que o usuário possa obter a visualização dos detalhes do cálculo do Preço Praticado, é necessário selecionar através do ícone \(Lupa\) a opção “__Preço praticado__” e ou “__Preço Parâmetro__”, de acordo com sua necessidade de análise\.

OS3645

__RN19__

Nesta tela o sistema também disponibiliza a visualização referente o método utilizado no cálculo da seguinte maneira:

__Calcular utilizando os métodos \(Importação\) : __Esta linha estará destacada em “negrito” e sua finalidade é apenas como título da tela\.

Calcula PRL Rev Lei 12\.715/12 

Calcula PRL Prod Lei 12\.715/12

Calcula PRL \- Rev

Calcula PRL \- Prod

Calcula CPL

Calcula PIC

Calcula PCI

Esta informação é ilustrada através de um ChekBox, em que vem “flegado” como default o método utilizado durante o processo de cálculo definido pelo usuário\.

OS3645/MFS\-651

__RN20__

Regra para verificação do __Preço Praticado__:

Nesta opção, o sistema deverá disponibilizar as seguintes informações para visualização e análise do usuário:

__Detalhes do cálculo __

__Ano de regerência: 2011__

Ambas deverão estar em “negrito” e o ano “2011” esta citado apenas como exemplo, pois no sistema devera ser processado o ano definido para o cálculo disponível na Aba Cadastros 🡪 Define ano de referência\.

Na mesma tela, o sistema deverá disponibilizar as informações abaixo, em que serão apresentadas apenas como cabeçalho, para o usuário identificar o processo calculado detalhadamente:

“__Cód Empresa__”: Código da empresa definido pelo usuário no cadastro\.

“__Empresa__”: Nome da empresa cadastrada para cálculo do Transfer Pricing

“__Código do produto__”: Código do produto ao qual o usuário pretende visualizar o cálculo detalhado\.

“__Produto__”: Descrição do produto\.

“__Unidade__”: Código da unidade do produto definida pelo usuário no cadastro\.

“__Detalhe de__”: Preço Praticado

Em sequencia na mesma tela, o sistema devera disponibilizar a linha: “__Tipo de custo de aquisição: Custo do Produto \+ Frete \+ Seguro \+ Imp\. Importação__”\.

Abaixo, o sistema devera disponibilizar a visualização dos valores das seguintes informações do cálculo que foram executadas através da Aba “__Processar Cálculo__”, conforme as RNs descritas no documento “do documento__ __“__MTZ \- Transfer Pricing \- Preço Praticado \- Método PRL Lei 12\.715\_12\.docx__”__\.__ :

\(A\) Quantidade de Produtos Importados

\(B\) saldo Inicial Estoque

\(C\) Custo Médio do Produto no Estoque

\(D\) Imposto de Importação

\(E\) Frete

\(F\) Seguro

\(G\) Despesas

\(H\) Total de Imp\. e Desp\. \(Conforme tipo de custo\)

\(I\) Valor total de Importação \(em reais\)

\(J\) Custo Médio Estoque = \(B\) x \(C\)

\(K\) Custo Total de Importação  = \(H\) \+ \(I\) – \(J\)

\(L\) Quantidade total de produtos = \(A\) \+ \(B\)

\(M\) Preço Praticado = \(K\) / \(L\)

OS3645

__RN21__

Regra para visualização do __Preço Parâmetro \(Revenda\) Lei 12\.715/12__:

Nesta opção, o sistema deverá disponibilizar as seguintes informações para visualização e análise do usuário:

__Detalhes do cálculo __

__Ano de regerência: 2011__

Ambas deverão estar em “negrito” e o ano “2011” esta citado apenas como exemplo, pois no sistema devera ser processado o ano definido para o cálculo disponível na Aba Cadastros 🡪 Define ano de referência\.

Campo “__Voltar__”

Na sequencia, o sistema deverá disponibilizar as informações abaixo, em que serão apresentadas apenas como cabeçalho, para o usuário identificar o processo calculado detalhadamente:

“__Cód Empresa__”: Código da empresa definido pelo usuário no cadastro\.

“__Empresa__”: Nome da empresa cadastrada para cálculo do Transfer Pricing

“__Código do produto__”: Código do produto ao qual o usuário pretende visualizar o cálculo detalhado\.

“__Produto__”: Descrição do produto\.

“__Unidade__”: Código da unidade do produto definida pelo usuário no cadastro\.

“__Método__”: PRL REVENDA Lei 12\.715/12

Abaixo, o sistema devera disponibilizar a visualização dos valores das seguintes informações do cálculo executado através da Aba “__Processar Cálculo__”, conforme as RNs descritas no documento “__MTZ \- Transfer Pricing \- Preço Parâmetro Revenda \- Método \- PRL Lei 12\.715\_12\.docx__”__\.__:

Tópico “__Detalhamento de revendas do produto__”

Nos tópicos seguintes, o sistema deverá disponibilizar a visualização dos seguintes campos preenchidos com valores, que serão exibidos um ao lado do outro na seguinte ordem:

Código / Produto / \(A\) Vlr Vendas / \(B\) Descontos / \(C\) Embalagem / \(C1\) Emb\. \(doações\) / \(D\) Aj\. Pr\. Pag\. 

Tópico “__Detalhamento de revendas do produto” \(continuação\)__

Código / Produto / \(E\) ICMS / \(F\) PIS / \(G\) COFINS / \(H\) ISS / \(I\) Comissões 

Tópico “__Detalhamento de revendas do produto” \(continuação\)__

Código / Produto / Quant\. Vend / Quant\. Doa / Unidade / Q\. Vend\. Prod\. / Doa Prod\.

\(J\) Custo médio

\(K\) ISS = Somatória de \(H\)

\(L\) ICMS = Somatória de \(E\)

\(M\) PIS/Pasep = Somatória de \(F\)

\(N\) Cofins = Somatória de \(G\)

\(O\) Imposto Sobre Vendas = \(K\) \+ \(L\) \+ \(M\) \+ \(N\)

\(P\) Quantidade Total

\(P1\) Quantidade em Notas Fiscais de saídas não Onerosas

\(Q\) Custo Total de Embalagem = Somatória de \(C\)

\(Q1\) Custo de Embalagens em Doações = Somatória de \(C1\)\(R\) Total de Vendas = Somatória de \(A\)

\(S\) Custos de Embalagem \(Q\) \- \(Q1\)\(T\) Ajustes por prazo de pagamento = Somatória de \(D\)

\(U\) Impostos Sobre Vendas = \(O\)

\(V\) Descontos Incondicionais = Somatória de \(B\)

\(W\) Comissões e Corretagens = Somatória de \(I\) 

\(Y\) Total de Venda Líquida

\(Y1\) Custo Médio Ponderado

\(Y2\) Percentual de Participação

\(Y3\) Valor de Participação

\(X\) Margem de Lucro = \(\(R\) \- \(V\)\) x __% __informado no campo__ __“__margprllei12715__”__ __da tabela__ “Produtos” __

\(X1\) Preço Parâmetro Total 

\(Z\) Quantidade Revendida

\(A1\) Preço Parâmetro

\(B1\) Preço Praticado

\(C1\) Margem de Divergência = \(\(B1\) \- \(A1\)\) / \(B1\) \* 100

\(D1\) Exposição Fiscal = \(\(B1\) \- \(A1\)\) \* \(P\) se \(C1\) > 5%

Exposição Fiscal: Baseado nas Notas Fiscais de Vendas \- Considerando quantidade total dos métodos/mesmas grandezas

Obs: O sistema deverá apresentar no campo “\(X\) Margem de Lucro” o valor da porcentagem conforme definido na RN01 do documento “MTZ \- Transfer Pricing \- Aba Cadastro \- Lei 12\.715\_12\.docx” 

OS3645

__RN22__

Regra para visualização do __Preço Parâmetro \(Produção\)__: 

Nesta opção, o sistema deverá disponibilizar as seguintes informações para visualização e análise do usuário:

__Detalhes do cálculo __

__Ano de regerência: 2011__

Ambas deverão estar em “negrito” e o ano “2011” esta citado apenas como exemplo, pois no sistema devera ser processado o ano definido para o cálculo disponível na Aba Cadastros 🡪 Define ano de referência\.

Campo “__Voltar__”

Na sequencia, o sistema deverá disponibilizar as informações abaixo, em que serão apresentadas apenas como cabeçalho, para o usuário identificar o processo calculado detalhadamente:

“__Cód Empresa__”: Código da empresa definido pelo usuário no cadastro\.

“__Empresa__”: Nome da empresa cadastrada para cálculo do Transfer Pricing

“__Código do produto__”: Código do produto ao qual o usuário pretende visualizar o cálculo detalhado\.

“__Produto__”: Descrição do produto\.

“__Unidade__”: Código da unidade do produto definida pelo usuário no cadastro\.

“__Método__”: PRL Lei 12\.715/12 \(Produção\) 

Abaixo, o sistema devera disponibilizar a visualização dos valores das seguintes informações do cálculo executado através da Aba “__Processar Cálculo__”, conforme as RNs descritas no documento “__MTZ \- Transfer Pricing \- Preço Parâmetro Produção \- Método \- PRL Lei 12\.715\_12\.docx__”__\.__:

\(A\) ISS

\(B\) ICMS

\(B1\) ICMS ST

\(C\) PIS/Pasep

\(D\) Cofins

\(E\) Impostos Sobre Vendas = \(A\) \+ \(B\) \+ \(B1\) \+ \(C\) \+ \(D\)

\(F\) Total de vendas

\(G \)Ajustes por prazo de pagamento

\(H\) Descontos Incondicionais

\(I\) Comissões e Corretagens

\(J\) Total Líquido de Vendas = \(F\) \- \(E\) \+ \(G\) \- \(H\) – \(I\)

Tópico “__Detalhamento de quantidades e valores por produto acabado__”

Neste tópico o sistema deverá disponibilizar a visualização dos seguintes campos preenchidos com valores, que serão exibidos um ao lado do outro na seguinte ordem:

Código / Produto / \(A\) Quant\. Vend / \(M\) Qt\. Vend\./ \(N\) Qt\.Pr\.Imp / Vl\. Vendas / Impostos / Descontos / Comissões / Aj\. Pr\. Pag\. 

Tópico “__Detalhamento de quantidades e valores por produto acabado__”

Neste tópico o sistema deverá disponibilizar a visualização dos seguintes campos preenchidos com valores, que serão exibidos um ao lado do outro na seguinte ordem:

Código / Produto / \(O\) Tot\. Liq\. \(P\) Cust\.Prod \(Q\) Ind\.Part\. = \(\(K\)/\(P\)\) \* \(M\) / \(R\) Vl\.Part\.=\(O\)\*\(Q\) \(R1\) Preço Parâmetro

\(S\) Quantidade total

\(S1\) Quantidade em Notas Fiscais de saídas não Onerosas

\(T\) Total de Vendas = Somatória de \(R\)

\(U\) Margem de Lucro = \(T\) x __% __informado no campo__ __“__margprllei12715__”__ __da tabela__ “Produtos” __

\(V\) Preço Parâmetro Total \(T\) \- \(U\)

\(W\) Quantidade Vendida

\(X\) Preço Parâmetro = \(V\) / \(W\) 

\(Y\) Preço Praticado \(K\)

\(Z\) Margem de Divergência = \(\(Y\) \- \(X\)\) / \(Y\) \* 100

\(A1\) Exposição Fiscal = \(\(Y\) \- \(X\)\) \* \(S\) se \(Z\) > 5%

Exposição Fiscal: Baseado nas Notas Fiscais de Vendas \- Considerando quantidade total dos métodos/mesmas grandezas

Obs: O sistema deverá apresentar no campo “\(U\) Margem de Lucro” o valor da porcentagem conforme definido na RN01 do documento “MTZ \- Transfer Pricing \- Aba Cadastro \- Lei 12\.715\_12\.docx”

OS3645

__RN23__

Aba __Importações__:

Criação dos Links \(menus\) com o título “__PRL Lei 12\.715/12__” e com as seguintes descrições:

__“Dec\. De Importação”__

__“Saldos de Estoques”__

__“Comp\. Produtos”__

__“Custos Contábeis”__

__“Notas Fiscais”__

OS3645

__RN24__

__No Link \(menu\) “Dec\. De Importação” deverá conter os seguintes Campos/CheckBox/ComboBox/Botões:__

Número do DI: Número de identificação que consta na Declaração de Importação

Empresa Destino

Data da DI

Contendo produto

Filtrar

OS3645/MFS\-651

__RN25__

Para o campo “__Número do DI__”: Número que consta na Declaração de Importação

Se não preenchido: O sistema deverá possibilitar a visualização de todas as Declarações de Importação previamente cadastradas/integradas que poderão ser utilizadas como filtro\.

Se preenchido: O sistema deverá possibilitar a visualização somente da Declaração de Importação previamente cadastrada/Integrada que poderá ser utilizada como filtro\.

OS3645/MFS\-651

__RN26__

Para o parâmetro “__Empresa Destino__”, o sistema deverá possibilitar a escolha da empresa \(que está recebendo o produto importado\) previamente cadastrada que será utilizado como filtro\.

OS3645/MFS\-651

__RN27__

Para o parâmetro “__Data da DI__”: Data que consta na Declaração de Importação

Opção para obter a visualização das Declarações de Importação previamente cadastradas através do preenchimento do ComboBox “Período”:

Se o ComboBox “Período” não estiver preenchido, o sistema deverá possibilitar a visualização de todas as Declarações de Importação previamente cadastradas/integradas que poderão ser utilizadas como filtro\.

Se o ComboBox “Período” estiver preenchido com as opções do título “Corrente”, o sistema deverá preencher automaticamente os campos “De” e “a” de acordo com as respectivas opões “Semana Corrente”, “Mês Corrente”, “Trimestre Corrente”, “Semestre Corrente”, e “Ano Corrente”, e possibilitar a visualização somente das Declarações de Importação previamente cadastradas/Integradas que poderão ser utilizadas como filtro\.

Se o ComboBox “Período” estiver preenchido com as opções do título “Passada”, o sistema deverá preencher automaticamente os campos “De” e “a” de acordo com as respectivas opões “Semana Passada”, “Mês Passado”, “Trimestre Passado” “Semestre Passado”, e “Ano Passado”, e possibilitar a visualização somente das Declarações de Importação previamente cadastradas/Integradas que poderão ser utilizadas como filtro\.

Se o ComboBox “Período” estiver preenchido com as opções do título “Próximo”, o sistema deverá preencher automaticamente os campos “De” e “a” de acordo com as respectivas datas “Próxima Semana”, “ Próximo Mês”, “Próximo Trimestre ”, “Próximo Semestre”, e “Próximo Ano”, e possibilitar a visualização somente das Declarações de Importação previamente cadastradas/Integradas que poderão ser utilizadas como filtro\.

Opção para obter a visualização das Declarações de Importação previamente cadastradas através do preenchimento dos campos “De” e “a”:

Este campo devera ser preenchido somente quando o usuário não optar por nenhuma das opções de preenchimento do ComboBox “Período”

Se o usuário digitar um período nos campos “De” e “a”, ex: dd/mm/aaaa, o sistema deverá possibilitar a visualização das Declarações de Importação previamente cadastradas somente do período escolhido que será utilizado como filtro\.

OS3645/MFS\-651

__RN28__

Parâmetro “__Contendo produto__”: Identificar produto a ser consultado no Documento Fiscal, desenvolvido na seguinte composição de possibilidades de filtros:  


Campo: “Empresa ou estabelecimento” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

Campo: “Código”   
  
Se preenchido: O sistema deverá possibilitar a visualização somente do Produto que contém o código informado, previamente cadastrado/Integrado que poderá ser utilizado como filtro\.

  
Campo: “Descrição” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

OS3645/MFS\-651

__RN29__

Para o botão “__Filtrar__” o sistema deverá trazer todas as Declarações de Importação de acordo com os filtros utilizados\. Caso não seja utilizado nenhum filtro o sistema ira carregar todos as Declarações de Importação previamente cadastras/Integradas\.

OS3645/MFS\-651

__RN30__

Para o Botão “__Adicionar__” quando selecionado o usuário será direcionado para o sub\-menu “Detalhes de Declarações de Importação”, para inclusão da DI\.

OS3645

MFS\-651

__RN31__

__Adicionar: __Quando selecionado o usuário será direcionado para tela de parametrização de “Ajustes por Diferença de Condições de Negócios”

MFS\-651

__RN32__

__Detalhe de ajustes por Diferença de Condições de Negócios__

\*Os campos deverão seguir o mesmo padrão de telas existentes\. Ex: Detalhe de ajustes por Diferença de Condições de Negócios em Notas Fiscais\. \(Aba Importações, Menu Notas Fiscais\)

Para cada registro \(diário\) deverá existir um __*Sub\-Menu *__para inserção dos dados pertinentes aos ajustes permitimos pela IN 1\.312/12, os campos são:

__Item\(0 para todo o documento\);__

__Diferença por;__

__Valor da diferença; __

__Indicador Econômico; __

__Documento;__

__Tipo; __

__Data de emissão;__

MFS\-651

__RN33__

__“Item\(0 para todo o documento\)” – __ informar o número do item do Documento Fiscal para o qual se está realizando este ajuste\. Caso o ajuste de valor deva se refletir para toda a nota fiscal, independente do item, deve\-se informar 0 \(Zero\)\.

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN34__

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

Os dados pertinentes aos ajustes citados acima, deverão ser excluídos/adicionados no resultado de apuração do preço parâmetro do método PCI\.

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN35__

“__Valor da diferença__” – Informar o valor da diferença de preço\.

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN36__

“__Indicador Econômico__” \- Informar o indicador econômico\. Ex: Taxa SELIC

MFS\-651

__RN37__

“__Documento__” – Informar o documento de comprovação do ajuste realizado

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN38__

“__Tipo__” – Informar o tipo de documento de comprovação

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN39__

“__Data de emissão__” – Informar a data de emissão do documento comprobatório

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN40__

__No Link \(menu\) “Saldos de Estoques” deverá conter os seguintes Campos/ComboBox:__

Produto

Filtrar

OS3645/MFS\-651

__RN41__

Parâmetro “__Produto__”: Identificar o produto de referencia para controle do estoque a ser consultado na seguinte composição, e possibilidades de filtros:

Campo: “Empresa ou estabelecimento” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

Campo: “Código”   
  
Se preenchido: O sistema deverá possibilitar a visualização somente do Produto que contém o código informado, previamente cadastrado/Integrado que poderá ser utilizado como filtro\.

  
Campo: “Descrição” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

OS3645/MFS\-651

__RN42__

Para o botão “__Filtrar__” o sistema deverá carregar os códigos de produtos contidos no estoque de acordo com o filtro conforme instrui a RN34\. Caso não seja utilizado nenhum filtro o sistema ira carregar todos os Saldos de Estoque cadastrado\.

OS3645/MFS\-651

__RN43__

Para o Botão “__Adicionar__” quando selecionado o usuário será direcionado para o sub\-menu “Detalhes de Saldo de Estoque”, para inclusão do saldo\.

OS3645/

MFS\-651

__RN44__

__No Link \(menu\) “Comp\. Produtos” deverá conter os seguintes Campos/CheckBox/ComboBox/Botões:__

Através desta opção o usuário poderá consultar a árvore de Produção de cada um dos produtos acabados, previamente cadastrados/integrados, bem como verificar a atribuição do valor do custo contábil que se tem na produção de cada unidade deste produto acabado\. Esta informação será utilizada pelos Métodos de Cálculo: CPL e PRL LEI 12\.715/12

Produto 

Componente

Tipo 

Fornecedor 

Data 

Data da Expiração 

Filtrar 

OS3645

__RN45__

Parâmetro “__Produto__”: Visualizar o Produto Acabado para o qual se está montado a árvore de produção a ser consultado na seguinte composição, e possibilidades de filtros:

Campo: “Empresa ou estabelecimento” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

Campo: “Código”   
  
Se preenchido: O sistema deverá possibilitar a visualização somente do Produto que contém o código informado, previamente cadastrado/Integrado que poderá ser utilizado como filtro\.

  
Campo: “Descrição” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

OS3645

__RN46__

Parâmetro “__Componente__”: Visualizar  componente integrante do Produto Acabado previamente cadastrados/integrados na seguinte composição, e possibilidades de filtros:

Campo: “Empresa ou estabelecimento” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

Campo: “Código”   
  
Se preenchido: O sistema deverá possibilitar a visualização somente do Produto que contém o código informado, previamente cadastrado/Integrado que poderá ser utilizado como filtro\.

  
Campo: “Descrição” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

OS3645

__RN47__

ComboBox “__Tipo__”: Classificação deste componente, conforme previamente cadastrado/integrado na tabela de Cadastro de Produtos\.

OS3645

__RN48__

Parâmetro “__Fornecedor__”: Visualizar a Pessoa Física / Jurídica fornecedora deste componente, previamente cadastrada/integrada na seguinte composição, e possibilidades de filtros:

CNPJ: Se preenchido, o sistema ira carregar os componentes somente deste fornecedor\. Se não preenchido o sistema ira carregar todos os componentes cadastrados na base\.

Razão Social: \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\) 

OS3645

__RN49__

Para o parâmetro “__Data”: __Validade do período em se compões o Produto acabado\.

Opção para obter a visualização das datas de validades da composição do Produto Acabado previamente cadastrados/interados através do preenchimento do ComboBox “Período”:

Se o ComboBox “Período” não estiver preenchido, o sistema deverá possibilitar a visualização de todas os componentes previamente cadastrados/integrados que poderão ser utilizadas como filtro\.

Se o ComboBox “Período” estiver preenchido com as opções do título “Corrente”, o sistema deverá preencher automaticamente os campos “De” e “a” de acordo com as respectivas opões “Semana Corrente”, “Mês Corrente”, “Trimestre Corrente”, “Semestre Corrente”, e “Ano Corrente”, e possibilitar a visualização somente dos componentes cadastrados/Integrados que poderão ser utilizadas como filtro\.

Se o ComboBox “Período” estiver preenchido com as opções do título “Passada”, o sistema deverá preencher automaticamente os campos “De” e “a” de acordo com as respectivas opões “Semana Passada”, “Mês Passado”, “Trimestre Passado” “Semestre Passado”, e “Ano Passado”, e possibilitar a visualização somente dos componentes previamente cadastrados/Integrados que poderão ser utilizadas como filtro\.

Se o ComboBox “Período” estiver preenchido com as opções do título “Próximo”, o sistema deverá preencher automaticamente os campos “De” e “a” de acordo com as respectivas datas “Próxima Semana”, “ Próximo Mês”, “Próximo Trimestre ”, “Próximo Semestre”, e “Próximo Ano”, e possibilitar a visualização somente dos componentes previamente cadastrados/Integrados que poderão ser utilizadas como filtro\.

Opção para obter a visualização dos componentes previamente cadastrados/integrados através do preenchimento dos campos “De” e “a”:

Este campo devera ser preenchido somente quando o usuário não optar por nenhuma das opções de preenchimento do ComboBox “Período”

Se o usuário digitar um período nos campos “De” e “a”, ex: dd/mm/aaaa, o sistema deverá possibilitar a visualização dos componentes previamente cadastrados/integrados somente do período escolhido que será utilizado como filtro\.

OS3645

__RN50__

Para o parâmetro “__Data de expiração”: __Campo não obrigatório \(Desenvolvido para utilização futura\)\.

OS3645

__RN51__

Para o botão “__Filtrar__” o sistema deverá trazer somente os componentes de acordo com os filtros utilizados\. Caso não seja utilizado nenhum filtro o sistema ira carregar todos componentes previamente cadastras/Integradas no sistema\.

OS3645

__RN52__

__No Link \(menu\) “Custos Contábeis” deverá conter os seguintes Campos/ComboBox:__

Produto 

Data 

OS3645

__RN53__

Parâmetro “__Produto__”: Visualizar o custo contábil do Produto a ser consultado na seguinte composição, e possibilidades de filtros:

Campo: “Empresa ou estabelecimento” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

Campo: “Código”   
  
Se preenchido: O sistema deverá possibilitar a visualização somente o custo do Produto que contém o código informado, previamente cadastrado/Integrado que poderá ser utilizado como filtro\.

  
Campo: “Descrição” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

OS3645

__RN54__

Para o parâmetro “__Data”: __Validade do custo contábil do Produto\.

Opção para obter a visualização das datas de validades do custo contábil do Produto previamente cadastrados/interados através do preenchimento do ComboBox “Período”:

Se o ComboBox “Período” não estiver preenchido, o sistema deverá possibilitar a visualização de todos os custos contábeis dos produtos previamente cadastrados/integrados que poderão ser utilizadas como filtro\.

Se o ComboBox “Período” estiver preenchido com as opções do título “Corrente”, o sistema deverá preencher automaticamente os campos “De” e “a” de acordo com as respectivas opões “Semana Corrente”, “Mês Corrente”, “Trimestre Corrente”, “Semestre Corrente”, e “Ano Corrente”, e possibilitar a visualização somente dos custos contábeis dos produtos cadastrados/Integrados que poderão ser utilizadas como filtro\.

Se o ComboBox “Período” estiver preenchido com as opções do título “Passada”, o sistema deverá preencher automaticamente os campos “De” e “a” de acordo com as respectivas opões “Semana Passada”, “Mês Passado”, “Trimestre Passado” “Semestre Passado”, e “Ano Passado”, e possibilitar a visualização somente dos custos contábeis dos produtos previamente cadastrados/Integrados que poderão ser utilizadas como filtro\.

Se o ComboBox “Período” estiver preenchido com as opções do título “Próximo”, o sistema deverá preencher automaticamente os campos “De” e “a” de acordo com as respectivas datas “Próxima Semana”, “ Próximo Mês”, “Próximo Trimestre ”, “Próximo Semestre”, e “Próximo Ano”, e possibilitar a visualização somente dos custos contábeis dos produtos previamente cadastrados/Integrados que poderão ser utilizadas como filtro\.

Opção para obter a visualização dos custos contábeis dos produtos previamente cadastrados/integrados através do preenchimento dos campos “De” e “a”:

Este campo devera ser preenchido somente quando o usuário não optar por nenhuma das opções de preenchimento do ComboBox “Período”

Se o usuário digitar um período nos campos “De” e “a”, ex: dd/mm/aaaa, o sistema deverá possibilitar a visualização dos custos contábeis previamente cadastrados/integrados somente do período escolhido que será utilizado como filtro\.

OS3645

__RN55__

__No Link \(menu\) “Notas Fiscais” deverá conter os seguintes Campos/CheckBox/ComboBox/Botões:__

Número do Doc\. Fiscal 

Empresa Origem

Cliente

Data de Emissão

Série

Tipo de Doc\. Fiscal

Contendo produto: __\[Ver RN05\]__

Filtrar

OS3645

MFS\-651

__RN56__

Para o campo “__Número do Doc\. Fiscal__”: Número de documento do item a ser consultado

Se não preenchido: O sistema deverá possibilitar a visualização de todas as Notas Fiscais previamente cadastradas/integradas que poderão ser utilizadas como filtro\.

Se preenchido: O sistema deverá possibilitar a visualização somente da Nota fiscal previamente cadastrada/Integrada que poderá ser utilizada como filtro\.

OS3645

MFS\-651

__RN57__

Parâmetro “__Empresa Origem__”: Visualizar o emitente do documento fiscal, previamente cadastrada/integrada na seguinte composição, e possibilidades de filtros:

CNPJ: Se preenchido, o sistema ira carregar os componentes somente deste emitente\. Se não preenchido o sistema ira carregar todos os emitentes cadastrados na base\.

Razão Social: \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\) 

OS3645

MFS\-651

__RN58__

Parâmetro “__Cliente__”: Visualizar o cliente descrito no documento fiscal, previamente cadastrada/integrada na seguinte composição, e possibilidades de filtros:

CNPJ: Se preenchido, o sistema ira carregar os componentes somente deste cliente\. Se não preenchido o sistema ira carregar todos os clientes cadastrados na base\.

Razão Social: \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\) 

OS3645

MFS\-651

__RN59__

Para o parâmetro “__Data Emissão__”: Data em foi emitido o documento fiscal\.

Opção para obter a visualização das Notas Fiscais previamente cadastradas através do preenchimento do ComboBox “Período”:

Se o ComboBox “Período” não estiver preenchido, o sistema deverá possibilitar a visualização de todas as Notas Fiscais previamente cadastradas/integradas que poderão ser utilizadas como filtro\.

Se o ComboBox “Período” estiver preenchido com as opções do título “Corrente”, o sistema deverá preencher automaticamente os campos “De” e “a” de acordo com as respectivas opões “Semana Corrente”, “Mês Corrente”, “Trimestre Corrente”, “Semestre Corrente”, e “Ano Corrente”, e possibilitar a visualização somente das Notas Fiscais previamente cadastradas/Integradas que poderão ser utilizadas como filtro\.

Se o ComboBox “Período” estiver preenchido com as opções do título “Passada”, o sistema deverá preencher automaticamente os campos “De” e “a” de acordo com as respectivas opões “Semana Passada”, “Mês Passado”, “Trimestre Passado” “Semestre Passado”, e “Ano Passado”, e possibilitar a visualização somente das Notas Fiscais previamente cadastradas/Integradas que poderão ser utilizadas como filtro\.

Se o ComboBox “Período” estiver preenchido com as opções do título “Próximo”, o sistema deverá preencher automaticamente os campos “De” e “a” de acordo com as respectivas datas “Próxima Semana”, “ Próximo Mês”, “Próximo Trimestre ”, “Próximo Semestre”, e “Próximo Ano”, e possibilitar a visualização somente das Notas Fiscais previamente cadastradas/Integradas que poderão ser utilizadas como filtro\.

Opção para obter a visualização das Notas Fiscais previamente cadastradas através do preenchimento dos campos “De” e “a”:

Este campo devera ser preenchido somente quando o usuário não optar por nenhuma das opções de preenchimento do ComboBox “Período”

Se o usuário digitar um período nos campos “De” e “a”, ex: dd/mm/aaaa, o sistema deverá possibilitar a visualização das Notas Fiscais previamente cadastradas somente do período escolhido que será utilizado como filtro\.

OS3645

MFS\-651

__RN60__

Para o parâmetro “__Série”: __Série do documento fiscal a ser consultado\. Este campo foi desenvolvido apenas para complementar as opções de filtragem\.

OS3645

MFS\-651

__RN61__

Para o parâmetro “__Tipo de Documento Fiscal__”: Selecionar através das opções Combo/Box: “Todas \(as\)”, “NF Entradas” ou “NF Saídas”, para complementar as opções de filtragem\.

OS3645

MFS\-651

__RN62__

Para o botão “__Filtrar__” o sistema deverá trazer todas as Notas Fiscais de acordo com os filtros utilizados\. Caso não seja utilizado nenhum filtro o sistema ira carregar todas as Notas Fiscais previamente cadastras/Integradas\.

OS3645

MFS\-651

__RN63__

Aba __Importações__:

Criação dos Links \(menus\) com o título “__PCI__” e com as seguintes descrições:

__“Declaração de Importação”__

__“Saldos de Estoque”__

__“Produtos Similares”__

__“Notas Fiscais”__

__“Cotação em Bolsa – Commodities”__

MFS\-651

__RN64__

__No Link \(menu\) “Produtos Similares” deverá conter os seguintes Campos/CheckBox/ComboBox/Botões:__

Produto 

Produto Similar

Seguir o mesmo padrão de tela já existente\. Ex: PIC >> Produtos Similares

MFS\-651

__RN65__

Parâmetro “__Produto__”: Identificar o produto de referencia para controle do estoque a ser consultado na seguinte composição, e possibilidades de filtros:

Campo: “Empresa ou estabelecimento” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

Campo: “Código”   
  
Se preenchido: O sistema deverá possibilitar a visualização somente do Produto que contém o código informado, previamente cadastrado/Integrado que poderá ser utilizado como filtro\.

  
Campo: “Descrição” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

MFS\-651

__RN66__

Parâmetro “__Produto Similar__”: Identificar o produto de referencia para controle do estoque a ser consultado na seguinte composição, e possibilidades de filtros:

Campo: “Empresa ou estabelecimento” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

Campo: “Código”   
  
Se preenchido: O sistema deverá possibilitar a visualização somente do Produto que contém o código informado, previamente cadastrado/Integrado que poderá ser utilizado como filtro\.

  
Campo: “Descrição” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

MFS\-651

__RN67__

Para o botão “__Filtrar__” o sistema deverá carregar os códigos de produtos e produtos similar contidos no estoque de acordo com o filtro\. Caso não seja utilizado nenhum filtro o sistema ira carregar todos cadastrados\.

MFS\-651

__RN68__

Para o Botão “__Adicionar__” quando selecionado o usuário será direcionado para o sub\-menu “Detalhes de Produtos Similares”, para inclusão do Produto\.

MFS\-651

__RN69__

No menu: Importações >> PCI \(Criação de Link com as seguintes descrição\):

__Cotação em Bolsa – Commodities__

\*Os campos deverão seguir o mesmo padrão de telas existentes\.

Para atendimento à IN 1312/12 deverá ser criada uma nova tela para inserção, visualização e edição das informações pertinentes aos valores de cotação de commodities contendo os seguintes campos:

__Produto__

__Data__

MFS\-651

__RN70__

Parâmetro “__Produto__”: Visualizar a cotação do produto a ser consultado na seguinte composição, e possibilidades de filtros:

Campo: “Empresa ou estabelecimento” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

Campo: “Código”   
  
Se preenchido: O sistema deverá possibilitar a visualização somente o custo do Produto que contém o código informado, previamente cadastrado/Integrado que poderá ser utilizado como filtro\.

  
Campo: “Descrição” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

MFS\-651

__RN71__

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

__RN72__

Para o botão “__Filtrar__” o sistema deverá trazer somente as cotações de acordo com os filtros utilizados\. Caso não seja utilizado nenhum filtro o sistema ira carregar todas as cotações previamente cadastras/integradas no sistema\.

MFS\-651

__RN73__

__Botão Adicionar: __Quando selecionado o usuário será direcionado para tela de parametrização de Detalhes de Cotação de Commodities\.

MFS\-651

__RN74__

__Detalhes de Cotação de Commodities\.__

\*Os campos deverão seguir o mesmo padrão de telas existentes\.

Para cada registro \(por produto\) deverá existir um __*Sub\-Menu *__para inserção dos dados correspondentes aos valores de cotação e moeda, os campos são:

__Produto__

__Data__

__Preço__

__Moeda__

__Unidade__

MFS\-651

__RN75__

“__Produto__”: Visualizar o detalhe do preço do produto a ser consultado na seguinte composição, e possibilidades de filtros:

Campo: “Empresa ou estabelecimento” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

Campo: “Código”   
  
Se preenchido: O sistema deverá possibilitar a visualização somente o custo do Produto que contém o código informado, previamente cadastrado/Integrado que poderá ser utilizado como filtro\.

  
Campo: “Descrição” \(habilitado somente para pesquisa através do ComboBox do lado direito da tela\)

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN76__

__“Data”: __Informar a data para inclusão dos dados de detalhe de preços\.

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN77__

__“Preço”: __Informar o preço obtido através de instituição de pesquisa para inclusão dos dados de detalhe de Cotação de Commodities\. 

MFS\-651

__RN78__

“__Moeda__”: Serão listadas as moedas, conforme cadastro na Aba “Cadastro” menu “Moedas”

Campo obrigatório de preenchimento, se não preenchido, exibir mensagem padrão\.

MFS\-651

__RN79__

“__Unidade__”: Serão listadas as unidades, conforme cadastro na Aba “Cadastro” menu “Unidade”

MFS\-651

__RN80__

No menu: Importações >> Res\. Importações \(Ao selecionar o resultado de cálculo para um produto controlado pelo __PCI e clicar na lupa existente no lado esquerdo da tela__\):

Deve\-se apresentar o resultado somente do produto em análise a exemplo do que já ocorre com os demais métodos;

MFS\-651

__RN81__

No menu: Importações >> Res\. Importações \(Ao selecionar o resultado de cálculo para um produto controlado pelo __PCI e clicar na lupa existente ao lado da informação “preço praticado”__\):

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

Na sequência da mesma tela, o sistema devera disponibilizar a linha: “__Tipo de custo de aquisição: Custo do Produto \+ Frete \+ Imp\. Importação \+ Outras Despesas\.__

Os tipos acima são apenas exemplos, os tipos de custos serão apresentados conforme parametrização na tela de “Parâmetros de Cálculo” na aba Cadastros\.

Abaixo, o sistema devera disponibilizar a visualização dos valores das seguintes informações do cálculo que foram executadas através da Aba “__Processar Cálculo__”, conforme as RNs descritas no documento “do documento__ __“__MTZ \- Transfer Pricing \- Preço Praticado \- Método PCI\.docx__”__\.__ :

![](data:image/png;base64,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)

MFS\-651

__RN82__

No menu: Importações >> Res\. Importações \(Ao selecionar o resultado de cálculo para um produto controlado pelo __PCI e clicar na lupa existente ao lado da informação “preço parâmetro”__\):

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

“__Método__”: PCI

Na sequência da mesma tela, o sistema devera disponibilizar a linha: __Resultado proveniente de:__

Abaixo, o sistema devera disponibilizar a visualização dos valores das seguintes informações do cálculo que foram executadas através da Aba “__Processar Cálculo__”, conforme as RNs descritas no documento “do documento__ __“__MTZ \- Transfer Pricing \- Preço Parâmetro \- Método PCI\.docx__”__\.__ :

![](data:image/png;base64,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)

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


# MTZ_Transfer_Pricing_Preco_Parametro_Producao_Metodo_PRL_Lei_12715_12

- **Fonte:** MTZ_Transfer_Pricing_Preco_Parametro_Producao_Metodo_PRL_Lei_12715_12.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 44 KB

---

# Módulo \- Transfer Pricing \- Cálculo do Preço Parâmetro Produção \- Lei 12\.715/12

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3645

Conversão da Medida Provisória Nº 563/12 na* *Lei 12\.715/12 \- “Plano Brasil Maior”

Esse documento contempla as regras definidas para o Cálculo do Preço Parâmetro Produção \(Componentes importados para utilização em um produto acabado\) para atendimento a Lei 12\.715/12 do produto Transfer Pricing/Mastersaf\.

OS4404

Alteração do Produto

Criação da linha de Outros Ajustes

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Através do comando “__Executar__” da __Aba Processar Cálculo__, para processar o __Preço Parâmetro Produção __\(Componentes importados para utilização em um produto acabado\) no __Método PRL Rev LEI12\.715/12__, o sistema deverá verificar as seguintes condições no cadastro do produto disponível na __Aba Cadastro 🡪 Produtos:__

- Se o “flag” “__Calcula PRL Rev Lei 12\.715/12__” está marcado 
- Se o “flag” __Margem \(PRL Lei 12\.715\)__ está preenchido com a definição pelo usuário dos percentuais 40%, 30% ou 20%  de acordo com o setor de atividade econômica, conforme instrui o parágrafo 12 do Artigo 18 da Lei 12\.715/12\.

__       __

Caso as condições acima sejam atendidas, o sistema deverá processar as informações descritas nas regras seguintes e deverão ser disponibilizadas para visualização de acordo com as definições do link “__Res\. Importações__” descritas nas RNs __ __do documento__ “MTZ \- Transfer Pricing \- Aba Importação \- Lei 12\.715\_12”\.__

As informações das regras seguintes deverão ser processadas contemplando o período conforme definido na opção “__Define Ano de Referência”__ disponível na aba Admin\. 

OS3645

__RN01__

__ISS:__

O sistema devera calcular a soma individualmente por código do campo “__vliss__”__ __da__ __tabela “__docfisit__”__\.__

OS3645

__RN02__

__ICMS:__

O sistema devera calcular a soma individualmente por código do campo “__vlicms__”__ __da__ __tabela “__docfisit__”__\.__

OS3645

__RN03__

__PIS/Pasep:__

O sistema devera calcular a soma individualmente por código do campo “__vlpis__”__ __da__ __tabela “__docfisit__”__\.__

OS3645

__RN04__

__COFINS:__

O sistema devera calcular a soma individualmente por código do campo “__vlcofins__”__ __da__ __tabela “__docfisit__”__\.__

OS3645

__RN05__

__Imposto Sobre Vendas = ISS \+ ICMS \+ PIS/Pasep \+ Cofins__

OS3645

__RN06__

__Total de Vendas:__

O sistema devera calcular a soma individualmente por código do campo “__vltotal__”__ __da__ __tabela “__docimpt__”\.

OS3645

__RN07__

__Ajustes por prazo de pagamento:__

Para processar este campo, o sistema deverá calcular a soma individualmente por código do produto__ __somente se o contribuinte possuir Ajustes por Diferenças de Condições de Negócio em Notas, em que é necessário que seja efetuado o cadastro de forma manual do valor ajustado na Aba Importação 🡪 Notas Fiscais, o campo “Diferença por” preenchido com conteúdo igual a " Ajustes por prazo de pagamento"__\.__

OS3645

OS4404

__RN07\.1__

__Outros Ajustes:__

Para processar este campo, o sistema deverá calcular a soma individualmente por código do produto__ __somente se o contribuinte possuir Ajustes por Diferenças de Condições de Negócio em Notas, em que é necessário que seja efetuado o cadastro de forma manual do valor ajustado na Aba Importação 🡪 Notas Fiscais, o campo “Diferença por” preenchido com conteúdo diferente de " Ajustes por prazo de pagamento"__\.__

OS4404

__RN08__

__Descontos Incondicionais:__

O sistema devera calcular a soma individualmente por código do campo “__vldesconto__”__ __da__ __tabela “__docfisit__”__\.__

OS3645

__RN09__

__Comissões e Corretagens:__

O sistema devera calcular a soma individualmente por código do campo “__vlcomissoes__”__ __da__ __tabela “__docfisit__”__\.__

OS3645

__RN10__

__Total Líquido de Vendas = \(\(Total de Vendas \- Imposto Sobre Vendas\) \+ \(Ajustes por prazo de pagamento \+ Outros Ajustes \- Descontos Incondicionais \- Comissões e Corretagens\)\)__

OS3645

OS4404

__RN11__

__Custo Médio__

OS3645

__RN12__

Devera ser processada uma linha com o título “__Detalhamento de quantidades e valores por produto acabado__” com os seguintes campos exibidos um ao lado do outro na seguinte ordem:

Código

Produto

Qt\. Vend\.

Q\.U\. Prod\. 

Qt\.Pr\.Imp

Vl\. Vendas

Impostos

Descontos

Comissões 

OS3645

__RN13__

__Código: __

O sistema devera recuperar a informação do campo  “__codprod__”__ __da__ __tabela “__Produto__”__\.__

OS3645

__RN14__

__Produto__

O sistema devera recuperar a informação do campo  “__descricao__”__ __da__ __tabela “__Produto__”__\.__

OS3645

__RN15__

__Qt\. Vend:__

O sistema devera calcular a soma individualmente por código do campo “__quant__”__ __da__ __tabela “__docfisit__”__\.__

OS3645

__RN16__

__Q\.U\. Prod\.: __

O sistema devera recuperar a informação do campo  “__quantidade__”__ __da__ __tabela “__CompProduto__”__\.__

OS3645

__RN17__

__Qt\.Pr\.Imp: __

O sistema devera recuperar a informação do campo  “__quantidade__”__ __da__ __tabela “__CompProduto__”__\.__

OS3645

__RN18__

__Vl\. Vendas:__

O sistema devera calcular a soma individualmente por código do campo “__vltotal__”__ __da__ __tabela “__docimpt__”\.

OS3645

__RN19__

__Impostos = __Total da__ RN06__

OS3645

__RN20__

__Descontos = __Total da__ RN09__

OS3645

__RN21__

__Comissões = __Total da__ RN10__

O sistema devera calcular a soma individualmente por código do campo “__vlcomissoes__”__ __da__ __tabela “__docfisit__”__\.__

OS3645

__RN22__

Devera ser processada uma linha com o título “__Detalhamento de quantidades e valores por produto acabado__” com os seguintes campos exibidos um ao lado do outro na seguinte ordem:

Código

Produto

Tot\.Liq\.

CustoProd\. 

Ind\.Part\.

Vl\. Part\.

Preço Parâmetro

OS3645

__RN23__

__Código: __

O sistema devera recuperar a informação do campo  “__codprod__”__ __da__ __tabela “__Produto__”__\.__

OS3645

__RN24__

__Produto__

O sistema devera recuperar a informação do campo  “__descricao__”__ __da__ __tabela “__Produto__”__\.__

OS3645

__RN25__

__Tot\.Liq\. = __Total de__ RN11__

OS3645

__RN26__

__CustoProd\.: __

O sistema deverá recuperar a soma do campo__ “valor” __da tabela__ “cpprod” __dividindo a quantidade de meses informados para o ano em que esta sendo efetuado o cálculo\.

Ex: Jan       80,00

      Jan       70,00

      Fev     100,00

      Mar     120,00

       Jul     160,00

       Jul     140,00

      Out     110,00

      Nov      90,00

    Total =     870,00 / 6 \(meses\)   Custo Médio Ponderado = 145,00

Caso não exista informação, deverá ser considerado o mesmo valor__ __calculado para o __“Preço Praticado”__

Deverá ser processado o mesmo valor calculado para o __“Preço Praticado”__

OS3645 

__RN27__

__Ind\.Part\. = \(\(Custo Médio / Cust\.Prod\) \* \(Q\.U\.Prod\.\)\)__

OS3645

__RN28__

__Vl\. Part\. =  \(Tot\.Liq\. \* Ind\.Part\.\) __

OS3645

__RN29__

__\[ALTERADO – CH2977\_2014\] Preço Parâmetro \(R1\) = \(Valor de Participação – Margem de Lucro\) / Qt\.Pr\.Imp__

__OBS: __A Margem de Lucro deverá ser referente ao Produto Importado

OS3645

CH2977\_2014

__RN30__

__Quantidade total = __Total da __RN16__

OS3645

__RN31__

__Quantidade em Notas Fiscais de saídas não Onerosas: __

O sistema devera calcular a soma individualmente por código do campo “__quant__”__ __da__ __tabela “__docfisit__”__, __considerando somente os itens das notas fiscais, cujo CFOP não estiver definido como doação\.

OS3645

__RN32__

__Total de Vendas = __Total da__ RN29__

OS3645

__RN33__

__Margem de Lucro = \(\(Total de Vendas \* % __informado no campo__ __“__margprllei12715__”__ __da tabela__ “Produtos”__

OS3645

__RN34__

__Preço Parâmetro Total = \(Total de Vendas \- Margem de Lucro\)__

OS3645

__RN35__

__Quantidade Vendida = __Total de__ RN31__

OS3645

__RN36__

__Preço Parâmetro =  \(Preço Parâmetro Total / Quantidade Vendida\)__

OS3645

__RN37__

__Preço Praticado = Custo Médio__

OS3645

__RN38__

__Margem de Divergência = \(\(Preço Praticado \- Preço Parâmetro\) / Preço Praticado\) \* 100__

OS3645

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


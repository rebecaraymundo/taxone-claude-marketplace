# MTZ_Transfer_Pricing_Preco_Prarametro_Revenda_Metodo_PRL_Lei_12715_12

- **Fonte:** MTZ_Transfer_Pricing_Preco_Prarametro_Revenda_Metodo_PRL_Lei_12715_12.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 44 KB

---

# Módulo \- Transfer Pricing \- Cálculo do Preço Parâmetro Revenda \- Lei 12\.715/12

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3645

Conversão da Medida Provisória Nº 563/12 na* *Lei 12\.715/12 \- “Plano Brasil Maior”

Esse documento contempla as regras definidas para o Cálculo do Preço Parâmetro para atendimento a Lei 12\.715/12 do produto Transfer Pricing/Mastersaf\.

OS4404

Alteração do Produto

Criação da linha de Outros Ajustes

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Através do comando “__Executar__” da __Aba Processar Cálculo__, para processar o __Preço Parâmetro__ no __Método PRL LEI12\.715/12__, o sistema deverá verificar as seguintes condições no cadastro do produto disponível na __Aba Cadastro 🡪 Produtos:__

- Se o “flag” “__Calcula PRL Lei 12\.715/12__” está marcado 
- Se o “flag” __Margem \(PRL Lei 12\.715\)__ está preenchido com a definição pelo usuário dos percentuais 40%, 30% ou 20%  de acordo com o setor de atividade econômica, conforme instrui o parágrafo 12 do Artigo 18 da Lei 12\.715/12\.

Em caso positivo, deverá processar as informações descritas nas regras seguintes e deverão ser disponibilizadas para visualização de acordo com as definições do link “__Res\. Importações__” descritas nas RNs 00 à 22 do documento__ “MTZ \- Transfer Pricing \- Aba Importação \- Lei 12\.715\_12”\.__

As informações das regras seguintes deverão ser processadas contemplando o período conforme definido na opção “__Define Ano de Referência”__ disponível na aba Admin\. 

OS3645

__RN01__

Devera ser processada uma linha com o título “__Detalhamento de revenda do produto__” com os seguintes campos exibidos um ao lado do outro na seguinte ordem:

Código

Produto

Vlr Vendas

Descontos

Embalagem

Emb\. \(doações\)

Aj\. Pr\. Pag\.

ICMS

PIS

COFINS

ISS

Comissões

Quant\. Vend

Quant\. Doa

Unidade

Q\. Vend\. Prod\.

Doa Prod\.

OS3645

__RN02__

__Código: __

O sistema devera recuperar a informação do campo  “__codprod__”__ __da__ __tabela “__Produto__”__\.__

OS3645

__RN03__

__Produto__

O sistema devera recuperar a informação do campo  “__descricao__”__ __da__ __tabela “__Produto__”__\.__

OS3645

__RN04__

__VIr Vendas:__

O sistema devera calcular a soma individualmente por código do campo “__vltotal__”__ __da__ __tabela “__docimpt__”\.

OS3645

__RN05__

__Descontos:__

O sistema devera calcular a soma individualmente por código do campo “__vldesconto__”__ __da__ __tabela “__docfisit__”__\.__

OS3645

__RN06__

__Embalagem:__

O sistema devera calcular a soma individualmente por código do campo “__quant__”__ __do cadastro de Reacondicionamento__\.__

OS3645

__RN07__

__Emb\. \(doações\):__

Para o sistema disponibilizar a visualização deste campo, é necessário que seja efetuado o pré\-cadastro do CFOP relacionado a doações na Aba Cadastro 🡪 CFOPs com tratamento especial, então, o sistema devera calcular a soma individualmente por código do campo “__cfop__”__ __da__ __tabela “__docfisit__”__\.__

OS3645

__RN08__

__Aj\. Pr\. Pag\.:__

Para processar este campo, o sistema deverá calcular a soma individualmente por código do produto__ __somente se o contribuinte possuir Ajustes por Diferenças de Condições de Negócio em Notas, em que é necessário que seja efetuado o cadastro de forma manual do valor ajustado na Aba Importação 🡪 Notas Fiscais, o campo “Diferença por” preenchido com conteúdo igual a " Ajustes por prazo de pagamento"__\.__

OS3645

OS4404

__RN08\.1__

__Aj\. Pr\. Pag\.:__

Para processar este campo, o sistema deverá calcular a soma individualmente por código do produto__ __somente se o contribuinte possuir Ajustes por Diferenças de Condições de Negócio em Notas, em que é necessário que seja efetuado o cadastro de forma manual do valor ajustado na Aba Importação 🡪 Notas Fiscais, o campo “Diferença por” preenchido com conteúdo diferente de " Ajustes por prazo de pagamento"__\.__

OS4404

__RN09__

__ICMS:__

O sistema devera calcular a soma individualmente por código do campo “__vlicms__”__ __da__ __tabela “__docfisit__”__\.__

OS3645

__RN10__

__PIS:__

O sistema devera calcular a soma individualmente por código do campo “__vlpis__”__ __da__ __tabela “__docfisit__”__\.__

OS3645

__RN11__

__COFINS:__

O sistema devera calcular a soma individualmente por código do campo “__vlcofins__”__ __da__ __tabela “__docfisit__”__\.__

OS3645

__RN12__

__ISS:__

O sistema devera calcular a soma individualmente por código do campo “__vliss__”__ __da__ __tabela “__docfisit__”__\.__

OS3645

__RN13__

__Comissões:__

O sistema devera calcular a soma individualmente por código do campo “__vlcomissoes__”__ __da__ __tabela “__docfisit__”__\.__

OS3645

__RN14__

__Quant\. Vend:__

O sistema devera calcular a soma individualmente por código do campo “__quant__”__ __da__ __tabela “__docfisit__”__, __considerando somente os itens das notas fiscais, cujo CFOP não estiver definido como doação\.

OS3645

__RN15__

__Quant\. Doa:__

O sistema devera calcular a soma individualmente por código do campo “__quant__”__ __da__ __tabela “__docfisit__”__, __considerando somente os itens das notas fiscais, cujo CFOP estiver definido como doação

OS3645

__RN16__

__Unidade:__

O sistema devera calcular a soma individualmente por código do campo “__unidade__”__ __da__ __tabela “__docfisit__”__\.__

OS3645

__RN17__

__Q\. Vend\. Prod\.:__

O sistema devera calcular a soma individualmente por código do campo “__quant__”__ __da__ __tabela “__docfisit__”__, __considerando somente os itens das notas fiscais, cujo CFOP não estiver definido como doação\.

OS3645

__RN18__

__Doa Prod\.:__

O sistema devera calcular a soma individualmente por código do campo “__quant__”__ __da__ __tabela “__docfisit__”__, __considerando somente os itens das notas fiscais, cujo CFOP estiver definido como doação__\.__

OS3645

__RN19__

__Custo Médio:__

Deverá ser processado o mesmo valor calculado para o __“Preço Praticado”__

OS3645

__RN20__

__ISS = __Total da__ RN12__

OS3645

__RN21__

__ICMS = __Total da__ RN09__

OS3645

__RN23__

__PIS/Pasep = __Total da__ RN10__

OS3645

__RN24__

__Cofins = __Total de__ RN11__

OS3645

__RN25__

__Imposto Sobre Vendas = ISS \+ ICMS \+ PIS/Pasep \+ Cofins__

OS3645

__RN26__

__Quantidade total = __Total da __RN14 __

OS3645

__RN27__

__Quantidade em Notas Fiscais de saídas não Onerosas:__

O sistema devera calcular a soma individualmente por código do campo “__quant__”__ __da__ __tabela “__docfisit__”__, __considerando somente os itens das notas fiscais, cujo CFOP não estiver definido como doação\.

OS3645

__RN28__

__Custo Total de Embalagem = __Total da__ RN06__

OS3645

__RN29__

__Custo de Embalagens em Doações = __Total da__ RN07__

OS3645

__RN30__

__Total de Vendas = __Total da__ RN04__

OS3645

__RN31__

__Custos de Embalagem = Custo Total de Embalagem \- Custo de Embalagens em Doações__

OS3645

__RN32__

__Ajustes por prazo de pagamento = __Total da__ RN08__

OS3645

__RN32\.1__

__Outros Ajustes = __Total da__ RN08\.1__

OS4404

__RN33__

__Imposto Sobre Vendas = __Total da__ RN25__

OS3645

__RN34__

__Descontos Incondicionais = __Total da__ RN05__

OS3645

__RN35__

__Comissões e Corretagens = __Total da__ RN13__

OS3645

__RN36__

__Total de Venda Líquida = Total de Vendas \- Imposto Sobre venda \- Descontos Incondicionais \- Comissões e Corretagens__

OS3645

__RN37__

__C\.Med\.Pond\.__

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

OS3645 

__RN38__

__Percentual de Participação = Custo Médio / C\.Med\.Pond\.__

OS3645

__RN39__

__Valor de participação = \(Total de Venda Líquida\) x \(Percentual de Participação\)__

OS3645

__RN40__

__Margem de Lucro = \(Valor de participação\) \* \(Margem \(PRL Lei 12\.715/12\)\* \) __da tabela__ “Produtos” __

OS3645

__RN41__

__Preço Parâmetro Total = \(Valor de participação\) \- \(Margem de Lucro\)__

OS3645

__RN42__

__Quantidade Total Revendida = __Total da__ RN26__

OS3645

__RN43__

__Preço Parâmetro =  \(Preço Parâmetro Total\) / \(Quantidade Total Revendida\)__

OS3645

__RN44__

__Preço Praticado = __Valor encontrado conforme__ RN13 __do documento__ “MTZ \- Transfer Pricing \- Preço Praticado \- Método PRL Lei 12\.715\_12”__

OS3645

__RN45__

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


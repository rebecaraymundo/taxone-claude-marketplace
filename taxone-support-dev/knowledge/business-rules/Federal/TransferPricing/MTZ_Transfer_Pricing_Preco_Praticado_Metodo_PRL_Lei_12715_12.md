# MTZ_Transfer_Pricing_Preco_Praticado_Metodo_PRL_Lei_12715_12

- **Fonte:** MTZ_Transfer_Pricing_Preco_Praticado_Metodo_PRL_Lei_12715_12.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 52 KB

---

# Módulo \- Transfer Pricing \- Cálculo do Preço Praticado \- Lei 12\.715/12

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3645

Conversão da Medida Provisória Nº 563/12 na* *lei 12\.715/12 \- “Plano Brasil Maior”

Esse documento contempla as regras definidas para o Cálculo do Preço Praticado para atendimento a Lei 12\.715/12 do produto Transfer Pricing/Mastersaf\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Através do comando “__Executar__” da __Aba Processar Cálculo__, para processar o __Preço Praticado__ no Método PRL LEI12\.715/12, o sistema deverá verificar se o “flag” __Margem \(PRL Lei 12\.715\)__ \(Campo obrigatório\) do cadastro do produto disponível na __Aba Cadastro 🡪 Produtos__ está marcado\. 

A visualização dos resultados, após o processo do cálculo,  estarão disponíveis na Aba Importações 🡪 “__Res\. Importações__”, bem como definidas no documento__ “MTZ \- Transfer Pricing \- Aba Importação \- Lei 12\.715\_12”\.__

Obs: As informações das regras seguintes deverão ser processadas contemplando o período conforme definido na opção “__Define Ano de Referência”__ disponível na aba Admin\.

OS3645

__RN01__

__Quantidade de Produtos Importados:__

O sistema devera calcular a soma individualmente por código do campo “__quant__”__ __da__ __tabela “__docimpt__”__\. __ 

OS3645

__RN02__

__Saldo Inicial Estoque: __

O sistema deverá calcular a soma individualmente por código do campo “__saldo__”__ __da__ __tabela “__SaldoProduto__”__\.__

OS3645

__RN03__

__Custo Médio do Produto no Estoque __

__???__

OS3645

__RN04__

__Imposto de Importação:__

O sistema devera calcular a soma individualmente por código do campo “__vlii__”__ __da__ __tabela “__docimpt__”__\.__

OS3645

__RN05__

__Frete:__

O sistema devera calcular a soma individualmente por código do campo “__vlfrete__”__ __da__ __tabela “__docimpt__”__\.__

OS3645

__RN06__

__Seguro:__

O sistema devera calcular a soma individualmente por código do campo “__vlseguro__”__ __da__ __tabela “__docimpt__”__\.__

OS3645

__RN07__

__Despesas:__

O sistema devera calcular a soma individualmente por código do campo “__vldesp__”__ __da__ __tabela “__docimpt__”__\.__

OS3645

__RN08__

__Total de Imp\. e Desp\. \(Conforme tipo de custo\) = \(Frete\) \+ \(Seguro\)__

OS3645

__RN09__

__Valor total de Importações \(em reais\):__

O sistema devera calcular a soma individualmente por código do campo “__vltotal__”__ __da__ __tabela “__docimpt__”\.

OS3645

__RN10__

__Custo Médio Estoque = \(Saldo Inicial Estoque\) \* \(Custo Médio do Produto no Estoque\)__

OS3645

__RN11__

__Custo Total de Importação = \(Total de Imp\. e Desp\. \(Conforme tipo de custo\)\) \+ \(Valor total de Importações \(em reais\)\) \+\( Custo Médio Estoque = \(Saldo Inicial Estoque\) \* \(Custo Médio do Produto no Estoque\)\)__

OS3645

__RN12__

__Quantidade total de produtos = \(Quantidade de Produtos Importados\) \+ \(Saldo Inicial Estoque\)__

OS3645

__RN13__

__Preço Praticado = \(Custo Total de Importação = \(Total de Imp\. e Desp\. \(Conforme tipo de custo\)\) \+ \(Valor total de Importações \(em reais\)\) \+\( Custo Médio Estoque = \(Saldo Inicial Estoque\) \* \(Custo Médio do Produto no Estoque\)\)\) / \(Quantidade total de produtos = \(Quantidade de Produtos Importados\) \+ \(Saldo Inicial Estoque\)\)__

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


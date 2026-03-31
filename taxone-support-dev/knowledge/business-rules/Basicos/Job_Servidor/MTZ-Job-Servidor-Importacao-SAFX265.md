# MTZ-Job-Servidor-Importacao-SAFX265

- **Fonte:** MTZ-Job-Servidor-Importacao-SAFX265.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX265

Tabela dos Saldos Iniciais do Estoque \(Port\. CAT 42/2018\)

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS20551__

Criação da SAFX265 

Criação da SAFX265 para a importação dos saldos iniciais do estoque, para atendimento à Portaria CAT 42/2018\. 

23/08/2018

__MFS24176__

Aumento do campo valor unitário\.

Aumento da quantidade de decimais do campo Valor Unitário de 4 para 6 casas\.\.

04/02/2019

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX265__ 🡪 vide manual de layout

A SAFX265 foi criada na __MFS20551__, para a importação dos saldos iniciais do estoque dos produtos sujeitos ao ICMS\-ST\. Estes saldos são utilizados no módulo Ressarcimento e Complemento ICMS\-ST – SP \(Portaria CAT 42/2018\), para emissão da Ficha 3\.

Os saldos iniciais serão importados apenas na implantação do módulo, ou eventualmente, para novos produtos\. A partir da utilização do módulo, estes saldos passam a ser atualizados automaticamente ao final de cada período\.

__Campos que compõe a chave da tabela \(PK\):__

                    Código da Empresa \+ Código do Estabelecimento \+ Data do Saldo \+ Produto \(Indicador e Código\)

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

* \(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

Deve ser um estabelecimento do estado de São Paulo\. Caso contrário, será gravada uma mensagem de erro no log e o registro não será importado *\(“Estabelecimento inválido\. Deve ser um estabelecimento do estado de São Paulo”\)\.*

__RN03__

__Campo Data do Saldo __

Campo de preenchimento obrigatório\.

Quando não preenchido, ou quando for uma data inválida, será gravada mensagem de erro padrão e o registro não será importado\.

__RN04__

__Campo Indicador do Produto__

Campo de preenchimento obrigatório\.

Valores válidos: Deve ser um dos indicadores de produto da SAFX2013 \(1, 2, 3, 4, 5, 6, 7 ou 8\)\.

Quando não preenchido ou inválido, será gravada mensagem de erro padrão e o registro não será importado\.

__RN05__

__Campo Código do Produto__

Campo de preenchimento obrigatório\.

O indicador e o código informados, deve ser um de um produto existente na Tabela de Produtos \(SAFX2013\), considerando o Grupo a ser utilizado, de acordo com a data informada no campo “Data do Saldo”\.

Para pesquisar o produto na SAFX2013, considerar:

\-Grupo – Grupo obtido conforme regra padrão __\(\*\*\*\)__;

\-Indicador do Produto – Indicador informado no campo 04;

\-Código do Produto – Código informado neste campo \(campo 05\);

\-Validade Inicial – maior data existente, que seja <= a data informada no campo 03 \(Data do Saldo\);

__*\(\*\*\*\)*__* O *__*Grupo*__* a ser utilizado será obtido a partir da regra básica, considerando o Grupo \(Relacionamento Tabelas x Grupos\) de maior data de validade, que seja <= a data do saldo informada, e para o qual a tabela SAFX2013 esteja associada\.*

Quando o campo não for preenchido, ou o produto não existir na SAFX2013, será gravada mensagem de erro padrão e o registro não será importado\.

__RN06__

__Campo Quantidade__

Quando não preenchido, o campo será gravado com zeros\.

__RN07__

__Campo Valor Total __

Quando não preenchido, o campo será gravado com zeros\. 

__RN08__

__Campo Valor Unitário __

Quando não preenchido, o campo será gravado com zeros\. 

MFS24176: Este campo teve a quantidade de casas decimais aumentada de 4 para 6, para evitar diferenças decorrente de arredondamentos, e possibilitar maior precisão dos resultados\.

*Observação sobre o valor unitário do saldo:*

*Conceitualmente esta coluna não precisaria existir na tabela, pois é o resultado do Valor Total dividido pelo Quantidade\. No entanto, devido as regras de emissão da Ficha 3, o campo foi incluído para refletir exatamente o valor obtido no cálculo dos saldos\. Este procedimento evita a ocorrência de pequenas diferenças de decimais que possa ocorrer \(lembrando que na Ficha 3 o valor só é calculado para os movimentos de entrada, e para as saídas, o valor é sempre “copiado” da última entrada\)\.*


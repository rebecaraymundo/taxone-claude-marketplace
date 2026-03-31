# OTF_Matriz

- **Fonte:** OTF_Matriz.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 31 KB

---

# Obrigações de Tributos Federais

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

CH50401

# Demonstrativo de INSS – OTF

Atualmente os demonstrativos das retenções de INSS são tirados sem um separador de totais identificando os meses e as pessoas fis/jur\. Esse chamado trata da inclusão desses totais nos demonstrativos\.

CH50401\-A

# Demonstrativo de INSS – OTF

Inclusão de mais um quebra de totais nos demonstrativos 

CH68941

# Relatório de Tributos Federais por Empresa

Incluir mais uma opção de parametrização do relatório para que o mesmo apresente um subtotal por data de movimento e data de fato gerador\.

OS2763

# Emissão de Declaração por Centro de Custo – OTF 

Incluir mais duas opções de parametrização da emissão para que o mesmo possa filtrar por Setor e Funcionários Ativos/Demitidos\.

CH67054

# Emissão de Declaração de Rendimentos 🡪 Por CPF

Recuperar para Linha 02 do Quadro 5 no IR, o código 8053 

CH76108

# Relatórios 🡪 Comprovante/Etiqueta Anual de Retenção – PIS/COFINS/CSLL

Permitir a emissão de Comprovante Anual de Retenção \- PIS/COFINS/CSLL para CSRF

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Após a demonstração de cada pessoa jurídica terá um totalizador da “PJ”\. Porém, essas quebras do relatório deverão ser conforme o critério utilizado pelo usuário no momento da seleção das informações\.

Ex: O = Empresa \+ Estabelecimento \+ Pessoa Fis/Jur\.

Logo se o critério de geração do demonstrativo for \(competência\) o demonstrativo será organizado por ordem de Data emissão:

Por data Competência = O \+ Data de Emissão \+ Data Fiscal\.

Ou seja, o demonstrativo será organizado pela data de emissão\. Dentro das datas de emissão terá uma quebra a cada pessoa Fis/Jur diferente e quando o mês de emissão mudar, será apresentada outra quebra com o valor total daquele mês\.

CH50401

__RN01__

Após a demonstração de cada pessoa jurídica terá um totalizador da “PJ”\. Porém, essas quebras do relatório deverão ser conforme o critério utilizado pelo usuário no momento da seleção das informações\.

Ex: O = Empresa \+ Estabelecimento \+ Pessoa Fis/Jur\.

Logo se o critério de geração do demonstrativo for \(competência \+ Extemporâneo\) o demonstrativo será organizado por ordem de Data emissão:

Por data Competência \+ Extemporâneo = O \+ Data de Emissão \+ Data Fiscal\.

Ou seja, o relatório traz as notas cujo período de emissão seja diferente do período de lançamento e que ultrapasse a data limite parametrizada no sistema\. Com a alteração solicitada nesse chamado, esse mesmo resultado deverá ser organizado da seguinte forma:

O demonstrativo será organizado pela data de emissão\. Dentro das datas de emissão terá uma quebra a cada pessoa Fis/Jur diferente e quando o mês de emissão mudar, será apresentada outra quebra com o valor total daquele mês\.

CH50401

__RN02__

Após a demonstração de cada pessoa jurídica terá um totalizador da “PJ”\. Porém, essas quebras do relatório deverão ser conforme o critério utilizado pelo usuário no momento da seleção das informações\.

Ex: O = Empresa \+ Estabelecimento \+ Pessoa Fis/Jur\.

Logo se o critério de geração do demonstrativo for \(Data Fiscal\) o demonstrativo será organizado por ordem de Data de lançamento:

Por Data Fiscal = O \+ Data Fiscal \+ Data de Emissão\.

Ou seja, o relatório traz as notas cujo período de lançamento seja diferente do período de emissão, trazendo inclusive as notas que passaram da data limite parametrizada no sistema\. Com a alteração solicitada nesse chamado, esse mesmo resultado deverá ser organizado da seguinte forma:

O demonstrativo será organizado pela data de lançamento\. Dentro das datas fiscais terá uma quebra a cada pessoa Fis/Jur diferente e quando o mês de lançamento mudar, será apresentada outra quebra com o valor total daquele mês\.

CH50401

__RN03__

Após a demonstração de cada pessoa jurídica terá um totalizador da “PJ”\. Porém, essas quebras do relatório deverão ser conforme o critério utilizado pelo usuário no momento da seleção das informações\.

Ex: O = Empresa \+ Estabelecimento \+ Pessoa Fis/Jur\.

Logo se o critério de geração do demonstrativo for \(Data Fiscal \+ Extemporâneo\) o demonstrativo será organizado por ordem de Data de lançamento:

Por Data Fiscal \+ Extemporâneo = O \+ Data Fiscal \+ Data de Emissão\.

Ou seja, o relatório traz as notas cujo período de lançamento seja diferente do período de emissão e que ultrapasse a data limite parametrizada no sistema\. Com a alteração solicitada nesse chamado, esse mesmo resultado deverá ser organizado da seguinte forma:

O demonstrativo será organizado pela data de lançamento\. Dentro das datas fiscais terá uma quebra a cada pessoa Fis/Jur diferente e quando o mês de lançamento mudar, será apresentada outra quebra com o valor total daquele mês\.

CH50401

__RN04__

Ao final do relatório, independente do critério utilizado para geração do mesmo, terá um totalizador geral\. Que deverá se igual a soma dos meses apresentados no relatório\.

Obs: Essa regra será aplicada para os demonstrativos que apresentarem os totalizadores “geral e por estabelecimento”, caso exista demonstrativos que não apresentem esses totais, este não deverá ser inserido, permanecendo assim como esta\.

CH50401

__RN05__

🡺demonstrativo for competência

*Conforme regra definida RN00 \-  CH50401, com inclusão abaixo:*

Será incluso mais uma quebra conforme o mês de lançamento, ou seja o relatório terá 2 totalizadores referentes as 2 colunas de data do relatório\.

CH50401\-A

__RN06__

     

    🡺demonstrativo for competência \+ Extemporâneo

*     Conforme regra definida RN01 \-  CH50401, com inclusão abaixo:*

Será incluso mais uma quebra conforme o mês de lançamento, ou seja o relatório terá 2 totalizadores referentes as 2 colunas de data do relatório\.

CH50401\-A

__RN07__

    

   🡺demonstrativo for \(Data Fiscal\)

*   Conforme regra definida RN02 \-  CH50401, com inclusão abaixo:*

Será incluso mais uma quebra conforme o mês de emissão, ou seja o relatório terá 2 totalizadores referentes as 2 colunas de data do relatório\.

CH50401\-A

__RN08__

*    *

*    *🡺demonstrativo for Data Fiscal \+ Extemporâneo

*   Conforme regra definida RN03 \-  CH50401, com inclusão abaixo:*

Será incluso mais uma quebra conforme o mês de emissão, ou seja o relatório terá 2 totalizadores referentes as 2 colunas de data do relatório\.

CH50401\-A

__RN09__

Incluir mais uma opção \(“Utilizar Subtotal por Data”\) na tela “Emissão de Tributos \- Empresa” para que o relatório apresente um subtotal por data de movimento e data do fato gerador\. Habilitar esta opção apenas quando uma das opções “por Data do Movimento” ou “por Data do Fato Gerador” estiver selecionada\.

CH68941

__RN10__

Gerar o relatório com mais um grupamento totalizando os valores por data de pagamento ou por data do fato gerador, quando a opção “Utilizar Subtotal por Data” estiver selecionada na tela de parametrização\.

CH68941

__RN11__

O parâmetro “Setor” deverá ser um campo do tipo Pastinha recuperando todos os setores existentes seguindo os dados abaixo\.

Deverá recuperar os setores da tabela x2037\_setor, onde o grupo\_estab da tabela X2037\_SETOR seja o de maior validade na tabela relac\_tab\_grupo para a empresa e estabelecimento selecionado\. Os campos envolvidos na recuperação dos setores são: Empresa, Estabelecimento e Data Emissão da tela\.

O filtro por Setor será opcional, caso o usuário não o informe, o sistema não o irá considerar no momento de recuperar os informes de rendimentos\.

OS2763

__RN12__

Caso o usuário informe um ou mais de um range de Centro de Custos e um setor em especifico o sistema irá recuperar todos os funcionários que pertençam aquele\(s\) Centro de Custo\(s\) E Setor informado\.

OS2763

__RN13__

Caso seja escolhida a opção “Todos” no estabelecimento, o campo de Setor ficara desabilitado\.

OS2763

__RN14__

O parâmetro “Emitir Funcionarios Demitidos” deverá ser um campo do tipo check Box com o seguinte domínio: 0 – Desmarcado/ 1 – Marcado<default>\.

Este campo deverá verificar o campo “data\_demissao” da tabela x15\_funcionário\. Caso o campo esteja marcador, deverá ser considerado todos os funcionários\(Ativos e Demitidos\), caso seja desmarcado deverá ser recuperado apenas os funcionários ativos\.

OS2763

__RN15__

Na Geração de Dados para a Emissão de Declaração de Rendimentos Outros por CPF, deverá ser feita alteração na demonstração de valores, e também no Cálculo da mesma, quando o Código de Pagamento DARF for 8053 – Título de Renda Fixa – Pessoa Física\.

Na geração da tabela IRT\_CEDULA\_D, caso o COD\_DARF = 8053, deverá ser feito o seguinte cálculo:

Vlr\_Outros\_Trib\_Excl = Valor\_Rend – Irrf\_Retido;

Valor\_Rend = 0;

Conforme ex\. abaixo:

Antes:

__Quadro 3: 01\.Total dos Rendimentos \(Inclusive Férias\)	=  1\.500,00__

__Quadro 3: 05\.Imposto de Renda Retido		=       15,00__

__\.\.\.__

__Quadro 5: 02\.Outros				=         0,00__

Depois:

Quadro 3: 01\.Total dos Rendimentos \(Inclusive Férias\)	=        0,00

__Quadro 3: 05\.Imposto de Renda Retido		=      15,00__

__\.\.\.__

__Quadro 5: 02\.Outros				= 1\.485,00__

CH67054

__RN16__

No Comprovante Anual de Retenção – PIS/COFINS/CSLL, deverá ser colocada a seguinte crítica:

- Se Código de Retenção = 5952 e o Código do Tributo = 11, deverá ser emitido o comprovante pelo MasterSAF

CH76108


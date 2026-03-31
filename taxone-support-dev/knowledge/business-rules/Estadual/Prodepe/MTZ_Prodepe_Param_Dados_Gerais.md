# MTZ_Prodepe_Param_Dados_Gerais

- **Fonte:** MTZ_Prodepe_Param_Dados_Gerais.docx
- **Modificado:** 2024-06-05
- **Tamanho:** 83 KB

---

THOMSON REUTERS

                                                                                     __Módulo PRODEPE__

__  __

__                                                    Parametrização dos Dados Gerais__

__Localização__: Menu Estadual, Módulo Prodepe, item de menu Parâmetros à Dados Gerais

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS4402

Tratamento das Devoluções

Alteração do cálculo do crédito presumido para tratamento das notas fiscais de devolução de vendas 

23/01/2014

\(criação do docto\)

OS4138

Lançamentos Automáticos 

Inclusão do código de ajuste do SEF II\-PE nas telas de parametrização dos lançamentos

03/02/2014

MFS6317

Novo Parâmetro

Alteração nos parâmetros do incentivo das saídas p/fora do NE \(ver __RN02__\)\.

23/12/2016

__MFS21917__

Novo Parâmetro

Inclusão do Código de Ajuste do Sped Fiscal na parametrização dos quatro lançamentos\.

05/07/2019

REGRAS DE NEGÓCIO

__RN00__

__                                  Tratamento das Devoluções de Vendas no Rateio dos Créditos__

Campo “__Tratamento das Devoluções de Vendas no Rateio dos Créditos__”

Parâmetro criado na __OS4402__ 

Este campo apresenta duas opções *alternativas*:

                                        

![](data:image/png;base64,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)Na abertura da tela a opção default é a primeira, que aparecerá sempre marcada\.

__RN02__

__                                            Parâmetros para o Incentivo das Saídas p/fora do NE__

Alteração __MFS6317: __Retirado da tela o parâmetro “*Tipo de Documento dos CTRC’s*”, pois o incentivo das saídas p/fora do NE não utiliza mais esse parâmetro há muitos anos, desde que este incentivo deixou de ser baseado no valor do frete das operações p/fora do NE\.

Campo “__Valor base p/o cálculo do incentivo”:__       *\(campo criado na *__*MFS6317*__*\)* 

Este campo apresenta as seguintes opções:      \- Base tributada do ICMS

                                                                             \- Valor contábil do item

As opções são alternativas, e a opção default é = “*Base tributada do ICMS*”\.

Este parâmetro é utilizado na rotina de cálculo do incentivo das saídas para fora da região nordeste \(menu “Obrigações > Cálculo do Incentivo das Saídas p/fora do NE”\)\.

Campo “__Código de Ajuste SEF II – PE:__”       *\(campo criado na *__*OS4138*__*\)* 

Formato do campo: campo numérico de 3 posições, não obrigatório

Este campo é uma lista de acordo com a tabela interna  “*5\.2\.1\-Detalhamento e Ajustes da Apuração do ICMS*” do SEF II \(vide planilha de layout, aba TAB INT, item 5\.2\.1\)\.

*\(a lista apresentada terá a primeira linha em branco, pois trata\-se de campo não obrigatório\) *

*\(corresponde ao mesmo campo da tela dos lançamentos complementares do menu “Obrigações à Lançamentos Complementares”\)*

Campo “__Código de Ajuste \(Sped Fiscal \- Reg\. E111\)__”:       __*\(campo criado na MFS21917\)* __

Formato do campo: campo alfanumérico de 8 posições, não obrigatório

Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste do Sped Fiscal \(módulo ICMS, menu *Apuração à Apuração do ICMS à Lançamentos Complementares à Código de Ajuste Sped Fiscal*\)\.

Para este tipo de lançamento, serão disponibilizados apenas os *códigos* da tabela que atendam aos seguintes requisitos:

- Apenas códigos referentes a UF do Estabelecimento \(as duas primeiras posições do código = sigla da UF\);
- Apenas códigos da apuração do ICMS Próprio \(a terceira posição deve ser = “0”\);
- Apenas códigos de __créditos__ \(a quarta posição deve ser = “2”, “3” ou “4” \(Outros Créditos / Estorno de Débito / Deduções\)\); 

Quando o código for digitado, será verificada a sua existência na tabela, e também se atende aos requisitos acima\. Caso não, será exibida uma das mensagens de erro abaixo \(no campo destinado a exibir a descrição do ajuste\), conforme o caso, e a operação não será salva:

*                                                     “Código de Ajuste \(Sped Fiscal \- Reg\. E111\) não cadastrado”*

*                                                                                                ou*

*                                 “Código de Ajuste \(Sped Fiscal \- Reg\. E111\) incompatível com o tipo de lançamento”  *

__RN03__

__                                                 Parâmetros p/o Lançamento do Crédito do CIAP __

 

Campo “__Código de Ajuste SEF II – PE:__”     *\(campo criado na *__*OS4138*__*\)* 

Formato do campo: campo numérico de 3 posições, não obrigatório

Este campo é uma lista de acordo com a tabela interna  “*5\.2\.1\-Detalhamento e Ajustes da Apuração do ICMS*” do SEF II \(vide planilha de layout, aba TAB INT, item 5\.2\.1\)\.

*\(a lista apresentada terá a primeira linha em branco, pois trata\-se de campo não obrigatório\) *

*\(corresponde ao mesmo campo da tela dos lançamentos complementares do menu “Obrigações à Lançamentos Complementares”\)*

Campo “__Código de Ajuste \(Sped Fiscal \- Reg\. E111\)__”:       __*\(campo criado na MFS21917\)* __

Formato do campo: campo alfanumérico de 8 posições, não obrigatório

Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste do Sped Fiscal \(módulo ICMS, menu *Apuração à Apuração do ICMS à Lançamentos Complementares à Código de Ajuste Sped Fiscal*\)\.

Para este tipo de lançamento, serão disponibilizados apenas os *códigos* da tabela que atendam aos seguintes requisitos:

- Apenas códigos referentes a UF do Estabelecimento \(as duas primeiras posições do código = sigla da UF\);
- Apenas códigos da apuração do ICMS Próprio \(a terceira posição deve ser = “0”\);
- Apenas códigos de __créditos__ \(a quarta posição deve ser = “2”, “3” ou “4” \(Outros Créditos / Estorno de Débito / Deduções\)\); 

Quando o código for digitado, será verificada a sua existência na tabela, e também se atende aos requisitos acima\. Caso não, será exibida uma das mensagens de erro abaixo \(no campo destinado a exibir a descrição do ajuste\), conforme o caso, e a operação não será salva:

*                                                     “Código de Ajuste \(Sped Fiscal \- Reg\. E111\) não cadastrado”*

*                                                                                                ou*

*                                 “Código de Ajuste \(Sped Fiscal \- Reg\. E111\) incompatível com o tipo de lançamento”  *

__RN04__

__                                        Parâmetros p/o Lançamento de Rateio do Crédito das Entradas __

__Lançamento de Saída do Crédito do livro não incentivado__:

Campo “__Código de Ajuste SEF II – PE:__”     *\(campo criado na *__*OS4138*__*\)* 

Formato do campo: campo numérico de 3 posições, não obrigatório

Este campo é uma lista de acordo com a tabela interna  “*5\.2\.1\-Detalhamento e Ajustes da Apuração do ICMS*” do SEF II \(vide planilha de layout, aba TAB INT, item 5\.2\.1\)\.

*\(a lista apresentada terá a primeira linha em branco, pois trata\-se de campo não obrigatório\) *

*\(corresponde ao mesmo campo da tela dos lançamentos complementares do menu “Obrigações à Lançamentos Complementares”\)*

Campo “__Código de Ajuste \(Sped Fiscal \- Reg\. E111\)__”:       __*\(campo criado na MFS21917\)* __

Formato do campo: campo alfanumérico de 8 posições, não obrigatório

Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste do Sped Fiscal \(módulo ICMS, menu *Apuração à Apuração do ICMS à Lançamentos Complementares à Código de Ajuste Sped Fiscal*\)\.

Para este tipo de lançamento, serão disponibilizados apenas os *códigos* da tabela que atendam aos seguintes requisitos:

- Apenas códigos referentes a UF do Estabelecimento \(as duas primeiras posições do código = sigla da UF\);
- Apenas códigos da apuração do ICMS Próprio \(a terceira posição deve ser = “0”\);
- Apenas códigos de __débitos__ \(a quarta posição deve ser = “0” ou “1” \(Outros Débitos / Estorno de Crédito\)\); 

Quando o código for digitado, será verificada a sua existência na tabela, e também se atende aos requisitos acima\. Caso não, será exibida uma das mensagens de erro abaixo \(no campo destinado a exibir a descrição do ajuste\), conforme o caso, e a operação não será salva:

*                                                     “Código de Ajuste \(Sped Fiscal \- Reg\. E111\) não cadastrado”*

*                                                                                                ou*

*                                 “Código de Ajuste \(Sped Fiscal \- Reg\. E111\) incompatível com o tipo de lançamento”  *

__Lançamento de Entrada do Crédito no livro incentivado:__

Campo “__Código de Ajuste SEF II – PE:__”     *\(campo criado na *__*OS4138*__*\)* 

*\(idem campo de mesmo nome do lançamento anterior\)*

Campo “__Código de Ajuste \(Sped Fiscal \- Reg\. E111\)__”:       __*\(campo criado na MFS21917\)* __

Formato do campo: campo alfanumérico de 8 posições, não obrigatório

Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste do Sped Fiscal \(módulo ICMS, menu *Apuração à Apuração do ICMS à Lançamentos Complementares à Código de Ajuste Sped Fiscal*\)\.

Para este tipo de lançamento, serão disponibilizados apenas os *códigos* da tabela que atendam aos seguintes requisitos:

- Apenas códigos referentes a UF do Estabelecimento \(as duas primeiras posições do código = sigla da UF\);
- Apenas códigos da apuração do ICMS Próprio \(a terceira posição deve ser = “0”\);
- Apenas códigos de __créditos__ \(a quarta posição deve ser = “2”, “3” ou “4” \(Outros Créditos / Estorno de Débito / Deduções\)\); 

Quando o código for digitado, será verificada a sua existência na tabela, e também se atende aos requisitos acima\. Caso não, será exibida uma das mensagens de erro abaixo \(no campo destinado a exibir a descrição do ajuste\), conforme o caso, e a operação não será salva:

*                                                     “Código de Ajuste \(Sped Fiscal \- Reg\. E111\) não cadastrado”*

*                                                                                                ou*

*                                 “Código de Ajuste \(Sped Fiscal \- Reg\. E111\) incompatível com o tipo de lançamento”  *

*= = = = =*


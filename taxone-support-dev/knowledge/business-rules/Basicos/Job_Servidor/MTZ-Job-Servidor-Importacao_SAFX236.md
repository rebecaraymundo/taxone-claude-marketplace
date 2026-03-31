# MTZ-Job-Servidor-Importacao_SAFX236

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX236.docx
- **Modificado:** 2026-03-10
- **Tamanho:** 76 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX236

Tabela dos Itens das Correções de Apontamento da EFD \(Bloco K\)

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS4626

Novos registros Bloco K 

Criação das novas tabelas SAFX235 e SAFX236 para car5ga das informações de correção de apontamento\.

MFS2110

Alteração tamanho do código da OP

Aumento do número da ordem de produção de 15 para 30 posições \(13/03/2017\)

MFS\-13327

Julyana Perrucini

Inclusão das origens 6, 7, 8 e 9, referentes aos registros K291, K292, K301 e K302, em atendimento ao Ato COTEPE 48/2017\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

As tabelas SAFX235 e SAFX236 foram criadas na __MFS4991__ para a geração dos registros de correção de apontamento do Bloco K da EFD \(registros K270, K275 e K280\), conforme Ato Cotepe ICMS 7/2016\.

__Estrutura da tabela SAFX236__ 🡪 vide manual de layout

__Campos que compõe a chave da tabela__:

A SAFX236 é uma tabela “filha” da SAFX235, portanto, sua chave é composta pelos campos chave da SAFX235 \+ campos de identificação do produto componente / insumo:

01\-Código da Empresa

02\-Código do Estabelecimento

03\-Período de Referência

04\-Tipo da Correção

05\-Indicador do Produto

06\-Código do Produto

07\-Data Inicial do Período de Apuração

08\-Data Final do Período de Apuração

09\-Código da Ordem de Produção/Serviço

10\-Cód\. Diferenciador de Produção

11\-Data do Estoque Final

12\-Grupo de Contagem

13\-Indicador da Pessoa Fis/Jur

14\-Código da Pessoa Fis/Jur

     Campos chave da tabela “mãe” \(SAFX235\)

15\- Indicador do Produto \(Componente/Insumo\)

16\-Código do Produto \(Componente/Insumo\)

__Campos obrigatórios__ 🡪 Todos os que aparecem com asterisco \(__\*__\) na coluna “Obrigatoriedade” do manual de layout\. 

Alguns campos são obrigatórios apenas para algumas condições, e nestes casos, eles não estarão marcados com “\*” no manual de layout\. As condições de obrigatoriedade destes campos estão descritas nas orientações de preenchimento do manual, e também nas regras da importação\.

__OBS sobre a chave das tabelas__:

Como estas tabelas foram criadas para a geração do Bloco K, todos os campos que podem ser chave dos registros K270, K275 e K280, foram inseridos na chave das tabelas\. O Bloco K do Sped trabalha com chaves “variáveis”, que dependem das informações estarem preenchidas ou não\. Assim, vários campos chave das tabelas __*não*__ são campos obrigatórios, e quando não forem informados, serão preenchidos com branco e zero, \(dependendo do tipo\), já que não podem ficar nulo por serem campos chave\.   

__Validação da existência do registro “pai” na tabela SAFX235:__

Como esta tabela é “filha” da SAFX235 \(Correção de Apontamento\), além da crítica isolada de cada um dos campos que compõem a chave da tabela “mãe”, será verificada a existência do registro “pai” na SAFX235\. Caso não exista o registro “pai”, o registro não será importado e será__ __gravada a seguinte mensagem no log de erro:

 “*Não existe registro de correção de apontamento na Tabela de Correções de Apontamento \- SAFX235 \(verificar orientações do Manual de Layout\)*” 

__Mensagens de erro__:

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação do registro \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

\(a importação irá recuperar do arquivo texto apenas as linhas que tenham este campo preenchido\)

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

\(a importação irá recuperar do arquivo texto apenas as linhas que tenham este campo preenchido\)

__RN03__

__Campo Periodo de Referência__

Este campo compõe a chave da tabela “mãe” SAFX235\. As regras do seu tratamento são as mesmas definidas para a tabela SAFX235\. Ver documento “__MTZ\-Job\-Servidor\_Importacao\_SAFX235__”, regra __RN03__\.

__RN04__

__Campo Tipo da Correção__

__MFS\-13327:__ O tamanho deste campo foi alterado de 01 para 02 posições e inclui as origens 6, 7, 8 e 9, referentes aos registros K291, K292, K301 e K302, em atendimento ao Ato COTEPE 48/2017\.

Este campo compõe a chave da tabela “mãe” SAFX235\. As regras do seu tratamento são as mesmas definidas para a tabela SAFX235, __exceto__ o fato da SAFX236 __não trabalhar com correções de apontamento de estoque escriturado__ \(tipo 1\), conforme as orientações descritas no manual de layout\.

Assim, a crítica deste campo é feita da seguinte forma:

Campo de preenchimento obrigatório\.

Valores válidos:  2, 3, 4, 5, 6, 7, 8, 9 ou 10\.* \(observar que na SAFX235 aparece também o valor “1”, mas na SAFX236 ele não é aceito\)*

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*  *

*                                          “Tipo da Correção não preenchido ou inválido \(consultar o Manual de Layout\)”*

__RN05__

__Campo Indicador do Produto__

Este campo compõe a chave da tabela “mãe” SAFX235\. As regras do seu tratamento são as mesmas definidas para a tabela SAFX235\. Ver documento “__MTZ\-Job\-Servidor\_Importacao\_SAFX235__”, regra __RN05__\.

__RN06__

__Campo Código do Produto__

Este campo compõe a chave da tabela “mãe” SAFX235\. As regras do seu tratamento são as mesmas definidas para a tabela SAFX235\. Ver documento “__MTZ\-Job\-Servidor\_Importacao\_SAFX235__”, regra __RN06__\.

__RN07__

__Campo Data Inicial do Período de Apuração__

Este campo compõe a chave da tabela “mãe” SAFX235\. As regras do seu tratamento são as mesmas definidas para a tabela SAFX235\. Ver documento “__MTZ\-Job\-Servidor\_Importacao\_SAFX235__”, regra __RN07__\.

__RN08__

__Campo Data Final do Período de Apuração__

Este campo compõe a chave da tabela “mãe” SAFX235\. As regras do seu tratamento são as mesmas definidas para a tabela SAFX235\. Ver documento “__MTZ\-Job\-Servidor\_Importacao\_SAFX235__”, regra __RN08__\.

__RN09__

__Campo Código da Ordem de Produção/Serviço__

Alteração da __MFS2110__: O tamanho deste campo foi alterado de 15 para 30 posições\.

Este campo compõe a chave da tabela “mãe” SAFX235\. As regras do seu tratamento são as mesmas definidas para a tabela SAFX235\. Ver documento “__MTZ\-Job\-Servidor\_Importacao\_SAFX235__”, regra __RN09__\.

__RN10__

__Campo Código Diferenciador de Produção/Serviço__

Este campo compõe a chave da tabela “mãe” SAFX235\. As regras do seu tratamento são as mesmas definidas para a tabela SAFX235\. Ver documento “__MTZ\-Job\-Servidor\_Importacao\_SAFX235__”, regra __RN10__\.

__RN11__

__Campo Data do Estoque Final__

Este campo compõe a chave da tabela “mãe” SAFX235\. As regras do seu tratamento são as mesmas definidas para a tabela SAFX235\. Ver documento “__MTZ\-Job\-Servidor\_Importacao\_SAFX235__”, regra __RN11__\.

Observar que, como a SAFX236 não aceita Tipo de Correção = 1 \(vide RN04\), a informação deste campo será sempre desconsiderada, e o campo será gravado com zeros, uma vez que faz parte da chave da tabela\.

__ __

__RN12__

__Campo Grupo de Contagem__

Este campo compõe a chave da tabela “mãe” SAFX235\. As regras do seu tratamento são as mesmas definidas para a tabela SAFX235\. Ver documento “__MTZ\-Job\-Servidor\_Importacao\_SAFX235__”, regra __RN12__\.

Observar que, como a SAFX236 não aceita Tipo de Correção = 1 \(vide RN04\), a informação deste campo será sempre desconsiderada, e o campo será gravado com brancos, uma vez que faz parte da chave da tabela\.

__RN13__

__Campo Indicador da Pessoa Fis/Jur__

Este campo compõe a chave da tabela “mãe” SAFX235\. As regras do seu tratamento são as mesmas definidas para a tabela SAFX235\. Ver documento “__MTZ\-Job\-Servidor\_Importacao\_SAFX235__”, regra __RN13__\.

Observar que, como a SAFX236 não aceita Tipo de Correção = 1 \(vide RN04\), a informação deste campo será sempre desconsiderada, e o campo será gravado com brancos, uma vez que faz parte da chave da tabela\.

__RN14__

__Campo Código da Pessoa Fis/Jur__

Este campo compõe a chave da tabela “mãe” SAFX235\. As regras do seu tratamento são as mesmas definidas para a tabela SAFX235\. Ver documento “__MTZ\-Job\-Servidor\_Importacao\_SAFX235__”, regra __RN14__\.

Observar que, como a SAFX236 não aceita Tipo de Correção = 1 \(vide RN04\), a informação deste campo será sempre desconsiderada, e o campo será gravado com brancos, uma vez que faz parte da chave da tabela\.

__RN15__

__Campo Indicador do Produto \(Componente/Insumo\)__

Campo de preenchimento obrigatório\.

Valores válidos, de acordo com os indicadores da Tabela de Produtos \(SAFX2013\): 1, 2, 3, 4, 5, 6, 7 e 8\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                    * *“Indicador do Produto Componente/Insumo não preenchido ou inválido”*

__RN16__

__Campo Código do Produto \(Componente/Insumo\)__

Campo de preenchimento obrigatório\.

Será validada a existência do produto informado \(Indicador e Código\) na Tabela de Produtos \(SAFX2013\)\. Para obtenção do Grupo de Relacionamento a ser utilizado na recuperação dos produtos, será utilizado o período de referência informado no campo 03, considerando o grupo de maior data de validade que seja <= a da do primeiro dia do período\. 

Quando não preenchido, ou o produto não for encontrado na SAFX2013, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                          * *“Produto Componente/Insumo não preenchido ou não existente na Tabela de Produtos \(SAFX2013\)”*

__RN17__

__Campo Unidade de Medida__

Campo de preenchimento obrigatório\.

Será validada a existência do código informado na Tabela de Unidades de Medida \(SAFX2007\)\. Para obtenção do Grupo de Relacionamento a ser utilizado na recuperação das medidas, será utilizado o período de referência informado no campo 03, considerando o grupo de maior data de validade que seja <= a da do primeiro dia do período\. 

Quando não preenchido, ou o código não for encontrado na SAFX2007, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                           * *“Unidade de Medida não preenchida ou não existente na Tabela de Unidades de Medida \(SAFX2007\)”*

__RN18__

__Quantidade da Correção__

Campo de preenchimento *não* obrigatório\.

Quando informada, deve ser sempre um valor positivo\. Caso contrário, o registro não será importado e será gravada a seguinte mensagem no log de erros:

*                                         “A quantidade da correção deve ser um valor positivo \(consultar o Manual de Layout\)”*

__RN19__

__Correção Positiva / Negativa__

Campo de preenchimento *não* obrigatório\.

Quando informada, deve conter um dos seguintes valores: 1 ou 2 \(positiva ou negativa\)\. Caso contrário, o registro não será importado, e será gravada a seguinte mensagem no log de erro:

*                                 “Campo Correção Positiva / Negativa inválido \(consultar o Manual de Layout\)”*

Quando não informado, será gravado o valor default = “1”\.

__RN20__

__Indicador do Insumo Substituído__

Campo de preenchimento *não* obrigatório\.

O tratamento deste campo depende do tipo de correção informado no campo 04, da seguinte forma:

A informação deste campo será considerada *apenas* quando o tipo de correção for __=__ __“4”__ ou __“5”__, conforme a regra abaixo:

__Se__  Tipo de Correção __<> “4” __e__ <> “5”__

      A informação será desconsiderada, e o campo será gravado sem informação;

__Senão__   \(Tipo de Correção __=__ __“4”__ ou __“5”__\) 

     Neste caso, o campo poderá ou não estar preenchido\.

     Caso tenha sido informado, seu conteúdo será validado de acordo com os indicadores da Tabela de Produtos \(SAFX2013\), e

     se inválido, o registro não será importado, e será gravada a seguinte mensagem no log de erro:

*                                                      * *“Indicador do Insumo Substituído inválido”*

__RN21__

__Código do Insumo Substituído__

Campo de preenchimento *não* obrigatório\.

O tratamento deste campo depende do tipo de correção informado no campo 04, da seguinte forma:

A informação deste campo será considerada *apenas* quando o tipo de correção for __=__ __“4”__ ou __“5”__, conforme a regra abaixo:

__Se__  Tipo de Correção __<> “4” __e__ <> “5”__

      A informação será desconsiderada, e o campo será gravado sem informação;

__Senão__   \(Tipo de Correção __=__ __“4”__ ou __“5”__\) 

     Neste caso, o campo poderá ou não estar preenchido\.

     Caso tenha sido informado, o produto informado \(campos 20 e 21\) será validado na Tabela de Produtos \(SAFX2013\)\. Para

     obtenção do Grupo de Relacionamento a ser utilizado na recuperação dos produtos, será utilizado o período de referência

     informado no campo 03, considerando o grupo de maior data de validade que seja <= a da do primeiro dia do período\. Se o produto

     não for encontrado, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                       * *“Insumo Substituído não existente na Tabela de Produtos \(SAFX2013\)”*

O produto informado neste campo \(Insumo Substituído\)  deve ser diferente do produto informado nos campos 15/16 \(Produto Componente / Insumo\)\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

                                                  “*O Insumo Substituído não pode ser igual ao Produto Componente/Insumo*”\.

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


# MTZ-Job-Servidor-Importacao_SAFX235

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX235.docx
- **Modificado:** 2026-03-10
- **Tamanho:** 81 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX235

Tabela das Correções de Apontamento da EFD \(Bloco K\)

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS4991

Vânia Mattos 

Criação das novas tabelas SAFX235 e SAFX236 para car5ga das informações de correção de apontamento\.

MFS2110

Vânia Mattos

Aumento do número da ordem de produção de 15 para 30 posições \(13/03/2017\)

MFS\-13327

Julyana Perrucini

Inclusão das origens 6, 7, 8 e 9, referentes aos registros K291, K292, K301 e K302, em atendimento ao Ato COTEPE 48/2017\.

MFS594148

Andréa Rocha

Alteração da regra dos campos data inicial e data final do Período de Apuração, para permitir preencher esses campos para o tipo de correção igual a “1”\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

As tabelas SAFX235 e SAFX236 foram criadas na __MFS4991__ para a geração dos registros de correção de apontamento do Bloco K da EFD \(registros K270, K275 e K280\), conforme Ato Cotepe ICMS 7/2016\.

__Estrutura da tabela SAFX235__ 🡪 vide manual de layout

__Campos que compõe a chave da tabela:__

__Campo__

__Condição de Obrigatoriedade__

01\-Código da Empresa

02\-Código do Estabelecimento

03\-Período de Referência

04\-Tipo da Correção

05\-Indicador do Produto

06\-Código do Produto

    Campos obrigatórios incondicionalmente

07\-Data Inicial do Período de Apuração

08\-Data Final do Período de Apuração

09\-Código da Ordem de Produção/Serviço

10\-Cód\. Diferenciador de Produção

11\-Data do Estoque Final

12\-Grupo de Contagem

13\-Indicador da Pessoa Fis/Jur

14\-Código da Pessoa Fis/Jur

            Campos __*não*__ obrigatórios 

\(quando não informados no arquivo texto, serão preenchidos com “ “ ou “0”\)

__Campos obrigatórios__ 🡪 Todos os que aparecem com asterisco \(__\*__\) na coluna “Obrigatoriedade” do manual de layout\. 

Alguns campos são obrigatórios apenas para algumas condições, e nestes casos, eles não estarão marcados com “\*” no manual de layout\. As condições de obrigatoriedade destes campos estão descritas nas orientações de preenchimento do manual, e também nas regras da importação\.

__OBS sobre a chave das tabelas:__

Como estas tabelas foram criadas para a geração do Bloco K, todos os campos que podem ser chave dos registros K270, K275 e K280, foram inseridos na chave das tabelas\. O Bloco K do Sped trabalha com chaves “variáveis”, que dependem das informações estarem preenchidas ou não\. Assim, vários campos chave das tabelas __*não*__ são campos obrigatórios, e quando não forem informados, serão preenchidos com branco e zero, \(dependendo do tipo\), já que não podem ficar nulo por serem campos chave\.   

__Mensagens de erro__:

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem de erro no log, e os dados de identificação do registro \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

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

Campo de preenchimento obrigatório\.

Deve ser preenchido com a informação do mês e ano, no formato MMAAAA\.

Quando não preenchido, ou o mês ou o ano forem inválidos, o registro não será importado e será gravada a seguinte mensagem de erro no log:

                                                                “*Período de Referência não preenchido ou inválido*”

__RN04__

__Campo Tipo da Correção__

Campo de preenchimento obrigatório\.

__MFS\-13327:__ O tamanho deste campo foi alterado de 01 para 02 posições e inclui as origens 6, 7, 8 e 9, referentes aos registros K291, K292, K301 e K302, em atendimento ao Ato COTEPE 48/2017\.

Valores válidos: 1, 2, 3, 4, 5, 6, 7, 8, 9 ou 10\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*  *

*                                          “Tipo da Correção não preenchido ou inválido \(consultar o Manual de Layout\)”*

__RN05__

__Campo Indicador do Produto __

Campo de preenchimento obrigatório\.

Valores válidos, de acordo com os indicadores da Tabela de Produtos \(SAFX2013\): 1, 2, 3, 4, 5, 6, 7 e 8\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                   * *“Indicador do Produto não preenchido ou inválido”*

__RN06__

__Campo Código do Produto __

Campo de preenchimento obrigatório\.

Será validada a existência do produto informado \(Indicador e Código\) na Tabela de Produtos \(SAFX2013\)\. Para obtenção do Grupo de Relacionamento a ser utilizado na recuperação dos produtos, será utilizado o período de referência informado no campo 03, considerando o grupo de maior data de validade que seja <= a da do primeiro dia do período\. 

Quando não preenchido, ou o produto não for encontrado na SAFX2013, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                      * *“Produto não preenchido ou não existente na Tabela de Produtos \(SAFX2013\)”*

__RN07__

__\[MFS594148\] __Retirar o filtro para o campo tipo de correção igual a “1”\.

__Campo Data Inicial do Período de Apuração __

Campo de preenchimento *não* obrigatório\.

O tratamento deste campo depende do tipo de correção informado no campo 04, da seguinte forma:

A informação deste campo será considerada *apenas* quando o tipo de correção for __<>__ __“1”__, conforme a regra abaixo:

__Se__ Tipo de Correção __= “1”__ *ou* quando o campo não estiver preenchido:

      O campo será gravado com zeros, uma vez que faz parte da chave da tabela;

__Senão__ \(tipo de correção __<> “1”__\)

     Nesse caso serão realizadas as seguintes críticas:

      \- Deve ser uma data válida\. Caso contrário, o registro não será importado e será gravada a seguinte mensagem de erro no log:

*                                                            “Data Inicial do Período de Apuração inválida”\.*

     \- Deve ser uma data anterior a data do primeiro dia do período de referência informado no campo 03\. Caso contrário, o registro não será importado

       e será gravada a seguinte mensagem de erro no log:

*                                        “A Data Inicial do Período de Apuração deve ser anterior ao período de referência informado”\.*

__RN08__

__\[MFS594148\] __Retirar o filtro para o campo tipo de correção igual a “1”\.

__Campo Data Final do Período de Apuração __

Campo de preenchimento *não* obrigatório\.

O tratamento deste campo depende do tipo de correção informado no campo 04, da seguinte forma:

A informação deste campo será considerada *apenas* quando o tipo de correção for __<> “1”__, conforme a regra abaixo:

__Se__ Tipo de Correção __= “1”__ *ou* quando o campo não estiver preenchido:

      O campo será gravado com zeros, uma vez que faz parte da chave da tabela;

__Senão__ \(tipo de correção __<> “1”__\)

     Nesse caso serão realizadas as seguintes críticas:

      \- Deve ser uma data válida\. Caso contrário, o registro não será importado e será gravada a seguinte mensagem de erro no log:

*                                                                    “Data Final do Período de Apuração inválida”\.*

     \- Deve ser uma data anterior a data do primeiro dia do período de referência informado no campo 03\. Caso contrário, o registro não será importado

       e será gravada a seguinte mensagem de erro no log:

*                                        “A Data Final do Período de Apuração deve ser anterior ao período de referência informado”\.*

     \- Deve ser uma data >= a “Data Inicial do Período de Apuração” informada no campo 07\. Caso contrário, o registro não será importado e será

       gravada a seguinte mensagem de erro no log:

  

*                                            “A Data Final do Período de Apuração deve ser igual ou superior a Data Inicial”\.*

      \- Crítica em relação aos dois campos de data inicial e final do período \(campos 07 e 08\): Quando uma das datas for informada, e a outra

         não, o registro não será importado e será gravada a seguinte mensagem de erro no log:

                         *“Para informar o Período de Apuração do Erro, é necessário preencher a data inicial e a data final \(campos 07 e 08\)”*  

__RN09__

__Campo Código da Ordem de Produção/Serviço __

Alteração da __MFS2110__: O tamanho deste campo foi alterado de 15 para 30 posições\.

Campo de preenchimento *não* obrigatório\.

O tratamento deste campo depende do tipo de correção informado no campo 04, da seguinte forma:

A informação desse campo será considerada *apenas* quando o tipo de correção for __= 2, 4, 5 ou 6__, conforme a regra abaixo:

__Se__ \(Tipo de Correção __= 1 ou 3__\)  *ou* quando o campo não estiver preenchido:

      O campo será gravado com brancos, uma vez que faz parte da chave da tabela;

__Senão__ \(tipo de correção __= 2, 4, 5 ou 6__\)

     Nesse caso o campo será gravado normalmente com a informação importada\.

__RN10__

__Campo Código Diferenciador de Produção __

Campo de preenchimento *não* obrigatório\.

O tratamento deste campo depende do tipo de correção informado no campo 04, da seguinte forma:

A informação desse campo será considerada *apenas* quando o tipo de correção for __= 2, 4, 5 ou 6__, conforme a regra abaixo:

__Se__ \(Tipo de Correção __= 1 ou 3__\)  *ou* quando o campo não estiver preenchido:

      O campo será gravado com brancos, uma vez que faz parte da chave da tabela;

__Senão__ \(tipo de correção __= 2, 4, 5 ou 6__\)

     Nesse caso o campo será gravado normalmente com a informação importada\.

__RN11__

__Campo Data do Estoque Final__

Campo de preenchimento *não* obrigatório\.

O tratamento deste campo depende do tipo de correção informado no campo 04, da seguinte forma:

A informação deste campo será considerada *apenas* quando o tipo de correção for __=__ __“1”__, conforme a regra abaixo:

__Se__ Tipo de Correção __<> “1”__ 

      A informação será desconsiderada, e o campo será gravado com zeros, uma vez que faz parte da chave da tabela;

__Senão__ \(tipo de correção __= “1”__\)

     Nesse caso a informação é obrigatória, por isso, serão realizadas as seguintes críticas:

     \- Se o campo não estiver preenchido, o registro não será importado, e será gravada a seguinte mensagem no log: 

                      *“A Data do Estoque Final é de preenchimento obrigatório para o tipo de correção = 1”*

     \- Deve ser uma data válida, que seja *inferior* a data do primeiro dia do período de referência informado no campo 03\. Caso

       contrário, o registro não será importado e será gravada a seguinte mensagem no log: 

                    *“A Data do Estoque Final deve ser uma data anterior ao período de referência informado”\.*

__RN12__

__Campo Grupo de Contagem__

Campo de preenchimento *não* obrigatório\.

O tratamento deste campo depende do tipo de correção informado no campo 04, da seguinte forma:

A informação deste campo será considerada *apenas* quando o tipo de correção for __=__ __“1”__, conforme a regra abaixo:

__Se__ Tipo de Correção __<> “1”__ 

      A informação será desconsiderada, e o campo será gravado com brancos, uma vez que faz parte da chave da tabela;

__Senão__ \(tipo de correção __= “1”__\)

     Nesse caso a informação é obrigatória, e seu conteúdo deve ser um dos valores válidos: 1, 2, 3 ou 5, conforme a orientação do

     Manual de Layout\. Se o campo não estiver preenchido, ou se o seu conteúdo for inválido, o registro não será importado, e será 

     gravada uma das seguintes mensagens de erro no log, conforme o caso:

      \- Se o campo não estiver preenchido 🡪 *“O Grupo de Contagem é de preenchimento obrigatório para o tipo de correção = 1”*

      \- Se o conteúdo for inválido 🡪 *“Grupo de Contagem inválido \(consultar o Manual de Layout\)”* 

__RN13__

__Campo Indicador da Pessoa Fis/Jur__

Campo de preenchimento *não* obrigatório\.

O tratamento deste campo depende do tipo de correção informado no campo 04, da seguinte forma:

A informação deste campo será considerada *apenas* quando o \(Tipo de Correção for __=__ __“1”\)__, __e__ o Grupo de Contagem do \(campo 12\) for __= 2 ou 3__\. Desta forma, teremos a seguinte regra:

__Se__  \( Tipo de Correção __<> “1” __\)  __ou__  \( Tipo de Correção __= “1”__ e Grupo de Contagem = 1 ou 5 \)

      A informação será desconsiderada, e o campo será gravado com brancos, uma vez que faz parte da chave da tabela;

__Senão__  \(Tipo de Correção __= “1” __e Grupo de Contagem = 2 ou 3\) 

     Neste caso, o campo é obrigatório\. Caso não preenchido, ou se o seu conteúdo não estiver de acordo com os indicadores da

     Tabela de Pessoas Fis/Jur \(SAFX04\), o registro não será importado, e será gravada a seguinte mensagem no log de erro:

*                          * *“Indicador da Pessoa Física / Jurídica não informado ou inválido \(consultar o Manual de Layout\)”*

__RN14__

__Campo Código da Pessoa Fis/Jur __

Campo de preenchimento *não* obrigatório\.

O tratamento deste campo depende do tipo de correção informado no campo 04, da seguinte forma:

A informação deste campo será considerada *apenas* quando o \(Tipo de Correção for __=__ __“1”\)__, __e__ o Grupo de Contagem do \(campo 12\) for __= 2 ou 3__\. Desta forma, teremos a seguinte regra:

__Se__  \( Tipo de Correção __<> “1” __\)  __ou__  \( Tipo de Correção __= “1”__ e Grupo de Contagem = 1 ou 5 \)

      A informação será desconsiderada, e o campo será gravado com brancos, uma vez que faz parte da chave da tabela;

__Senão__    \(Tipo de Correção __= “1” __e Grupo de Contagem = 2 ou 3\)

     Neste caso, o campo é obrigatório\. Caso não preenchido, o registro não será incluído e será gravada a seguinte mensagem no

     log de erro:    *“A Pessoa Fisica /Jurídica é de preenchimento obrigatório para os Grupos de Contagem = 2 ou 3”*  

     A pessoa informada \(campos 13 e 14\) será validada na Tabela de Pessoas Fis/Jur \(SAFX04\)\. Para obtenção do Grupo de

     Relacionamento a ser utilizado na recuperação dos dados, será utilizado o período de referência informado no campo 03,

     considerando o grupo de maior data de validade que seja <= a da do primeiro dia do período\. Se a pessoa fis/jur não for

     encontrada, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                      * *“Pessoa Fisica /Jurídica não existente na Tabela de Pessoas Fis/Jur \(SAFX04\)”*

__RN15__

__Campo Unidade de Medida__

Campo de preenchimento obrigatório\.

Será validada a existência do código informado na Tabela de Unidades de Medida \(SAFX2007\)\. Para obtenção do Grupo de Relacionamento a ser utilizado na recuperação das medidas, será utilizado o período de referência informado no campo 03, considerando o grupo de maior data de validade que seja <= a da do primeiro dia do período\. 

Quando não preenchido, ou o código não for encontrado na SAFX2007, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                            * *“Unidade de Medida não preenchida ou não existente na Tabela de Unidades de Medida \(SAFX2007\)”*

__RN16__

__Campo Quantidade da Correção__

Campo de preenchimento *não* obrigatório\.

Quando informada, deve ser sempre um valor positivo\. Caso contrário, o registro não será importado e será gravada a seguinte mensagem no log de erros:

*                                         “A quantidade da correção deve ser um valor positivo \(consultar o Manual de Layout\)”*

__RN17__

__Campo Correção Positiva/Negativa__

Campo de preenchimento *não* obrigatório\.

Quando informada, deve conter um dos seguintes valores: 1 ou 2 \(positiva ou negativa\)\. Caso contrário, o registro não será importado, e será gravada a seguinte mensagem no log de erro:

*                                 “Campo Correção Positiva / Negativa inválido \(consultar o Manual de Layout\)”*

Quando não informado, será gravado o valor default = “1”\.

__RN18__

__Campo Inscrição Estadual \- AM__

Campo de preenchimento *não* obrigatório\.

Quando informado, será verificada a existência da inscrição no cadastro das inscrições estaduais do AM \(módulo Parâmetros, menu “Funcionais 🡪 Inscrições Estaduais do Estabelecimento AM”\), considerando apenas as inscrições cadastradas para o estabelecimento em questão\. Caso não exista, o registro não será importado, e será gravada a seguinte mensagem no log de erro:

*                “Inscrição Estadual – AM não cadastrada na Tabela das Inscrições Estaduais do AM \(consultar o Manual de Layout\)”*

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


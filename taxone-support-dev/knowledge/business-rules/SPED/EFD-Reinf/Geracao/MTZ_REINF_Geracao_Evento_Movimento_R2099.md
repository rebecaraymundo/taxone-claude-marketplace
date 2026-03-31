# MTZ_REINF_Geracao_Evento_Movimento_R2099

- **Fonte:** MTZ_REINF_Geracao_Evento_Movimento_R2099.docx
- **Modificado:** 2023-03-28
- **Tamanho:** 78 KB

---

THOMSON REUTERS

Geração evento R\-2099 \- REINF

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-11898

Lara Aline

Definição de regras para geração do evento R\-2099 Reinf 

MFS17973

Lara Aline

Inclusão da geração do R\-2099 sem movimento

MFS20930

Lara Aline

Ajuste nos campos evtPgtos e compSemMovto, conforme Layout 1\.4

MFS59340

Alessandra Cristina Navatta

Inclusão das informações do campo evtAquis, conforme Layout 1\.5\.1 \(RN15\.01\)

[__MFS\-79878__](https://jira.thomsonreuters.com/browse/MFS-79874)

Alessandra Cristina Navatta

Exclusão dos campos 25 \- evtPgtos e 26 – compSemMovto, no evento R\-2099, a partir da versão 2\.1 do REINF \(RN16 e RN17\)

MFS\-90001

Alessandra Cristina Navatta

Alteração da versão 2\.1 para 2\.1\.1 e referência do arquivo de de\_para

__Obs\. Os ajustes mapeados nesta demanda, referem\-se a atualização funcional\. Não há impactos na implementação__

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral de Geração do Evento R\-2099\.__

O evento R\-2099 do SPED \- REINF tem por objetivo informar o encerramento da transmissão dos eventos periódicos na EFD\-Reinf, no período de apuração\. Neste momento são consolidadas todas as informações prestadas nos eventos R\-2010 a R\-2070\. Ele será gerado com os registros:

 __Reinf__ – EFD \- Reinf

 __evtFechaEvPer __– Evento de Fechamento

 __ideEvento__ – Informações de Identificação do Evento

 __ideContri__ – Informações de Identificação do Contribuinte

 __ideRespInf __– Responsável pelas informações 

__ infoFech __– Informações do Fechamento\. 

Observar orientações existentes no arquivo " TR\_REINF\_DEXPARA\_V2\.1\.1\.xlsx"\.

- __Origem das informações__: Tela de Dados Iniciais, Cadastro do Estabelecimento\. 
- __Regra de seleção__: O Registro R\-2099 é utilizado para informar o encerramento da transmissão dos eventos periódicos na EFD\-Reinf, no período de apuração\. Neste momento são consolidadas todas as informações prestadas nos eventos R\-2010 a R\-2070\. Caso na geração prévia dos movimentos o parâmetro “R\-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado esse evento também será gerado, porém apenas se não existir eventos de movimento gerados no período R\-2010 a R\-2070\.

__Mensageria Log:__ 

1 \- Verificar se dentro do período de apuração existe algum evento periódico nas tabelas de ocorrência com IND\_STATUS = ‘1’ ou ‘2’, então não permitir a geração do Evento R\-2099 – Fechamento e exibir a seguinte mensagem: 

Evento R\-2099 – Fechamento dos Eventos Periódicos

“Período de Apuração não pode ser fechado, enquanto existir eventos de movimento não enviados ou aguardando retorno do Fisco\.”

Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód\. do Estab\.: XXXXXX

2 \- Verificar se já foi efetuada a geração e envio do evento R\-2099 – Fechamento para esse período de apuração, caso ainda não tenha retorno \(IND\_STATUS = 2\), exibir a seguinte mensagem:

Evento R\-2099 – Fechamento dos Eventos Periódicos

“O fechamento do período já foi executado e seu evento enviado ao Fisco, mas ainda aguarda retorno\. Somente refazer esta operação, caso o retorno seja erro\.”

Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód\. do Estab\.: XXXXXX

__Tratamento para geração do Evento R\-2099 \- Fechamento dos Eventos Periódicos – Sem Movimento:__

Esse evento será gerado apenas se não existir nenhum evento de movimento \(R\-2010 a R\-2070\) gerado no período que o usuário estiver tentando efetuar a geração prévia, caso encontrado algum evento de movimento no período será gerada uma mensagem de erro no log da tela de Geração Prévia dos Movimentos, e a geração não será efetuada: *“Evento R\-2099 sem movimento não será gerado, pois existe evento de movimento gerado nesse período\.*”\. 

MFS\-11898

MFS17973

MFS\-90001

- __Registro ideEvento – Informações de Identificação do Evento__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

- __Registro ideContri – Informações de Identificação do Contribuinte__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN01

- __Origem das informações__: Cadastro do Estabelecimento\.
- __Regra de seleção__: Este registro servirá para identificar o estabelecimento centralizador \(Matriz\)\.
- __Campos\-Chave__: tpInsc, nrInsc
- __Nível hierárquico do registro__: filho do registro evtFechaEvPer
- __Ordenação__: não se aplica\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Um por arquivo

MFS\-11898

RN02

__Campo tpInsc__

Será gerado com conteúdo igual a “1”

MFS\-11898

RN03

__Campo nrInsc__

Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento\. Com base neste campo podemos entender que o REINF será gerado com base em um estabelecimento Centralizador\. 

MFS\-11898

- __Registro ideRespInf – Responsável pelas informações__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN04

- __Origem das informações__: Tela de Dados Iniciais 
- __Regra de seleção__: Este registro servirá identificar o responsável pelas informações
- __Campos\-Chave__: nmResp, cpfResp
- __Nível hierárquico do registro__: filho do registro evtFechaEvPer\.
- __Ordenação__: Não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Poderá existir 1 ou não existir

MFS\-11898

RN05

__Campo nmResp__

Informação será recuperada do campo Nome da tela de “Dados Iniciais”\.

MFS\-11898

RN06

__Campo cpfResp__

Informação será recuperada do campo CPF da tela de “Dados Iniciais”\.

MFS\-11898

RN07

__Campo telefone__

Informação será recuperada do campo Telefone, caso não preenchido será recuperado do campo Celular da tela de “Dados Iniciais”\. 

MFS\-11898

RN08

__Campo email__

Informação será recuperada do campo Email da tela de “Dados Iniciais”\.

MFS\-11898

- __Registro infoFech – Informações do Fechamento\.__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN09

- __Origem das informações__: Eventos R\-2010 ao R\-2070
- __Regra de seleção__: Este registro apresenta as informações do Fechamento\.
- __Nível hierárquico do registro__: filho do registro evtFechaEvPer\.
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Um por arquivo\.

MFS\-11898

RN10

__Campo evtServTm__

Informação a ser gravada nesse campo:

S – Sim;

N – Não\.

Validação: Se existir evento R\-2010 para o período de apuração com IND\_STATUS = ‘3’, gravar ‘S – Sim’\. Caso contrário gravar ‘N – Não’\.

__\[MFS17973\]__

Caso na geração prévia dos movimentos o parâmetro “R\-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo gravar ‘N – Não’

MFS\-11898

MFS17973

RN11

__Campo evtServPr__

Informação a ser gravada nesse campo:

S – Sim;

N – Não\.

Validação: Se existir evento R\-2020 para o período de apuração com IND\_STATUS = ‘3’, gravar ‘S – Sim’\. Caso contrário gravar ‘N – Não’\.

__\[MFS17973\]__

Caso na geração prévia dos movimentos o parâmetro “R\-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo gravar ‘N – Não’

MFS\-11898

MFS17973

RN12

__Campo evtAssDespRec__

Informação a ser gravada nesse campo:

S – Sim;

N – Não\.

Validação: Se existir evento R\-2030 para o período de apuração com IND\_STATUS = ‘3’, gravar ‘S – Sim’\. Caso contrário gravar ‘N – Não’\.

__\[MFS17973\]__

Caso na geração prévia dos movimentos o parâmetro “R\-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo gravar ‘N – Não’

MFS\-11898

MFS17973

RN13

__Campo evtAssDespRep__

Informação a ser gravada nesse campo:

S – Sim;

N – Não\.

Validação: Se existir evento R\-2040 para o período de apuração com IND\_STATUS = ‘3’, gravar ‘S – Sim’\. Caso contrário gravar ‘N – Não’\.

__\[MFS17973\]__

Caso na geração prévia dos movimentos o parâmetro “R\-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo gravar ‘N – Não’

MFS\-11898

MFS17973

RN14

__Campo evtComProd__

Informação a ser gravada nesse campo:

S – Sim;

N – Não\.

Validação: Se existir evento R\-2050 para o período de apuração com IND\_STATUS = ‘3’, gravar ‘S – Sim’\. Caso contrário gravar ‘N – Não’\.

__\[MFS17973\]__

Caso na geração prévia dos movimentos o parâmetro “R\-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo gravar ‘N – Não’

MFS\-11898

MFS17973

RN15

__Campo evtCPRB__

Informação a ser gravada nesse campo:

S – Sim;

N – Não\.

Validação: Se existir evento R\-2060 para o período de apuração com IND\_STATUS = ‘3’, gravar ‘S – Sim’\. Caso contrário gravar ‘N – Não’\.

__\[MFS17973\]__

Caso na geração prévia dos movimentos o parâmetro “R\-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo gravar ‘N – Não’

MFS\-11898

MFS17973

RN15\.01

__Campo evtAquis__

Informação a ser gravada nesse campo:

S – Sim;

N – Não\.

Validação: Se existir evento R\-2055 para o período de apuração com IND\_STATUS = ‘3’, gravar ‘S – Sim’\. Caso contrário gravar ‘N – Não’\.

Caso na geração prévia dos movimentos o parâmetro “R\-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo gravar ‘N – Não’

MFS\-59340

RN16

__Campo evtPgtos__

Informação a ser gravada nesse campo:

S – Sim;

N – Não\.

Validação: Se existir evento R\-2070 para o período de apuração com IND\_STATUS = ‘3’, gravar ‘S – Sim’\. Caso contrário gravar ‘N – Não’\.  A partir do layout 1\.4 gravaremos nesse campo sempre o valor ‘N – Não’\. 

Até a inclusão da família de eventos "R\-40" que substituirão o evento R\-2070, esse campo possivelmente sofrerá alteração de regra de validação nesse momento\.

__\[MFS17973\]__

Caso na geração prévia dos movimentos o parâmetro “R\-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo gravar ‘N – Não’

__\[MFS20930\]__

Este campo deve ser gerado se período da apuração for menor ou igual a 31/10/2018

__\[ALTERAÇÃO MFS\-90001\] – __Alteração de versão

__\[ALTERAÇÃO MFS79876\] __

A partir da versão 2\.1 2\.1\.1 do REINF este campo não deve ser mais gerado\.

MFS\-11898

MFS17973

MFS20930

[MFS\-79878](https://jira.thomsonreuters.com/browse/MFS-79874)

MFS\-90001

RN17

__Campo compSemMovto__

__\[MFS17973/MFS20930\]__

Caso__ __estiver preenchido o campo “Comp\. Sem Movto MM/AAAA” da tela de Geração Prévia do Movimentos será gravada a informação preenchida no mesmo\.

Caso na geração prévia dos movimentos o parâmetro “R\-2099 – Fechamento dos Eventos Periódicos – Sem Movimento” estiver selecionado, nesse campo será gravada a informação preenchida no campo “Comp\. Sem Movto MM/AAAA” da tela de Geração Prévia do Movimentos se estiver preenchido\.

Caso contrário, esse campo será gerado como nulo, sem informação\.

__\[ALTERAÇÃO MFS\-90001\] – __Alteração de versão

__\[ALTERAÇÃO MFS79876\] __

A partir da versão 2\.1 2\.1\.1 do REINF este campo não deve ser mais gerado\.

MFS\-11898

MFS17973

MFS20930

[MFS\-79878](https://jira.thomsonreuters.com/browse/MFS-79874)

MFS\-90001

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


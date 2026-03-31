# MTZ_REINF_Geracao_Evento_Movimento_R4099

- **Fonte:** MTZ_REINF_Geracao_Evento_Movimento_R4099.docx
- **Modificado:** 2023-04-27
- **Tamanho:** 75 KB

---

THOMSON REUTERS

Geração evento R\-4099 \- REINF

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

[MFS\-79914](https://jira.thomsonreuters.com/browse/MFS-79914)

Alessandra Cristina Navatta

Definição de regras para geração do evento R\-4099 Reinf \(2\.1\)

MFS\-90001

Alessandra Cristina Navatta

Alteração da versão 2\.1 para 2\.1\.1 e referência do arquivo de de\_para

__Obs\. Os ajustes mapeados nesta demanda, referem\-se a atualização funcional\. Não há impactos na implementação__

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral de Geração do Evento R\-4099\.__

O evento R\-4099 do SPED \- REINF tem por objetivo informar o encerramento da transmissão dos eventos da série 40 na EFD\-Reinf, no período de apuração\. Ele será gerado com os registros:

 __Reinf__ – EFD \- Reinf

 __evtFech __– Evento de Fechamento

 __ideEvento__ – Informações de Identificação do Evento

 __ideContri__ – Informações de Identificação do Contribuinte

 __ideRespInf __– Responsável pelas informações 

__ infoFech __–Fechamento/reabertura do PA reativo às retenções na fonte

Observar orientações existentes no arquivo " TR\_REINF\_DEXPARA\_V2\.1\.1\.xlsx"\.

- __Origem das informações__: Tela de Dados Iniciais, Cadastro do Estabelecimento, Geração dos Eventos R\-4010 a R4080\. 
- __Regra de seleção__: O Registro R\-4099 é utilizado para informar o fechamento ou reabertura da transmissão dos eventos da família 40 na EFD\-Reinf, no período de apuração\. Caso na geração prévia dos movimentos o parâmetro “R\-4099 – Fechamento/reabertura dos eventos da séria 40” estiver selecionado esse evento também será gerado, porém apenas se existir eventos da série 40 no período \(R\-4010 a R\-4080\)\.

__Mensageria Log:__ 

1 \- Verificar se dentro do período de apuração existe algum evento periódico da família 40 nas tabelas de ocorrência com IND\_STATUS = ‘1’ ou ‘2’, então não permitir a geração do Evento R\-4099 \- Fechamento/reabertura dos eventos da série R\-4000 e exibir a seguinte mensagem: 

Evento R\-4099 \- Fechamento/reabertura dos eventos da série R\-4000

“Período de Apuração não pode ser fechado, enquanto existir eventos de movimento não enviados ou aguardando retorno do Fisco\.”

Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód\. do Estab\.: XXXXXX

2 \- Verificar se já foi efetuada a geração e envio do evento R\-4099 \- Fechamento/reabertura dos eventos da série R\-4000 para esse período de apuração, caso ainda não tenha retorno \(IND\_STATUS = 2\), exibir a seguinte mensagem:

Evento R\-4099 \- Fechamento/reabertura dos eventos da série R\-4000

“O fechamento do período já foi executado e seu evento enviado ao Fisco, mas ainda aguarda retorno\. Somente refazer esta operação, caso o retorno seja erro\.”

Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód\. do Estab\.: XXXXXX

[MFS\-79914](https://jira.thomsonreuters.com/browse/MFS-79914)

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
- __Nível hierárquico do registro__: filho do registro evtFech
- __Ordenação__: não se aplica\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Um por arquivo

[MFS\-79914](https://jira.thomsonreuters.com/browse/MFS-79914)

RN02

__Campo tpInsc__

Será gerado com conteúdo igual a “1”

[MFS\-79914](https://jira.thomsonreuters.com/browse/MFS-79914)

RN03

__Campo nrInsc__

Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento\. Com base neste campo podemos entender que o REINF será gerado com base em um estabelecimento Centralizador\.

[MFS\-79914](https://jira.thomsonreuters.com/browse/MFS-79914)

- __Registro ideRespInf – Responsável pelas informações__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN04

- __Origem das informações__: Tela de Dados Iniciais 
- __Regra de seleção__: Este registro servirá identificar o responsável pelas informações
- __Campos\-Chave__: nmResp, cpfResp
- __Nível hierárquico do registro__: filho do registro evtFech\.
- __Ordenação__: Não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Poderá existir 1 ou não existir

[MFS\-79914](https://jira.thomsonreuters.com/browse/MFS-79914)

RN05

__Campo nmResp__

Informação será recuperada do campo Nome da tela de “Dados Iniciais”\.

[MFS\-79914](https://jira.thomsonreuters.com/browse/MFS-79914)

RN06

__Campo cpfResp__

Informação será recuperada do campo CPF da tela de “Dados Iniciais”\.

[MFS\-79914](https://jira.thomsonreuters.com/browse/MFS-79914)

RN07

__Campo telefone__

Informação será recuperada do campo Telefone, caso não preenchido será recuperado do campo Celular da tela de “Dados Iniciais”\. 

[MFS\-79914](https://jira.thomsonreuters.com/browse/MFS-79914)

RN08

__Campo email__

Informação será recuperada do campo Email da tela de “Dados Iniciais”\.

[MFS\-79914](https://jira.thomsonreuters.com/browse/MFS-79914)

- __Registro infoFech – Informações do Fechamento\.__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN09

- __Origem das informações__: Eventos R\-4010 ao R\-4080
- __Regra de seleção__: Este registro apresenta as informações do Fechamento\.
- __Nível hierárquico do registro__: filho do registro evtFech
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Um por arquivo\.

[MFS\-79914](https://jira.thomsonreuters.com/browse/MFS-79914)

RN10

__Campo fetcRet__

Informação a ser gravada nesse campo:

1. Fechamento
2. Reabertura

Na primeira geração do evento, deve ser gravado ‘0’, depois, se for enviado novamente o evento R\-4099, este campo deve ser gerado com ‘1’\. 

[MFS\-79914](https://jira.thomsonreuters.com/browse/MFS-79914)

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


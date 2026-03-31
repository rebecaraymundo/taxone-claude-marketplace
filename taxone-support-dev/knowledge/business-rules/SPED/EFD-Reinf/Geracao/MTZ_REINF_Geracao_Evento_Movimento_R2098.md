# MTZ_REINF_Geracao_Evento_Movimento_R2098

- **Fonte:** MTZ_REINF_Geracao_Evento_Movimento_R2098.docx
- **Modificado:** 2023-03-28
- **Tamanho:** 70 KB

---

THOMSON REUTERS

Geração evento R\-2098 \- REINF

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-11898

Lara Aline

Definição de regras para geração do evento R\-2098 Reinf 

MFS\-90001

Alessandra Cristina Navatta

Alteração da referência do arquivo de de\_para \(versão 2\.1\.1\)

__Obs\. O ajuste mapeado nesta demanda, refere\-se a atualização funcional\. Não há impactos na implementação__

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral de Geração do Evento R\-2098\.__

O evento R\-2098 do SPED \- REINF tem por objetivo informar a reabertura do movimento de um período já encerrado, possibilitando o envio de retificações ou novos eventos periódicos\. Ele será gerado com os registros:

 __Reinf__ – EFD \- Reinf

 __evtReabreEvPer __– Evento de reabertura de eventos periódicos

 __ideEvento__ – Informações de Identificação do Evento

 __ideContri__ – Informações de Identificação do Contribuinte

Observar orientações existentes no arquivo " TR\_REINF\_DEXPARA\_V2\.1\.1\.xlsx "\.

- __Origem das informações__: Cadastro do Estabelecimento\. 
- __Regra de seleção__: O Registro R\-2098 é utilizado para informar a reabertura do movimento de um período já encerrado, possibilitando o envio de retificações ou novos eventos periódicos\. 

__Mensageria Log:__ 

1 \- Verificar se dentro do período de apuração existe algum evento periódico nas tabelas de ocorrência com IND\_STATUS = ‘1’ ou ‘2’, então não permitir a geração do Evento R\-2098 – Reabertura e exibir a seguinte mensagem:

Evento R\-2098 – Reabertura dos Eventos Periódicos

“Período de Apuração não pode ser fechado, enquanto existir eventos de movimento não enviados ou aguardando retorno do Fisco\.”

Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód\. do Estab\.: XXXXX

2 \- Verificar se já foi efetuada a geração e envio do evento R\-2098 – Reabertura para esse período de apuração, caso ainda não tenha retorno \(IND\_STATUS = 2\), exibir a seguinte mensagem:

Evento R\-2098 – Reabertura dos Eventos Periódicos

“A reabertura do período já foi executada e seu evento enviado ao Fisco, mas ainda aguarda retorno\. Somente refazer esta operação, caso o retorno seja erro\.”

Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód\. do Estab\.: XXXXXX

MFS\-11898

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

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


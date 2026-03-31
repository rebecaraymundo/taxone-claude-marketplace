# MTZ_REINF_Geracao_Evento_Movimento_R9000

- **Fonte:** MTZ_REINF_Geracao_Evento_Movimento_R9000.docx
- **Modificado:** 2023-03-28
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Geração evento R\-9000 \- REINF

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-11897

Lara Aline

Definição de regras para geração do evento R\-9000 Reinf 

MFS\-90001

Alessandra Cristina Navatta

Alteração da referência do arquivo de de\_para \(versão 2\.1\.1\)

__Obs\. O ajuste mapeado nesta demanda, refere\-se a atualização funcional\. Não há impactos na implementação__

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral de Geração do Evento R\-9000\.__

O evento R\-9000 do SPED \- REINF tem por objetivo tornar sem efeito os eventos, quando enviados indevidamente, seja como evento não periódico \(R\-3010\), seja como um dos eventos periódicos \(R\-2010 a R\-2070\)\. Ele será gerado com os registros:

 __Reinf__ – EFD \- Reinf

 __evtExclusao__ – Evento destinado a exclusão de eventos

 __ideEvento__ – Informações de Identificação do Evento

 __ideContri__ – Informações de Identificação do Contribuinte

 __infoExclusao __– Registro que identifica o evento objeto da exclusão

Observar orientações existentes no arquivo " TR\_REINF\_DEXPARA\_V2\.1\.1\.xlsx"\. 

- __Origem das informações__: Cadastro do Estabelecimento\. 
- __Regra de seleção__: O Registro R\-9000 é utilizado para informar a exclusão de algum evento enviado indevidamente\.

__Mensageria Log:__ 

1 \- Se o evento anterior do processo ainda não foi recebido com sucesso/advertência no fisco \(IND\_STATUS <> ‘3’\) então exibir a seguinte mensagem: 

Evento R\-9000 – Exclusão de Eventos

“Evento não pode ser excluído, enquanto não for recebido pelo fisco com sucesso ou advertência"\. 

Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód\. do Estab\.: XXXXXX

2 \- Se o evento anterior do processo já tiver sido enviado e não tiver retorno ainda \(IND\_STATUS = 2 \- “Evento REINF Enviado”\) então exibir a seguinte mensagem: 

Evento R\-9000 – Exclusão de Eventos

“A exclusão deste evento já foi executada e seu evento enviado ao Fisco, mas ainda aguarda retorno\. Somente refazer esta operação caso o retorno seja erro\.” 

Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód\. do Estab: XXXXXX

3 \- Se o evento já foi excluído e recebido com sucesso/advertência no fisco \(IND\_STATUS = ‘3’\) então exibir a seguinte mensagem: 

Evento R\-9000 – Exclusão de Eventos

“Evento já foi excluído\. O Evento de Exclusão foi recebido pelo Fisco com sucesso ou advertência\.

Identificação do Contribuinte: Tipo Inscrição: X / N° de Inscrição: XXXXXXXX / Validade Inicial: XXXXX / Cód\. do Estab\.: XXXXXX

MFS\-11897

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
- __Nível hierárquico do registro__: filho do registro evtExclusao
- __Ordenação__: não se aplica\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Um por arquivo

MFS\-11897

RN02

__Campo tpInsc__

Será gerado com conteúdo igual a “1”

MFS\-11897

RN03

__Campo nrInsc__

Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento\. Com base neste campo podemos entender que o REINF será gerado com base em um estabelecimento Centralizador\.

MFS\-11897

- __Registro infoExclusao – Registro que identifica o evento objeto da exclusão\.__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


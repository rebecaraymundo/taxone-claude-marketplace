# MTZ_REINF_Geracao_Evento_Movimento_R4040

- **Fonte:** MTZ_REINF_Geracao_Evento_Movimento_R4040.docx
- **Modificado:** 2024-04-04
- **Tamanho:** 89 KB

---

THOMSON REUTERS

Módulo REINF

Geração do Evento R\-4040

\(Pagamentos/Créditos a Beneficiários não Identificados\) 

__Localização__: Menu SPED, módulo EFD\-REINF, menu REINF à Geração Prévia à Movimentos à Evento R\-4040

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS\-79893__

Alessandra Cristina Navatta

Criação da geração do Evento R\-4040\- Pagamentos/créditos a beneficiários não identificados \(atendimento ao layout 2\.1 do REINF\)

11/04/2022

MFS\-90001

Alessandra Cristina Navatta

Alteração da versão 2\.1 para 2\.1\.1 e referência do arquivo de de\_para

__Obs\. Os ajustes mapeados nesta demanda, referem\-se a atualização funcional\. Não há impactos na implementação__

02/08/2022

MFS537211

Alessandra Cristina Navatta

Adequação da geração do evento R\-4040, para atendimento ao layout 2\.1\.2

Ajustes efetuados:

- Inclusão do campo ideEvtAdic na tag ideEstab
- Inclusão de opção válida no campo natRend \(tag ideNat\)
- Inclusão de validação no campo vlrLiq \(tag infoPgto\)
- Inclusão de validação no campo vlrBaseIR \(tag infoPgto\)
- Inclusão do campo dtEscrCont \(tag infoPgto\)

13/07/2023

 

###### __DESCRIÇÃO__

__OS/CH__

__Regra Geral de Geração do Evento R\-4040\.__

O evento R\-4040 do SPED \- REINF tem por objetivo gerar informações de Pagamentos/créditos a beneficiários não identificados\. Ele será gerado com os registros:

 __Reinf__ – EFD \- Reinf

__ evtBenefNId__ – Evento Beneficiários não identificados

 __ideEvento__ – Informações de Identificação do Evento

 __ideContri__ – Informações de Identificação do Contribuinte

__ideEstab \-__ Informações de Identificação do Estabelecimento

__ideNat __– Identificação da Natureza do Rendimento

__infoPgto–__ Informações de pagamentos a beneficiários não identificados

__ infoProcRet__– Processos relacionados a não retenção de tributos

Observar orientações existentes no arquivo " TR\_REINF\_DEXPARA\_V2\.1\.1\.xlsx "\. 

__Origem das informações__: Cadastro do Estabelecimento;

                             SAFX279 \-Tabela de Retenções na Fonte \- Beneficiários Não Identificados;

                             SAFX282 \- Processos Administrativos/Judiciais Referente aos Beneficiários não Identificados;

- __Regra de seleção__: O Registro R\-4040 é demonstrará as informações de Pagamentos/créditos a beneficiários não identificados\.

Ele será gerado com base nas informações da SAFX279\- Tabela de Retenções na Fonte \- Beneficiários Não Identificados e SAFX282 \- Processos Administrativos/Judiciais Referente aos Beneficiários não Identificados; , considerando os seguintes critérios:

\- O COD\_ESTAB seja de um estabelecimento indicado pelo usuário;

\-Os registros devem estar compreendidos \(Data do Movimento, da SAFX279\) no período da Apuração do Arquivo 

- __Tela de Geração Prévia e Painel de Eventos:__
- Pela tela de Geração Prévia, só serão permitidas gerações originais\. 
- Na tela de Painel de Eventos, dependendo do status pode ser feita geração original\. Já as gerações retificadoras, sempre serão realizadas pela tela do painel, pela opção ‘Reprocessar Evento’\.
- __Original/Retificação__: Os critérios para identificar se o evento a ser gerado será original ou retificador serão os seguintes:
- Se não houver ocorrência de geração de evento anterior, criar nova ocorrência de arquivo original\.
- Se houver ocorrência de geração anterior com status “Evento Enviado” exibir a seguinte mensagem no log de geração:

Evento R4040 – Pagamentos/créditos a beneficiários não identificados                   

              Evento não gerado\. Existe evento anterior enviado aguardando retorno\.

              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração anterior com status “Evento REINF Recebido com Sucesso ou Advertência” verificar se há evento de exclusão, então:

\- Se __não__ existir evento de exclusão então, criar ocorrência de arquivo de retificação\.

\- Se existir, evento de exclusão considerar os status, então:

Evento de exclusão com status de “Evento REINF Enviado” exibir a seguinte mensagem no log de geração:

  

             Evento R4040 – Pagamentos/créditos a beneficiários não identificados   

             Evento não gerado\. Existe evento de exclusão anterior enviado aguardando retorno\.

             Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

          Evento de exclusão com status “Evento Recebido com sucesso ou Advertência” então, verificar se há ocorrência

          anterior de evento periódico com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova

          ocorrência de arquivo de retificação, se __não__ houver, criar original\.

              \- Se existir evento de exclusão com status “Evento REINF Recebido com Erro” ou “Cancelado” ou “Erro na Geração do XML” então, criar nova ocorrência de retificação\.

             \- Se existir evento de exclusão com status “Aguardando Geração do XML” então exibir a seguinte mensagem no log de      geração:

                

              Evento R4040 – Pagamentos/créditos a beneficiários não identificados   

              Evento não gerado\. Existe evento anterior não enviado\.

              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração anterior com status “Evento REINF Recebido com erro”, então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova ocorrência de arquivo de retificação, se __não__ houver, criar original\.
- Se houver ocorrência de geração anterior com status “Aguardando Geração do XML” ou “Cancelado” ou “Erro na Geração do XML” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova ocorrência de arquivo de retificação, se __não__ houver, criar original\.
- __Fechamento/Reabertura:__ Critérios de geração do evento considerando a situação do período\.
- Se não houver ocorrência de geração de evento de fechamento, prosseguir com a geração\.
- Se houver ocorrência de geração de evento de fechamento considerar os status então:

                      \- Evento de fechamento com status de “Evento Reinf Enviado” exibir a seguinte mensagem no log de geração:

                      

                  R4040 – Pagamentos/créditos a beneficiários não identificados   

                  Evento não gerado\. Existe evento de fechamento do período enviado aguardando retorno\.

                  Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

                      \- Evento de fechamento com status de “Evento REINF Recebido com Sucesso ou Advertência” exibir a seguinte

                        mensagem no log de geração:

               

                  R4040 – Pagamentos/créditos a beneficiários não identificados   

                  Evento não gerado\. Período Fechado\.

                  Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração de evento de reabertura correspondente, com status “Evento REINF Recebido com

Sucesso ou Advertência”, prosseguir com a geração\.

        

       \- Evento de fechamento com status de “Evento REINF Recebido com erro” ou “Cancelado” ou “Erro na Geração do 

           XML” ou “Evento Excluído na Mensageria” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, exibir a seguinte mensagem no log de geração:

                   R4040 – Pagamentos/créditos a beneficiários não identificados                     

                   Evento não gerado\. Período Fechado\.

                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

 

                   Se não houver evento de fechamento com status “Evento REINF Recebido com Sucesso ou Advertência”,

                   prosseguir com a geração\. 

                       \- Evento de Fechamento com status de “Aguardando Geração do XML”, exibir a seguinte mensagem no log de   

                         geração:

                   R4040 – Pagamentos/créditos a beneficiários não identificados   

                   Evento não gerado\. Existe evento de fechamento do período não enviado\.

                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- __Gravação dos Registros__: Todos os registros recuperados na geração do evento R\-4040; são gravados em uma tabela\. Esta tabela é utilizada na emissão do relatório de conferência do evento \(formato “Analítico”\), que mostra por natureza de rendimento e data de fato gerador as informações de Pagamentos/créditos a beneficiários não identificados\. Além do formato sintético, que o agrupamento, não considera a data do movimento\.      

MFS\-79893

MFS\-90001

__ __

*Detalhamento das Regras:*

__Registro evtBenefNId__ – Evento Beneficiários não identificados

id

Identificação do evento, conforme REGRA\_VALIDA\_ID\_EVENTO: 

“ID” \+ “1” \+ CNPJ do estabelecimento \+ data da geração \(AAAAMMDD\) \+ hora da geração \(HHMMSS\) \+ sequencial

<a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>CNPJ – 8 primeiras posições do CNPJ, completando com zeros à direita;

Sequencial \(99999\) \- Número sequencial da chave\. Deve ser incrementado apenas quando houver a geração de eventos na mesma data/hora\. 

__Registro ideEvento__ \- Informações de Identificação do evento\.

indRetif

Este campo será gerado de acordo com a verificação de status descrita no item “*3\-Verificação do Status de Eventos já Gerados*”:

__Se__ for a primeira geração do evento do contribuinte no período:

      O campo será gerado com “__1__” \(__Arquivo Original__\);

__Senão__

      Neste caso o preenchimento do campo depende do status do evento gerado anteriormente:

      Se status do evento original = 8 ou = 9 à O campo será gerado com “__2__” \(__Retificação__\);

      Se status do evento original <> 8 e <> 9 à O campo será gerado com “__1__” \(__Arquivo Original__\);

nrRecibo

Este campo será gerado de acordo com o conteúdo do campo anterior \(__indRetif__\), da seguinte forma:

Se indRetif = “1” \(Arquivo Original\)

     Nesse caso este campo *não* será gerado;

Se indRetif = “2” \(Retificação\)

     Nesse caso este campo será gravado com o número do recibo do arquivo a ser retificado\. Ou seja, com o conteúdo

     do campo nrRecibo que consta no *evento original*;

 

perApur

Mês e ano do período informado na tela da geração, no formato AAAA\-MM \(conforme orientação do layout\)

tpAmb

Campo “Tipo de ambiente” da parametrização “Dados Iniciais” \(ver acima a regra para a recuperação dos dados desta parametrização\)

procEmi

Conteúdo fixo = “1” \(= Aplicativo do contribuinte\)

verProc 

Versão do sistema DW\. Esta informação é gerada de forma fixa = “V2R010”\. 

*Obs: A princípio, a definição previa informar neste campo a versão do produto informada na tela da geração\. No entanto, este entendimento é equivocado, pois como descreve o manual trata\-se da versão do aplicativo \(do empregador ou governamental\) utilizado para gerar o evento\. No caso, trata\-se da versão do próprio DW\. O REINF já trabalha desta forma\.*

__Registro ideContri__ \- Informações de identificação do contribuinte\.

tpInsc

Conteúdo fixo = “1”

nrInsc

CNPJ do estabelecimento, considerando apenas as 8 primeiras posições do CNPJ, completando com zeros à direita\. 

__Registro ideEstab__\- Informações de identificação do estabelecimento

tpInscEstab

Conteúdo fixo = “1”

nrInscEstab

CNPJ do estabelecimento

ideEvtAdic

__\[ALTERAÇÂO MFS\-537211\]__ Identificador de evento adicional por beneficiário a critério do declarante

Este campo foi inserido na versão 2\.1\.2 do layout\. Não será gerado pelo sistema\.

__Registro ideNat__ – Identificação da Natureza do Rendimento 

NatRend

__\[ALTERAÇÃO MFS\-537211\]__ Inclusão de valor válido \(nat\. Rendimento 12052\), atendendo o layout 2\.1\.2

Valores Válidos: 

12052;

19001;

19009

O Registro será recuperado da SAFX279, campo Natureza do Rendimento\.

__Registro __<a id="_Hlk523501001"></a>__infoPgto__ \- Informações de pagamentos a beneficiários não identificados

Este registro será gerado quando existir informações na SAFX279\-Tabela de Retenções na Fonte \- Beneficiários Não Identificados\. 

Agrupar por contribuinte, natureza de rendimento e data de movimento, dentro do período de apuração\. 

Poderão existir até 31 registros de pagamentos, para cada registro recuperado, será gerado um registro __infoPgto, __com as informações descritas abaixo:

dtFG

Campo 03 \- Data do Movimento \(SAFX279\)

O formato da data deve ser AAAA\-MM\-DD\.

 

__MFS\-79893__

vlrLiq

Campo 05 \- Valor Líquido \(SAFX279\)

Validação: \*\* O valor deve ser maior que zero\. 

__\[ALTERAÇÂO MFS\-537211\] __Inclusão de Validação:

Informação obrigatória e exclusiva se a natureza do rendimento informada em \{natRend\} for igual a \[19001\] ou \[19009\]\.

\*\*Estas validações ocorrem na importação da SAFX279 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >>Beneficiários não Identificados\)

__MFS\-79893__

__MFS\-53211__

vlrBaseIR

Campo 06 \- Valor Reajustado \(SAFX279\)

__\[ALTERAÇÂO MFS\-537211\]__ Validações: 

\*\*Deve ser maior que zero\. 

\*\*Se a natureza de rendimento informada em \{natRend\} for igual a \[19001\] ou \[19009\], deve corresponder a \(\{vlrLiq\} / 0,65\)\.

\(\*\*Estas validações ocorrem na importação da SAFX279 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Beneficiários não identificados\)

__MFS\-79893__

__MFS\-53211__

VlrIR

Campo 07 \- Valor do Imposto de Renda Retido na Fonte \(SAFX279\)

__MFS\-79893__

dtEscrCont

__\[ALTERAÇÂO MFS\-537211\]__ Data da escrituração Contábil 

Este campo foi inserido na versão 2\.1\.2 do layout\. 

Recuperar o campo 09 – Data Escrituração Contábil da SAFX279\.

Validações:

\*\* Informação obrigatória e exclusiva se a natureza do rendimento informada no campo \{natRend\} for igual a \[12052\]\. 

\*\*Se informada, deve ser uma data compreendida no período de apuração informado em \{perApur\}\.

\(\*\*Estas validações ocorrem na importação da SAFX279 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Beneficiários não identificados\)

__MFS\-53211__

descr

Campo 08 – Descrição \(SAFX279\)

__MFS\-79893__

__Registro __<a id="_Hlk524440900"></a><a id="_Hlk524441786"></a>__infoProcRet__ \- Informações de processos relacionados a não retenção de tributos ou a depósitos judiciais\.

Este registro será gerado quando existir informações na SAFX282\-Processos Administrativos/Judiciais Referente aos Beneficiários não Identificados\.

Poderão existir 50 registros de processos \(__infoProcRet\)\. __Para cada registro recuperado,__ __será gerado um registro com as informações descritas abaixo: 

TpProcRet

Campo 05 \- Tipo do Processo \(SAFX282\)\. Este campo deve estar previamente cadastrado na SAFX2058, Campo 01 Tipo do Processo \(SAFX2058\)

Opções Válidas:

1 \- Administrativo;

2 \- Judicial\. 

Valores válidos: 1, 2

__MFS\-79893__

nrProcRet

Campo 06 \- Número do Processo \(SAFX282\)\. Este campo deve estar previamente cadastrado na SAFX2058, Campo 02 Número do Processo \(SAFX2058\)

__MFS\-79893__

codSusp

Campo 07 \- Código do Indicativo da Suspensão de Exigibilidade de Tributos \(SAFX282\)\. Este campo deve estar previamente cadastrado na SAFX2059, Campo 05 \- Indicador da Suspensão de Exigibilidade de Tributos \(SAFX2059\) 

__MFS\-79893__

vlrBaseSuspIR

Campo 08\- Valor da Base com Exigibilidade Suspensa \(SAFX282\)

__MFS\-79893__

vlrNIR

Campo 09 \- Valor da Retenção que Deixou de ser Efetuada \(SAFX282\)

Validações:

\*\*Este campo é de preenchimento obrigatório se o campo IND\_DEPOSITO da SAFX2059 for igual a ‘N’\.

\(\*\*Esta validação ocorre na importação da SAFX282 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >>Beneficiários Não Identificados >> Processos R\-4040\)

__MFS\-79893__

VlrDepIR

Campo 10 \- Valor do Depósito Judicial \(SAFX282\)

Validações:

\*\*Este campo é de preenchimento obrigatório se o campo IND\_DEPOSITO da SAFX2059 for igual a ‘S’\. \(\*\*Esta validação ocorre na importação da SAFX282 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >>Beneficiários Não Identificados >> Processos R\-4040\)

__MFS\-79893__

= = = = = =

 


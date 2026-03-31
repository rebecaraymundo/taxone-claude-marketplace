# MTZ_REINF_Geracao_Evento_Movimento_R2060

- **Fonte:** MTZ_REINF_Geracao_Evento_Movimento_R2060.docx
- **Modificado:** 2024-06-11
- **Tamanho:** 87 KB

---

­­­­

THOMSON REUTERS

Geração evento R\-2060 \- REINF

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-9074

Geração Evento

Definição de regras para geração do evento R\-2060 Reinf\. 

MFS\-10589

Geração Evento

Inclusão de Campo no Registro IdeEstab

MFS\-12176

Elenilson Coutinho

Regra para tipo de arquivo Original/Retificação

MFS\-12180

Elenilson Coutinho

Regra de geração considerando eventos de fechamento/reabertura

MFS14002

Lara Aline

Alteração no layout conforme versão 1\.2

MFS14476

Lara Aline

Inclusão de observação no campo codAjuste

MFS14461

Lara Aline

Inclusão de regra de geração para o registro infoProc

MFS14129

Lara Aline

Inclusão de regra para o campo observação do registro nfs\.

MFS14997

Lara Aline

Inclusão da informação da SAFX252 no registro tipoAjuste

MFS16053

Lara Aline

Alteração no layout conforme versão 1\.3

MFS17138

Lara Aline

Inclusão status “Excluído na Mensageria” no tratamento de Fechamento/Reabertura

MFS17269

Lara Aline

Ajuste no campo VlrCPRBSuspTotal conforme nova versão 1\.3\.02\.

MFS18674

Lara Aline

Inclusão regra para sumarização dos valores do registro tipoCod

MFS18702

Lara Aline

Alteração da Geração Prévia retirando a possibilidade de Geração de Eventos Retificados, eventos retificadores serão gerados apenas no Painel de Controle de Eventos

MFS18785

Lara Aline

Ajuste na geração dos campos vlrExcRecBruta e vlrAdicRecBruta para recuperar da SAFX252\.

MFS21178

Lara Aline

Ajuste no campo vlrCPRBapur

MFS\-90001

Alessandra Cristina Navatta

Alteração da referência do arquivo de de\_para \(versão 2\.1\.1\)

__Obs\. O ajuste mapeado nesta demanda, refere\-se a atualização funcional\. Não há impactos na implementação__

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral de Geração do Evento R\-2060\.__

O evento R\-2060 do SPED \- REINF tem por objetivo gerar informações de Retenção Contribuição Previdenciária Sobre a Receita Bruta\. Ele será gerado com os registros:

 __Reinf__ – EFD \- Reinf

 __evtCPRB__ – Evento da Contribuição Previdenciária Sobre a Receita Bruta\- CPRB

 __ideEvento__ – Informações de Identificação do Evento

 __ideContrib__ – Informações de Identificação do Contribuinte

 __infoCPRB__ – Informações da Contribuição Previdenciária Sobre a Receita Bruta

 __ideEstab__ – Identificação do Estabelecimento

 __tipoCod__ – Registro que apresenta o valor total da receita por tipo de código de atividade econômica\.

__\[Alterado MFS14002\]__

\[MFS\-10589\]

__ nfs__– Detalhamento do Receita Bruta

__ tipoAjuste – __Tipo do ajuste da CPRB

__ infoProc __– Informações de processos relacionados a Suspensão da CPRB

Observar orientações existentes no arquivo " "TR\_REINF\_DEXPARA\_V2\.1\.1\.xlsx"\.

- __Origem das informações__: SAFX185, SAFX252 e SAFX2113
- __Regra de seleção__: O Registro R\-2060 é utilizado para demonstrar informações de Contribuição Previdenciária sobre a Receita Bruta \- CPRB\. Ele será gerado com base em Informações da tabela de Apuração da Contribuição Previdenciária sobre a Receita Bruta\.
- Para obtermos as informações para sua geração, devemos recuperar registros da tabela SAFX185, SAFX252 e SAFX2113, considerando os seguintes critérios:
- \- O COD\_ESTAB seja de um estabelecimento indicado pelo usuário;

\- Os campos DATA\_INI e DATA\_FIM compreendam o período informado pelo usuário;

__\[MFS\-12176\]__

- __Original/Retificação__: Os critérios para identificar se o evento a ser gerado será original ou retificador serão os seguintes:
- Se não houver ocorrência de geração de evento anterior, criar uma nova ocorrência de arquivo original\.
- Se houver ocorrência de geração anterior com status “Evento Enviado” exibir a seguinte mensagem no log de geração:

              Evento R2060 – Contribuição Previdenciária Sobre a Receita Bruta \- CPRB

              Evento não gerado\. Existe evento anterior enviado aguardando retorno\.

              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração anterior com status “Evento REINF Recebido com Sucesso ou Advertência” verificar se há evento de exclusão, então:

\- Se __não__ existir evento de exclusão então, criar ocorrência de arquivo de retificação\.

\- Se existir, evento de exclusão considerar os status, então:

Evento de exclusão com status de “Evento REINF Enviado” exibir a seguinte mensagem no log de geração:

  

             Evento R2060 – Contribuição Previdenciária Sobre a Receita Bruta \- CPRB

             Evento não gerado\. Existe evento de exclusão anterior enviado aguardando retorno\.

             Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

          Evento de exclusão com status “Evento Recebido com sucesso ou Advertência” então, verificar se há ocorrência

          anterior de evento periódico com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar uma ocorrência de arquivo de retificação, se __não__ houver, criar original\.

              \- Se existir evento de exclusão com status “Evento REINF Recebido com Erro” ou “Cancelado” ou “Erro na Geração do                          XML” então, criar uma ocorrência de retificação\.

             \- Se existir evento de exclusão com status “Aguardando Geração do XML” então exibir a seguinte mensagem no log de      geração:

                

              Evento R2060 – Contribuição Previdenciária Sobre a Receita Bruta \- CPRB

              Evento não gerado\. Existe evento anterior não enviado\.

              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração anterior com status “Evento REINF Recebido com erro”, então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar  uma ocorrência de arquivo de retificação, se __não__ houver, criar original\.
- Se houver ocorrência de geração anterior com status “Aguardando Geração do XML” ou “Cancelado” ou “Erro na Geração do XML” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar uma ocorrência de arquivo de retificação, se __não__ houver, criar original\.

__\[MFS18702\]__

__Importante:__ Na tela Geração Prévia dos Movimentos serão gerados APENAS os eventos Originais, os eventos de Retificação deverão ser gerados diretamente pelo Painel de Controle de Eventos pela opção ‘Reprocessar Evento’\. Caso os eventos encontrados na tela de Geração Prévia dos Movimentos sejam identificados nos critérios acima como Retificação esses deverão ser desconsiderados e não gerados, pela tela de Geração Prévia dos Movimentos serão gerados apenas os eventos que se enquadrarem como ‘Original’\.

__\[MFS\-12180\]            __

- __Fechamento/Reabertura:__ Critérios de geração do evento considerando a situação do período\.
- Se não houver ocorrência de geração de evento de fechamento, prosseguir com a geração\.
- Se houver ocorrência de geração de evento de fechamento considerar os status então:

                      \- Evento de fechamento com status de “Evento Reinf Enviado” exibir a seguinte mensagem no log de geração:

                      

                  Evento R2060 – Contribuição Previdenciária Sobre a Receita Bruta \- CPRB

                  Evento não gerado\. Existe evento de fechamento do período enviado aguardando retorno\.

                  Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

                      \- Evento de fechamento com status de “Evento REINF Recebido com Sucesso ou Advertência” exibir a seguinte

                        mensagem no log de geração:

               

                  Evento R2060 – Contribuição Previdenciária Sobre a Receita Bruta \- CPRB

                  Evento não gerado\. Período Fechado\.

                  Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração de evento de reabertura correspondente, com status “Evento REINF Recebido com

Sucesso ou Advertência”, prosseguir com a geração\.

        

       __\[Alterado MFS17138\]__ 

       \- Evento de fechamento com status de “Evento REINF Recebido com erro” ou “Cancelado” ou “Erro na Geração do 

           XML” ou “Evento Excluído na Mensageria” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, exibir a seguinte mensagem no log de geração:

                   Evento R2060 – Contribuição Previdenciária Sobre a Receita Bruta \- CPRB

                   Evento não gerado\. Período Fechado\.

                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

 

                   Se não houver evento de fechamento com status “Evento REINF Recebido com Sucesso ou Advertência”,

                   prosseguir com a geração\. 

                       \- Evento de Fechamento com status de “Aguardando Geração do XML”, exibir a seguinte mensagem no log de   

                         geração:

                   Evento R2060 – Contribuição Previdenciária Sobre a Receita Bruta \- CPRB

                   Evento não gerado\. Existe evento de fechamento do período não enviado\.

                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

   MFS\-9074

MFS\-10589

MFS\-12176

MFS12180

MFS14002

MFS14461

MFS17138

MFS18702

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
- __Nível hierárquico do registro__: filho do registro evttCPRB
- __Ordenação__: não se aplica\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Um por arquivo

MFS9074

RN02

__Campo TpInsc__

Será gerado com conteúdo "1", uma vez que não atendemos PF\.

MFS14821

RN03

__Campo nrInsc__

Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento\. Com base neste campo podemos entender que o REINF será gerado com base em um estabelecimento Centralizador\. 

MFS14821

- __Registro IdeEstab – Identificação do Estabelecimento que Comercializou a Produção__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN02

- __Origem das informações__: Cadastro do Estabelecimento e SAFX185
- __Regra de seleção__: Este registro servirá para identificar o estabelecimento centralizador \(Matriz\)\.
- __Campos\-Chave__: tpInscEstab, nrInscEstab
- __Nível hierárquico do registro__: filho do registro infoCPRB
- __Ordenação__: não se aplica\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Para cada infoCPRB poderá existir “N” ideEstab

MFS\-9074

RN03

__Campo tpInsEstab__

Será gerado com conteúdo igual a “1”

MFS9074

RN04

__nrInscEstab__

Será Gerado com o conteúdo do campo “CGC” do Cadastro do Estabelecimento informado na SAFX185\.

MFS9074

RN05

__VlrRecBrutaTotal__

Será gerado com o conteúdo do campo “VLR\_REC\_BRT” da SAFX185

MFS9074

RN06

__VlrCPApurTotal__

Será gerado com a somatória do conteúdo do campo “VLR\_CONT\_PREV\_REINF” da SAFX185\. 

MFS9074

RN07

__VlrCPRBSuspTotal__

Será gerado com a somatória do conteúdo do campo “VLR\_PREV\_EXIG\_SUSP” da SAFX2113, com exceção dos valores informados com o Indicador de Suspenção \(ind\_susp\) igual a ‘92’, ou seja, deve ser identificado o indicador de suspensão \(SAFX2059 – Cadastro de Informação de Suspensão de Exigibilidade de Tributos\) através do campo Código de Suspensão \(COD\_SUSP\) informado na SAFX2113\.

MFS14461

MFS17269

RN08

__tpProcesso__

MFS9074

MFS14002

RN09

__nrProcesso__

MFS9074

MFS14002

RN10

__codSusp__

MFS10589

MFS14002

- __Registro TipoCod – Identificação do Valor Total da Receita por Tipo de Código de Atividade Econômica__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN11

- __Origem das informações__: SAFX185, Aba Ajustes \(Tela de “Contribuição Previdenciária da Receita da Bruta”\)
- __Regra de seleção__: Este registro servirá identificar valor total da receita por tipo de código de atividade econômica\.
- __Campos\-Chave__: codAtivEcon
- __Nível hierárquico do registro__: filho do registro ideEstab\.
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: para cada ideEstabPrest poderá existir “N” tipoCod

MFS9074

RN12

__Campo codAtivEcon__

Será gerado com o conteúdo do campo “COD\_ATIV\_CONT\_PREV” da SAFX185

MFS9074

RN13

__Campo vlrRecBrutaAtiv__

Será gerado com o conteúdo do campo VLR\_REC\_BRT\_ATIV da SAFX185, sumarizado por Atividade \(campo COD\_ATIV\_CONT\_PREV\)\.

MFS9074

MFS18674

RN14

__Campo vlrExcRecBruta__

Será gerado com o conteúdo do campo “VL\_AJ\_REINF” quando “IND\_AJ\_REINF = 0 \- Ajuste de redução” da SAFX252, sumarizado por Atividade \(campo COD\_ATIV\_CONT\_PREV\)\. Caso não preenchido gravar “0”\. 

MFS9074

MFS18674

MFS18785

RN15

__vlrAdicRecBruta__

Será gerado com o conteúdo do campo “VL\_AJ\_REINF” quando “IND\_AJ\_REINF = 1 \- Ajuste de acréscimo” da SAFX252, sumarizado por Atividade \(campo COD\_ATIV\_CONT\_PREV\)\. Caso não preenchido gravar “0”\.

MFS9074

MFS18674

MFS18785

RN16

__vlrBcCPRB__

Será gerado com o conteúdo do campo “VLR\_BASE\_CONT\_PREV\_REINF” da SAFX185, sumarizado por Atividade \(campo COD\_ATIV\_CONT\_PREV\)\.

MFS9074

MFS18674

RN17

__Campo vlrCPRBapur__

Será gerado com o conteúdo do campo “VLR\_CONT\_PREV\_REINF” da SAFX185, sumarizado por Atividade \(campo COD\_ATIV\_CONT\_PREV\)\.

\[MFS21178\]

O valor deve ser truncado na segunda casa decimal\.

MFS9074

MFS18674

MFS21178

RN18

__Campo codAnaCont__

Será tratado na geração do registro R\-1000

MFS9074

MFS14002

- __Registro nfs \- Registro de Detalhamento da Receita Bruta__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN19

- __Origem das informações__: SAFX07 e SAFX09 \(Notas fiscais que são apresentadas na aba "Detalhamento da Receita Bruta"\)
- __Regra de seleção__: Este registro servirá para detalhar a receita bruta no nível de nota\.
- __Campos\-Chave__: serie, numDocto
- __Nível hierárquico do registro__: filho do registro tipoCod\.
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.

__\[MFS10589\]__

- __Ocorrência__: para cada tipoCod poderá existir “N” nfs\.

MFS9074

MFS10589

MFS14002

RN20

__Campo serie__

Será gerado com o conteúdo do campo SERIE\_DOCFIS da SAFX07/09\. Caso não preenchido gravar “0”\.

MFS9074

MFS14002

RN21

__Campo numDocto__

Será gerado com a informação do campo NUM\_DOCFIS da SAFX07/09\.

MFS9074

MFS14002

RN22

__Campo dtEmissaoNF__

Será gerado com o conteúdo do campo DATA\_EMISSAO da SAFX07/09\.

MFS9074

MFS14002

RN23

__Campo vlrBruto__

Será gerado com o conteúdo do campo VALOR\_PRODUTO da SAFX07\.

MFS9074

MFS14002

- __Registro tipoAjuste \- Registro Tipo de Ajuste__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN24

- __Origem das informações__: Aba Ajustes \(Tela de “Contribuição Previdenciária da Receita da Bruta”\) \(SAFX252\)
- __Regra de seleção__: Registro de Identificação do tipo de Ajuste
- __Campos\-Chave__: Não se aplica\.
- __Nível hierárquico do registro__: filho do registro tipoCod\.
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Poderá não existir ou existir “N” tipoAjuste\.

MFS9074

MFS14997

RN25

__Campo tpAjuste__

Será gerado com o conteúdo do campo “Tipo de Ajuste” da aba Ajustes da Contribuição Previdenciária Apurada \(SAFX252\)

MFS9074

MFS14997

RN26

__Campo codAjuste__

Será gerado com o conteúdo do campo “Código de Ajuste” da aba Ajustes da Contribuição Previdenciária Apurada \(SAFX252\)

Obs:

Caso selecionado os códigos 11, 12, ou 13 deverá considerar sempre o código “11”, pois para EFD\-REINF o código é genérico para as três situações\.

MFS9074

MFS14476

MFS14997

RN27

__Campo vlrAjuste__

Será gerado com o conteúdo do campo “Valor do Ajuste” da aba Ajustes da Contribuição Previdenciária Apurada \(SAFX252\)

MFS9074

MFS14997

RN28

__Campo descAjuste__

Será gerada com o conteúdo do campo “Descrição do Ajuste” da aba Ajustes da Contribuição Previdenciária Apurada \(SAFX252\)

MFS9074

MFS14997

RN29

__Campo dtAjuste__

Será gerado com o conteúdo do campo “Data do Ajuste” da aba Ajustes da Contribuição Previdenciária Apurada \(SAFX252\)

MFS9074

MFS14997

- __Registro__ __infoProc – Informações de processos relacionados a Suspensão da CPRB__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN30

- __Origem das informações__: SAFX2113, Aba Processos relacionados a Suspensão da CPRB \(Tela de “Contribuição Previdenciária da Receita da Bruta”\)\.
- __Regra de seleção__: Este registro servirá para informar os processos relacionados a Suspensão da CPRB
- __Campos\-Chave__: nrProc
- __Nível hierárquico do registro__: filho do registro tipoCod\.
- __Ordenação__: não se aplica\. 
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: para cada tipoCod poderá existir “50” infoProc

MFS14461

MFS16053

RN31

__Campo tpProc__

Será gerado com o conteúdo do campo “IND\_TIP\_PROC” da SAFX2113

MFS14461

RN32

__Campo nrProc__

Será gerado com o conteúdo do campo “NUM\_PROC” da SAFX2113\. 

MFS14461

RN33

__Campo codSusp__

Será gerado com o conteúdo do campo “COD\_SUSP” da SAFX2113\. 

Obs:

Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2060 \- Registro: Informações de processos relacionados a Suspensão da CPRB

“Campo Código do Indicativo da Suspensão deve ser numérico\." 

Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX

Estabelecimento: XXXX / Data Movimento: XXXX 

MFS14461

RN34

__Campo vlrCPRBSusp__

Será gerado com o conteúdo do campo “VLR\_PREV\_EXIG\_SUSP” da SAFX2113

MFS14461

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


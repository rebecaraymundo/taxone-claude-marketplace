# MTZ_REINF_Geracao_Evento_Movimento_R2010

- **Fonte:** MTZ_REINF_Geracao_Evento_Movimento_R2010.docx
- **Modificado:** 2026-02-12
- **Tamanho:** 109 KB

---

THOMSON REUTERS

Geração evento R\-2010 \- REINF

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-8958

Elenilson Coutinho

Definição de regras para geração do evento R\-2010 Reinf 

MFS\-10357

Elenilson Coutinho

Alteração/ Inclusão de registros

MFS\-11894

Lara Aline

Inclusão mensagens de logs RN03, 06, 09, 59, 60, 64 e 65\.

MFS\-12176

Elenilson Coutinho

Regra para tipo de arquivo Original/Retificação

MFS\-12180

Elenilson Coutinho

Regra de geração considerando eventos de fechamento/reabertura

MFS\-13131

Elenilson Coutinho

Alteração na geração considerando parametrização de Código de Atividade x Serviços Por Prestador

MFS\-13205 

Lara Aline

Ajuste nos campos vlrServicos15, vlrServicos20 e vlrServicos25 para recuperar informação dos novos campos da SAFX09\. 

MFS13362

Lara Aline

Exclusão dos campos codAnaCont, vlrMatEquip, vlrDedAlim, vlrDedTrans e codAtivEcon e ajuste na ocorrência do grupo idePrestServ\. Conforme Leiautes versão 1\.2\.

MFS13947

Lara Aline

Ajuste no campo nrInscEstab\.

MFS14222

Lara Aline

Ajuste para considerar o campo “Desconsiderar NFs sem Valor de Retenção informado” da tela de Dados Iniciais

MFS14463

Lara Aline

Ajuste na geração do evento R\-2010 para receber informações de notas de serviço de transporte \(SAFX08\)

MFS14129

Lara Aline

Inclusão de regra para o campo observação do registro nfs\.

MFS15338

Lara Aline

Ajuste para considerar o campo “Desconsiderar NFs fora da Competência” da tela de Geração Prévia dos Movimentos\.

MFS16568

Lara Aline

Ajuste no campo vlrBruto \(RN26\)

MFS17043

Lara Aline

Ajuste no campo numDocto \(RN24\)

MFS17138

Lara Aline

Inclusão status “Excluído na Mensageria” no tratamento de Fechamento/Reabertura

MFS17304

Lara Aline

Ajuste campo indCPRB e inclusão regra de agrupamento por CPF\_CGC da x04

MFS16936

Lara Aline

Inclusão de regra para as parametrizações de Retenção Previdenciárias\.

<a id="_Hlk515870749"></a>MFS18702

Lara Aline

Alteração da Geração Prévia retirando a possibilidade de Geração de Eventos Retificados, eventos retificadores serão gerados apenas no Painel de Controle de Eventos

MFS19130

Lara Aline

Inclusão do modelo 55 para notas conjugadas\.

MFS20045

Lara Aline

Ajuste no campo indCPRB

MFS20384

Lara Aline

Incluisão de log quando encontrar valor negativo nas notas fiscais\.

MFS20732

Lara Aline

Inclusão campo Período de Entrada das NFs\.

MFS21130

Lara Aline

Inclusão de mensagem de log para campo nrlnscEstab

MFS21632

Lara Aline

Ajuste no parâmetro Período de Entrada das NFs\.

MFS\-90001

Alessandra Cristina Navatta

Alteração da referência do arquivo de de\_para \(versão 2\.1\.1\)

__Obs\. O ajuste mapeado nesta demanda, refere\-se a atualização funcional\. Não há impactos na implementação__

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral de Geração do Evento R\-2010\.__

O evento R\-2010 do SPED \- REINF tem por objetivo gerar informações de Retenção Contribuição Previdenciária – Serviços Tomados\. Ele será gerado com os registros:

 __Reinf__ – EFD \- Reinf

 __evtServTom__ – Evento de Serviços Tomados 

 __ideEvento__ – Informações de Identificação do Evento

 __ideContri__ – Informações de Identificação do Contribuinte

 __infoServTom__ – Ser\. Tomados \(Cessão Mão de Obra ou Empreitada\)

 __ideEstabObra__ – Identificação do Estabelecimento/Obra Tomador dos Serviços

 __idePrestServ__ \-  Identificação do prestador de servi\-ços mediante cessão de mão de obra ou empreitada\.

 __nfs__ \- Notas Fiscais de Serviços \(CMO\) \- Emitidas por Terceiros

__\[MFS10357\]__

__infoTpServ \- __Informações sobre os tipos de Serviços constantes da NF

__infoProcRetPr – __Informação de Processo Retenção Principal

__infoProcRetAd \- __Informação de Processo Retenção Adicional

Observar orientações existentes no arquivo " TR\_REINF\_DEXPARA\_V2\.1\.1\.xlsx”

- __Origem das informações__: SAFX04, SAFX07, SAFX08, SAFX09 e Cadastro do Estabelecimento\.
- __Regra de seleção__: O Registro R\-2010 é utilizado para demonstrar informações de Retenção Contribuição Previdenciária \- Tomadores de Serviços\. Ele será gerado com base em Informações de Notas Fiscais de Serviço\.

Para obtermos as informações para sua geração, devemos recuperar registros das tabelas SAFX07, SAFX08 e SAFX09, considerando os seguintes critérios:

\- O COD\_ESTAB seja de um estabelecimento indicado pelo usuário; 

\- NFs cujo campo MOVTO\_E\_S seja diferente de "9";

\- O campo DATA\_EMISSAO deve compreender o período de geração\. Caso na tela de Geração Prévia dos Movimentos o parâmetro “Desconsiderar NFs fora da Competência” estiver selecionado, o campo DATA\_SAIDA\_REC também deve compreender o período de geração\.

__\[MFS20732/MFS21632\]__

\- Caso o campo ‘Período de Entrada das NFs’ estiver preenchido, o campo DATA\_EMISSAO e DATA\_SAIDA\_REC deve compreender o período de geração, mais as notas que o campo DATA\_EMISSAO compreender o período de geração e que o campo DATA\_SAIDA\_REC compreender o período informado no campo Período de Entrada das NFs, ou seja, iremos recuperar todas as notas que a Data de Emissão e Data de Entrada/Saída da nota compreender o período de geração __E__ as notas que a Data de Emissão compreender o período de geração e Data de Entrada/Saída da nota compreender o período informado no ‘Período de Entrada das NFs’\.

\- O campo SITUACAO deve ser diferente de "S";

\- Mercadoria : O campo COD\_CLASS\_DOC\_FIS deve ser igual a "1" ou "3";

\- Serviço : O campo COD\_CLASS\_DOC\_FIS deve ser igual a "2" ou "3";

\- O COD\_SERVICO OU COD\_PRODUTO deve ter sido associado a um tipo de Item na Parametrização de Identificação do Tipo de Serviço do Módulo REINF;

\- Para todas notas encontradas com o COD\_PRODUTO associado a um tipo de Item na Parametrização de Identificação do Tipo de Serviço do Módulo REINF, deverão ser recuperadas APENAS as notas fiscais cujo COD\_MODELO seja igual a ‘07’, ‘55’ ou ‘67’\.

- __Regra de Agrupamento__: O Registro R\-2010 será agrupado por CPF\_CGC da SAFX04\.

__Tratamento:__

__\[MFS20384\]__

Caso encontrado valores negativos \(\-\) nos campos de valores das notas recuperadas \(SAFX08/SAFX09\), a geração não será finalizada e será exibido a seguinte mensagem no log de geração:

       Evento R2010 – Retenção Contribuição Previdenciária – Serviços Tomados

       ‘A geração não foi concluída pois foi encontrado campo com valor negativo, favor verificar’\.

       Empresa/Estabelecimento: XX / XXXXX / Identificação do Nota: NF: XXXXX / Serie: XXXXXX

       Identificação do Campo: XXXXXX

__\[Alterado MFS16936\]__

Regra para as parametrizações de Retenção Previdenciária:

As parametrizações de Retenção Previdenciária são possíveis efetua\-las para qualquer Estabelecimento sendo ou não o Estabelecimento Centralizador, por padrão deverá ser utilizada a parametrização do estabelecimento Centralizador para todos os estabelecimentos que não possuam sua parametrização\. 

Para os estabelecimentos que possuem parametrização na geração será considerada a sua parametrização conforme exemplo abaixo:

Exemplo:

Estabelecimento Centralizador: REINFP – Possui ‘parametrização 1’

Estabelecimento Centralizado: REINF1 – Possui ‘parametrização 2’

Estabelecimento Centralizado: REINF2 – Não possui parametrização

1 \- Na geração dos dados do Estabelecimento Centralizador REINFP utilizaremos a ‘parametrização 1’;

2 \- Na geração dos dados do Estabelecimento Centralizado REINF1 utilizaremos a ‘parametrização 2’;

3 \- Na geração dos dados do Estabelecimento Centralizado REINF2 utilizaremos a ‘parametrização 1’;

__Importante: __Para os estabelecimentos que possuírem grupos diferentes do Estabelecimento Centralizador esses estabelecimentos somente serão considerados se houver a sua própria parametrização\. Caso contrário todas as notas desse estabelecimento centralizado não serão consideradas na geração\.__  __

__ \[Alterado MFS14222\]__

Importante:

Caso o campo “Desconsiderar NFs sem Valor de Retenção informado” estiver selecionado na tela de Dados Iniciais, deverão ser desconsideradas todas as notas fiscais que não tenham o Valor Base INSS \(VLR\_BASE\_INSS da SAFX08/SAFX09\) e/ou Valor de INSS Retido \(VLR\_INSS\_RETIDO da SAFX08/SAFX09\) informado\. Ou seja, quando o parâmetro estiver selecionado serão considerados apenas as notas fiscais que tenham o Valor Base INSS \(VLR\_BASE\_INSS da SAFX08/SAFX09\) e Valor de INSS Retido \(VLR\_INSS\_RETIDO da SAFX08/SAFX09\) informado\.

__\[MFS\-12176\]__

- __Original/Retificação__: Os critérios para identificar se o evento a ser gerado será original ou retificador serão os seguintes:
- Se não houver ocorrência de geração de evento anterior, criar nova ocorrência de arquivo original\.
- Se houver ocorrência de geração anterior com status “Evento Enviado” exibir a seguinte mensagem no log de geração:

              Evento R2010 – Retenção Contribuição Previdenciária – Serviços Tomados

              Evento não gerado\. Existe evento anterior enviado aguardando retorno\.

              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX\.

- Se houver ocorrência de geração anterior com status “Evento REINF Recebido com Sucesso ou Advertência” verificar se há evento de exclusão, então:

\- Se __não__ existir evento de exclusão então, criar ocorrência de arquivo de retificação\.

\- Se existir, evento de exclusão considerar os status, então:

Evento de exclusão com status de “Evento REINF Enviado” exibir a seguinte mensagem no log de geração:

  

             Evento R2010 – Retenção Contribuição Previdenciária – Serviços Tomados

             Evento não gerado\. Existe evento de exclusão anterior enviado aguardando retorno\.

             Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

          Evento de exclusão com status “Evento Recebido com sucesso ou Advertência” então, verificar se há ocorrência

          anterior de evento periódico com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova

          ocorrência de arquivo de  retificação, se __não__ houver, criar original\.

         

              \- Se existir evento de exclusão com status “Evento REINF Recebido com Erro” ou “Cancelado” ou “Erro na Geração do                          XML” então, criar nova ocorrência de retificação\.

             \- Se existir evento de exclusão com status “Aguardando Geração do XML” então exibir a seguinte mensagem no log de      geração:

                

              Evento R2010 – Retenção Contribuição Previdenciária – Serviços Tomados

              Evento não gerado\. Existe evento anterior não enviado\.

              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração anterior com status “Evento REINF Recebido com erro”, então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar  nova ocorrência de arquivo de retificação, se __não__ houver, criar original\. 
- Se houver ocorrência de geração anterior com status “Aguardando Geração do XML” ou “Cancelado” ou “Erro na Geração do XML” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar  nova ocorrência de arquivo de retificação, se __não__ houver, criar original\.

__\[MFS18702\]__

__Importante:__ Na tela Geração Prévia dos Movimentos serão gerados APENAS os eventos Originais, os eventos de Retificação deverão ser gerados diretamente pelo Painel de Controle de Eventos pela opção ‘Reprocessar Evento’\. Caso os eventos encontrados na tela de Geração Prévia dos Movimentos sejam identificados nos critérios acima como Retificação esses deverão ser desconsiderados e não gerados, pela tela de Geração Prévia dos Movimentos serão gerados apenas os eventos que se enquadrarem como ‘Original’\.

__\[MFS\-12180\]            __

- __Fechamento/Reabertura:__ Critérios de geração do evento considerando a situação do período\.
- Se não houver ocorrência de geração de evento de fechamento, prosseguir com a geração\.
- Se houver ocorrência de geração de evento de fechamento considerar os status então:

                      \- Evento de fechamento com status de “Evento Reinf Enviado” exibir a seguinte mensagem no log de geração:

                      

                  Evento R2010 – Retenção Contribuição Previdenciária – Serviços Tomados

                  Evento não gerado\. Existe evento de fechamento do período enviado aguardando retorno\.

                  Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

                      \- Evento de fechamento com status de “Evento REINF Recebido com Sucesso ou Advertência” exibir a seguinte

                        mensagem no log de geração:

               

                  Evento R2010 – Retenção Contribuição Previdenciária – Serviços Tomados

                  Evento não gerado\. Período Fechado\.

                  Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração de evento de reabertura correspondente, com status “Evento REINF Recebido com

Sucesso ou Advertência”, prosseguir com a geração\.

         

        __\[Alterado MFS17138\]__

       \- Evento de fechamento com status de “Evento REINF Recebido com erro” ou “Cancelado” ou “Erro na Geração do 

           XML” ou “Evento Excluído na Mensageria” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, exibir a seguinte mensagem no log de geração:

                   Evento R2010 – Retenção Contribuição Previdenciária – Serviços Tomados

                   Evento não gerado\. Período Fechado\.

                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

 

                   Se não houver evento de fechamento com status “Evento REINF Recebido com Sucesso ou Advertência”,

                   prosseguir com a geração\. 

                       \- Evento de Fechamento com status de “Aguardando Geração do XML”, exibir a seguinte mensagem no log de   

                         geração:

                   Evento R2010 – Retenção Contribuição Previdenciária – Serviços Tomados

                   Evento não gerado\. Existe evento de fechamento do período não enviado\.

                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

MFS\-8958

MFS\-10357

MFS\-12176

MFS\-12180

 MFS14222

 MFS14463

MFS15338

MFS17138

MFS17304

MFS16936

MFS18702

MFS19130

MFS20384

MFS20732

MFS21632

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
- __Campos\-Chave__: tpInscTom, nrInscTom
- __Nível hierárquico do registro__: filho do registro evtServTom
- __Ordenação__: não se aplica\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Um por arquivo

MFS\-8958

RN02

Campo TpInsc

Será gerado com conteúdo "1", uma vez que não atendemos PF\.

MFS8958

RN03

Campo nrInsc

Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento\.

Com base neste campo podemos entender que o REINF será gerado com base em um estabelecimento Centralizador\.

\[ALTERADA MFS11894\]

Obs:

Caso a informação do campo seja inferior a 14 posições deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2010 \- Registro : Informações de Identificação do Contribuinte

“Campo Número de Inscrição tem tamanho inferior a 14 posições\." 

Identificação do Contribuinte: CNPJ: XXXXX / Nome/Razão: XXXX

MFS11894

- __Registro ideEstabObra – Identificação do Estabelecimento /Obra Contratante dos Serviços__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN04

- __Origem das informações__: SAFX04, SAFX07 e Cadastro do Estabelecimento\.
- __Regra de seleção__: Este registro servirá identificar a obra ou estabelecimento "contratante" dos serviços prestados mediante cessão de mão de obra\.
- __Campos\-Chave__: tpInscEstab, nrInscEstab
- __Nível hierárquico do registro__: filho do registro infoServTom\.
- __Ordenação__: Não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: para cada InfServTom poderá existir “N” IdeEstabObra\.

MFS8958

RN05

__Campo tplnsEstab__

Este campo será gerado com a seguinte regra:

Se o campo IND\_PREST\_SERV da SAFX07 for diferente de "1" ou "2", gerar "1"\.

Se o campo IND\_PREST\_SERV da SAFX07 for igual a "1" ou "2", gerar "4"\.

Obs:

Caso não preenchido assumir o valor “1”\. Deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2010 \- Registro Identificação do Estabelecimento/Obra Tomador de Serviços

“Campo Indicador de Prestação de Serviço não preenchido, assumido o valor “1” para o campo Tipo de Inscrição do registro”\.

Identificação da Nota Fiscal: Estabelecimento: XXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

MFS8958

RN06

__Campo nrlnscEstab__

Este campo será gerado com a seguinte regra:

Se o campo IND\_PREST\_SERV da SAFX07 for diferente de "1" ou "2", será gerado com o conteúdo do campo CGC do Cadastro do Estabelecimento da NF;

Se o campo IND\_PREST\_SERV da SAFX07 for igual a "1", será gerado com o conteúdo do campo CEI da SAFX04 da PFJ vinculada a NF;

Obs1: Caso o campo CEI não preenchido exibir a seguinte mensagem no log de pré\-geração: 

Evento R2010 – Registro Identificação do Estabelecimento/Obra Tomador de Serviços

“Campo CEI do cadastro Fis/Jur não preenchido”

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

Se o campo IND\_PREST\_SERV da SAFX07 for igual a "0", será gerado com o conteúdo do campo CGC do Cadastro do Estabelecimento da NF;

Se o campo IND\_PREST\_SERV da SAFX07 for igual a "1 ou 2", será gerado com o conteúdo do campo COD\_CEI da SAFX07;

Se o campo IND\_PREST\_SERV da SAFX07 for igual a "2", será gerado com o conteúdo do campo COD\_CEI da SAFX07;

Obs2: Caso o campo COD\_CEI não preenchido exibir a seguinte mensagem no log de pré\-geração:

Evento R2010 – Registro Identificação do Estabelecimento/Obra Tomador de Serviços

“Campo COD\_CEI da Nota não preenchido”

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

Caso não preenchido o campo IND\_PREST\_SERV da SAFX07, gravar "0"\. Deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2010 – Registro Identificação do Estabelecimento/Obra Tomador de Serviços

 “Campo Indicador de Prestação de Serviço da Nota não preenchido“\.

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

\[ALTERADO MFS21130\]

Obs3: Caso a informação do campo seja maior que 14 posições deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2010 \- Registro: Identificação do Estabelecimento /Obra Contratante dos Serviços

“'Número de Inscrição \(Código CEI\) maior que o permitido \(14 posições\)\." 

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX Inscrição: XXXXXXXX

Obs3: Caso o campo IND\_PREST\_SERV não preenchido assumir o conteúdo do campo “CGC” do cadastro do Estabelecimento\. Deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2010 – Registro Identificação do Estabelecimento/Obra Tomador de Serviços

 “Campo Indicador de Prestação de Serviço da Nota não preenchido“ assumido o “CGC” do Estabelecimento tomador dos serviços para o campo Número de Inscrição do registro\.

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

\[ALTERADO MFS11894\]

Obs4: Caso a informação do campo seja inferior a 14 posições deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2010 \- Registro : Identificação do Estabelecimento /Obra Contratante dos Serviços

“Campo Número de Inscrição tem tamanho inferior a 14 posições\." 

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

MFS8958

MFS11894

MFS13947

MFS21130

RN07

__Campo indObra__

Este campo será gerado com a informação carregada no campo IND\_PREST\_SERV da SAFX07\.

Obs:

Caso o campo IND\_PREST\_SERV não preenchido, assumir o valor “0”\. Deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2010 \- Registro Identificação do Estabelecimento/Obra Tomador de Serviços

 “Campo Indicador de Prestação de Serviço da Nota não preenchido“ assumido o valor “0” para o campo Indicador de Obra do registro\.

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXXX / Serie: XXXXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

MFS8958

- __Registro idePrestServ – Identificação do Prestador de Serviços Mediante cessão de mão de obra ou empreitada __

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN08

- __Origem das informações__: SAFX04, SAFX08 e SAFX09\.
- __Regra de seleção__: Este registro servirá identificar o prestador de serviços mediante cessão de mão de obra ou empreitada\.
- __Campos\-Chave__: cnpjPrestador
- __Nível hierárquico do registro__: filho do registro ideEstabObra
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.

__\[Alteração MFS13362\]__

- __Ocorrência__: Um por arquivo\. Para cada ideEstabObra poderá existir “N” idePrestServ\.

MFS8958

MFS13362

MFS14463

RN09

__Campo cnpjPrestador__

Será gerado com a informação do campo CPF\_CGC da SAFX04 informado na nota detalhada no registro “nfs”

Obs1:

Caso não preenchido deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2010 \- Registro: Identificação do Prestador de Serviços 

“Campo CPF\_CGC não preenchido“\. 

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

\[ALTERADO MFS11894\]

Obs2:

Obs4: Caso a informação do campo seja inferior a 14 posições deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2010 \- Registro : Identificação do Prestador de Serviços

“Campo CNPJ Prestador tem tamanho inferior a 14 posições\." 

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

MFS8958

MFS11894

RN10

__vlrTotalBruto__

Será resultado da somatória do campo VLR\_ITEM da SAFX08 ou VLR\_TOT da SAFX09 informado na nota detalhada no registro “nfs”

MFS8958

MFS14463

RN11

__Campo vlrTotalBaseRet__

Será resultado da somatória do campo VLR\_BASE\_INSS da SAFX08 ou SAFX09 informado na nota detalhada no registro “infoTpServ”

MFS8958

MFS14463

RN12

__Campo vlrTotalRetPrinc__

Será resultado da somatória do campo VLR\_INSS\_RETIDO – VLR\_RET\_SERV da SAFX08 ou SAFX09 informado na nota detalhada no registro “infoTpServ”\.

MFS8958

MFS14463

RN13

__Campo vlrTotalRetAdic__

Será resultado da somatória do campo VLR\_TOT\_ADIC da SAFX08 ou SAFX09 informado na nota detalhada no registro “infoTpServ”

MFS8958

MFS14463

RN14

__Campo vlrTotalNRetPrinc__

Será resultado da somatória do campo VLR\_N\_RET\_PRINC da SAFX08 ou SAFX09 informado na nota detalhada no registro “infoTpServ”

MFS8958

MFS14463

RN15

MFS8958

MFS10357

RN16

MFS8958

MFS10357

RN17

__Campo vlrTotalINRetAdic__

Será o resultado da somatória do campo “VLR\_N\_RET\_ADIC” da SAFX08 ou SAFX09 informado na nota detalhadas na tag “infoTpServ”\.

 

MFS8958

MFS14463

RN18

MFS8958/

MFS10357

RN19

MFS8958

MFS10357

RN20

__Campo codAnaCont__

Será tratado na geração do registro R\-1070

MFS8958

MFS13362

RN21

__Campo indCPRB__

__\[MFS20045\]__

Caso existir informação no campo VLR\_ALIQ\_INSS da SAFX08 ou SAFX09 considerar a regra abaixo:

__\[Alterado MFS13205/MFS17304\]__

Se houver pelo menos uma nota com o campo VLR\_ALIQ\_INSS da SAFX08 ou SAFX09 = 3,5% gravar ‘1’

Se não, gravar ‘0’

Caso não existir informação no campo VLR\_ALIQ\_INSS da SAFX08 ou SAFX09 considerar a regra abaixo:

Gravar nulo e apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2010 \- Identificação do Prestador de Serviços

“Não foi possível gerar o indicativo da CPRB, pois o campo Alíquota INSS não está preenchido“\. 

Caso o código do serviço prestado fora parametrizado na tela de  “Código de Atividade x Serviços \(Por Prestador\)” Menu: Parâmetros >> CPRB, gerar “1”, caso contrário gerar “0”

MFS10357

MFS13131

MFS\-13205

MFS14463

MFS17304

MFS20045

- __Registro nfs \- Registro de Detalhamento das notas fiscais de serviços prestados pela empresa__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN22

- __Origem das informações__: SAFX07, SAFX08 e SAFX09\.
- __Regra de seleção__: Este registro servirá para identificar as notas fiscais de serviços prestados pela empresa declarada no registro idePrestServ\.
- __Campos\-Chave__: serie, numDocto
- __Nível hierárquico do registro__: filho do registro idePrestServ\.
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: para cada idePrestServ poderá existir “N” nfs\.

MFS8958

MFS14463

RN23

__Campo serie__

Informação será recuperada do campo SERIE\_DOCFIS da SAFX08 ou SAFX09\. Caso não preenchido gravar “0”\.

MFS8958

MFS14463

RN24

__Campo NumDocto__

Informação será recuperada inicialmente do campo NUM\_DOCFIS\_SERV da SAFX07, caso não encontrar valor preenchido será recuperada a informação do campo NUM\_DOCFIS da SAFX08 ou SAFX09\.

Obs: Caso número da nota for maior que 15 posições a informação será truncada, utilizando as 15 ultimas posições da direita para esquerda\.

MFS8958

MFS14463

MFS17043

RN25

__Campo dtEmissaoNF__

Informação será recuperada do campo DATA\_EMISSAO da SAFX07\.

MFS8958

RN26

__Campo vlrBruto__

Informação será recuperada do campo VLR\_ITEM da SAFX08 ou VLR\_TOT da SAFX09\. Nesse campo deverá gerar o valor bruto da nota, ou seja, será recuperada o valor de todos os itens da nota, mesmo se o usuário estiver com o parâmetro “Desconsiderar NFs sem Valor de Retenção informado” selecionado nos Dados Iniciais\.

MFS8958

MFS14463

MFS16568

RN27

__Campo obs__

Informação será recuperada do campo OBS\_REINF da SAFX07\.

MFS8958

MFS14129

RN28

MFS8958

MFS10357

RN29

MFS8958

MFS10357

RN30

MFS8958

MFS10357

RN31

MFS8958

MFS10357

RN32

MFS8958

MFS10357

MFS8958

MFS10357

RN33

MFS8958

MFS10357

RN34

MFS8958

MFS10357

RN35

MFS8958

MFS10357

RN36

MFS8958

MFS10357

RN37

MFS8958

MFS10357

RN38

MFS8958

MFS10357

RN39

MFS8958

MFS10357

RN40

MFS8958

MFS10357

RN41

MFS8958

MFS10357

- __Registro infoTpServ \- Registro de Informações do Tipo de Serviços__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN42

- __Origem das informações__: SAFX07, SAFX08 e SAFX09\.
- __Regra de seleção__: Este registro servirá para identificar os tipos de serviços constantes da nota fiscal\.
- __Campos\-Chave__: tpServico
- __Nível hierárquico do registro__: filho do registro nfs
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: para cada nfs poderá existir “9” infoTpServ\.

MFS10357

MFS14463

RN43

__Campo tpServiço__

Pela SAFX08:

Caso o código do produto fora parametrizado na tela de “Identificador do Tipo de Serviço > Por Produto” Menu: Retenções Previdenciárias>> Parâmetros, gerar o código do tipo de serviço vinculado\.

Pela SAFX09:

Caso o código do serviço prestado fora parametrizado na tela de “Identificador do Tipo de Serviço” Menu: Retenções Previdenciárias>> Parâmetros, gerar o código do tipo de serviço vinculado\.

MFS10357

MFS14463

RN44

__Campo codAtivEcon__

Caso o código do serviço prestado fora parametrizado na tela de  “Código de Atividade x Serviços \(Por Prestador\)” Menu: Parâmetros >> CPRB, gerar o código de atividade econômica vinculado\.

MFS10357

MFS13131

MFS13362

RN45

__Campo vlrMatEquip__

Será a somatória dos campos VLR\_MAT\_PROP \+ VLR\_MAT\_TERC da SAFX09\. Caso não preenchido gravar “0”\.

MFS10357

MFS13362

RN46

__Campo vlrDedAlim__

Recuperar a informação do campo VLR\_DED\_ALIM da SAFX09\. Caso não preenchido gravar “0”\.

MFS10357

MFS13362

RN47

__Campo vlrDedTrans__

Recuperar a informação do campo VLR\_DED\_TRANS da SAFX09\. Caso não preenchido gravar “0”\.

MFS10357

MFS13362

RN48

__Campo vlrBaseRet__

Recuperar a informação do campo VLR\_BASE\_INSS da SAFX08 ou SAFX09\.

Obs:

Caso não preenchido deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2010 \- Registro: Notas Fiscais de Serviços

“Campo Valor Base de Cálculo da Retenção do INSS não preenchido“\. 

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

 Item de Serviço: XXXXXX

MFS10357

MFS14463

RN49

__Campo vlrRetencao__

Recuperar a informação do campo VLR \_INSS\_RETIDO da SAFX08 ou SAFX09\.

Obs:

Caso não preenchido deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2010 \- Registro: Notas Fiscais de Serviços

“Campo Valor da Retenção do INSS não preenchido“

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

 Item de Serviço: XXXXX

MFS10357

MFS14463

RN50

__Campo vlrRetSub__

Recuperar a informação do campo VLR\_RET\_SERV da SAFX08 ou SAFX09\.

MFS10357

MFS14463

RN51

__Campo vlrNRetPrinc__

Recuperar a informação do campo VLR\_N\_RET\_PRINC da SAFX08 ou SAFX09\.

MFS10357

MFS14463

RN52

__Campo vlrServicos15__

Será a somatória do campo VLR\_SERVICO da SAFX09, considerando os itens cujo código de serviço tenha sido parametrizado na tela de Identificador do Tipo de Serviço – com identificador de Aposentadoria Especial com o Indicador igual “15 anos“\.

__\[Alteração MFS13205\]__

Recuperar a informação do campo VLR\_SERV\_15 da SAFX08 ou SAFX09\.

MFS10357

MFS13205

MFS14463

RN53

__Campo vlrServicos20__

Será a somatória do campo VLR\_SERVICO da SAFX09, considerando os itens cujo código de serviço tenha sido parametrizado na tela de Identificador do Tipo de Serviço – com identificador de Aposentadoria Especial com o Indicador igual “20 anos“\.

__\[Alteração MFS13205\]__

Recuperar a informação do campo VLR\_SERV\_20 da SAFX08 ou SAFX09\.

MFS10357

MFS13205

MFS14463

RN54

__Campo vlrServicos25__

Será a somatória do campo VLR\_SERVICO da SAFX09, considerando os itens cujo código de serviço tenha sido parametrizado na tela de Identificador do Tipo de Serviço – com identificador de Aposentadoria Especial com o Indicador igual “25 anos“\.

__\[Alteração MFS13205\]__

Recuperar a informação do campo VLR\_SERV\_25 da SAFX08 ou SAFX09\.

MFS10357

MFS13205

MFS14463

RN55

__Campo vlrAdicional__

Recuperar a informação do campo VLR\_TOT\_ADIC da SAFX08 ou SAFX09\.

MFS10357

MFS14463

RN56

__Campo vlrNRetAdic__

Recuperar a informação do campo VLR\_N\_RET\_ADIC da SAFX08 ou SAFX09\.

MFS10357

MFS14463

- __Registro infoProcRetPr \- Registro de Informações de Processo Retenção Principal__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN57

- __Origem das informações__: SAFX08 ou SAFX09\.
- __Regra de seleção__: Este registro servirá para identificar os processos de retenção principal relacionados a não retenção da contribuição previdenciária\. 
- __Campos\-Chave__: tpProcRetPrinc, nrProcRetPrinc, codSuspPrinc
- __Nível hierárquico do registro__: filho do registro idePrestServ\.
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Poderá existir “50” infoProcRetAd ou não existir

MFS10357

MFS14463

RN58

__Campo tpProcRetPrinc__

Recuperar a informação do campo IND\_TP\_PROC\_ADJ\_PRINC da SAFX08 ou SAFX09\.

MFS10357

MFS14463

RN59

__Campo nrProcRetPrinc__

Recuperar a informação do campo NUM\_PROC\_ADJ\_PRINC da SAFX08 ou SAFX09\.

\[ALTERADO MFS11894\]

Obs:

Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2010 \- Registro : Informações de Processo Retenção Principal

“Campo Número do Processo deve ser numérico\."

Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX

Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX

MFS10357

MFS11894

MFS14463

RN60

__Campo codSuspPrinc__

Recuperar a informação do campo COD\_SUSP\_PRINC da SAFX08 ou SAFX09\.

\[ALTERADO MFS11894\]

Obs:

Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2010 \- Registro : Informações de Processo Retenção Principal

“Campo Código do Indicativo da Suspensão deve ser numérico\." 

Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX

Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX

MFS10357

MFS11894

MFS14463

RN61

__Campo valorPrinc__

Recuperar a informação do campo VLR\_N\_RET\_PRINC da SAFX08 ou SAFX09\.

MFS10357

MFS14463

- __Registro infoProcRetAd \- Registro de Informações de Processo Retenção Adicional__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN62

- __Origem das informações__: SAFX08 ou SAFX09\.
- __Regra de seleção__: Este registro servirá para identificar os processos de retenção adicional relacionados a não retenção da contribuição previdenciária\. 
- __Campos\-Chave__: tpProcRetAdic, nrProcRetAdic, codSuspAdic
- __Nível hierárquico do registro__: filho do registro idePrestServ\.
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: poderá existir “50” infoProcRetAd ou não existir

MFS10357

MFS14463

RN63

__Campo tpProcRetAdic__

Recuperar a informação do campo IND\_TP\_PROC\_ADJ\_ADIC da SAFX08 ou SAFX09\.

MFS10357

MFS14463

RN64

__Campo nrProcRetAdic__

Recuperar a informação do campo NUM\_PROC\_ADJ\_ADIC da SAFX08 ou SAFX09\.

ALTERADO MFS11894\]

Obs:

Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2010 \- Registro : Informações de Processo Retenção Adicional

“Campo Número do Processo deve ser numérico\."

Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX

Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX

MFS10357

MFS11984

MFS14463

RN65

__Campo codSuspAdic__

Recuperar a informação do campo COD\_SUSP\_ADIC da SAFX08 ou SAFX09\.

\[ALTERADO MFS11984\]

Obs: 

Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2010 \- Registro : Informações de Processo Retenção Adicional

“Campo Código do Indicativo da Suspensão deve ser numérico\." 

Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX

Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX

MFS10357

MFS11984

MFS14463

RN66

__Campo valorAdic__

Recuperar a informação do campo VLR\_N\_RET\_ADIC da SAFX08 ou SAFX09\.

MFS10357

MFS14463

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


# MTZ_REINF_Geracao_Evento_Movimento_R2020

- **Fonte:** MTZ_REINF_Geracao_Evento_Movimento_R2020.docx
- **Modificado:** 2023-03-28
- **Tamanho:** 102 KB

---

 

THOMSON REUTERS

Geração evento R\-2020 \- REINF

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-8959

Geração Evento

Definição de regras para geração do evento R\-2020 Reinf 

MFS\-10414

Alteração 

Alteração/ Inclusão de registros

MFS\-11895

Lara Aline

Inclusão mensagens de logs RN06, 54, 55, 56, 59, 60 e 61\.

MFS\-12176

Elenilson Coutinho

Regra para tipo de arquivo Original/Retificação

MFS\-12180

Elenilson Coutinho

Regra de geração considerando eventos de fechamento/reabertura

MFS\-13205

Lara Aline

Ajuste nos campos vlrServicos15, vlrServicos20 e vlrServicos25 para recuperar informação dos novos campos da SAFX09\.

MFS13631

Lara Aline

Exclusão dos campos codAnaCont, vlrMatEquip, vlrDedAlim, vlrDedTrans e codAtivEcon e ajuste na ocorrência do grupo ideTomador\. Conforme Leiautes versão 1\.2\.

MFS14404

Lara Aline

Ajuste para considerar o campo “Desconsiderar NFs sem Valor de Retenção informado” da tela de Dados Iniciais

MFS14129

Lara Aline

Inclusão de regra para o campo observação do registro nfs\.

MFS16568

Lara Aline

Ajuste no campo vlrBruto \(RN26\)

MFS17043

Lara Aline

Ajuste no campo numDocto \(RN21\)

MFS17138

Lara Aline

Inclusão status “Excluído na Mensageria” no tratamento de Fechamento/Reabertura

MFS16936

Lara Aline

Inclusão de regra para as parametrizações de Retenção Previdenciárias\.

MFS17919

Lara Aline

Inclusão de tratamento para empresa que possuam Operação de transporte de passageiros

MFS18702

Lara Aline

Alteração da Geração Prévia retirando a possibilidade de Geração de Eventos Retificados, eventos retificadores serão gerados apenas no Painel de Controle de Eventos

MFS19169

Lara Aline

Ajuste na mensagem de log dos campos vlrBaseRet e vlrRetencao\.

MFS20384

Lara Aline

Incluisão de log quando encontrar valor negativo nas notas fiscais\.

MFS\-90001

Alessandra Cristina Navatta

Alteração da referência do arquivo de de\_para \(versão 2\.1\.1\)

__Obs\. O ajuste mapeado nesta demanda, refere\-se a atualização funcional\. Não há impactos na implementação__

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral de Geração do Evento R\-2020\.__

O evento R\-2020 do SPED \- REINF tem por objetivo gerar informações de Retenção Contribuição Previdenciária \- Prestadores de Serviços\. Ele será gerado com os registros:

 __Reinf__ – EFD \- Reinf

 __evtServPrest__ – Evento de Serviços Prestados

 __ideEvento__ – Informações de Identificação do Evento

 __ideContri__ – Informações de Identificação do Contribuinte

 __infoServPrest__ – Serviços Prestados \(Cessão Mão de Obra ou Empreitada\)

 __ideEstabPrest__ – Registro de Identificação do Estabelecimento Prestador de Serviços mediante cessão de mão de obra

 __ideTomador__ \-  Identificação dos Tomadores dos Serviços

 __nfs__ \- Notas Fiscais de Serviços \(CMO\) \- Emitidas por Terceiros

__\[MFS10414\]__

__ InfoTpServ__ – Informações do Tipo de Serviços Constantes da Nota Fiscal

__ InfoProcRetPr__ – Informações de Processo de Retenção Principal

__ InfoProcRetAd__ – Informações de Processo de Retenção Adicional 

Observar orientações existentes no arquivo " TR\_REINF\_DEXPARA\_V2\.1\.1\.xlsx "\.

- __Origem das informações__: SAFX04, SAFX07, SAFX09 e Cadastro do Estabelecimento\.
- __Regra de seleção__: O Registro R\-2020 é utilizado para demonstrar informações de Retenção Contribuição Previdenciária \- Prestadores de Serviços\. Ele será gerado com base em Informações de Notas Fiscais de Serviço\.

Para obtermos as informações para sua geração, devemos recuperar registros das tabelas SAFX07 e SAFX09, considerando os seguintes critérios:

\- O COD\_ESTAB seja de um estabelecimento indicado pelo usuário;

\- NFs cujo campo MOVTO\_E\_S seja igual a "9";

\- O campo DATA\_EMISSAO deve compreender o período de geração;

\- O campo SITUACAO deve ser diferente de "S";

\- O campo COD\_CLASS\_DOC\_FIS deve ser igual a "2" ou "3" ou "4" ou "5" ou “6”;

\- O COD\_SERVICO deve ter sido associado a um tipo de Item na Parametrização de Identificação do Tipo de Serviço do Módulo REINF;

__Tratamento:__

__\[MFS20384\]__

Caso encontrado valores negativos \(\-\) nos campos de valores das notas recuperadas \(SAFX07/SAFX09\), a geração não será finalizada e será exibido a seguinte mensagem no log de geração:

       Evento R2020 – Retenção Contribuição Previdenciária – Serviços Prestados

       ‘A geração não foi concluída pois foi encontrado campo com valor negativo, favor verificar’\.

       Empresa/Estabelecimento: XX / XXXXX / Identificação do Nota: NF: XXXXX / Serie: XXXXXX

       Identificação do Campo: XXXXXX

Caso o sistema encontre notas que correspondem aos critérios acima e o campo COD\_CLASS\_DOC\_FIS seja igual a __"4" ou "5" ou “6”__ essas notas serão consideradas como __Operações de transporte de passageiros:__

__Tratamento para Operações de transporte de passageiros__

- __Origem das informações__: SAFX07, SAFX263 e Cadastro do Estabelecimento\.
- __Regra de seleção__: O Registro R\-2020 é utilizado para demonstrar informações de Retenção Contribuição Previdenciária \- Prestadores de Serviços\. Ele será gerado com base em Informações de Notas Fiscais de Serviço no caso de Operações de transporte de passageiros, como nesse caso não possui item a origem das informações se faz pela SAFX07 e origem dos processos pela SAFX263\.

Para obtermos as informações para sua geração, devemos recuperar registros das tabelas SAFX07, considerando os seguintes critérios:

SAFX07:

\- O COD\_ESTAB seja de um estabelecimento indicado pelo usuário;

\- NFs cujo campo MOVTO\_E\_S seja igual a "9";

\- O campo DATA\_EMISSAO deve compreender o período de geração;

\- O campo SITUACAO deve ser diferente de "S";

\- O campo COD\_CLASS\_DOC\_FIS deve ser igual a "4" ou "5" ou “6”;

\- NFs com Modelo do Documento igual a:

2E \- Bilhete de Passagem emitido por ECF

07 \- Nota Fiscal de Serviço de Transporte

67 \- Conhecimento de Transporte Eletrônico para Outros Serviços \- CT\-e OS

63 \- Bilhete de Passagem Eletrônico \- BP\-e

16 \- Bilhete de Passagem Ferroviário

57 \- Conhecimento de Transporte Eletrônico – CT\-e

13 \- Bilhete de Passagem Rodoviário

14 \- Bilhete de Passagem Aquaviário

15 \- Bilhete de Passagem e Nota de Bagagem

\- Os campos VLR\_BASE\_INSS  e VLR\_INSS\_RETIDO devem ser maior que zero;

Fim regra de seleção para Operações de transporte de passageiros\.

- __Regra de Agrupamento__: O Registro R\-2020 será agrupado por CPF\_CGC da SAFX04\.

__\[Alterado MFS16936\]__

Regra para as parametrizações de Retenção Previdenciária:

As parametrizações de Retenção Previdenciária são possíveis efetua\-las para qualquer Estabelecimento sendo ou não o Estabelecimento Centralizador, por padrão deverá ser utilizada a parametrização do estabelecimento Centralizador para todos os estabelecimentos que não possuam sua parametrização\. Para os estabelecimentos que possuem parametrização na geração será considerada a sua parametrização conforme exemplo abaixo:

Exemplo:

Estabelecimento Centralizador: REINFP – Possui ‘parametrização 1’

Estabelecimento Centralizado: REINF1 – Possui ‘parametrização 2’

Estabelecimento Centralizado: REINF2 – Não possui parametrização

1 \- Na geração dos dados do Estabelecimento Centralizador REINFP utilizaremos a ‘parametrização 1’;

2 \- Na geração dos dados do Estabelecimento Centralizado REINF1 utilizaremos a ‘parametrização 2’;

3 \- Na geração dos dados do Estabelecimento Centralizado REINF2 utilizaremos a ‘parametrização 1’;

__Importante: __Para os estabelecimentos que possuírem grupos diferentes do Estabelecimento Centralizador esses estabelecimentos somente serão considerados se houver a sua própria parametrização\. Caso contrário todas as notas desse estabelecimento centralizado não serão consideradas na geração\.__  __

__\[Alterado MFS14404\]__

Importante:

Caso o campo “Desconsiderar NFs sem Valor de Retenção informado” estiver selecionado na tela de Dados Iniciais, deverão ser desconsideradas todas as notas fiscais que não tenham o Valor Base INSS \(VLR\_BASE\_INSS/SAFX09\) e o Valor de INSS Retido \(VLR\_INSS\_RETIDO/SAFX09\) informado\. Ou seja, quando o parâmetro estiver selecionado serão considerados apenas as notas fiscais que tenham o Valor Base INSS \(VLR\_BASE\_INSS da SAFX08/SAFX09\) e Valor de INSS Retido \(VLR\_INSS\_RETIDO da SAFX08/SAFX09\) informado\.

__\[MFS\-12176\]__

- __Original/Retificação__: Os critérios para identificar se o evento a ser gerado será original ou retificador serão os seguintes:
- Se não houver ocorrência de geração de evento anterior, criar nova ocorrência de arquivo original\.
- Se houver ocorrência de geração anterior com status “Evento Enviado” exibir a seguinte mensagem no log de geração:

              Evento R2020 – Retenção Contribuição Previdenciária – Serviços Prestados

              Evento não gerado\. Existe evento anterior enviado aguardando retorno\.

              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração anterior com status “Evento REINF Recebido com Sucesso ou Advertência” verificar se há evento de exclusão, então:

\- Se __não__ existir evento de exclusão então, criar ocorrência de arquivo de retificação\.

\- Se existir, evento de exclusão considerar os status, então:

Evento de exclusão com status de “Evento REINF Enviado” exibir a seguinte mensagem no log de geração:

  

             Evento R2020 – Retenção Contribuição Previdenciária – Serviços Prestados

             Evento não gerado\. Existe evento de exclusão anterior enviado aguardando retorno\.

             Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

          Evento de exclusão com status “Evento Recebido com sucesso ou Advertência” então, verificar se há ocorrência

          anterior de evento periódico com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova

          ocorrência de arquivo de  retificação, se __não__ houver, criar original\.

              \- Se existir evento de exclusão com status “Evento REINF Recebido com Erro” ou “Cancelado” ou “Erro na Geração do                          XML” então, criar nova ocorrência de retificação\.

             \- Se existir evento de exclusão com status “Aguardando Geração do XML” então exibir a seguinte mensagem no log de      geração:

                

              Evento R2020 – Retenção Contribuição Previdenciária – Serviços Prestados

              Evento não gerado\. Existe evento anterior não enviado\.

              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração anterior com status “Evento REINF Recebido com erro”, então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar  nova ocorrência de arquivo de retificação, se __não__ houver, criar original\.
- Se houver ocorrência de geração anterior com status “Aguardando Geração do XML” ou “Cancelado” ou “Erro na Geração do XML” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar  nova ocorrência de arquivo de retificação, se __não__ houver, criar original\.

__\[MFS18702\]__

__Importante:__ Na tela Geração Prévia dos Movimentos serão gerados APENAS os eventos Originais, os eventos de Retificação deverão ser gerados diretamente pelo Painel de Controle de Eventos pela opção ‘Reprocessar Evento’\. Caso os eventos encontrados na tela de Geração Prévia dos Movimentos sejam identificados nos critérios acima como Retificação esses deverão ser desconsiderados e não gerados, pela tela de Geração Prévia dos Movimentos serão gerados apenas os eventos que se enquadrarem como ‘Original’\.

__\[MFS\-12180\]__

- __Fechamento/Reabertura:__ Critérios de geração do evento considerando a situação do período\.
- Se não houver ocorrência de geração de evento de fechamento, prosseguir com a geração\.
- Se houver ocorrência de geração de evento de fechamento considerar os status então:

                      \- Evento de fechamento com status de “Evento Reinf Enviado” exibir a seguinte mensagem no log de geração:

                      

                  Evento R2020 – Retenção Contribuição Previdenciária – Serviços Prestados

                  Evento não gerado\. Existe evento de fechamento do período enviado aguardando retorno\.

                  Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

                      \- Evento de fechamento com status de “Evento REINF Recebido com Sucesso ou Advertência” exibir a seguinte

                        mensagem no log de geração:

               

                  Evento R2020 – Retenção Contribuição Previdenciária – Serviços Prestados

                  Evento não gerado\. Período Fechado\.

                  Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração de evento de reabertura correspondente, com status “Evento REINF Recebido com

Sucesso ou Advertência”, prosseguir com a geração\.

         

       __\[Alterado MFS17138\]__

       \- Evento de fechamento com status de “Evento REINF Recebido com erro” ou “Cancelado” ou “Erro na Geração do 

           XML” ou “Evento Excluído na Mensageria” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, exibir a seguinte mensagem no log de geração:

                   Evento R2020 – Retenção Contribuição Previdenciária – Serviços Prestados

                   Evento não gerado\. Período Fechado\.

                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

 

                   Se não houver evento de fechamento com status “Evento REINF Recebido com Sucesso ou Advertência”,

                   prosseguir com a geração\. 

                       \- Evento de Fechamento com status de “Aguardando Geração do XML”, exibir a seguinte mensagem no log de   

                         geração:

                   Evento R2020 – Retenção Contribuição Previdenciária – Serviços Prestados

                   Evento não gerado\. Existe evento de fechamento do período não enviado\.

                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

MFS\-8959

MFS10414

MFS12176

MFS12180

MFS14404

MFS17138

MFS16936

MFS17919

MFS18702

MFS20384

MFS\-90001

- __Registro ideEvento – Informações de Identificação do Evento__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

- __Registro ideContri – Informações de Identificação do Contribuinte__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

- __Origem das informações__: Cadastro do Estabelecimento\.
- __Regra de seleção__: Este registro servirá para identificar o estabelecimento centralizador \(Matriz\)\.
- __Campos\-Chave__: tpInsc, nrInsc
- __Nível hierárquico do registro__: filho do registro evtServPrest
- __Ordenação__: não se aplica\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Um por arquivo

RN02

__Campo TpInsc__

Será gerado com conteúdo "1", uma vez que não atendemos PF\.

MFS14821

RN03

__Campo nrInsc__

Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento\.

Com base neste campo podemos entender que o REINF será gerado com base em um estabelecimento Centralizador\.

Obs:

Caso a informação do campo seja inferior a 14 posições deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2020 \- Registro : Informações de Identificação do Contribuinte

“Campo Número de Inscrição tem tamanho inferior a 14 posições\." 

Identificação do Contribuinte: CNPJ: XXXXX / Nome/Razão: XXXX

MFS14821

- __Registro IdeEstabPrest – Identificação do Estabelecimento Prestador de Serviços__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN01

- __Origem das informações__: Cadastro do Estabelecimento\.
- __Regra de seleção__: Este registro servirá para identificar o estabelecimento centralizador \(Matriz\)\.
- __Campos\-Chave__: tpInscEstabPrest, nrInscEstabPrest
- __Nível hierárquico do registro__: filho do registro infoServPrest
- __Ordenação__: não se aplica\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Para cada infoServPrest poderá existir “N” ideEstabPrest

MFS\-8959

RN02

__Campo tpInscricao__

Gerar com conteúdo igual a “1”\.

MFS\-8959

RN03

__Campo nrInscricao__

Gerar com o conteúdo do campo “CGC” do Cadastro do Estabelecimento da Nota Fiscal\.

MFS\-8959

- __Registro ideTomador – Identificação dos Tomadores dos Serviços__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN04

- __Origem das informações__: SAFX04, SAFX07 e SAFX09\.
- __Regra de seleção__: Este registro servirá identificar o estabelecimento "Tomador" de Serviços
- __Campos\-Chave__: tpInscTomador, nrInscTomador
- __Nível hierárquico do registro__: filho do registro ideEstabPrest\.
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.

__\[Alteração MFS13631\]__

- __Ocorrência__: Um por arquivo\. para cada ideEstabPrest poderá existir “N” ideTomador

MFS8959

MFS13631

RN05

__Campo tplnscTomador__

Este campo será gerado com a seguinte regra:

Se o campo IND\_PREST\_SERV da SAFX07 for diferente de "1" ou "2", gerar "1"\.

Se o campo IND\_PREST\_SERV da SAFX07 for igual a "1" ou "2", gerar "4"\.

Obs:

Caso não preenchido assumir o valor “1”\. Deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2020 – Registro: Identificação dos Tomadores de Serviços

“Campo Indicador de Prestação de Serviço da Nota não preenchido, assumido o valor “1” para o campo Tipo de Inscrição do registro”\.

Identificação da Nota Fiscal: Estabelecimento: XXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

MFS8959

RN06

__Campo nrlnscTomador__

Este campo será gerado com a seguinte regra:

Se o campo IND\_PREST\_SERV da SAFX07 for diferente de "1" ou "2", será gerado com o conteúdo do campo CPF\_CGC da SAFX04 vinculada a NF\.

Obs:

Caso não preenchido deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2020 \- Registro: Identificação dos Tomadores de Serviços 

“Campo CPF\_CGC não preenchido“\. 

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

Se o campo IND\_PREST\_SERV da SAFX07 for igual a "1" ou “2”, será gerado com o conteúdo do campo COD\_CEI da SAFX07 

Obs1: Caso o campo COD\_CEI não preenchido exibir a seguinte mensagem no log de pré\-geração: 

Evento R2020 – Registro Identificação dos Tomadores de Serviços

“Campo COD\_CEI da Nota Fiscal não preenchido”

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

Obs2: Caso o campo IND\_PREST\_SERV não preenchido assumir o conteúdo do campo “CPF\_CGC” da SAFX04\. Deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2020 – Registro: Identificação dos Tomadores de Serviços

 “Campo Indicador de Prestação de Serviço da Nota não preenchido, assumido o “CPF\_CGC” do cadastro da Pessoa Física/Jurídica para o campo Número de Inscrição Tomador do registro”\.

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

\[ALTERADA MFS11895\]

Obs3: Caso a informação do campo seja inferior a 14 posições deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2020 – Registro: Identificação dos Tomadores de Serviços

 “Campo Número de Inscrição tem tamanho inferior a 14 posições\."

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

MFS8959

MFS11895

RN07

__Campo indObra__

Este campo será gerado com a informação carregada no campo IND\_PREST\_SERV da SAFX07\.

Obs:

Caso o campo IND\_PREST\_SERV não preenchido, assumir o valor “0”\. Deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2020 – Registro: Identificação dos Tomadores de Serviços

 “Campo Indicador de Prestação de Serviço da Nota não preenchido“ assumido o valor “0” para o campo Indicador de Obra do registro\.

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXXX / Serie: XXXXXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

MFS8959

RN08

__vlrTotalBruto__

Será resultado da somatória do campo VLR\_TOT da SAFX09 informado na nota detalhada no registro “nfs”

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Será resultado da somatória do campo VLR\_TOT\_NOTA da SAFX07 informado na nota detalhada no registro “nfs”

MFS8959

MFS17919

RN09

__Campo vlrTotalBaseRet__

Será resultado da somatória do campo VLR\_BASE\_INSS da SAFX09 informado na nota detalhada no registro “infoTpServ”

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Será resultado da somatória do campo VLR\_BASE\_INSS da SAFX07 informado na nota detalhada no registro “infoTpServ”

MFS8959

MFS17919

RN10

__Campo vlrTotalRetPrinc__

Será resultado da somatória do campo VLR\_INSS\_RETIDO – VLR\_RET\_SERV da SAFX09 informado na nota detalhada no registro “infoTpServ”

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Será resultado da somatória do campo VLR\_INSS\_RETIDO – VLR\_RET\_SERV da SAFX07 informado na nota detalhada no registro “infoTpServ”

MFS8959

MFS17919

RN11

__Campo vlrTotalRetAdic__

Será resultado da somatória do campo VLR\_TOT\_ADIC da SAFX09 informado na nota detalhada no registro “infoTpServ”

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Será resultado da somatória do campo VLR\_TOT\_ADIC da SAFX07 informado na nota detalhada no registro “infoTpServ”

MFS8959

MFS17919

RN12

__Campo vlrTotalNRetPrinc__

Será resultado da somatória do campo VLR\_N\_RET\_PRINC da SAFX09 informado na nota detalhada no registro “infoTpServ”

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Será resultado da somatória do campo VLR\_N\_RET da SAFX263, somatório do valor informado no campo vlrNRetPrinc na tag “infoTpServ”

MFS8959

MFS17919

RN13

MFS8959

MFS10414

RN14

MFS8959

MFS10414

RN15

__Campo vlrTotalINRetAdic__

Será o resultado da somatória do campo “VLR\_N\_RET\_ADIC” das notas fiscais de serviço detalhadas na tag “infoTpServ”\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Será resultado da somatória do campo VLR\_N\_RET da SAFX263, somatório do valor informado no campo vlrNRetAdic na tag “infoTpServ”

 

MFS8959

RN16

MFS8959

MFS10414

RN17

MFS8959

MFS10414

RN18

__Campo codAnaCont__

MFS8959

MFS13631

- __Registro nfs \- Registro de Detalhamento das notas fiscais de serviços prestados pela empresa__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN19

- __Origem das informações__: SAFX07 e SAFX09\.
- __Regra de seleção__: Este registro servirá para identificar as notas fiscais de serviços prestados pela empresa declarada no registro ideTomador\.
- __Campos\-Chave__: serie, numDocto
- __Nível hierárquico do registro__: filho do registro ideTomador\.
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: para cada ideTomador poderá existir “N” nfs\.

MFS8959

RN20

__Campo serie__

Informação será recuperada do campo SERIE\_DOCFIS da SAFX09\. Caso não preenchido gravar “0”\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Informação será recuperada do campo SERIE\_DOCFIS da SAFX07\. Caso não preenchido gravar “0”\.

MFS8959

MFS17919

RN21

__Campo NumDocto__

Informação será recuperada inicialmente do campo NUM\_DOCFIS\_SERV da SAFX07, caso não encontrar valor preenchido será recuperada a informação do campo NUM\_DOCFIS da SAFX09\.

Obs: Caso número da nota for maior que 15 posições a informação será truncada, utilizando as 15 ultimas posições da direita para esquerda\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Informação será recuperada do campo NUM\_DOCFIS da SAFX07\.

MFS8959

MFS17043

MFS17919

RN22

__Campo dtEmissaoNF__

Informação será recuperada do campo DATA\_EMISSAO da SAFX07\.

MFS8959

RN23

__Campo vlrBruto__

Informação será recuperada do campo VLR\_TOT da SAFX09\. Nesse campo deverá gerar o valor bruto da nota, ou seja, será recuperada o valor de todos os itens da nota, mesmo se o usuário estiver com o parâmetro “Desconsiderar NFs sem Valor de Retenção informado” selecionado nos Dados Iniciais\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Informação será recuperada do campo VLR\_TOT\_NOTA da SAFX07\.

MFS8959

MFS16568

MFS17919

RN24

MFS8959

MFS10414

RN25

__Campo obs__

Informação será recuperada do campo OBS\_REINF da SAFX07\.

MFS8959

MFS14129

RN26

MFS8959

MFS10414

RN27

MFS8959

MFS10414

RN28

MFS8959

MFS10414

RN29

MFS8959

MFS10414

RN30

MFS8959

MFS10414

RN31

MFS8959

MFS10414

RN32

MFS8959

MFS10414

RN33

MFS8959

MFS10414

RN34

MFS8959

MFS10414

RN35

MFS8959

MFS10414

RN36

MFS8959

MFS10414

RN37

MFS8959

MFS10414

- __Registro infoTpServ \- Registro de Informações do Tipo de Serviço__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN38

- __Origem das informações__: SAFX07, SAFX09 e SAFX263 Botão Processos Administrativos/Judiciais – \(Tela de “Documento Fiscal”\)\.
- __Regra de seleção__: Este registro servirá para identificar os tipos de serviços constantes da nota fiscal\.
- __Campos\-Chave__: tpServico
- __Nível hierárquico do registro__: filho do registro nfs
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: para cada nfs poderá existir “9” infoTpServ\.

MFS10414

MFS17919

RN39

__Campo tpServico__

Caso o código do serviço prestado fora parametrizado na tela de “Identificação do Tipo de Serviço” Menu: Retenções Previdenciárias >> Parâmetros, gerar o código do tipo de serviço vinculado\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Será gerado fixo com o código “100000024” \- Operações de transporte de passageiros\.

MFS10414

MFS17919

RN40

__Campo codAtivEcon__

Caso o código do serviço prestado fora parametrizado na tela de “Código de Atividade x Serviços” Menu: CPRB >> Parâmetros, gerar o código de atividade econômica vinculado\.

MFS10414

MFS13631

RN41

__Campo vlrMatEquip__

Será a somatória dos campos VLR\_MAT\_PROP \+ VLR\_MAT\_TERC da SAFX09\. Caso não preenchido gravar “0”\.

MFS10414

MFS13631

RN42

__Campo vlrDedAlim__

Recuperar a informação do campo VLR\_DED\_ALIM da SAFX09\. Caso não preenchido gravar “0”\.

MFS10414

MFS13631

RN43

__Campo vlrDedTrans__

Recuperar a informação do campo VLR\_DED\_TRANS da SAFX09\. Caso não preenchido gravar “0”\.

MFS10414

MFS13631

RN44

__Campo vlrBaseRet__

Recuperar a informação do campo VLR\_BASE\_INSS da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo VLR\_BASE\_INSS da SAFX07\.

Obs:

__\[MFS19169\]__

Caso não preenchido e o campo “Desconsiderar NFs sem Valor de Retenção informado” NÃO estiver selecionado na tela de Dados Iniciais deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2020 \- Registro: Notas Fiscais de Serviços

“Campo Valor Base de Cálculo da Retenção do INSS não preenchido“\. 

Identificação da Nota Fiscal: Estabelecimento: XXXX / NF: XXXX / Serie: XXXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

Item de Serviço: XXXXXX

MFS10414

MFS17919

MFS19169

RN45

__Campo vlrRetencao__

Recuperar a informação do campo VLR \_INSS\_RETIDO da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo VLR \_INSS\_RETIDO da SAFX07\.

Obs:

__\[MFS19169\]__

Caso não preenchido e o campo “Desconsiderar NFs sem Valor de Retenção informado” NÃO estiver selecionado na tela de Dados Iniciais deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2020 \- Registro: Notas Fiscais de Serviços

“Campo Valor da Retenção do INSS não preenchido“

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

Item de Serviço: XXXXX

MFS10414

MFS17919

MFS19169

RN46

__Campo vlrRetSub__

Recuperar a informação do campo VLR\_RET\_SERV da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo VLR\_RET\_SERV da SAFX07\.

MFS10414

MFS17919

RN47

__Campo vlrNRetPrinc__

Recuperar a informação do campo VLR\_N\_RET\_PRINC da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo VLR\_N\_RET da SAFX263, valor informado no campo valorPrinc detalhadas na tag “infoProcRetPr”

MFS10414

MFS17919

RN48

__Campo vlrServicos15__

Será a somatória do campo VLR\_SERVICO da SAFX09, considerando os itens cujo código de serviço tenha sido parametrizado na tela de Identificador do Tipo de Serviço – com identificador de Aposentadoria Especial com o Indicador igual “15 anos“\.

__\[Alteração MFS13205\]__

Recuperar a informação do campo VLR\_SERV\_15 da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo VLR\_SERV\_15 da SAFX07\.

MFS10414

MFS13205

MFS17919

RN49

__Campo vlrServicos20__

Será a somatória do campo VLR\_SERVICO da SAFX09, considerando os itens cujo código de serviço tenha sido parametrizado na tela de Identificador do Tipo de Serviço – com identificador de Aposentadoria Especial com o Indicador igual “20 anos“\.

__\[Alteração MFS13205\]__

Recuperar a informação do campo VLR\_SERV\_20 da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo VLR\_SERV\_20 da SAFX07\.

MFS10414

MFS13205

MFS17919

RN50

__Campo vlrServicos25__

Será a somatória do campo VLR\_SERVICO da SAFX09, considerando os itens cujo código de serviço tenha sido parametrizado na tela de Identificador do Tipo de Serviço – com identificador de Aposentadoria Especial com o Indicador igual “25 anos“\.

__\[Alteração MFS13205\]__

Recuperar a informação do campo VLR\_SERV\_25 da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo VLR\_SERV\_25 da SAFX07\.

MFS10414

MFS13205

MFS17919

RN51

__Campo vlrAdicional__

Recuperar a informação do campo VLR\_TOT\_ADIC da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo VLR\_TOT\_ADIC da SAFX07\.

MFS10414

MFS17919

RN52

__Campo vlrNRetAdic__

Recuperar a informação do campo VLR\_N\_RET\_ADIC da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo VLR\_N\_RET da SAFX263, valor informado no campo valorAdic detalhadas na tag “infoProcRetAd”

MFS10414

MFS17919

- __Registro infoProcRetPr \- Registro de Informações de Processo Retenção Principal__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN53

- __Origem das informações__: SAFX09 e SAFX263 Botão Processos Administrativos/Judiciais – \(Tela de “Documento Fiscal”\)\.
- __Regra de seleção__: Este registro servirá para identificar os processos de retenção principal relacionados a não retenção da contribuição previdenciária\. 
- __Campos\-Chave__: tpProcRetPrinc, nrProcRetPrinc, codSuspPrinc
- __Nível hierárquico do registro__: filho do registro ideTomador\.
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Poderá existir “50” infoProcRetAd ou não existir

MFS10414

MFS17919

RN54

__Campo tpProcRetPrinc__

Recuperar a informação do campo IND\_TP\_PROC\_ADJ\_PRINC da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo IND\_TP\_PROC\_ADJ para o Indicador de Processo \(IND\_PRINC\_ADIC\) igual a ‘1 \- Principal’ da SAFX263\.

\[ALTERADO MFS11895\]

Obs:

Caso o tipo de processo informado seja ‘3’ deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2020 \- Registro: Informações de Processo Retenção Principal

“O tipo de processo não poderá ser ‘3’, não corresponde a um valor válido\." 

Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX

Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX

MFS10414

MFS11895

MFS17919

RN55

__Campo nrProcRetPrinc__

Recuperar a informação do campo NUM\_PROC\_ADJ\_PRINC da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo NUM\_PROC\_ADJ para o Indicador de Processo \(IND\_PRINC\_ADIC\) igual a ‘1 \- Principal’ da SAFX263\.

ALTERADO MFS118958\]

Obs:

Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2010 \- Registro: Informações de Processo Retenção Adicional

“Campo Número do Processo deve ser numérico\."

Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX

Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX

MFS10414

MFS11895

MFS17919

RN56

__Campo codSuspPrinc__

Recuperar a informação do campo COD\_SUSP\_PRINC da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo COD\_SUSP para o Indicador de Processo \(IND\_PRINC\_ADIC\) igual a ‘1 \- Principal’ da SAFX263\.

\[ALTERADO MFS11895\]

Obs:

Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2020 \- Registro: Informações de Processo Retenção Principal

“Campo Código do Indicativo da Suspensão deve ser numérico\."" 

Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX

Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX

MFS10414

MFS11895

MFS17919

RN57

__Campo valorPrinc__

Recuperar a informação do campo VLR\_N\_RET\_PRINC da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo VLR\_N\_RET para o Indicador de Processo \(IND\_PRINC\_ADIC\) igual a ‘1 \- Principal’ da SAFX263\.

MFS10414

MFS17919

- __Registro infoProcRetAd \- Registro de Informações de Processo Retenção Adicional__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN58

- __Origem das informações__: SAFX09 e SAFX263 Botão Processos Administrativos/Judiciais – \(Tela de “Documento Fiscal”\)\.
- __Regra de seleção__: Este registro servirá para identificar os processos de retenção adicional relacionados a não retenção da contribuição previdenciária\. 
- __Campos\-Chave__: tpProcRetAdic, nrProcRetAdic, codSuspAdic
- __Nível hierárquico do registro__: filho do registro ideTomador\.
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: poderá existir “50” infoProcRetAd ou não existir

MFS10414

MFS17919

RN59

__Campo tpProcRetAdic__

Recuperar a informação do campo IND\_TP\_PROC\_ADJ\_ADIC da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo IND\_TP\_PROC\_ADJ para o Indicador de Processo \(IND\_PRINC\_ADIC\) igual a ‘2 \- Adicional’ da SAFX263\.

\[ALTERADO MFS11895\]

Obs:

Caso o tipo de processo informado seja ‘3’ deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2020 \- Registro: Informações de Processo Retenção Adicional

“O tipo de processo não poderá ser ‘3’, não corresponde a um valor válido\." 

Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX

Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX

MFS10414

MFS11895

MFS17919

RN60

__Campo nrProcRetAdic__

Recuperar a informação do campo NUM\_PROC\_ADJ\_ADIC da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo NUM\_PROC\_ADJ para o Indicador de Processo \(IND\_PRINC\_ADIC\) igual a ‘2 \- Adicional’ da SAFX263\.

ALTERADO MFS11895\]

Obs:

Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2010 \- Registro: Informações de Processo Retenção Adicional

“Campo Número do Processo deve ser numérico\."

Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX

Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX

MFS10414

MFS11895

MFS17919

RN61

__Campo codSuspAdic__

Recuperar a informação do campo COD\_SUSP\_ADIC da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo COD\_SUSP para o Indicador de Processo \(IND\_PRINC\_ADIC\) igual a ‘2 \- Adicional’ da SAFX263\.

\[ALTERADO MFS11895\]

Obs:

Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2020 \- Registro: Informações de Processo Retenção Adicional

“Campo Código do Indicativo da Suspensão deve ser numérico\." 

Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX

Estabelecimento: XXXX / NF: XXXX / Data Movimento: XXXX

MFS10414

MFS11895

MFS17919

RN62

__Campo valorAdic__

Recuperar a informação do campo VLR\_N\_RET\_ADIC da SAFX09\.

Caso a nota se enquadrar em __Operações de transporte de passageiros \(RN00\):__

Recuperar a informação do campo VLR\_N\_RET para o Indicador de Processo \(IND\_PRINC\_ADIC\) igual a ‘2 \- Adicional’ da SAFX263\.

MFS10414

MFS17919

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


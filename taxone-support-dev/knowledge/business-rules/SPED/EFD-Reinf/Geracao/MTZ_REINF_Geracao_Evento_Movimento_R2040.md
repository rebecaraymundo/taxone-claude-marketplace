# MTZ_REINF_Geracao_Evento_Movimento_R2040

- **Fonte:** MTZ_REINF_Geracao_Evento_Movimento_R2040.docx
- **Modificado:** 2023-03-28
- **Tamanho:** 86 KB

---

 

THOMSON REUTERS

Geração evento R\-2040 \- REINF

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-11670

Elenilson Coutinho

Definição de regras para geração do evento R\-2040 Reinf 

MFS\-11925

Lara Aline

Inclusão mensagens de logs RN10 e 11\.

MFS\-12777

Elenilson Coutinho

Alteração de Regra para tratamento da geração do evento a partir da SAFX03 – Contas a Pagar

MFS\-12176

Elenilson Coutinho

Regra para tipo de arquivo Original/Retificação

MFS\-12180

Elenilson Coutinho

Regra de geração considerando eventos de fechamento/reabertura

CH17024\_2017

Lara Aline

Inclusão da opção 1 – Patrocínio no campo Tipo de Repasse

MFS13861

Lara Aline

Alteração no layout conforme versão 1\.2

MFS14864

Lara Aline

Alteração para recuperação de notas de entradas\.

MFS14129

Lara Aline

Inclusão de regra para o campo observação do registro nfs\.

MFS15284

Lara Aline

Ajuste nos campos vlrTotalRep e vlrBruto\.

MFS16067

Lara Aline

Ajuste para considerar o campo “Desconsiderar sem Valor de Retenção informado” da tela de Dados Iniciais\.

MFS17138

Lara Aline

Inclusão status “Excluído na Mensageria” no tratamento de Fechamento/Reabertura

MFS17269

Lara Aline

Ajuste no campo vlrTotalNRet conforme nova versão 1\.3\.02\.

MFS18702

Lara Aline

Alteração da Geração Prévia retirando a possibilidade de Geração de Eventos Retificados, eventos retificadores serão gerados apenas no Painel de Controle de Eventos

MFS20930

Lara Aline

Inclusão dos campos chaves na regra do registro infoProc, acordo com layout 1\.4

MFS\-90001

Alessandra Cristina Navatta

Alteração da referência do arquivo de de\_para \(versão 2\.1\.1\)

__Obs\. O ajuste mapeado nesta demanda, refere\-se a atualização funcional\. Não há impactos na implementação__

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral de Geração do Evento R\-2040\.__

O evento R\-2040 do SPED \- REINF tem por objetivo gerar informações de Recursos Repassados para Associação Desportiva\. Ele será gerado com os registros:

 __Reinf__ – EFD \- Reinf

 __evtAssocDespRep__ – Evento Recursos Repassados para Associação Desportiva

 __ideEvento__ – Informações de Identificação do Evento

 __ideContri__ – Informações de Identificação do Contribuinte

__ ideEstab – __Informações de identificação

 __recursosRep__ – Recursos repassados para associação desportiva

__ infoRecurso__ – Detalhamento dos recursos repassados

__\[Alterado MFS13861\]__

__ infoProc__ – Informações de processos relacionados a não retenção de contribuição previdenciária

Observar orientações existentes no arquivo " TR\_REINF\_DEXPARA\_V2\.1\.1\.xlsx "\.

- __Origem das informações__: SAFX03, SAFX04, SAFX09 e Cadastro do Estabelecimento\.
- __Regra de seleção__: O Registro R\-2040 é utilizado para demonstrar informações de Recursos Repassados para Associação Desportiva\. Ele será gerado com base em Informações de Notas Fiscais de Serviço ou Contas a Pagar\.

Para obtermos as informações para sua geração, devemos recuperar registros das tabelas SAFX03 e SAFX09, considerando os seguintes critérios:

__\[MFS12777\]__

\- O COD\_ESTAB seja de um estabelecimento indicado pelo usuário;

\- A origem das informações deve ter sido parametrizada na tela de “Dados Iniciais” com a definição de geração com base em “Documentos Fiscais de Serviço” ou “Contas a Pagar”\.

\- Se na tela de Dados Iniciais para o Evento R\-2040 – Recursos Repassados a Associação Desportiva houver parametrização para geração com base nas informações de: 

__\[Alteração MFS14864\]__

Documento Fiscal de Serviço, então: 

O “Código de Serviço” deve ser associado a um tipo de repasse na parametrização de Identificação do Tipo de Repasse Por Código de Serviço\.

\- NFs cujo campo MOVTO\_E\_S seja diferente de "9";

\- O campo DATA\_EMISSAO deve compreender o período de geração;

\- O campo SITUACAO deve ser diferente de "S";

\- O campo COD\_CLASS\_DOC\_FIS deve ser igual a "2", "3" ou “9”;

Contas a Pagar, Então:

\- O “Código de Operação” deve ser associado a um tipo de repasse na parametrização de Identificação do Tipo de Repasse Por Código de Operação\.

\- O campo DATA\_MOVTO deve compreender o período de geração;

__\[Alterado MFS16067\]__

*Importante:*

Caso o campo “Desconsiderar sem Valor de Retenção informado” estiver selecionado na tela de Dados Iniciais:

__SAFX09__ \- Deverão ser desconsideradas todas as notas fiscais que não tenham o Valor Base INSS \(VLR\_BASE\_INSS da SAFX08/SAFX09\) e/ou Valor de INSS Retido \(VLR\_INSS\_RETIDO da SAFX08/SAFX09\) informado\. Ou seja, quando o parâmetro estiver selecionado serão considerados apenas as notas fiscais que tenham o Valor Base INSS \(VLR\_BASE\_INSS da SAFX08/SAFX09\) e Valor de INSS Retido \(VLR\_INSS\_RETIDO da SAFX08/SAFX09\) informado\.

__SAFX03__ \- Deverão ser desconsiderados todos os Arquivo de Fornecedores \(Contas a Pagar\) que não tenham o Valor da Retenção \(VLR\_RET da SAFX03\) informado\.

__\[MFS\-12176\]__

- __Original/Retificação__: Os critérios para identificar se o evento a ser gerado será original ou retificador serão os seguintes:
- Se não houver ocorrência de geração de evento anterior, criar nova ocorrência de arquivo original\.
- Se houver ocorrência de geração anterior com status “Evento Enviado” exibir a seguinte mensagem no log de geração:

              Evento R2040 – Recursos Repassados para Associação Desportiva

              Evento não gerado\. Existe evento anterior enviado aguardando retorno\.

              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração anterior com status “Evento REINF Recebido com Sucesso ou Advertência” verificar se há evento de exclusão, então:

\- Se __não__ existir evento de exclusão então, criar ocorrência de arquivo de retificação\.

\- Se existir, evento de exclusão considerar os status, então:

Evento de exclusão com status de “Evento REINF Enviado” exibir a seguinte mensagem no log de geração:

  

             Evento R2040 – Recursos Repassados para Associação Desportiva

             Evento não gerado\. Existe evento de exclusão anterior enviado aguardando retorno\.

             Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

          Evento de exclusão com status “Evento Recebido com sucesso ou Advertência” então, verificar se há ocorrência

          anterior de evento periódico com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova

          ocorrência de arquivo de  retificação, se __não__ houver, criar original\.

              \- Se existir evento de exclusão com status “Evento REINF Recebido com Erro” ou “Cancelado” ou “Erro na Geração do                          XML” então, criar nova ocorrência de retificação\.

             \- Se existir evento de exclusão com status “Aguardando Geração do XML” então exibir a seguinte mensagem no log de      geração:

                

              Evento R2040 – Recursos Repassados para Associação Desportiva

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

                      

                  Evento R2040 – Recursos Repassados para Associação Desportiva

                  Evento não gerado\. Existe evento de fechamento do período enviado aguardando retorno\.

                  Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

                      \- Evento de fechamento com status de “Evento REINF Recebido com Sucesso ou Advertência” exibir a seguinte

                        mensagem no log de geração:

               

                  Evento R2040 – Recursos Repassados para Associação Desportiva

                  Evento não gerado\. Período Fechado\.

                  Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração de evento de reabertura correspondente, com status “Evento REINF Recebido com

Sucesso ou Advertência”, prosseguir com a geração\.

         

         __\[Alterado MFS17138\]__

         \- Evento de fechamento com status de “Evento REINF Recebido com erro” ou “Cancelado” ou “Erro na Geração do 

           XML” ou “Evento Excluído na Mensageria” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, exibir a seguinte mensagem no log de geração:

                   Evento R2040 – Recursos Repassados para Associação Desportiva

                   Evento não gerado\. Período Fechado\.

                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

 

                   Se não houver evento de fechamento com status “Evento REINF Recebido com Sucesso ou Advertência”,

                   prosseguir com a geração\. 

                       \- Evento de Fechamento com status de “Aguardando Geração do XML”, exibir a seguinte mensagem no log de   

                         geração:

                   Evento R2040 – Recursos Repassados para Associação Desportiva

                   Evento não gerado\. Existe evento de fechamento do período não enviado\.

                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

MFS11670

MFS12777

MFS12176

MFS12180

MFS13861

MFS14864

MFS16067

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
- __Nível hierárquico do registro__: filho do registro evtAssocDespRep
- __Ordenação__: não se aplica\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Um por arquivo

RN02

__Campo TpInsc__

Será gerado com conteúdo "1", uma vez que não atendemos PF\.

MFS14821

RN03

__Campo nrInsc__

Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento\.Com base neste campo podemos entender que o REINF será gerado com base em um estabelecimento Centralizador\.

MFS14821

- __Registro IdeEstab – Identificação do Estabelecimento que repassou recursos__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN04

- __Origem das informações__: Cadastro do Estabelecimento\.
- __Regra de seleção__: Este registro servirá para identificar o estabelecimento que repassou recursos
- __Campos\-Chave__: tpInscEstab, nrInscEstab
- __Nível hierárquico do registro__: filho do registro ideContri
- __Ordenação__: não se aplica\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Um por arquivo

MFS11670

RN05

__Campo tpInscricao__

Gerar com conteúdo igual a “1”\.

MFS11670

RN06

__Campo nrInscricao__

Gerar com o conteúdo do campo “CGC” do Cadastro do Estabelecimento da NF\.

Se para

MFS11670

- __Registro recursosRep – Recursos Repassados para Associação Desportiva__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN07

- __Origem das informações__: SAFX03, SAFX04 e SAFX09\.
- __Regra de seleção__: Este registro servirá identificar os repasses efetuados a associação Desportiva pelo estabelecimento\.
- __Campos\-Chave__: Não se aplica\.
- __Nível hierárquico do registro__: filho do registro ideEstab
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: para cada ideEstab poderá existir “N” recursosRep

MFS11670

RN08

__Campo cnpjAssocDesp__

Este campo será gerado com a informação carregada no campo CPF\_CGC da SAFX04\. 

Obs: CNPJ da Pessoa Jurídica vinculada a NF\.

Caso não preenchido deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2040 \- Registro: Recursos Repassados para Associação Desportiva 

“Campo CPF\_CGC não preenchido“\. 

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

__\[MFS12777\]__

Se houver parametrização em “Dados Inicias” para a opção de geração com base nas informações do “Contas a Pagar” a descrição da mensagem no log deve ser alterada caso não preenchido o campo, deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2040 \- Registro: Recursos Repassados para Associação Desportiva 

“Campo CPF\_CGC não preenchido“\. 

Identificação do Documento Fiscal: Estabelecimento: XXXXX / N° Documento: XXXXX / Cód\. Operação: XXXXX Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

MFS11670

MFS\-12777

RN09

__Campo vlrTotalRep__

Será resultado da somatória do campo VLR\_TOT da SAFX09 informado nos recursos repassados detalhado no registro infoRecurso\.

__\[MFS12777\]\[MFS15284\]__

Carregar com a resultado da somatória do campo “VLR\_BRUTO” da SAFX03 informado nos recursos repassados detalhado no registro infoRecurso, se houver parametrização em “Dados Inicias” para a opção de geração com base nas informações do “Contas a Pagar”\.

MFS11670

MFS12777

MFS15284

RN10

__Campo vlrTotalRet__

Será resultado da somatória do campo VLR\_INSS\_RETIDO da SAFX09 informado nos recursos repassados detalhado no registro “infoRecurso”\.

__\[MFS12777\]__

Carregar com a resultado da somatória do campo “VLR\_RET” da SAFX03 informado nos recursos repassados detalhado no registro infoRecurso, se houver parametrização em “Dados Inicias” para a opção de geração com base nas informações do “Contas a Pagar”\.

MFS11670

MFS12777

RN11

__vlrTotalNRet__

Será resultado da somatória do campo VLR\_N\_RET\_PRINC da SAFX09 informado nos recursos repassados detalhado no registro “infoRecurso”, com exceção dos valores informados com o Indicador de Suspenção \(ind\_susp\) igual a ‘92’, ou seja, deve ser identificado o indicador de suspensão \(SAFX2059 – Cadastro de Informação de Suspensão de Exigibilidade de Tributos\) através do campo Código de Suspensão \(COD\_SUSP\_PRINC\) informado na SAFX09\.

__\[MFS12777\]__

Carregar com a resultado da somatória do campo “VLR\_N\_RET” da SAFX03 informado nos recursos repassados detalhado no registro infoRecurso, se houver parametrização em “Dados Inicias” para a opção de geração com base nas informações do “Contas a Pagar”, com exceção dos valores informados com o Indicador de Suspenção \(ind\_susp\) igual a ‘92’, ou seja, deve ser identificado o indicador de suspensão \(SAFX2059 – Cadastro de Informação de Suspensão de Exigibilidade de Tributos\) através do campo Código de Suspensão \(COD\_SUSP\) informado na SAFX03\.

MFS11670

MFS12777

MFS17269

- __Registro infoRecurso \- Registro de Detalhamento dos Recursos Repassados a Associação Desportiva__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN12

- __Origem das informações__: SAFX09 e SAFX03
- __Regra de seleção__: Este registro servirá para identificar os recursos repassados a associação desportiva
- __Campos\-Chave__: Não se aplica\.
- __Nível hierárquico do registro__: filho do registro recursosRep
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: para cada recursosRep poderá existir “N” infoRecursos\.

MFS11670

MFS12777

RN13

__Campo tpRepasse__

Informação será recuperada do campo “Tipo de Repasse” da Tela de “Identificador do Tipo de Repasse por Código de Serviço”\.

\[Alteração CH17024\_2017\]

Valores válidos: 1, 2, 3, 4 e 5\.

__\[MFS12777\]__

Informação será recuperada do campo “Tipo de Repasse” da tela de “Identificador do Tipo de Repasse por Código de Operação” quando houver parametrização em “Dados Iniciais” para a opção de geração com base nas informações de “Contas a Pagar”\.

MFS11670

MFS12777

CH17024\_2017

RN14

__Campo descRecurso__

Nesse campo será gravada a descrição de acordo com o campo “Tipo de Repasse” da Tela de “Identificador do Tipo de Repasse por Código de Serviço”\. Conforme abaixo:

1 \- 'Patrocínio';

2 \- 'Lic\. marcas símbolos';

3 \- ‘Publicidade';

4 \- 'Propaganda';

5 \- 'Transmite espetáculo';

Valores Válidos: 1,2,3,4,5

MFS13861

RN15

__Campo vlrBruto__

Informação será recuperada do campo VLR\_TOT da SAFX09\.

__\[MFS12777\]\[MFS15284\]__

Informação será recuperada do campo “VLR\_BRUTO” da SAFX03 quando houver parametrização em “Dados Iniciais” para a opção de geração com base nas informações de “Contas a Pagar”\.

 MFS11670

MFS12777

MFS15282

RN16

__Campo vlrRetApur__

Informação será recuperada do campo VLR\_INSS\_RETIDO SAFX09\. 

Caso não preenchido deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2040 \- Registro: Detalhamento dos Recursos Repassados a Associação Desportiva 

“Campo Valor da Retenção do INSS não preenchido“\.

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

__\[MFS12777\]__

Informação será recuperada do campo “VLR\_RET” da SAFX03 quando houver parametrização em “Dados Iniciais” para a opção de geração com base nas informações de “Contas a Pagar”\.

Caso não preenchido deverá apresentar a seguinte mensagem no log de pré\-geração: 

Evento R2040 \- Registro: Detalhamento dos Recursos Repassados a Associação Desportiva 

“Campo Valor da Retenção do INSS não preenchido“\.

Identificação do Documento Fiscal: Estabelecimento: XXXXX / N° Documento: XXXXX / Cód\. Operação: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

MFS11670

MFS12777

RN23

__Campo vlrNRet__

Informação será recuperada do campo VLR\_N\_RET\_PRINC da SAFX09\.

__\[MFS12777\]__

Informação será recuperada do campo “VLR\_N\_RET” da SAFX03 quando houver parametrização em “Dados Iniciais” para a opção de geração com base nas informações de “Contas a Pagar”\.

MFS11670

MFS12777

MFS13861

- __Registro infoProc – Informações de processos relacionados a não retenção de contribuição previdenciária\.__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN17

- __Origem das informações__: SAFX09 e SAFX03
- __Regra de seleção__: Este registro servirá identificar os processos relacionados a não retenção de contribuição previdenciária\.
- __Campos\-Chave__: tpProc, nrProc e codSusp\.
- __Nível hierárquico do registro__: filho do registro recursosRep
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Poderá existir “50” infoProc\.

MFS13861

MFS20930

RN18

Campo tpProc

Informação será recuperada do campo IND\_TP\_PROC\_ADJ\_PRINC da SAFX09\.

Informação será recuperada do campo IND\_TP\_PROC\_ADJ\_PRINC da SAFX03 quando houver parametrização em “Dados Iniciais” para a opção de geração com base nas informações de “Contas a Pagar”\.

MFS13861

RN19

Campo nrProc

Informação será recuperada do campo NUM\_PROC\_ADJ\_PRINC da SAFX09\.

Obs:

Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2040 \- Registro: Recursos Recebidos ou Repassados para Clube de Futebol

“Campo Número do Processo deve ser numérico\." 

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

Informação será recuperada do campo NUM\_PROC\_ADJ\_PRINC da SAFX03 quando houver parametrização em “Dados Iniciais” para a opção de geração com base nas informações de “Contas a Pagar”\.

Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2040 \- Registro: Recursos Repassados para Associação Desportiva 

“Campo Número do Processo deve ser numérico\." 

Identificação do Documento Fiscal: Estabelecimento: XXXXX / N° Documento: XXXXX / Cód\. Operação: XXXXX Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

MFS13861

RN20

Campo codSusp

Informação será recuperada do campo COD\_SUSP\_PRINC da SAFX09\.

Obs:

Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2040 \- Registro: Recursos Recebidos ou Repassados para Clube de Futebol

“Campo Código do Indicativo da Suspensão deve ser numérico\." 

Identificação da Nota Fiscal: Estabelecimento: XXXXX / NF: XXXXX / Serie: XXXX / Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

Informação será recuperada do campo COD\_SUSP da SAFX03 quando houver parametrização em “Dados Iniciais” para a opção de geração com base nas informações de “Contas a Pagar”\.

Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2040 \- Registro: Recursos Repassados para Associação Desportiva 

“Campo Código do Indicativo da Suspensão deve ser numérico\." 

Identificação do Documento Fiscal: Estabelecimento: XXXXX / N° Documento: XXXXX / Cód\. Operação: XXXXX Pessoa Física/Jurídica: Código: XXXXX Indicador: XXXXX

MFS13861

RN21

__vlrNRet__

Será resultado da somatória do campo VLR\_N\_RET\_PRINC da SAFX09 informado nos recursos repassados detalhado no registro “infoRecurso”\.

Carregar com a resultado da somatória do campo “VLR\_N\_RET” da SAFX03 informado nos recursos repassados detalhado no registro infoRecurso, se houver parametrização em “Dados Inicias” para a opção de geração com base nas informações do “Contas a Pagar”\.

MFS13861


# MTZ_REINF_Geracao_Evento_Movimento_R4010

- **Fonte:** MTZ_REINF_Geracao_Evento_Movimento_R4010.docx
- **Modificado:** 2026-03-04
- **Tamanho:** 169 KB

---

 

THOMSON REUTERS

Módulo REINF

Geração do Evento R\-4010

\(Pagamentos/Créditos a Beneficiário Pessoa Física\) 

__Localização__: Menu SPED, módulo EFD\-REINF, menu REINF à Geração Prévia à Movimentos à Evento R\-4010

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS\-79885__

Alessandra Cristina Navatta

Criação da geração do Evento R\-4010\- Pagamentos/Créditos a Beneficiário Pessoa Física \(atendimento ao layout 2\.1 do REINF\)

06/05/2022

__MFS\-90001 __

Alessandra Cristina Navatta

Alterações referente a versão 2\.1\.1: 

- Alteração no nome do arquivo de de\_para
- Inclusão de validação no campo indFciScp
- Inclusão de validação no campo nrInscPrevComp

__Obs\. Os ajustes mapeados nesta demanda, serão contemplados no pacote da MFS\-79885 __

03/08/2022

__MFS\-511669 __

Alessandra Cristina Navatta

Inclusão de filtro na recuperação dos beneficiários do Exterior\. Inclusão dos critérios: \(UF = EX e PAÍS diferente de ‘105’\),

09/02/2023

__MFS\-512715__

Alessandra Cristina Navatta

Ajuste dos valores válidos do campo infoEntid

09/02/2023

__MFS\-518080__

Alessandra Cristina Navatta

Inclusão de regras para o campo Observ \(observação\), quando for recuperado mais de um registro para o mesmo beneficiário, data e natureza de rendimento\.

08/03/2023

__MFS\-518252__

Alessandra Cristina Navatta

Criação das regras para atender o cenário de rendimentos sem retenção\. 

Inclusão de regras nos campos vlrRendTrib e vlrIR da tag infoPgto\.

13/03/2023

__MFS\-529150__

Alessandra Cristina Navatta

Ajuste na regra da tag detDed, considerando mais de um tipo de dedução oriundo de um mesmo rendimento tributável\. E ajuste do valor tributável \(vlrRendTrib da \(tag infoPgto\), desconsiderando o valor das deduções \(se existir\)\. 

Ajuste na regra da tag benefPen \(filha das tags dedDet e dedSusp\), para indTpDeducao= 5 e 7\. E inclusão de regra para apresentar as informações dos beneficiários e dependentes de pensão apenas uma vez\.

13/04/2023

__MFS\-532760__

Alessandra Cristina Navatta

Inclusão de mensagem no log para a geração centralizada\.

Inclusão de regras e mensagem no log para a consolidação das informações por CPF e não código pessoa física/jurídica \(cod\_fis\_jur\)

05/05/2023

__MFS\-535745__

Alessandra Cristina Navatta

Adequação da geração do evento R\- vlr\_isencao 4010, para atendimento ao layout 2\.1\.2

Ajustes efetuados:

- Inclusão da regra de quebra por arquivo na regra geral
- Inclusão do campo ideEvtAdic na tag ideBenef
- Mudança de domínio no campo relDep
- Exclusão de validação no campo ind\_Fci\_Scp
- Inclusão de validação, no campo percscp
- Inclusão do campo dtEscrCont na tag infopagto
- Inclusão do campo Observ na tag infopagto
- Exclusão de regra no campo Observ da tag idepgto, pois trata\-se de uma observação da natureza de rendimento e neste momento não iremos criar campo nas nossas tabelas\.
- Alteração de regra \(formato\) campo telef
- Inclusão de validação no campo frmTribut

18/05/2023

__BUG\-539450__

Alessandra Cristina Navatta

- Exclusão da validação do campo vlrIsento, validando se o campo é maior que zero, quando tipo de isenção ‘1 \- Parcela isenta 65 anos’\. Essa validação não se faz necessário, pois, já consideramos no tipo isenção valores maiores que zero, independentemente do tipo de isenção\.
- Inclusão de mensagem no log quando utilizado algum tipo de isenção não prevista pelo REINF\.

26/05/2023

__MFS\-543053__

Alessandra Cristina Navatta

Quando for recuperado mais de um registro para o mesmo beneficiário, data e natureza de rendimento, na SAFX53, os valores dos registros, serão somados e apresentados uma única linha no XML \(consolidação por beneficiário, data e natureza de rendimento, na tag infoPgto\)\. Essa regra se aplica também para as tags ‘detDed’ \(consolidação por tipo de dedução\), tag ‘benefPen’ \(consolidação por beneficiário\) e tag ‘rendIsento’ \(consolidação por tipo de isenção\)\.

Já os campos indFciScp \(indicador FCI ou SCP\), nrInscFciScp \(número inscrição FCI ou SCP\), percSCP \(percentual SCP\), indRRA \(indicador de RRA\), indJud \(indicador de processo\), Observ \(observação, da tag infoPgto\) e para as tags infoRRA, despProcJud, infoProcJud, despProcJud, que não fazem parte da chave do evento, serão consideradas as informações do primeiro registro recuperado\.

Inclusão de log no campo cpfBenef, para orientar os clientes sobre o cenário do beneficiário estar com a UF preenchida com ‘EX’ e no cadastro ter CPF informado\.

13/06/2023

__MFS\-549365__

Alessandra Cristina Navatta

Mudança de domínio no campo Tipo de Isenção\. Ajuste na mensagem apresentada\. Ajuste na regra do campo vlrIsento

 Atendimento ao layout 2\.1\.2 

11/07/2023

__MFS\-561263__

Alessandra Cristina Navatta

Inclusão da origem arquivos externos \(localização REINF>> Arquivos Externos >> Importação\), tabela reinf\_xml\_imp\_r4000, para a geração do R\-4010

28/08/2023

__MFS\-566870__

Alessandra Cristina Navatta

Ajustes referente a nota técnica 03/2023, conforme INFOLEGIS 1740/23 \- Z \- 084 \- EFD REINF\_NT 03/2023 \- DW/T1

Alterações nos campos:

qtdMesesRRA \(tag __infoRRA__\) – Exclusão de Validação

indTpDeducao \- inclusão do tipo de dedução “8 – Desconto simplificado mensal” nos grupos de informações \{detDed\} e \{dedSusp\}\. 

vlrDeducao – Inclusão de regra quando o campo indTpDeducao = "8" 

Não houve necessidade de ajustar/incluir a validação nos campos abaixo:

 __tpIsencao __abaixo, pois só geramos no produto ideContri/tpInsc\}=\[1\]\)

Campo \{tpIsencao\}: alteração da validação “Só é permitido informar \[5, 6, 7, 11\] se o declarante for PJ \(\{ideContri/tpInsc\}=\[1\]\)”\.

codPostal \(tag __endExt\)__ – retirada da validação “Devem ser informados apenas caracteres numéricos”\. O campo 20 \- CEP está definido com tipo numérico

__Outras alterações:__

Ajuste da regra do campo vlrRendTrib \.Abater as Isenções e não abater as deduções do valor bruto para informar o resultado no campo vlrRendTrib__ \[TICKET 77628\] __

14/09/2023

Bug \- 572300

Alessandra Cristina Navatta

Truncar em 30 posições o campo ‘complem’ da tag endExt, caso no cadastro da SAFX04 o campo 14 \- Complemento do Endereço, possua mais que 30 posições\.

28/09/2023

MFS\-581956

Alessandra Cristina Navatta

Inclusão da regra para a recuperação dos registros da SAFX53 a partir da data de movimento ou fato gerador, considerando o parâmetro ‘Recuperação dos registros da SAFX53 com base na data de‘ criado na tela de Dados Iniciais\. Ajuste da regra do campo dtFG \(da tag infoPagto\), considerando a informação deste parâmetro\.

03/11/2023

MFS\-584211

Alessandra Cristina Navatta

Ajustes referente a nota técnica 04/2023, conforme INFOLEGIS 1740/23 \- Z \- 089 \- EFD REINF\_NT 04/2023

- Inclusão de regra para o campo dtFG da tag ‘infoPagto’, para os registros de natureza de rendimento igual a ‘12001’
- Inclusão de validação no campo vlrRendBruto da tag ‘infoPagto’

16/11/2023

MFS\-699550

Alessandra Cristina Navatta

Ajustes referente a nota técnica 04/2024, conforme INFOLEGIS 1740/24 \- Z \- 099 \- EFD REINF\_NT 03/2024

- Exclusão de validação no campo: vlrRendBruto \(tag infoPgto\)
- Inclusão da exclusividade na validação do campo nifBenef \(tag infoPgtoExt\)  
- Inclusão de validações no campo frmTribut \(tag infoPgtoExt\) com relação ao código x vlrIR

30/10/2024

MFS\-748238

Bruna Ribeiro 

Ajuste na tag <vlrRendBruto> quando o campo estiver zerado\. 

16/01/2025

MFS\-805178

Alessandra Cristina Navatta

Ajuste nos Campos tpProcRRA, nrProcRRA, indOrigRec, da tag infoRRA e campo nrProc, da tag infoProcJud atendendo a NT01/2025

07/05/2025

MFS\-841314

Rosemeire Santos

Inclusão da validação na geração prévia do JCP dos eventos R\-4010 para informar que o período já está fechado\.

03/07/2025

 

###### __DESCRIÇÃO__

__MFS__

__Regra Geral de Geração do Evento R\-4010\.__

O evento R\-4010 do SPED \- REINF tem por objetivo gerar informações de Pagamentos/Créditos a Beneficiário Pessoa Física\. Ele será gerado com os registros:

__Reinf__ – EFD \- Reinf

__evtRetPF__ – Evento pagamentos ou créditos efetuados a pessoa física

__ideEvento__ – Informações de Identificação do Evento

__ideContri__ – Informações de Identificação do Contribuinte

__infoComplContri –__ Informações complementares do contribuinte

__ideEstab \-__ Informações de Identificação do Estabelecimento

__ideBenef –__ Identificação do Beneficiário

__ideDep –__ Identificação dos Dependentes

__idePgto –__ Identificação do rendimento

__infoPgto–__ Informações relativas ao rendimento pago/creditado

__detDed __\- Informações relativas às deduções do rendimento tributável

__benefPen – __Dependentes e beneficiários da pensão alimentícia

__rendIsento – __Rendimentos isentos ou não tributáveis

__infoProcRet__– Processos relacionados a não retenção de tributos

__dedSusp – __Detalhamento das deduções suspensas

__benefPen – __Deduções suspendas por dependentes e beneficiários da pensão alimentícia

__infoRRA – __Informações complementares \- RRA

__despProcJud – __Despesas com processo judicial

__ideAdv –__ Identificação do advogado

__infoProcJud – __Informações de processo judicial

__despProcJud – __Despesas com processo judicial

__ideAdv –__ Identificação do advogado

__infoPgtoExt – __Informações complementares relativas a pagamentos do Exterior

__endExt – __Endereço do beneficiário residente ou domiciliado no exterior

__ideOpSaude – __Identificação da operadora do plano privado coletivo empresarial de assistência à saúde

__infoReemb  \- __Informações de reembolso do titular do 

 coletivo empresarial

__infoDependIPl \- __Informações de dependente do plano de saúde coletivo empresarial

__infoReembDep  \- __Informações de reembolso do dependente do plano de saúde coletivo empresarial

Observar orientações existentes no arquivo "TR\_REINF\_DEXPARA\_V2\.1\.1\.xlsx" e "TR\_REINF\_DEXPARA\_V2\.1\.2\.xlsx"\.

__Origem das informações__: 

- SAFX2064 – Cadastro de Estabelecimento;
- SAFX04 \- Arquivo de Cadastro de Pessoas Físicas/Jurídicas;
- SAFX53 \- Arquivo de Controle de Tributos;
- SAFX531 \- Rendimentos de Decisão Judicial;
- SAFX532 \- Identificação do Advogado;
- SAFX534 \- Detalhamento das deduções com exigibilidade suspensa \(Evento R\-4010\); 
- SAFX535\-Informação das deduções suspensas por dependentes e beneficiários da pensão   
alimentícia \(Evento R\-4010\);
- SAFX536 \- Informações de Dependentes e Beneficiários da Pensão Alimentícia \(Evento R\-4010\)
- SAFX275 \- Tabela de Dependentes sem Vínculo;
- SAFX276 \- Tabela de Valores de Pagamentos e Reembolsos do Plano de Saúde referente ao Titular;
- SAFX277 \- Tabela de valores de Pagamento e Reembolsos do Plano de Saúde referente aos Dependentes

Ele será gerado com base nas informações da SAFX53\- Controle de Tributos, considerando os seguintes critérios:

\- O COD\_ESTAB seja de um estabelecimento indicado pelo usuário;

\- __\[ALTERAÇÃO MFS\- 581956\]__ Os registros devem estar compreendidos \(na Data do Movimento ou Data do Fato Gerador\), da SAFX53\. A data será definida, de acordo com o preenchimento do parâmetro ‘Recuperação dos registros da SAFX53 com base na data de‘ na tela de Dados e deve estar compreendida no período da Apuração do Arquivo 

\- Pessoa Física/Jurídica \(apenas pessoa Física\)\. A pessoa jurídica da SAFX53, deve estar cadastrada na tabela de pessoa física/jurídica \(SAFX04\) com CPF \(campo 06 \- CPF\-CGC com 11 posições\)\. 

\- __\[ALTERAÇÃO MFS\-511669\] __Para os Beneficiários do exterior \(UF = EX e PAÍS diferente de ‘105’\), quando campo 26\-IND\_CLASSE\_PFJ da safx04 estiver preenchido com informação ‘01\-Pessoa Física’;

\- Natureza de Rendimento deve estar preenchido na SAFX53

__\[ALTERAÇÃO MFS\-561263\] – Geração Arquivo JCP – Origem Arquivos Externos__

Considerar as informações da tabela reinf\_xml\_imp\_r4000, do estabelecimento e período da apuração indicados na tela de geração prévia\. Será gerado um XML para cada beneficiário, período e ideEvtAdic\.

__\[INCLUSÃO MFS\-841314\] \- Geração Arquivo JCP – Origem Arquivos Externos__

Incluir uma validação na geração prévia do JCP \(Arquivos Externos\) dos eventos R\-4010 \(Pagamentos/Créditos a Beneficiário Pessoa Física\) e para informar que o período já está fechado e não prosseguir com o processamento dos eventos\.

- __\[ALTERAÇÃO MFS\-535745\] Quebra das informações por arquivo:__

 Como regra geral, os rendimentos pagos ou creditados a um determinado beneficiário devem  
ser informados em um único arquivo xml, detalhando\-se cada um dos pagamentos ou créditos  
efetuados\. Há, no entanto, duas exceções a essa regra:

1. Prestação das informações de forma descentralizada por estabelecimento; e
2. Utilização do campo \{ideEvtAdic\}

- __Tela de Geração Prévia e Painel de Eventos:__
- Pela tela de Geração Prévia, só serão permitidas gerações originais\. 
- Na tela de Painel de Eventos, dependendo do status pode ser feita geração original\. Já as gerações retificadoras, sempre serão realizadas pela tela do painel, pela opção ‘Reprocessar Evento’\.
- __Original/Retificação__: Os critérios para identificar se o evento a ser gerado será original ou retificador serão os seguintes:
- Se não houver ocorrência de geração de evento anterior, criar nova ocorrência de arquivo original\.
- Se houver ocorrência de geração anterior com status “Evento Enviado” exibir a seguinte mensagem no log de geração:

Evento R4010 \- Pagamentos/Créditos a Beneficiário Pessoa Física                   

              Evento não gerado\. Existe evento anterior enviado aguardando retorno\.

              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração anterior com status “Evento REINF Recebido com Sucesso ou Advertência” verificar se há evento de exclusão, então:

\- Se __não__ existir evento de exclusão então, criar ocorrência de arquivo de retificação\.

\- Se existir, evento de exclusão considerar os status, então:

Evento de exclusão com status de “Evento REINF Enviado” exibir a seguinte mensagem no log de geração:

  

             Evento R4010 \- Pagamentos/Créditos a Beneficiário Pessoa Física   

             Evento não gerado\. Existe evento de exclusão anterior enviado aguardando retorno\.

             Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

          Evento de exclusão com status “Evento Recebido com sucesso ou Advertência” então, verificar se há ocorrência

          anterior de evento periódico com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova

          ocorrência de arquivo de retificação, se __não__ houver, criar original\.

              \- Se existir evento de exclusão com status “Evento REINF Recebido com Erro” ou “Cancelado” ou “Erro na Geração do XML” então, criar nova ocorrência de retificação\.

             \- Se existir evento de exclusão com status “Aguardando Geração do XML” então exibir a seguinte mensagem no log de      geração:

                

              Evento R4010 \- Pagamentos/Créditos a Beneficiário Pessoa Física   

              Evento não gerado\. Existe evento anterior não enviado\.

              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração anterior com status “Evento REINF Recebido com erro”, então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova ocorrência de arquivo de retificação, se __não__ houver, criar original\.
- Se houver ocorrência de geração anterior com status “Aguardando Geração do XML” ou “Cancelado” ou “Erro na Geração do XML” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova ocorrência de arquivo de retificação, se __não__ houver, criar original\.
- __Fechamento/Reabertura:__ Critérios de geração do evento considerando a situação do período\.
- Se não houver ocorrência de geração de evento de fechamento, prosseguir com a geração\.
- Se houver ocorrência de geração de evento de fechamento considerar os status então:

                      \- Evento de fechamento com status de “Evento Reinf Enviado” exibir a seguinte mensagem no log de geração:

                      

                  R4010 \- Pagamentos/Créditos a Beneficiário Pessoa Física   

                  Evento não gerado\. Existe evento de fechamento do período enviado aguardando retorno\.

                  Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

                      \- Evento de fechamento com status de “Evento REINF Recebido com Sucesso ou Advertência” exibir a seguinte

                        mensagem no log de geração:

               

                  R4010 \- Pagamentos/Créditos a Beneficiário Pessoa Física   

                  Evento não gerado\. Período Fechado\.

                  Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração de evento de reabertura correspondente, com status “Evento REINF Recebido com

Sucesso ou Advertência”, prosseguir com a geração\.

        

       \- Evento de fechamento com status de “Evento REINF Recebido com erro” ou “Cancelado” ou “Erro na Geração do 

           XML” ou “Evento Excluído na Mensageria” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, exibir a seguinte mensagem no log de geração:

                   R4010 \- Pagamentos/Créditos a Beneficiário Pessoa Física                     

                   Evento não gerado\. Período Fechado\.

                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

 

                   Se não houver evento de fechamento com status “Evento REINF Recebido com Sucesso ou Advertência”,

                   prosseguir com a geração\. 

                       \- Evento de Fechamento com status de “Aguardando Geração do XML”, exibir a seguinte mensagem no log de   

                         geração:

                   R4010 \- Pagamentos/Créditos a Beneficiário Pessoa Física   

                   Evento não gerado\. Existe evento de fechamento do período não enviado\.

                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- __Gravação dos Registros__: Todos os registros recuperados na geração do evento R\-4010; são gravados em uma tabela\. 

MFS\-79885

MFS\-90001

MFS\-561263

MFS\-581956

__ __

*Detalhamento das Regras:*

__Registro evtRetPF__– Evento pagamentos ou créditos efetuados a pessoa física

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

__\[ALTERAÇÃO MFS\-532760\]__ Na geração centralizada, exibir a mensagem no log: “O evento foi gerado de forma centralizada, portanto, todos os dados cadastrais foram considerados do estabelecimento centralizador <<Cód\-Razao social estabelecimento centralizador>>\.”

tpInsc

Conteúdo fixo = “1”

nrInsc

CNPJ do estabelecimento, considerando apenas as 8 primeiras posições do CNPJ, completando com zeros à direita\. 

__Registro infoComplContri__\- Informações complementares do contribuinte

natJur

Campo 95 – Natureza Jurídica \(SAFX2064\)

__Registro ideEstab__\- Informações de identificação do estabelecimento

tpInscEstab

Conteúdo fixo = “1”

nrInscEstab

CNPJ do estabelecimento

__Registro ideBenef__ – Identificação do Beneficiário

__\[ALTERAÇÃO MFS\-532760\]__ Caso exista mais de um beneficiário com o mesmo CPF e no período existir movimentação para esses beneficiários \(com mesmo CPF\), as informações de todas as tags deste evento, a partir da tag de beneficiários, deverão ser consolidadas, gerando o evento para um único beneficiário\. O sistema irá considerar a movimentação de todos esses beneficiários, em um único arquivo\.

A consolidação das informações será feita pelos campos chaves do evento\. Já os campos que não compõem a chave, e que são campos de cadastros, serão considerados conforme cadastrados pelo primeiro beneficiário recuperado \(considerando o cenário acima\)\. Os campos de valores devem ser somados\.

Atendendo o cenário:

  
__SAFX04:__

Cod\_fis\_jur = 123456 | CPF 269\.125\.627\-87|  01/01/2023 |  

Cod\_fis\_jur = 999999 | CPF 269\.125\.627\-87|  12/01/2023 |

 __SAFX53:__

Cod\_fis\_jur = 123456 | CPF 269\.125\.627\-87|  NF 001 | 10/01/2023 |  

Cod\_fis\_jur = 999999 | CPF 269\.125\.627\-87|  NF 002 | 12/01/2023 |

__Geração do Evento:__

Consolidar os dados, gerando apenas um XML

Quando existir o cenário acima, exibir a mensagem no log: “No período, há movimentos de beneficiários com o mesmo CPF\. Para evitar a geração de mais de um XML, as informações foram consolidadas no beneficiário <<Cód\-Razao social do beneficiário consolidador>>\.”

cpfBenef

CPF da PJ indicada no campo 04 da SAFX53\.  Recuperar Campo 06 da SAFX04

__\[ALTERAÇÃO MFS\-543053\]: __Inclusão de Validação

Se o campo CPF estiver preenchido e no cadastro da SAFX04 o campo 19 \- UF estiver preenchida com ‘EX’, exibir a mensagem no log:

“O campo ‘cpfBenef’ só deve ser preenchido se houver ao menos um registro da tag idePgto, cujo campo ‘paisResidExt’ não tenha sido informado\.”

nmBenef

Razão Social da PJ indicada no campo 04 da SAFX53\. Recuperar Campo 05 da SAFX04

ideEvtAdic

__\[ALTERAÇÂO MFS\-535745\]__ Identificador de evento adicional por beneficiário a critério do declarante

Este campo foi inserido na versão 2\.1\.2 do layout\. 

__Registro ideDep__ – Identificação dos Dependentes

cpfDep

Campo 06 \- CPF do Dependente \(SAFX275\)

Validação:

CPF deve ser válido e não pode ser igual ao CPF do beneficiário \(cpfBenef\)\. Se CPF do dependente for igual ao do beneficiário, exibir a mensagem: “O campo cpfDep não pode ser igual ao cpfBenef\. “

relDep

Campo 09 \- Relação de dependência \(SAFX275\)

Opções Válidas: 

1 \- Cônjuge;

2 \- Companheiro\(a\) com o\(a\) qual tenha filho ou viva há mais de 5 \(cinco\) anos ou possua declaração de união estável; 

3 \- Filho\(a\) ou enteado\(a\); 

6 \- Irmão\(ã\), neto\(a\) ou bisneto\(a\) sem arrimo dos pais, do\(a\) qual detenha a guarda judicial do\(a\) qual detenha a guarda judicial; 

8 \- Pais; 

9 \- Avós e bisavós; 

10 \- Menor pobre do qual detenha a guarda judicial; 

11 \- A pessoa absolutamente incapaz, da qual seja tutor ou curador; 

12 \- Ex\-cônjuge; 

99 \- Agregado/Outros\.

Valores Válidos: \(1, 2, 3, 6, 8, 9, 10, 11, 12, 99\)

__\[ALTERAÇÃO MFS\-535745\]__ Na versão 2\.1\.2, a lista de valores válidos do campo é:

1 \- Cônjuge; 

2 \- Companheiro\(a\) com o\(a\) qual tenha filho ou viva há mais de 5 \(cinco\) anos ou possua declaração de união estável; 

3 \- Filho\(a\) ou enteado\(a\); 

6 \- Irmão\(ã\), neto\(a\) ou bisneto\(a\) sem arrimo dos pais, do\(a\) qual detenha a guarda judicial; 

9 \- Pais, avós e bisavós; 

10 \- Menor pobre do qual detenha a guarda judicial; 

11 \- A pessoa absolutamente incapaz, da qual seja tutor ou curador; 

12 \- Ex\-cônjuge; 

99 \- Agregado/Outros\.

Valores válidos: 1, 2, 3, 6, 9, 10, 11, 12, 99\.

Caso o campo na SAFX275, esteja com a opção ‘8’, gravar ‘9’\.

descrDep

Campo 10 \- Descrição\(SAFX275\)

Validação: \*\*Este campo é de preenchimento obrigatório e exclusivo se o campo relDep estiver preenchido com ‘99’\. 

\(\*\*Esta validação ocorre na importação da SAFX275 e na tela de manutenção: Básicos > Matersaf DW > DataWarehouse > Manutenção > Cadastros >Pessoa Física/Jurídica\)

__idePgto –__ Identificação do rendimento

natRend

Campo 67 \- Natureza de Rendimento da SAFX53

Validação: \*\*Campo deve estar previamente cadastrado na TACES101

\(\*\*Esta validação ocorre na importação da SAFX53 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Controle de Tributos > Aba Retenção\)

observ

\[EXCLUSÃO MFS\-535745\] Exclusão de regra, pois, foi inserido novo campo de observação na tag de infopagto e essa observação refere\-se a uma observação da natureza de rendimento, que não estamos considerando no sistema

Campo  51 \- Observação da SAFX53

__\[ALTERAÇÃO__ __MFS\-518080\] __Caso seja recuperado mais de um registro \(para o mesmo beneficiário, data e natureza de rendimento\) e existir informações diferentes entre os registros, considerar a informação do primeiro registro recuperado\.

Campo de preenchimento não obrigatório\. Não geramos essa informação

__Registro __<a id="_Hlk523501001"></a>__infoPgto__ \- Informações relativas ao rendimento pago/creditado\.

- Este registro será gerado quando existir informações na SAFX53 \- Arquivo de Controle de Tributos; considerando o registro compreendido \(data do movimento/fato gerador\) no período de apuração do arquivo 

__\[ALTERAÇÃO MFS\-532760\]__ Considerando o cenário de mais de um beneficiário na base com o mesmo CPF e se existir registros de rendimentos para mais de um beneficiário com informações de países \(paisResidExt\) diferentes entre si, não consolidaremos as informações\. Serão exibidas N ocorrências de rendimentos nesta tag \(para este cenário\)\. Só consolidaremos as informações se o país dos registros for igual\. 

__\[ALTERAÇÃO MFS\-543053\]__ Caso exista mais de um registro na SAFX53 para o mesmo beneficiário, data de movimento/fato gerador e natureza de rendimento, as informações, deverão ser consolidadas, gerando um único registro para esta data\.

A consolidação das informações será feita pelos campos chaves do evento\. Já os campos que não compõem a chave, e que são campos de cadastros, serão considerados conforme cadastrados pelo primeiro registro recuperado \(considerando o cenário acima\)\. Os campos de valores devem ser somados\.

__\[ALTERAÇÃO MFS\- 584211\] Para os registros de natureza de rendimento 12001: A consolidação deve ocorrer normalmente, mas, considerar inclusive o mês e ano da competência quando este estiver preenchido\.__

Poderão existir até 999 registros de pagamentos, para cada registro recuperado, será gerado um registro infoPgto, com as informações descritas abaixo:

dtFG

__\[ALTERAÇÃO MFS\- 581956\]__ Se o parâmetro ‘Recuperação dos registros da SAFX53 com base na data de ‘ na tela de Dados Iniciais estiver preenchido com movimento, considerar o Campo 03 \- Data do Movimento da SAFX53, caso esteja preenchido com fato gerador, considerar o campo 26 – DATA\_FATO\_GERADOR da SAFX53\.

Gravar no formato: ‘AAAA\-MM\-DD’

Recuperar os registros cuja data do movimento e/ou a data do fato gerador esteja compreendida no período de apuração \(perApur\) ao qual se refere o arquivo\.

__\[ALTERAÇÃO MFS\- 584211\] __

__Para os registros de natureza de rendimento 12001:__

Se o parâmetro ‘Recuperação dos registros da SAFX53 com base na data de ‘na tela de Dados Iniciais estiver preenchido com movimento: 

Se o mês de competência \(campo13 da SAFX53\) e ano \(campo12 da SAFX53\), estiver preenchido e for diferente do mês e ano da data do movimento, considerar o último dia do mês e ano da competência neste campo e exibir a mensagem no log: “Campo dtFG com data diferente da apuração <<campos chave do registro de controle de tributo>>”\. Caso seja igual, ou não estiver preenchido, considerar a data do movimento \(Campo 03 \- Data do Movimento da SAFX53\)

	

Se o parâmetro ‘Recuperação dos registros da SAFX53 com base na data de ‘ na tela de Dados Iniciais estiver preenchido com fato gerador: 

Se o mês de competência \(campo13 da SAFX53\) e ano \(campo12 da SAFX53\), estiver preenchido e for diferente do mês e ano da data do fato gerador, considerar o último dia do mês e ano da competência neste campo e exibir a mensagem no log: “Campo dtFG com data diferente da apuração <<campos chave do registro de controle de tributo>>”\. Caso seja igual, considerar a data do movimento \(Campo 26 – DATA\_FATO\_GERADOR da SAFX53\.\)

__Outras Validações:__

Para os registros de Natureza de Rendimento = ‘12001’, verificar se o campo dtFG, está no range de data permitida, para o mês da apuração:

Mês da Apuração \(perApur\)

Datas Permitidas

Janeiro

Outubro, novembro, dezembro, do ano anterior ao período da apuração e janeiro\.

Fevereiro

Janeiro e fevereiro

Março

Janeiro, fevereiro e março

Abril

Janeiro, fevereiro, março e abril

Maio

Abril e maio

Junho

Abril, maio e junho

Julho

Abril, maio, junho e julho

Agosto

Julho e agosto

Setembro

Julho, agosto e setembro

Outubro

Julho, agosto, setembro e outubro

Novembro

Outubro e novembro

Dezembro

Outubro, novembro e dezembro

	

Caso não esteja, exibir a mensagem no log: “O campo dtFG não possui uma data permitida para esta apuração: <<dfFG: DD/MM/AAAA >>\. Identificação do pagamento: <<campos chave do registro da SAFX53>>”\.

compFP

Se o conteúdo de um dos campos 46 \- VLR\_SALARIO\_13 ou 47 \- VLR\_TRIBUTO\_13 > "0" gravar a informação do campo 12 \- Ano de Competência da SAFX53, caso contrário, gravar a informação do campo12 \- Ano de Competência ‘\-‘ campo13 \- Mês de Competência da SAFX53

Formato aceito: 

AAAA ou AAAA\-MM

__\[ALTERAÇÃO MFS\-90001\]__ – Inclusão de validação:

- Este campo só pode ser preenchido se o grupo de qualquer registro desta natureza de rendimento \(TACES101\) for igual a ‘10’ ou se o código da natureza de rendimento possuir na coluna ‘13’, a informação ‘Sim’\. Caso essas informações não forem verdadeiras, exibir a mensagem: “A natureza de rendimento indicada não possui o campo 13º igual a ‘Sim’, ou não está vinculada ao grupo ‘10’”\.

 

indDecTerc

Valores Válidos: S

Se o conteúdo de um dos campos 46\- VLR\_SALARIO\_13 ou 47 \- VLR\_TRIBUTO\_13 > "0" gravar "S" caso contrário não gerar

vlrRendBruto

Considerar a informação do campo 14 \- Valor Bruto, ou do campo 36 \- Valor de Lucro Pago por Pessoa Jurídica, ou do campo 38 \- Valor Outros para DIRF da SAFX53\.

Validação: 

Deve ser maior ou igual a \{vlrRendTrib\}

- Se este campo for menor que o campo vlrRendTrib, exibir a mensagem: “Campo vlrRendBruto deve ser maior ou igual ao valor do campo vlrRendTrib”

__\[EXCLUSÃO MFS\-699550\] \[ALTERAÇÃO MFS\-584211\]__ Deve ser maior que zero

- Se o campo não for maior que zero, exibir a mensagem: “Campo vlrRendBruto deve ser maior que zero”

__\[ALTERAÇÃO MFS\-748238\] __

__A tag <vlrRendBruto> não deve ser gerada no XML quando o campo  estiver zerado\.  __

__Validação: __

__Se o campo < vlrBruto> estiver zerado \(0,00\) na SAFX53 exibir a mensagem:__

__Aviso: O campo < vlrRendBruto> não foi informado, então não será gerado__\.

vlrRendTrib

__\[ALTERAÇÃO MFS\-566870 /TICKET 77628\] Abater as Isenções e não abater as deduções do campo vlrRendTrib __

Se campo 40 \- Indicador de Tipo de Lançamento na DIRF da SAFX53 igual a "0" ou "2", então:

Se indDecTerc do registro em questão diferente de ‘S’ então:

        Gravar \(Campo 14 \- Valor Bruto\) \- vlrIsento \(tag rendIsento\) independente do tipo de isenção – \(Campo 33 \- Valor de Aposentadoria Isento\) – \(Campo 41 \- VLR\_DED\_INSS\_TERC\)  \- \(Campo 29 \- VLR\_PREV\_PRIVADA\) – \(Campo 73 \- VLR\_FAPI\) \- \(Campo 76 \- VLR\_FUNPRESP\) \-  \(Campo 30 \- VLR\_PENS\_ALIMENT\) \- \(Campo 42 \- VLR\_DED\_DEP\_TERC\)

- Se indDecTerc do registro em questão = ‘S’, então:

         Gravar Campo47 –Valor Tributo 13º\. Salário \- vlrIsento \(tag rendIsento\) independente do tipo de isenção – \(Campo 41 \- VLR\_DED\_INSS\_TERC\) \- \(Campo 29 \- VLR\_PREV\_PRIVADA\) – \(Campo 73 \- VLR\_FAPI\) \- \(Campo 76 \- VLR\_FUNPRESP\) \-  \(Campo 30 \- VLR\_PENS\_ALIMENT\) \- \(Campo 42 \- VLR\_DED\_DEP\_TERC\)

Caso contrário gerar "0"\.

__\[ALTERAÇÃO MFS\-518252\]__ 

Se o código DARF \(origem SAFX2019\) do registro da SAFX53 estiver preenchido com ‘0000’, não gerar este campo\.

vlrIR

Se campo 40 \- Indicador de Tipo de Lançamento na DIRF da SAFX53 igual a "0", "1" ou "2", então:  
   Se indDecTerc do registro em questão = ‘N’, então:  
      Gravar Campo 15 \- Valor do Tributo da SAFX53  
   Se indDecTerc do registro em questão = ‘S’, então:  
        Gravar Campo 47 \- Valor Tributo 13º\. Salário da SAFX53  
Senão  
   Se indDecTerc do registro em questão = ‘N’, então:  
      Gravar Campo 15 \- Valor do Tributo \+ Campo 43 \- Valor Outros de Tributação Exclusiva da SAFX53  
   Se indDecTerc do registro em questão = ‘S’, então:  
        Gravar Campo 47 \- Valor Tributo 13º\. Salário da SAFX53  
  
Caso não preenchido gravar "0"

__\[ALTERAÇÃO MFS\-518252\]__ Se o código DARF \(origem SAFX2019\) do registro da SAFX53 estiver preenchido com ‘0000’, não gerar este campo\.

indRRA

Se existir informações no registro infoRRA gravar 'S'

Validações: Informação não permitida se \{indDecTerc\} for igual a \[S\]\.

- Se existir informação no registro infoRRA e campo indDecTerc for igual a ‘S’, exibir a mensagem: “Informação não permitida se campo indDecTerc for igual a S”

__\[ALTERAÇÃO__ __MFS\-543053\] __Caso seja recuperado mais de um registro \(para o mesmo beneficiário, data e natureza de rendimento\) e pelo menos um tenha informações da SAFX531, considerar ‘S’\. 

indFciScp

Valores Válidos: 1, 2\.

Se o campo 68 \- CNPJ\_FUND\_INV da SAFX53 estiver preenchido, gravar '1';  
se o campo 96 \- CNPJ\_SCP da SAFX53 estiver preenchido, gravar '2'

__\[EXCLUSÃO MFS\-535745\] – Exclusão de Validação__

__\[ALTERAÇÃO MFS\-90001\]__ – Inclusão de Validações:

- Se o campo indFciScp, estiver preenchido com ‘2’, verificar se a informação do código da natureza de rendimento \(taces101\), está preenchido com ‘12001’, caso diferente, exibir a mensagem: “A natureza de rendimento deve ser 12001, favor verificar\.

__\[ALTERAÇÃO__ __MFS\-543053\] __Caso seja recuperado mais de um registro \(para o mesmo beneficiário, data e natureza de rendimento\) e a informação estiver com origem da SAFX53, e existir informações diferentes entre os registros, considerar a informação do primeiro registro recuperado\.

nrInscFciScp

Recuperar as informações abaixo, quando o campo indFciScp = 1,2\.

Se campo 37 – indFciScp \(registro infoPgto, do evento R\-4010\) for preenchido com 1, recuperar a informação do campo 68 \- CNPJ\_FUND\_INV da SAFX53\.  
Se campo 37 \- indFciScp \(registro infoPgto, do evento R\-4010\) for preenchido com 2, recuperar a informação do campo 96 \- CNPJ\_SCP da SAFX53\.  

__\[ALTERAÇÃO__ __MFS\-543053\] __Caso seja recuperado mais de um registro \(para o mesmo beneficiário, data e natureza de rendimento\) e a informação estiver com origem da SAFX53, e existir informações diferentes entre os registros, considerar a informação do primeiro registro recuperado\.

percSCP

Recuperar o campo 97 \- Percentual de Participação do Beneficiário da SAFX53, quando o campo indFciScp estiver preenchido com 2 __\[ALTERAÇÃO MFS\-535745__\] e natureza de rendimento igual a ‘12001’

Validações: Se o campo for maior que 100, exibir a mensagem: Campo perSCP não pode ser maior que 100\. 

__\[ALTERAÇÃO__ __MFS\-543053\] __Caso seja recuperado mais de um registro \(para o mesmo beneficiário, data e natureza de rendimento\) e a informação estiver com origem da SAFX53, e existir informações diferentes entre os registros, considerar a informação do primeiro registro recuperado\.

indJud

Valores válidos: S, N

Se existir informação de rendimento de decisão judicial e tipo de rendimento =  '1 – Rendimento Recebido Acumuladamente'\. gravar "N", caso contrário gravar 'S"

__\[ALTERAÇÃO__ __MFS\-543053\] __Caso seja recuperado mais de um registro \(para o mesmo beneficiário, data e natureza de rendimento\) e pelo menos um tenha informações da SAFX531, considerar ‘S’\. 

paisResidExt

Recuperar o campo 21 \- "País” da SAFX04, quando o país da Pessoa que recebeu o pagamento for diferente de Brasil \(105\)

dtEscrCont

__\[ALTERAÇÂO MFS\-535745\]__ Data da escrituração Contábil 

Este campo foi inserido na versão 2\.1\.2 do layout\. 

Recuperar o campo 104 – Data Escrituração Contábil da SAFX53\.

Validações:

\*\* Informação obrigatória e exclusiva se a natureza do rendimento informada no campo \{natRend\} for igual a \[12052\]\. 

\*\*Se informada, deve ser uma data igual ou anterior ao período de apuração informado em \{perApur\}\.

\(\*\*Estas validações ocorrem na importação da SAFX53 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Controle de Tributos\)

Observ

__ALTERAÇÃO MFS\-535745\]__ Observação 

Este campo foi inserido na versão 2\.1\.2 do layout\. 

Recuperar o Campo  51 \- Observação da SAFX53\.

__\[ALTERAÇÃO__ __MFS\-543053\] __Caso seja recuperado mais de um registro \(para o mesmo beneficiário, data e natureza de rendimento\) e existir informações diferentes entre os registros, considerar a informação do primeiro registro recuperado\.

__detDed __\- Informações relativas às deduções do rendimento tributável

__\[ALTERAÇÃO MFS\-529150\]__ Este registro será gerado quando existir informações na SAFX53 \- Arquivo de Controle de Tributos; considerando o registro compreendido \(data do movimento/fato gerador\) no período de apuração do arquivo e pelo menos um dos campos 41 \- VLR\_DED\_INSS\_TERC,  29 \- VLR\_PREV\_PRIVADA,   73 \- VLR\_FAPI,  76 \- VLR\_FUNPRESP,  30 \- VLR\_PENS\_ALIMENT, ou 42 \- VLR\_DED\_DEP\_TERC com valor maior que zero  e com campo  40 \- IND\_TP\_LANCT\_DIRF = "0" OU "2"\.

__\[ALTERAÇÃO MFS\-543053\]__ Caso exista mais de um registro na SAFX53 para o mesmo beneficiário, data de movimento/fato gerador e natureza de rendimento, as informações de dedução, deverão ser consolidadas, gerando um único registro para esta data e tipo de dedução\.

A consolidação das informações será feita pelos campos chaves do evento\. 

Quando existir tipo de dedução igual a 5 e/ou 7: 

A consolidação das informações deve considerar inclusive se os registros possuem ou não dependentes\. Ou seja:

- Sem Dependentes Atrelado: Gerar uma linha com o somatórios dos registros da SAFX53 do mesmo beneficiário, data de movimento/fato gerador,  natureza de rendimento, que possuir dedução igual apenas a ‘5’ e/ou ‘7’ e não possuir beneficiários;
- Com Dependentes Atrelado com apenas uma das deduções \(5 ou 7\): Gerar uma linha com o somatórios dos registros da SAFX53 do mesmo beneficiário, data de movimento/fato gerador,  natureza de rendimento, que possuir dedução igual apenas a ‘5’ ou ‘7’ e possuir beneficiários\. 

Neste caso, os beneficiários devem ser todos exibidos na tag __benefPen, __, conforme regras detalhadas na tag \(benefPen – Dependentes e beneficiários da pensão alimentícia\)\.

- Com Dependentes Atrelado e as duas deduções 5 e 7: Gerar uma linha com o somatórios dos registros da SAFX53 do mesmo beneficiário, data de movimento/fato gerador,  natureza de rendimento, que possuir dedução igual apenas a ‘5’ ou ‘7’ e possuir beneficiários;

Neste caso, os beneficiários devem ser todos exibidos na tag __benefPen__, conforme regras detalhadas na tag \(benefPen – Dependentes e beneficiários da pensão alimentícia\)\.

Poderão existir até 25 registros de deduções do rendimento, para cada registro recuperado da SAFX53, desde que seja atendida as regras descritas abaixo:

indTpDeducao

__\[ALTERAÇÃO__ __ MFS\-566870\]__ Inclusão da opção 8

Valores válidos: 1, 2, 3, 4, 5, 7,8

Se campo 40 \- IND\_TP\_LANCT\_DIRF = "0" OU "2" E 41 \- VLR\_DED\_INSS\_TERC >0 gerar "1"

Se campo 40 \- IND\_TP\_LANCT\_DIRF = "0" OU "2" E  29 \- VLR\_PREV\_PRIVADA>0 gerar "2"

Se campo 40 \- IND\_TP\_LANCT\_DIRF = "0" OU "2" E  73 \- VLR\_FAPI>0 gerar "3"

Se campo 40 \- IND\_TP\_LANCT\_DIRF = "0" OU "2" E  76 \- VLR\_FUNPRESP>0 gerar "4" 

Se campo 40 \- IND\_TP\_LANCT\_DIRF = "0" OU "2" E  30 \- VLR\_PENS\_ALIMENT>0 gerar "5"

Se campo 40 \- IND\_TP\_LANCT\_DIRF = "0" OU "2" E  42 \- VLR\_DED\_DEP\_TERC>0 gerar "7"

Se campo 40 \- IND\_TP\_LANCT\_DIRF = "0" OU "2" E  105 \- VLR\_DESC\_SIMPL\_MENSAL>0 gerar "8"

vlrDeducao

__\[ALTERAÇÃO__ __ MFS\-566870\]__ Inclusão da regra quando o campo indTpDeducao = "8"

Se indTpDeducao = "1", gravar o conteúdo do campo 41 \- Valor de Deduções de INSS Terceiros

Se indTpDeducao = "2", gravar o conteúdo do campo 29 \- Valor de Previdência Privada

Se indTpDeducao = "3", gravar o conteúdo do campo 73 \-Valor FAPI

Se indTpDeducao = "4", gravar o conteúdo do campo 76 \- Valor Funpresp

Se indTpDeducao = "5", gravar o conteúdo do campo 30 \- Valor de Pensão Alimentícia

Se indTpDeducao = "7", gravar o conteúdo do campo 42 \- Valor da Dedução de Dependentes Terceiros

Se indTpDeducao = "8", gravar o conteúdo do campo 105 \- VLR\_DESC\_SIMPL\_MENSAL

Validação: Se \{indTpDeducao\} = \[5, 7\] e o grupo \{benefPen\} vinculado for informado, o valor informado neste campo deve ser a soma do campo \{vlrDepen\} do grupo \{benefPen\}\.

- Quando o indTpDeducao = “5” ou "7", o valor deste campo, deve ser o somatório do campo vlrDepen se existir informações no grupo benefPen\. Considerando este cenário, se o valor deste campo, não conter o somatório do grupo benefPen \(quando este existir\), exibir a mensagem: “Quando há informações no grupo benefPen, o valor do campo vlrDeducao deve ser o somatório do campo vlrDepen de todos os beneficiários\.”

infoEntid

Valores Válidos: S, N

Só preencher este campo se IndTpDeducao = 2, 3 ou 4, do registro detDed, do evento R\-4010, considerando as regras abaixo:

  
Se campo IndTpDeducao estiver preenchido com 2 e o campo 70 \- Número de inscrição da entidade de previdência complementar da SAFX53 estiver preenchido ou

Se campo IndTpDeducao estiver preenchido com 3 e o campo 71 \- Número Inscrição FAPI da SAFX53 estiver preenchido ou

Se campo IndTpDeducao estiver preenchido com 4 e o campo 74 – Número Inscrição Funpresp da SAFX53 estiver preenchido, preencher este campo com 'S'\. Caso contrário, preencher com 'N'

Validação: 

se IndTpDeducao = 2, 3 ou 4, do registro detDed, do evento R\-4010 e não existir informação neste campo, exibir a mensagem: “Quando o campo IndTpDeducao = 2, 3 ou 4, o campo  infoEntid deve ser informado”

nrInscPrevComp

Se campo IndTpDeducao estiver preenchido com 2, considerar a informação do campo 70\-Número de inscrição da entidade de previdência complementar ou

Se campo IndTpDeducao estiver preenchido com 3, considerar a informação do campo 71\-Número Inscrição FAPI ou

Se campo IndTpDeducao estiver preenchido com 4, considerar a informação do campo 74\- Número Inscrição Funpresp da SAFX53\.

__\[ALTERAÇÃO MFS\-90001\]__ – Inclusão de validações: 

- Se o infoEntid = \[S\], este campo é de preenchimento obrigatório\. No cenário infoEntid = \[S\] e o campo nrInscPrevComp estiver sem preenchimento, exibir a mensagem: “O campo nrInscPrevComp deve ser preenchido, quando infoEntid = \[S\]”
- Não pode ser repetido o campo nrInscPrevComp para um mesmo indicativo do tipo de dedução \(indTpDeducao\)\. Se para um mesmo tipo de dedução existir números de inscrições repetidos, exibir a mensagem: Esta nrInscPrevComp já foi indicada para este indicador de tipo de dedução\.

vlrPatrocFunp

Recuperar o campo 79 \- Valor Contribuição do ente público patrocinador da SAFX53, quando o campo indTpDeducao = 4

__benefPen – __Dependentes e beneficiários da pensão alimentícia

Este registro será gerado quando existir informações na SAFX536 \- Informações de Dependentes e Beneficiários da Pensão Alimentícia \(Evento R\-4010\);__\[Alteração MFS\-529150\] – __Apenas quando indTpDeducao = 5 ou 7 \(tag detDed\);

__\[Alteração MFS\-529150\] \- Atenção:__ Se indTpDeducao = 5 ou 7, recuperar as informações dos dependentes e beneficiários de pensão alimentícia \(SAFX536\), apenas uma vez\. Mesmo existindo as duas deduções no rendimento\.

__Orientações de como preencher essas informações na base:__

Caso no mesmo pagamento existir indTpDeducao = 5 e 7 \(tag detDed\), o total do grupo de beneficiários deve ser igual ao valor indicado no campo vlrDeducao, referente ao campo 30 \- Valor de Pensão Alimentícia \(tag infoPgto\)\. Caso só exista a dedução indTpDeducao =  7 \(tag detDed\), e existir dados nesta tag, o total do grupo de beneficiários deve ser igual ao valor indicado no campo vlrDeducao, referente ao campo 42 \- Valor da Dedução de Dependentes Terceiros \(tag infoPgto\)

__\[ALTERAÇÃO MFS\-543053\]__ Caso exista mais de um registro na SAFX53 para o mesmo beneficiário, data de movimento/fato gerador e natureza de rendimento, as informações de beneficiário, deverão ser consolidadas, gerando um único registro para esta data e beneficiário\.

A consolidação das informações será feita pelos campos chaves do evento\. 

Poderão existir 99 registros de dependentes e beneficiários de pensão alimentícia \(__benefPen\)\. __Para cada registro recuperado,__ __será gerado um registro com as informações descritas abaixo: 

cpfDep

Campo 12 \- CPF do Dependente da SAFX536

Validação:

\*\*Este CPF deve ter sido informado no registro ideDep/cpfDep

\(\*\*Esta validação ocorre na importação da SAFX536 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Controle de Tributos\)

vlrDepen

Campo 13 \- Valor da dedução relativa a dependentes ou a pensão alimentícia da SAFX536

__ALTERAÇÃO MFS\-535745\]__ Validação:

\*\*Quando informado o valor deve ser maior que zero

\(\*\*Esta validação ocorre na importação da SAFX536 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Controle de Tributos\)

__rendIsento – __Rendimentos isentos ou não tributáveis

__\[ALTERAÇÃO MFS\-532760\]__ Considerando o cenário de mais de um beneficiário na base com o mesmo CPF e se existir registros de rendimentos isentos ou não tributáveis para mais de um beneficiário com tpIsencao = ‘6 \- Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço e a dtLaudo destes cadastros estiverem diferentes entre si, não consolidaremos as informações\. Serão exibidas N ocorrências de rendimentos nesta tag \(para este cenário\)\. Só consolidaremos as informações se as datas forem iguais\. 

__\[ALTERAÇÃO MFS\-543053\]__ Caso exista mais de um registro na SAFX53 para o mesmo beneficiário, data de movimento/fato gerador e natureza de rendimento, as informações de rendimento isento, deverão ser consolidadas, gerando um único registro para esta data e tipo de isenção\.

A consolidação das informações será feita pelos campos chaves do evento\. 

tpIsencao

Valores válidos: 1, 2, 3, 4, 5, 6, 7, 8, 10,11, 99\.

Tipo de Isenção: 

1 \- Parcela isenta 65 anos; 

2 \- Diária de viagem; 

3 \- Indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho; 

4 \- Abono pecuniário; 

5 \- Valores pagos a titular ou sócio de microempresa ou empresa de pequeno porte, exceto pró\-labore, alugueis e serviços prestados; 

6 \- Pensão, aposentadoria ou reforma por moléstia grave ou acidente em serviço; 

7 \- Complementação de aposentadoria, correspondente às contribuições efetuadas no período de 01/01/1989 a 31/12/1995; 

8 \- Ajuda de custo; 

\[EXCLUSÃO MFS\-549365\] 9 \- Rendimentos pagos sem retenção do IR na fonte \- Lei 10\.833/2003; 

\[INCLUSÃO MFS\-549365\] – 10 \- Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função;

\[INCLUSÃO MFS\-549365\] – 11\- Resgate de previdência complementar por portador de moléstia grave;

99 \- Outros \(especificar\)\.

Aplicar as regras abaixo:

Se campo 33 \- Valor de Aposentadoria Isento > 0 e campo 65 – tipo de isenção <> "11", \(ambos da SAFX53\), gravar “1”\.

Se campo 34 \- Valor de Ajuda de Custo > 0 e campo 65 – tipo de isenção = “20”, \(ambos da SAFX53\) , gravar “2”\.

Se campo 37 \- Valor Pago a Titulares ou Sócios > 0, \(da SAFX53\), gravar “5”

Se campo 35 \- Valor de Pensão por Invalidez > 0, \(da SAFX53\), gravar “6”

Se campo 33 \- Valor de Aposentadoria Isento> 0 e campo 65 – tipo de isenção = "11", \(ambos da SAFX53\), gravar “7”\.

Se campo 34 \- Valor de Ajuda de Custo > 0 e campo 65 – tipo de isenção = “21”, \(ambos da SAFX53\) , gravar “8”\.

__\[EXCLUSÃO MFS\-549365\]__ Se campo 102 \- Valor Rendimentos Pagos sem Retenção do IR – Lei 10\.833/2003 > 0 e campo 65 – tipo de isenção IND\_TIPO\_ISENCAO = “12”, \(ambos da SAFX53\), gravar “9”\.

__\[INCLUSÃO MFS\-549365\]__ Se campo 100 – Juros de Mora Recebidos > 0 e campo 65 – tipo de isenção = “14”, \(ambos da SAFX53\) , gravar “10”\.

__\[INCLUSÃO MFS\-549365\]__ Se campo 101 \- Valor de Resgate de Previdência Complementar > 0 e campo 65 – tipo de isenção = “15”, \(ambos da SAFX53\) , gravar “11”\.

Se campo 38 \- Valor Outros para DIRF > 0, \(da SAFX53\), gravar “99”\.

Atualmente, para o layout do REINF não estamos atendendo os tipos de isenção 03\-Indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho e 04\- Abono pecuniário \(não há campos que consideram esses valores na nossa tabela\)

Obs\. Não estão sendo considerados no REINF \(layout 2\.1\.2\) as opções de tipo de isenção ‘02 \-  Diária e Ajuda de Custo’, ‘06\- Lucros e dividendos pagos a partir de 1996’, ‘09\-Benefícios indiretos e/ou reembolso de despesas recebidas por voluntário da copa do mundo ou da copa das confederações’ , ‘10\-Bolsa de estudo recebida por médico\-residente’, 12 – Rendimentos pagos sem retenção do IR na fonte – Lei 10\.833/2003 e 13\- Auxílio moradia  \(da SAFX53\), pois eles não são aceitos no layout do REINF\.__\[Alteração BUG\-539450\]__ Inclusão de validação:Neste caso, se o registro recuperado tiver preenchido com alguma dessas opções, exibir a mensagem: “No layout do REINF não estão sendo consideradas os tipos de isenção:  'Diária e Ajuda de Custo’, 'Lucros e dividendos pagos a partir de 1996’, ‘Benefícios indiretos e/ou reembolso de despesas recebidas por voluntário da copa do mundo ou da copa das confederações’, ‘Bolsa de estudo recebida por médico\-residente’, Rendimentos pagos sem retenção do IR na fonte – Lei 10\.833/2003 e Auxílio moradia  \(campo Tipo de Isenção da SAFX53\) ”

vlrIsento

Somatória dos campos da SAFX53: 

Campo 33 \- Valor de Aposentadoria Isento, quando campo 65 – tipo de isenção = "01" e "11"

Campo 38 \- Valor Outros para DIRF, quando campo 65 – tipo de isenção = "05"

Campo 37 \- Valor Pago a Titulares ou Sócios, quando campo 65 – tipo de isenção = “07”

Campo 35 \- Valor de Pensão por Invalidez, quando campo 65 – tipo de isenção = “08”

__\[EXCLUSÃO MFS\-549365\]__ Campo 102 \- Valor Rendimentos Pagos sem Retenção do IR – Lei 10\.833/2003, quando campo 65 – tipo de isenção = “12”

Campo 34 \- Valor de Ajuda de Custo, quando campo 65 – tipo de isenção = “21”

Campo 34 \- Valor de Ajuda de Custo, quando campo 65 – tipo de isenção = “20”

__\[INCLUSÃO MFS\-549365\]__ Campo 100 – Juros de Mora Recebidos, quando campo 65 – tipo de isenção = “14”

__\[INCLUSÃO MFS\-549365\]__ Campo 101 \- Valor de Resgate de Previdência Complementar quando campo 65 – tipo de isenção = “15”

Validações: 

__\[Exclusão BUG\-539450\]__ Exclusão de validação:

 Se tipos de isenção 1 \- Parcela isenta 65 anos, o valor deve ser maior que zero__: __

- O valor deste campo \(vlrIsento\) for zero, exibir a mensagem: “Campo vlrIsento deve ser maior que zero 

Não pode ser maior que \{vlrRendBruto\}\.

- O valor deste campo \(vlrIsento\), não pode ser maior que o valor indicado no campo vlrRendBruto\. Caso o valor de rendimento bruto for maior, exibir a mensagem: “O campo vlrIsento, não pode ser maior que o campo vlrRendBruto\.”

descRendimento

Recuperar a informação do Campo 39 \- Descrição do Valor Outros para DIRF da SAFX53, quando campo tpIsencao = 99

Validações: 

Quando existir informação, a descrição:

a\) Deve conter ao menos 5 caracteres alfabéticos; 

b\) Não é permitida a repetição consecutiva de caracteres especiais

- Se o tpIsencao = 99 e o campo não for preenchido, ou se preenchido e não respeitar as regras a e b, exibir a mensagem: “Campo de preenchimento obrigatório\. No formato deve conter 5 caracteres alfabéticos e não pode existir repetição consecutiva de caracteres especiais”

dtLaudo

Recuperar a informação do Campo 52\- Data da Atribuição da Moléstia Grave da SAFX04, quando o campo tpIsencao = ’6’

Validações: 

- Se o campo tpIsencao = ‘6’ e o campo dtLaudo não for preenchido, exibir a mensagem “O campo dtLaudo deve ser informado\.”

Data e Ano

- Quando a data for informada, o ano deve ser maior que 1900 e menor que o período de apuração do arquivo \(perApur\)\. Caso contrário exibir a mensagem: “A dtLaudo deve conter ano maior que 1900 e ser menor que o período de apuração do arquivo”

__Registro __<a id="_Hlk524440900"></a><a id="_Hlk524441786"></a>__infoProcRet__ \- Informações de processos relacionados a não retenção de tributos ou a depósitos judiciais\.

Este registro será gerado quando existir informações na SAFX531\- Rendimentos de Decisão Judicial, Quando campo Tipo de Rendimento = 3\- Não Retenção de Tributos ou Depósitos Judiciais\.

Poderão existir 50 registros de processos \(__infoProcRet\)\. __Para cada registro recuperado,__ __será gerado um registro com as informações descritas abaixo: 

TpProcRet

Campo 13 \- Tipo do Processo \(SAFX531\)\. Este campo deve estar previamente cadastrado na SAFX2058, Campo 01 Tipo do Processo \(SAFX2058\)

Opções Válidas:

1 \- Administrativo;

2 \- Judicial\. 

Valores válidos: 1, 2

nrProcRet

Campo 14 \- Número do Processo \(SAFX531\)\. Este campo deve estar previamente cadastrado na SAFX2058, Campo 02 Número do Processo \(SAFX2058\)

codSusp

Campo 15 \- Código do Indicativo da Suspensão de Exigibilidade de Tributos \(SAFX531\)\. Este campo deve estar previamente cadastrado na SAFX2059, Campo 05 \- Indicador da Suspensão de Exigibilidade de Tributos \(SAFX2059\) 

vlrNRetido

Campo 23 \- Valor da Retenção que Deixou de ser Efetuada \- IR da SAFX531

Validação: 

\*\*Quando o valor for informado,deve ser maior que zero\. \*\*Esta validação ocorre na importação da SAFX531 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Rendimentos de Decisão Judicial”

\*\*Ao preencher este campo, a natureza de rendimento \(registro da taces101\) deve ter IR na coluna tributo\. \*\*Esta validação ocorre na importação da SAFX531 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Rendimentos de Decisão Judicial”

vlrDepJud

Campo 24 \- Valor do Depósito Judicial \- IR da SAFX531	

Validação: 

\*\*Quando o valor for informado,deve ser maior que zero\. \*\*Esta validação ocorre na importação da SAFX531 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Rendimentos de Decisão Judicial”

\*\*Ao preencher este campo, a natureza de rendimento \(registro da taces101\) deve ter IR na coluna tributo\. \*\*Esta validação ocorre na importação da SAFX531 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Rendimentos de Decisão Judicial”

vlrCmpAnoCal

Campo 25 \- Valor da Compensação Referente ao Ano Calendário \- IR da SAFX531

Validação:

 \*\*Quando o valor for informado,deve ser maior que zero\. \*\*Esta validação ocorre na importação da SAFX531 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Rendimentos de Decisão Judicial”

\*\*Ao preencher este campo, a natureza de rendimento \(registro da taces101\) deve ter IR na coluna tributo\. \*\*Esta validação ocorre na importação da SAFX531 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Rendimentos de Decisão Judicial”

vlrCmpAnoAnt

Campo 26 \- Valor da Compensação Referente a Anos Anteriores \- IR da SAFX531

Validação: 

\*\*Quando o valor for informado,deve ser maior que zero\. \*\*Esta validação ocorre na importação da SAFX531 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Rendimentos de Decisão Judicial”

\*\*Ao preencher este campo, a natureza de rendimento \(registro da taces101\) deve ter IR na coluna tributo\. \*\*Esta validação ocorre na importação da SAFX531 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Rendimentos de Decisão Judicial”

vlrRendSusp

Campo 27 \- Valor do Rendimento Com Exigibilidade Suspensa \- IR da SAFX531

Validação: 

\*\*Quando o valor for informado,deve ser maior que zero\. \*\*Esta validação ocorre na importação da SAFX531 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Rendimentos de Decisão Judicial”

\*\*Ao preencher este campo, a natureza de rendimento \(registro da taces101\) deve ter IR na coluna tributo\. \*\*Esta validação ocorre na importação da SAFX531 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Rendimentos de Decisão Judicial”

__dedSusp – __Detalhamento das deduções suspensas

indTpDeducao

Campo 17 \- Indicador do tipo de dedução da SAFX534

Opções Válidas:

__\[ALTERAÇÃO__ __ MFS\-566870\]__ Inclusão da opção 8

Valores Válidos: 1, 2, 3, 4, 5, 7,8\.

vlrDedSusp

Campo 18 \- Valor da Dedução da Base de Cálculo do IR com Exigibilidade Suspensa da SAFX534

Validação

Se o campo indTpDeducao = \[5, 7\], e o grupo \{benefPen\} vinculado for informado, o valor informado neste campo deve ser a soma do campo vlrDepenSusp do grupo \{benefPen\}\. Caso a soma não seja igual ao somatório do campo vlrDepenSusp do grupo \{benefPen\}, exibir a mensagem “O vlrDedSusp, deve ser a soma do campo vlrDepenSusp do grupo \{benefPen\}”

__benefPen – __Deduções suspendas por dependentes e beneficiários da pensão alimentícia

Este registro será gerado quando existir informações na SAFX535 – Informação das deduções suspensas por dependentes e beneficiários da pensão   
alimentícia \(Evento R\-4010\)\. __\[Alteração MFS\-529150\] – __Apenas quando indTpDeducao = 5 ou 7 \(tag detDed\);

Poderão existir 99 registros de dependentes e beneficiários de pensão alimentícia \(__benefPen\)\. __Para cada registro recuperado,__ __será gerado um registro com as informações descritas abaixo: 

cpfDep

Campo 17 \- CPF do Dependente da SAFX535

Validação:

\*\*Este CPF deve ter sido informado no registro ideDep/cpfDep

\(\*\*Esta validação ocorre na importação da SAFX535 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Controle de Tributos\)

vlrDepenSusp

Campo 18 \- Valor da dedução suspensa relativa a dependentes ou a pensão alimentícia da SAFX535

__infoRRA – __Informações complementares – RRA

Este registro será gerado quando existir informações na SAFX531\- Rendimentos de Decisão Judicial, Quando campo Tipo de Rendimento = Rendimento Recebido Acumuladamente

__\[ALTERAÇÃO__ __MFS\-543053\] __Caso seja recuperado mais de um registro \(para o mesmo beneficiário, data e natureza de rendimento\) e existir informações diferentes entre os registros, considerar a informação do primeiro registro recuperado

tpProcRRA

Valores Válidos: 1, 2, 3

Campo 13 \- Tipo do Processo da SAFX531\. Este campo deve estar previamente cadastrado na SAFX2058, Campo 01 Tipo do Processo \(SAFX2058\), quando tpProcRRA for 1 ou 2\.

nrProcRRA

Campo 14 \- Número do processo da SAFX531

Validação: Informação obrigatória se \{tpProcRRA\} = \[2\]\.

- Se o campo tpProcRRA = 2 e este campo não estiver preenchido, exibir a mensagem: “Campo nrProcRRA deve ser informado\.”
- O número do processo, não pode conter caracter especial, precisa ter números e a quantidade de números precisa ser superior a quantidade de letras, caso contrário exibir a mensagem de aviso: “Campo nrProcRRA não pode conter caracteres especiais, deve conter números e a quantidade de números deve ser superior a quantidade de letras” 

indOrigRec

Campo 20 \- Indicador da origem dos recursos da SAFX531

Valores Válidos: 1,2

Validações: 

- Caso o campo esteja sem preenchimento, exibir a mensagem no log: “ Campo indOrigRec deve ser informado com “1” ou “2”\.
- Caso o campo esteja preenchido com informação diferente de “1” e o tipo do processo \(tpProcRRA\) for igual a “1” ou “3”, exibir a mensagem: “Quando o tpProcRRA for igual a ‘1’ ou ‘3’, o campo indOrigRec, deve ser preenchido com ‘1’\.”
- Se o campo natureza de rendimento \(natRend\) for preenchido com ‘11002’, o campo indOrigRec, deve ser preenchido com ‘2’, caso contrário, exibir a mensagem: “Quando natRend for igual a ‘11002’, o campo indOrigRec, deve ser preenchido com ‘2’\.”

descRRA

Campo 22 \- Descrição do Processo Judiciário da SAFX531

qtdMesesRRA

Campo 19 \- Quantidade de meses da SAFX531\. Formato do campo: 999,9 

\[Exclusão __MFS\-566870__\] – Exclusão de Validação

Validação: Se o campo for maior que zero, campo vlrRendTrib \{Registro infoPgto\} deve ser maior que zero\.

- Caso este campo seja maior que zero e vlrRendTrib não for informado, exibir a mensagem: “Quando qtdMesesRRA for maior que zero, campo vlrRendTrib \{Registro infoPgto\} deve ser maior que zero\.”

cnpjOrigRecurso

Recuperar a informação do Campo 21 \- CNPJ da empresa de origem dos recursos da SAFX531, quando o campo indOrigRec = 2\.

Validação: 

- Se o campo indOrigRec\} = \[2\] e este campo não estiver preenchido, exibir a mensagem “Campo cnpjOrigRecurso de preenchimento obrigatório”\.

__despProcJud – __Despesas com processo judicial

__\[ALTERAÇÃO__ __MFS\-543053\] __Caso seja recuperado mais de um registro \(para o mesmo beneficiário, data e natureza de rendimento\) e existir informações diferentes entre os registros, considerar a informação do primeiro registro recuperado

vlrDespCustas

Campo 16 \- Despesa com Custas Judiciais da SAFX531

vlrDespAdvogados

Campo 17 \- Despesa com Advogado\(s\) da SAFX531

__ideAdv –__ Identificação do advogado

Poderão existir 99 registros\.

tpInscAdv

Valores Válidos: 1, 2 

Preencher conforme regra:

   
Se campo 16 \- CNPJ/CPF do Advogado da SAFX532 possuir 11 posições, gravar '2', se possuir 14, gravar '1'

nrInscAdv

Campo 16 \- CNPJ/CPF do Advogado da SAFX532

vlrAdv

Campo 17 \- Despesa com o Advogado da SAFX532

__infoProcJud – __Informações de processo judicial

Este registro será gerado quando existir informações na SAFX531\- Rendimentos de Decisão Judicial, Quando campo Tipo de Rendimento = 2 – Demais Rendimentos de Decisão Judicial\. Informação específica REINF\.

__\[ALTERAÇÃO__ __MFS\-543053\] __Caso seja recuperado mais de um registro \(para o mesmo beneficiário, data e natureza de rendimento\) e existir informações diferentes entre os registros, considerar a informação do primeiro registro recuperado

nrProc

Campo 14 \- Número do processo da SAFX531

Validação:

O número do processo, não pode conter caracter especial, precisa ter números e a quantidade de números precisa ser superior a quantidade de letras, caso contrário exibir a mensagem de aviso: “Campo nrProc não pode conter caracteres especiais, deve conter números e a quantidade de números deve ser superior a quantidade de letras”

indOrigRec

Campo 20 \- Indicador da origem dos recursos da SAFX531

Valores Válidos: 1,2

Validações: 

- Caso o campo esteja sem preenchimento, exibir a mensagem no log: “ Campo indOrigRec deve ser informado com “1” ou “2”\.
- Se o campo natureza de rendimento \(natRend\) for preenchido com ‘11002’, o campo indOrigRec, deve ser preenchido com ‘2’, caso contrário, exibir a mensagem: “Quando natRend for igual a ‘11002’, o campo indOrigRec, deve ser preenchido com ‘2’\.”

cnpjOrigRecurso

Recuperar o campo 21 \- CNPJ da empresa de origem dos recursos da SAFX531, quando o campo indOrigRec = 2\.

Validação: Se indOrigRec = 2 e o campo não estiver preenchido, exibir a mensagem: “Campo cnpjOrigRecurso deve ser informado\.”

desc

Campo 22 \- Descrição do Processo Judiciário da SAFX531

__despProcJud – __Despesas com processo judicial

__\[ALTERAÇÃO__ __MFS\-543053\] __Caso seja recuperado mais de um registro \(para o mesmo beneficiário, data e natureza de rendimento\) e existir informações diferentes entre os registros, considerar a informação do primeiro registro recuperado

vlrDespCustas

Campo 16 \- Despesa com Custas Judiciais da SAFX531

vlrDespAdvogados

Campo 17 \- Despesa com Advogado\(s\) da SAFX531

__ideAdv –__ Identificação do advogado

Poderão existir 99 registros\.

tpInscAdv

Valores Válidos: 1,2

Preencher conforme regra:

   
Se campo 16 \- CNPJ/CPF do Advogado da SAFX532 possuir 11 posições, gravar '2', se possuir 14, gravar '1'

nrInscAdv

Campo 16 \- CNPJ/CPF do Advogado da SAFX532

Validação:

- Não pode ser igual ao número de inscrição do declarante ou de outras pessoas jurídicas/físicas informadas neste arquivo \(FCI, SCP entidade de previdência complementar, operador de plano de saúde ou prestador de serviço de saúde\)\. Caso a informação seja igual, exibir a mensagem: “A informação do campo nrInscAdv deve ser exclusiva, não pode ser igual ao número de inscrição de qualquer pessoa jurídica informada neste arquivo ”

vlrAdv

Campo 17 \- Despesa com o Advogado da SAFX532

__infoPgtoExt – __Informações complementares relativas a pagamentos do Exterior

Essa tag será gerada quando o beneficiário da SAFX53 for do exterior \(UF = EX e PAÍS diferente de ‘105’\) e o campo 26\-IND\_CLASSE\_PFJ da safx04 estiver preenchido com informação ‘01\-Pessoa Física’

indNIF

Valores Válidos: 1,2,3

Considerando o beneficiário \(da SAFX53\), recuperar o campo 59 \- Indicador do Nº de Identificação Fiscal da SAFX04

Validação: Se o beneficiário for do exterior, o campo 26\-IND\_CLASSE\_PFJ da safx04 estiver preenchido com informação ‘01\-Pessoa Física’ e o campo 59 \- Indicador do Nº de Identificação Fiscal da SAFX04, estiver sem preenchimento, exibir a mensagem no log: “Quando o beneficiário for do exterior, o campo Indicador do Nº de Identificação Fiscal da tabela Arquivo de Cadastro de Pessoas Físicas/Jurídicas deve estar preenchido”

nifBenef

Considerando o beneficiário \(da SAFX53\), recuperar o campo Campo 53\- Número de Identificação Fiscal da SAFX04

Validação:

__\[ALTERAÇÂO MFS\-699550\]__ Inclusão da exclusividade

Campo de preenchimento obrigatório e exclusivo, quando indNIF = 1\. Se o indNIF = 1 e o campo não for preenchido ou se preenchido e o indNIF diferente de ‘1’, exibir a mensagem: “O campo nifBenef deve ser informado apenas quando indNIF=1\.”

frmTribut

Campo 50 \- Forma Tributação da SAFX53

__\[ALTERAÇÃO MFS\-535745\] __Inclusão de__ __Validação: 

Se o campo não estiver preenchido, exibir a mensagem no log: “O campo frmTribut é de preenchimento obrigatório, favor preencher o campo ‘Forma Tributação’ na tela de Controle de Tributos \(Básicos/Data Warehouse/ Manutenção/Retenções/ Controle de Tributos\)”

__\[ALTERAÇÂO MFS\-699550\]__ Inclusão de validações com relação ao código x vlrIR

- Se for informado um código entre 10 a 30, deve existir informação relativa ao IR \(vlrIR\), caso não exista, exibir a mensagem: “Para os códigos \[10 a 30\], deve existir informação relativa ao imposto sobre a renda retido na fonte \{vlrIR\}”
- Se for informado um código entre 40 a 50, não é permitida a informação relativa ao IR \(vlrIR\), caso a condição não seja aceita, exibir a mensagem: “Para os códigos \[40 a 50\], não é permitida a informação relativa ao imposto sobre a renda retido na fonte \{vlrIR\}”

__endExt – __Endereço do beneficiário residente ou domiciliado no exterior

dscLograd

Considerando o beneficiário \(da SAFX53\), recuperar o campo 12 \- Endereço da SAFX04

nrLograd

Considerando o beneficiário \(da SAFX53\), recuperar o campo 13 \- Número do Endereço da SAFX04

complem

Considerando o beneficiário \(da SAFX53\), recuperar o campo 14 \- Complemento do Endereço da SAFX04

__\[ALTERAÇÃO Bug – 572300\] __Inclusão de tratamento:

Truncar em 30 posições, caso no cadastro da SAFX04 o campo 14 \- Complemento do Endereço, possua mais que 30 posições\.

bairro

Considerando o beneficiário \(da SAFX53\), recuperar o campo 15\- Bairro da SAFX04

cidade

Considerando o beneficiário \(da SAFX53\), recuperar o campo 16 \- Município da SAFX04

estado

Considerando o beneficiário \(da SAFX53\), recuperar o campo 55 \- Província Estrangeira da SAFX04

codPostal

Considerando o beneficiário \(da SAFX53\), recuperar o campo 20 \- CEP da SAFX04 

telef

__ALTERAÇÃO MFS\-535745\]__ Considerando o beneficiário \(da SAFX53\), recuperar os campos 22\-DDD e 23 \- Telefone da SAFX04 \(apenas caracteres numéricos\) e completar com zeros a esquerda até atingir 15 posições\.

Formato: 999999999999999

Este formato não está no manual, mas, foi definida nas reuniões com o FISCO na validação do REINF \(família 4000\)\. 

__ideOpSaude – __Identificação da operadora do plano privado coletivo empresarial de assistência à saúde

nrInsc

Campo 04 \- Número do CNPJ da Operadora da SAFX276

regANS

Campo Registro na Agência Nacional de Saúde – ANS da DWT\_OPERADORA\_SAUDE

vlrSaude

Campo 09 \- Valor de Dedução do Rendimento Tributável da SAFX276 

Validação: Ser for zero, deve haver informações em registro\(s\) filho\(s\), relativas a dependentes \(infoDependPl\) ou reembolso \(\{infoReemb/vlrReemb\} ou \{infoReemb/vlrReembAnt\}\)\.Caso o campo seja zero e não tenha informações em registro\(s\) filho\(s\), relativas a dependentes \(infoDependPl\) ou reembolso \(\{infoReemb/vlrReemb\} ou \{infoReemb/vlrReembAnt\}\), exibir a mensagem: “Quando o campo vlrSaude for igual a zero, deve existir informações nos registro\(s\) filho\(s\), relativas a dependentes \(infoDependPl\) ou reembolso \(\{infoReemb/vlrReemb\} ou \{infoReemb/vlrReembAnt\}\)\. “

__infoReemb  \- __Informações de reembolso do titular do plano de saúde coletivo empresarial

tpInsc

Valores Válidos: 1, 2 

Campo 07 \- Tipo de Inscrição do Prestador de Serviço da SAFX276

nrInsc

Campo 08 \- Número de Inscrição do Prestador de Serviço da SAFX276

vlrReemb

Campo 10\- Valor do Reembolso do período da SAFX276

Validação: Informação não obrigatória se \{vlrReembAnt\} for maior que zero\.

Se o campo vlrReembAnt não for maior que zero, este campo é de preenchimento obrigatório\. Caso este campo não seja informado e o campo vlrReembAnt não for maior que zero, exibir a mensagem: “O campo vlrReemb deve ser informado\.”

vlrReembAnt

Campo 11\- Valor do Reembolso de anos anteriores da SAFX276

Validação: Informação não obrigatória se \{vlrReemb\} for maior que zero\.

Se o campo vlrReemb não for maior que zero, este campo é de preenchimento obrigatório\. Caso este campo não seja informado e o campo vlrReemb não for maior que zero, exibir a mensagem: “O campo vlrReembAnt deve ser informado\.”

__infoDependIPl \- __Informações de dependente do plano de saúde coletivo empresarial

cpfDep

Campo 05 \- CPF do Dependente da SAFX277

Validação:

\*\*Este CPF deve ter sido informado no registro ideDep/cpfDep

\(\*\*Esta validação ocorre na importação da SAFX277 e na tela de manutenção, Básicos >> Data Warehouse >> Manutenção >> Retenções >> Plano de Saúde\)

vlrSaude

Campo 11 \- Valor de Dedução do Rendimento Tributável da SAFX277

Validação: O valor deve ser igual ou maior que zero\. Ser for zero, deve haver informações de reembolso do dependente \(\{infoReembDep\}\)\. Neste caso, se o valor for zero e não existir informações de reembolso do dependente, exibir a mensagem: 

“Quando o campo vlrSaude for zero, deve existir informações de reembolso do dependente \(infoReembDep\)\.”

__infoReembDep  \- __Informações de reembolso do dependente do plano de saúde coletivo empresarial

tpInsc

Valores Válidos: 1, 2 

Campo 09 \- Tipo de Inscrição do Prestador de Serviço da SAFX277

nrInsc

Campo 10 \- Número de Inscrição do Prestador de Serviço da SAFX277

vlrReemb

Campo 12 \- Valor do Reembolso do Periodo da SAFX277

Validação: Informação não obrigatória se \{vlrReembAnt\} for maior que zero\.

Se o campo vlrReembAnt não for maior que zero, este campo é de preenchimento obrigatório\. Caso este campo não seja informado e o campo vlrReembAnt não for maior que zero, exibir a mensagem: “O campo vlrReemb deve ser informado\.”

vlrReembAnt

Campo 13 \- Valor do Reembolso de anos anteriores da SAFX277 

Validação: Informação não obrigatória se \{vlrReemb\} for maior que zero\.

Se o campo vlrReemb não for maior que zero, este campo é de preenchimento obrigatório\. Caso este campo não seja informado e o campo vlrReemb não for maior que zero, exibir a mensagem: “O campo vlrReembAnt deve ser informado\.”

  


= = = = = =

 


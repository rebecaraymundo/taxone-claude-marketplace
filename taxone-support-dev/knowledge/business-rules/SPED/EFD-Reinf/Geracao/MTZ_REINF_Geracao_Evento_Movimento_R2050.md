# MTZ_REINF_Geracao_Evento_Movimento_R2050

- **Fonte:** MTZ_REINF_Geracao_Evento_Movimento_R2050.docx
- **Modificado:** 2024-09-11
- **Tamanho:** 106 KB

---

	

THOMSON REUTERS

Geração evento R\-2050 \- REINF

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-9073

Geração Evento

Definição de regras para geração do evento R\-2050 Reinf 

MFS\-12176

Elenilson Coutinho

Regra para tipo de arquivo Original/Retificação

MFS\-12180

Elenilson Coutinho

Regra de geração considerando eventos de fechamento/reabertura

MFS13897

Lara Aline

Alteração no layout conforme versão 1\.2

MFS17138

Lara Aline

Inclusão status “Excluído na Mensageria” no tratamento de Fechamento/Reabertura

MFS17448

Lara Aline

Inclusão de regra de geração para o registro infoProc

MFS17269

Lara Aline

Ajuste nos campos vlrCPSuspTotal, vlrRatSuspTotal e vlrSenarSuspTotal conforme nova versão 1\.3\.02\.

MFS17263

Lara Aline

Ajustes nos campos vlrRecBruta, vlrCPApur, vlrRatApur e vlrSenarApur e vlrRecBrutaTotal para inclusão das deduções da tela Lançamento de Deduções da Comercialização da Produção por Produtor Rural PJ/Agroindústria\. 

MFS18702

Lara Aline

Alteração da Geração Prévia retirando a possibilidade de Geração de Eventos Retificados, eventos retificadores serão gerados apenas no Painel de Controle de Eventos

MFS18769

Lara Aline

Alteração nos campos vlrRecBruta e vlrRecBrutaTotal para recuperar o valor do campo VLR\_TOT\_NOTA da SAFX07

MFS20930

Lara Aline

Ajuste na regra de ocorrência do registro tipoCom, conforme layout 1\.4\.

MFS21078

Lara Aline

Ajuste na regra do campo vlrRecBruta\.

MFS21937

<a id="OLE_LINK10"></a>Vânia Mattos

Ajustes na geração dos campos vlrRecBrutaTotal, vlrCPApur, vlrRatApur, vlrSenarApur e vlrRecBruta, devido à alteração feita na manutenção das deduções do evento R\-2050\. Esta manutenção foi alterada para criação do campo “Tipo de Ajuste” \(Adição/Dedução\), que permitirá lançamentos tanto de dedução, como de adição

MFS20474

Vânia Mattos

Alteração na gravação das notas fiscais na tabela REINF\_PGER\_R2050\_NF

MFS\-30234

Alessandra Cristina Navatta

Geração do evento R\-2050, considerando as informações dos ajustes de adição da tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria” que não possuem notas fiscais relacionadas\. 

__MFS27483__

Vânia Mattos

Alteração na geração do registro infoProc para considerar os ajustes de processos cadastrados na manutenção dos ajustes do R\-2050 \(“Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”\)\. 

MFS\-90001

Alessandra Cristina Navatta

Alteração da referência do arquivo de de\_para \(versão 2\.1\.1\)

__Obs\. O ajuste mapeado nesta demanda, refere\-se a atualização funcional\. Não há impactos na implementação__

MFS\-654436

Denilson André Santos

Este documento, tem o objetivo de readequar as regras das TAG’s a seguir: vlrRecBrutaTotal, vlrCPApur, vlrRatApur e vlrSenarApur\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral de Geração do Evento R\-2050\.__

O evento R\-2050 do SPED \- REINF tem por objetivo gerar informações de Comercialização da Produção por Produtor Rural PJ/Agroindústria\. Ele será gerado com os registros:

 __Reinf__ – EFD \- Reinf

 __evtComProd__ – Evento Comercialização da Produção

 __ideEvento__ – Informações de Identificação do Evento

 __ideContri__ – Informações de Identificação do Contribuinte

 __infoComProd __– Informação da Comercialização de Produção

 __ideEstab __– Registro que identifica o estabelecimento que comercializou a produção

 __tipoCom __– Registro que apresenta o valor total da Receita Bruta por "tipo" de comercialização\.

 __nfs__ \- Detalhamento da receita bruta por NF\. 

__ infoProc __– Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte

Observar orientações existentes no arquivo " TR\_REINF\_DEXPARA\_V2\.1\.1\.xlsx "\. 

- __Origem das informações__: SAFX07, SAFX263, Cadastro do Estabelecimento e tela Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria\. 
- __Regra de seleção__: O Registro R\-2050 é utilizado para demonstrar informações de Comercialização da Produção por Produtor Rural/PJ Agro\-Indústria\. 

Ele será gerado com base em Informações de Notas Fiscais de Mercadoria:

Para obtermos as informações para sua geração, devemos recuperar registros da tabela SAFX07, considerando os seguintes critérios:

\- O COD\_ESTAB seja de um estabelecimento indicado pelo usuário;

\- NFs cujo campo MOVTO\_E\_S seja igual a "9";

\- O campo DATA\_EMISSAO deve compreender o período de geração;

\- O campo SITUACAO deve ser diferente de "S";

\- O campo COD\_CLASS\_DOC\_FIS deve ser igual a "1" ou "3" ou “7”;

\- O campo IND\_TIPO\_AQUIS deve ser igual a "1", "8" ou "9";

__\[MFS\-30234\]__ – Ou ainda, se não for encontrada a nota fiscal \(conforme critérios acima\), mas existir ajustes de adição na tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”, para o estabelecimento e período de geração\.

__\[MFS\-12176\]__

- __Original/Retificação__: Os critérios para identificar se o evento a ser gerado será original ou retificador serão os seguintes:
- Se não houver ocorrência de geração de evento anterior, criar nova ocorrência de arquivo original\.
- Se houver ocorrência de geração anterior com status “Evento Enviado” exibir a seguinte mensagem no log de geração:

              Evento R2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria

              Evento não gerado\. Existe evento anterior enviado aguardando retorno\.

              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração anterior com status “Evento REINF Recebido com Sucesso ou Advertência” verificar se há evento de exclusão, então:

\- Se __não__ existir evento de exclusão então, criar ocorrência de arquivo de retificação\.

\- Se existir, evento de exclusão considerar os status, então:

Evento de exclusão com status de “Evento REINF Enviado” exibir a seguinte mensagem no log de geração:

  

             Evento R2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria

             Evento não gerado\. Existe evento de exclusão anterior enviado aguardando retorno\.

             Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

          Evento de exclusão com status “Evento Recebido com sucesso ou Advertência” então, verificar se há ocorrência

          anterior de evento periódico com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova

          ocorrência de arquivo de retificação, se __não__ houver, criar original\.

              \- Se existir evento de exclusão com status “Evento REINF Recebido com Erro” ou “Cancelado” ou “Erro na Geração do                          XML” então, criar nova ocorrência de retificação\.

             \- Se existir evento de exclusão com status “Aguardando Geração do XML” então exibir a seguinte mensagem no log de      geração:

                

              Evento R2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria

              Evento não gerado\. Existe evento anterior não enviado\.

              Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração anterior com status “Evento REINF Recebido com erro”, então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova ocorrência de arquivo de retificação, se __não__ houver, criar original\.
- Se houver ocorrência de geração anterior com status “Aguardando Geração do XML” ou “Cancelado” ou “Erro na Geração do XML” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova ocorrência de arquivo de retificação, se __não__ houver, criar original\.

__\[MFS18702\]__

__Importante:__ Na tela Geração Prévia dos Movimentos serão gerados APENAS os eventos Originais, os eventos de Retificação deverão ser gerados diretamente pelo Painel de Controle de Eventos pela opção ‘Reprocessar Evento’\. Caso os eventos encontrados na tela de Geração Prévia dos Movimentos sejam identificados nos critérios acima como Retificação esses deverão ser desconsiderados e não gerados, pela tela de Geração Prévia dos Movimentos serão gerados apenas os eventos que se enquadrarem como ‘Original’\.

__\[MFS\-12180\]            __

- __Fechamento/Reabertura:__ Critérios de geração do evento considerando a situação do período\.
- Se não houver ocorrência de geração de evento de fechamento, prosseguir com a geração\.
- Se houver ocorrência de geração de evento de fechamento considerar os status então:

                      \- Evento de fechamento com status de “Evento Reinf Enviado” exibir a seguinte mensagem no log de geração:

                      

                  R2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria

                  Evento não gerado\. Existe evento de fechamento do período enviado aguardando retorno\.

                  Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

                      \- Evento de fechamento com status de “Evento REINF Recebido com Sucesso ou Advertência” exibir a seguinte

                        mensagem no log de geração:

               

                  R2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria

                  Evento não gerado\. Período Fechado\.

                  Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Se houver ocorrência de geração de evento de reabertura correspondente, com status “Evento REINF Recebido com

Sucesso ou Advertência”, prosseguir com a geração\.

        

       __\[Alterado MFS17138\]__

       \- Evento de fechamento com status de “Evento REINF Recebido com erro” ou “Cancelado” ou “Erro na Geração do 

           XML” ou “Evento Excluído na Mensageria” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, exibir a seguinte mensagem no log de geração:

                   R2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria

                   Evento não gerado\. Período Fechado\.

                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

 

                   Se não houver evento de fechamento com status “Evento REINF Recebido com Sucesso ou Advertência”,

                   prosseguir com a geração\. 

                       \- Evento de Fechamento com status de “Aguardando Geração do XML”, exibir a seguinte mensagem no log de   

                         geração:

                   R2050 – Comercialização da Produção por Produtor Rural PJ/Agroindústria

                   Evento não gerado\. Existe evento de fechamento do período não enviado\.

                   Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- __Gravação das Notas Fiscais__: Todas as notas fiscais recuperadas para compor os valores do evento R\-2050 são gravadas numa tabela \(REINF\_PGER\_R2050\_NF\)\. Esta tabela é utilizada na emissão do relatório de conferência do evento \(formato “Analítico”\), que mostra nota a nota, com seus respectivos valores:

      \- Receita Bruta \(VLR\_TOT\_NOTA, VLR\_PRODUTO ou VLR\_BASE\_INSS da SAFX07, conforme parâmetro de “Dados Iniciais”\); 

      \- Contribuição Previdenciária \(VLR\_CONTRIB\_PREV da SAFX07\);

      \- GILRAT \(VLR\_GILRAT da SAFX07\);

      \- SENAR \(VLR\_CONTRIB\_SENAR da SAFX07\);

__       \[MFS20474\]: __Além do valor da receita bruta, passaram a ser armazenados também os valore da Contribuição Previdenciária, 

       GILRAT e SENAR, para cada nota fiscal\. O objetivo da alteração é o relatório de conferência analítico, que passou a exibir 

       também estes outros valores\.  

__\[MFS\-30234\]:__ Além disso, se existir ajustes de adição na tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”, para o estabelecimento e período de geração e não for encontrada nota fiscal que atenda os critérios indicados no início desta regra, as informações devem ser gravadas na tabela \(REINF\_PGER\_R2050\_NF\)\. Para este cenário, gravar nos campos relativos ao documento:  série, número de nota, o texto “AJUSTES”\. Na data de emissão, gravar a data do ultimo dia do mês da geração do evento\.

MFS\-9073

MFS12176

MFS12180

MFS13897

MFS17138

MFS17448

MFS17263

MFS18702

MFS30234

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
- __Nível hierárquico do registro__: filho do registro evtComProd
- __Ordenação__: não se aplica\.
- __Agrupamento__: não se aplica\.
- __Ocorrência__: Um por arquivo

MFS\-9073

RN02

__Campo tpInsc__

Será gerado com conteúdo igual a “1”

MFS9073

RN03

__Campo nrInsc__

Será gerado com as 8 primeiras posições do CNPJ do Estabelecimento\.Com base neste campo podemos entender que o REINF será gerado com base em um estabelecimento Centralizador\. 

MFS9073

- __Registro infoComProd – Informação da Comercialização de Produção__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

- __Registro IdeEstab – Registro que identifica o estabelecimento que comercializou a produção__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN04

- __Origem das informações__: SAFX07, Cadastro do Estabelecimento\.

__                                                   __Ajustes__ __da Comercialização da Produção por Produtor Rural PJ/Agroindústria

- __Regra de seleção__: Este registro servirá identificar identifica o estabelecimento que comercializou a produção
- __Campos\-Chave__: tpInscEstab, nrInscEstab
- __Nível hierárquico do registro__: filho do registro infoComProd\.
- __Ordenação__: Não se aplica\. 
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: para cada infoComProd poderá existir “1” IdeEstab\. 

MFS9073

RN05

__Campo tplnscEstab__

Será gerado com conteúdo igual a “1”

MFS9073

RN06

__Campo nrlnsEstab__

Será gerado com o conteúdo do campo CGC do Cadastro do Estabelecimento da NF\. 

\[MFS\-30234\] Quando não existir a nota, considerar o campo CGC do cadastro do Estabelecimento que está gerando o Evento

MFS9073

MFS30234

RN07

__vlrRecBrutaTotal__

Será o somatório do valor gerado no campo vlrRecBruta, do VLR\_PRODUTO da SAFX07 das NFS detalhadas na tag "tipoCom"\.

\[MFS\-30234\] Quando não existir a nota, considerar o campo VlrRecBrutaTotal do ajuste de adição da tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”\.

__Se__ não existir nota fiscal, __então__

    vlrRecBrutaTotal = Valor total do ajuste de adição – Valor total do ajuste de dedução

__Fim Se__

__Se__ Valor total do ajuste de dedução > Valor total do ajuste de adição, __então__

    vlrRecBrutaTotal = 0,00

    

    Exibir a mensagem: Evento R2050 \- Comercialização da Produção por Produtor Rural PJ/Agroindústria\.

    Valor de Dedução da Receita Bruta, excede o Valor da Receita Bruta do período\. Nesse caso, será gerado o valor 0\.

    Estabelecimento: XXXX / Data Movimento: XX/XXXX / Indicativo de Comercialização: XX

__Fim Se__

MFS9073

MFS17263

MFS30234

__MFS\-654436__

RN08

__vlrCPApur__

Deverá ser verificado o campo ‘Valor da Contribuição Previdenciária’ da tela Lançamento de Deduções da Comercialização da Produção por Produtor Rural PJ/Agroindústria correspondente ao Estabelecimento, período e indCom\. Caso encontrar valor preenchido no campo ‘Valor da Contribuição Previdenciária’ esse valor deverá ser deduzido do campo VLR\_CONTRIB\_PREV da SAFX07 da NF para compor o campo vlrCPApur, Caso contrário, o campo vlrCPApur será gerado a informação do campo VLR\_CONTRIB\_PREV da SAFX07 da NF\.

Alteração MFS21937: A manutenção dos lançamentos de dedução do evento R\-2050 foi alterada para a criação do campo “*Tipo de Ajuste*” \(1=Adição/2=Dedução\), para permitir o lançamento de valores tanto de dedução como de adição\. Com esta alteração, o campo vlrCPApur passou a ser gerado conforme regra a seguir: 

Totalização do campo VLR\_CONTRIB\_PREV das notas fiscais da SAFX07 \(conforme RN00\), 

__\(\+\) __Ajustes de Adição

__\(\-\) __Ajustes de Dedução

Os ajustes são cadastrados no menu “*Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria*”, e para cada 

Empresa, Estabelecimento, Período e Indicativo de Comercialização, poderão existir até dois ajustes, um de adição, e outro de dedução\.

\- Se existir ajuste com o Tipo de Ajuste = “1” \(Adição\):

      O conteúdo do campo “Contribuição Previdenciária”, quando preenchido, será somado ao total apurado nas notas;

\- Se existir ajuste com o Tipo de Ajuste = “2” \(Dedução\):

      O conteúdo do campo “Contribuição Previdenciária”, quando preenchido, será deduzido do total apurado nas notas;

 

Obs\.: Caso o valor de dedução da Contribuição Previdenciária informado seja maior que o valor do campo VLR\_CONTRIB\_PREV da SAFX07 será gravado o valor 0\-zero e apresentado a seguinte mensagem no log de pré\-geração:

Evento R2050 \- Comercialização da Produção por Produtor Rural PJ/Agroindústria

Valor de Dedução Contribuição Previdenciária excede o Valor da Contribuição Previdenciária do período\. Nesse caso será gerado o valor 0 \- zero\.

Estabelecimento: XXXX / Data Movimento: XX/XXXX 

/ Indicativo de Comercialização: XX

Alteração __\[MFS30234\]: __Se houver ajuste de adição e nenhuma nota fiscal for identificada, considerar o conteúdo do valor do campo “Contribuição Previdenciária” da tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”\.

__Se__ não existir nota fiscal, __então__

    vlrCPApur = Valor total do ajuste de adição – Valor total do ajuste de dedução

__Fim Se__

__Se__ Valor total do ajuste de dedução > Valor total do ajuste de adição, __então__

    vlrCPApur = 0,00

    

    Exibir a mensagem: Evento R2050 \- Comercialização da Produção por Produtor Rural PJ/Agroindústria\.

    Valor de Dedução Contribuição Previdenciária, excede o Valor da Contribuição Previdenciária do período\. Nesse caso, será gerado o valor 0

    Estabelecimento: XXXX / Data Movimento: XX/XXXX / Indicativo de Comercialização: XX

__Fim Se__

MFS9073

MFS17263

MFS21937

MFS30234

__MFS\-654436__

RN09

__vlrRatApur__

Deverá ser verificado o campo ‘Valor do GILRAT’ da tela Lançamento de Deduções da Comercialização da Produção por Produtor Rural PJ/Agroindústria correspondente ao Estabelecimento, período e indCom\. Caso encontrar valor preenchido no campo ‘Valor do GILRAT’ esse valor deverá ser deduzido do campo VLR\_GILRAT da SAFX07 da NF para compor o campo vlrRatApur, Caso contrário, o campo vlrRatApur será gerado a informação do campo VLR\_GILRAT da SAFX07 da NF\.

Alteração __MFS21937__: A manutenção dos lançamentos de dedução do evento R\-2050 foi alterada para a criação do campo “*Tipo de Ajuste*” \(1=Adição/2=Dedução\), para permitir o lançamento de valores tanto de dedução como de adição\. Com esta alteração, o campo vlrRatApur passou a ser gerado conforme regra a seguir: 

Totalização do campo VLR\_GILRAT das notas fiscais da SAFX07 \(conforme RN00\), 

__\(\+\) __Ajustes de Adição

__\(\-\) __Ajustes de Dedução

Os ajustes são cadastrados no menu “*Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria*”, e para cada 

Empresa, Estabelecimento, Período e Indicativo de Comercialização, poderão existir até dois ajustes, um de adição, e outro de dedução\.

\- Se existir ajuste com o Tipo de Ajuste = “1” \(Adição\):

      O conteúdo do campo “Valor do GILRAT”, quando preenchido, será somado ao total apurado nas notas;

\- Se existir ajuste com o Tipo de Ajuste = “2” \(Dedução\):

      O conteúdo do campo “Valor do GILRAT”, quando preenchido, será deduzido do total apurado nas notas;

Obs\.: Caso o valor de dedução do GILRAT informado seja maior que o valor do campo VLR\_GILRAT da SAFX07 será gravado o valor 0\-zero e apresentado a seguinte mensagem no log de pré\-geração:

Evento R2050 \- Comercialização da Produção por Produtor Rural PJ/Agroindústria

Valor de Dedução do GILRAT excede o Valor do GILRAT do período\. Nesse caso será gerado o valor 0 \- zero\.

Estabelecimento: XXXX / Data Movimento: XX/XXXX 

/ Indicativo de Comercialização: XX

Alteração __\[MFS30234\]: __Se houver ajuste de adição e nenhuma nota fiscal for identificada, considerar o conteúdo do valor do campo “Valor do GILRAT” da tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”\.

__Se__ não existir nota fiscal, __então__

    vlrRatApur = Valor total do ajuste de adição – Valor total do ajuste de dedução

__Fim Se__

__Se__ Valor total do ajuste de dedução > Valor total do ajuste de adição, __então__

    vlrRatApur = 0,00

    

    Exibir a mensagem: Evento R2050 \- Comercialização da Produção por Produtor Rural PJ/Agroindústria\.

    Valor de Dedução do GILRAT, excede o Valor do GILRAT do período\. Nesse caso, será gerado o valor 0

    Estabelecimento: XXXX / Data Movimento: XX/XXXX / Indicativo de Comercialização: XX

__Fim Se__

MFS9073

MFS17263

MFS21937

MFS30234

__MFS\-654436__

RN10

__vlrSenarApur__

Deverá ser verificado o campo ‘Valor do SENAR’ da tela Lançamento de Deduções da Comercialização da Produção por Produtor Rural PJ/Agroindústria correspondente ao Estabelecimento, período e indCom\. Caso encontrar valor preenchido no campo ‘Valor do SENAR’ esse valor deverá ser deduzido do campo VLR\_CONTRIB\_SENAR da SAFX07 da NF para compor o campo vlrSenarApur, Caso contrário, o campo vlrSenarApur será gerado a informação do campo VLR\_CONTRIB\_SENAR da SAFX07 da NF\.

Alteração __MFS21937__: A manutenção dos lançamentos de dedução do evento R\-2050 foi alterada para a criação do campo “*Tipo de Ajuste*” \(1=Adição/2=Dedução\), para permitir o lançamento de valores tanto de dedução como de adição\. Com esta alteração, o campo vlrSenarApur passou a ser gerado conforme regra a seguir: 

Totalização do campo VLR\_CONTRIB\_SENAR das notas fiscais da SAFX07 \(conforme RN00\), 

__\(\+\) __Ajustes de Adição

__\(\-\) __Ajustes de Dedução

Os ajustes são cadastrados no menu “*Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria*”, e para cada 

Empresa, Estabelecimento, Período e Indicativo de Comercialização, poderão existir até dois ajustes, um de adição, e outro de dedução\.

\- Se existir ajuste com o Tipo de Ajuste = “1” \(Adição\):

      O conteúdo do campo “Valor do SENAR”, quando preenchido, será somado ao total apurado nas notas;

\- Se existir ajuste com o Tipo de Ajuste = “2” \(Dedução\):

      O conteúdo do campo “Valor do SENAR”, quando preenchido, será deduzido do total apurado nas notas;

Obs\.: Caso o valor de dedução do SENAR informado seja maior que o valor do campo VLR\_CONTRIB\_SENAR da SAFX07 será gravado o valor 0\-zero e apresentado a seguinte mensagem no log de pré\-geração:

Evento R2050 \- Comercialização da Produção por Produtor Rural PJ/Agroindústria

Valor de Dedução do SENAR excede o Valor do SENAR do período\. Nesse caso será gerado o valor 0 \- zero\.

Estabelecimento: XXXX / Data Movimento: XX/XXXX 

/ Indicativo de Comercialização: XX

Alteração __\[MFS30234\]: __Se houver ajuste de adição e nenhuma nota fiscal for identificada, considerar o conteúdo do valor do campo “Valor do SENAR” da tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”\.

__Se__ não existir nota fiscal, __então__

    vlrSenarApur = Valor total do ajuste de adição – Valor total do ajuste de dedução

__Fim Se__

__Se__ Valor total do ajuste de dedução > Valor total do ajuste de adição, __então__

    vlrSenarApur = 0,00

    

    Exibir a mensagem: Evento R2050 \- Comercialização da Produção por Produtor Rural PJ/Agroindústria\.

    Valor de Dedução do SENAR, excede o Valor do SENAR do período\. Nesse caso, será gerado o valor 0

    Estabelecimento: XXXX / Data Movimento: XX/XXXX / Indicativo de Comercialização: XX

__Fim Se__ 

MFS9073

MFS17263

MFS21937

MFS30234

__MFS\-654436__

RN11

__vlrCPSuspTotal__

Será gerado com a somatória do conteúdo do campo “VLR\_PREV\_EXIG\_SUSP” da SAFX263, com exceção dos valores informados com o Indicador de Suspenção \(ind\_susp\) igual a ‘92’, ou seja, deve ser identificado o indicador de suspensão \(SAFX2059 – Cadastro de Informação de Suspensão de Exigibilidade de Tributos\) através do campo Código de Suspensão informado na SAFX263\.

\[__MFS27483__\] Ao resultado encontrado a partir dos valores da SAFX263, será somado/deduzido o valor dos ajustes de adição/dedução cadastrados na manutenção dos ajustes do R\-2050, no menu “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”, opção “*Processos*” \(ver RN21\)\. 

Conforme o layout da EFD\-REINF, este campo é a totalização do campo vlrCPSusp de todos os registros infoProc gerados, exceto aqueles em que o Código de Suspensão tenha o indicador de suspensão = 92\.

MFS13897

MFS17448

MFS17269

__MFS27483__

RN12

__vlrRatSuspTotal__

Será gerado com a somatória do conteúdo do campo “VLR\_GILRAT\_EXIG\_SUSP” da SAFX263, com exceção dos valores informados com o Indicador de Suspenção \(ind\_susp\) igual a ‘92’, ou seja, deve ser identificado o indicador de suspensão \(SAFX2059 – Cadastro de Informação de Suspensão de Exigibilidade de Tributos\) através do campo Código de Suspensão informado na SAFX263\.

\[__MFS27483__\] Ao resultado encontrado a partir dos valores da SAFX263, será somado/deduzido o valor dos ajustes de adição/dedução cadastrados na manutenção dos ajustes do R\-2050, no menu “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”, opção “*Processos*” \(ver RN21\)\. 

Conforme o layout da EFD\-REINF, este campo é a totalização do campo vlrCPSusp de todos os registros infoProc gerados, exceto aqueles em que o Código de Suspensão tenha o indicador de suspensão = 92\.

MFS13897

MFS17448

MFS17269

__MFS27483__

RN13

__vlrSenarSuspTotal__

Será gerado com a somatória do conteúdo do campo “VLR\_SENAR\_EXIG\_SUSP” da SAFX263, com exceção dos valores informados com o Indicador de Suspenção \(ind\_susp\) igual a ‘92’, ou seja, deve ser identificado o indicador de suspensão \(SAFX2059 – Cadastro de Informação de Suspensão de Exigibilidade de Tributos\) através do campo Código de Suspensão informado na SAFX263\. 

\[__MFS27483__\] Ao resultado encontrado a partir dos valores da SAFX263, será somado/deduzido o valor dos ajustes de adição/dedução cadastrados na manutenção dos ajustes do R\-2050, no menu “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”, opção “*Processos*” \(ver RN21\)\. 

Conforme o layout da EFD\-REINF, este campo é a totalização do campo vlrCPSusp de todos os registros infoProc gerados, exceto aqueles em que o Código de Suspensão tenha o indicador de suspensão = 92\.

MFS13897

MFS17448

MFS17269

__MFS27483__

- __Registro tipoCom – Registro que apresenta o valor total da Receita Bruta por "tipo" de comercialização\.__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN14

__Origem das informações__: SAFX07\. \[MFS30234\] \- Se houver ajuste de adição e nenhuma nota fiscal for identificada, considerar as informações do ajuste da tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”

- __Regra de seleção__: Este registro apresenta o valor total da Receita Bruta por "tipo" de comercialização\.
- __Campos\-Chave__: indCom
- __Nível hierárquico do registro__: filho do registro ideEstab\.
- __Ordenação__: não se aplica\.
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: para cada ideEstab poderá existir “4” tipoCom\.

MFS9073

MFS20930

MFS30234

RN15

__Campo indCom__

Será gerado com o conteúdo do campo “IND\_TIPO\_AQUIS” da SAFX07\.

\[MFS30234\] – Se houver ajuste de adição e nenhuma nota fiscal for identificada, considerar a informação do campo “Indicativo de Comercialização” da tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”

MFS9073

MFS30234

RN16

__Campo vlrRecBruta__

Deverá ser verificado o campo ‘Valor da Receita Bruta’ da tela Lançamento de Deduções da Comercialização da Produção por Produtor Rural PJ/Agroindústria correspondente ao Estabelecimento, período e indCom\. Caso encontrar valor preenchido no campo ‘Valor da Receita Bruta’ esse valor deverá ser deduzido do campo VLR\_PRODUTO VLR\_TOT\_NOTA da SAFX07 para compor o campo vlrRecBruta, Caso contrário, o campo vlrRecBruta será gerado com o conteúdo do campo VLR\_PRODUTO VLR\_TOT\_NOTA da SAFX07\. 

Para compor o valor a ser gravado nesse campo considerar conforme abaixo:

1 – Para correta gravação do campo será necessário verificar qual opção o usuário informou no parâmetro ‘Considerar para composição da Receita Bruta’ nos Dados Iniciais, sendo que:

- Caso selecionado Valor Contábil, recuperar a informação do campo VLR\_TOT\_NOTA da SAFX07;
- Caso selecionado Valor Total, recuperar a informação do campo VLR\_PRODUTO da SAFX07;
- Caso selecionado Base de Cálculo do INSS, recuperar a informação do campo VLR\_BASE\_INSS da SAFX07;

 

2 – Verificar o campo ‘Valor da Receita Bruta’ da tela Lançamento de Deduções Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria correspondente ao Estabelecimento, Período e Indicativo de Comercialização\. 

Alteração MFS21937: A manutenção dos lançamentos de dedução do evento R\-2050 foi alterada para a criação do campo “*Tipo de Ajuste*” \(1=Adição/2=Dedução\), para permitir o lançamento de valores tanto de dedução como de adição\. Com esta alteração, para cada Empresa, Estabelecimento, Período e Indicativo de Comercialização, poderão existir até dois ajustes, um de adição, e outro de dedução\.

- Se existir ajuste com o Tipo de Ajuste = “1” \(Adição\) à o conteúdo do campo “Valor da Receita Bruta”, quando preenchido, será somado ao valor apurado a partir das notas fiscais, conforme indicado acima \(1\);
- Se existir ajuste com o Tipo de Ajuste = “2” \(Dedução\) à o conteúdo do campo “Valor da Receita Bruta”, quando preenchido, será deduzido do valor apurado a partir das notas fiscais, conforme indicado acima \(1\);
- Se não existirem ajustes, o campo ‘Valor da Receita Bruta’, será gravado apenas com o valor apurado a partir das notas fiscais, conforme indicado acima \(1\);

Obs\.: Caso o valor de dedução da Receita Bruta informado seja maior que o valor do campo indicado em ‘Considerar para composição da Receita Bruta’ parametrizado nos Dados Iniciais VLR\_PRODUTO VLR\_TOT\_NOTA da SAFX07 será gravado o valor 0\-zero e apresentado a seguinte mensagem no log de pré\-geração:

Evento R2050 \- Comercialização da Produção por Produtor Rural PJ/Agroindústria

Valor de Dedução da Receita Bruta excede o Valor da Receita Bruta do período\. Nesse caso será gerado o valor 0 \- zero\.

Estabelecimento: XXXX / Data Movimento: XX/XXXX 

/ Indicativo de Comercialização: XX

Alteração __\[MFS30234\]: __Se houver ajuste de adição e nenhuma nota fiscal for identificada, considerar o conteúdo do valor do campo “Valor da Receita Bruta” da tela “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”\. 

MFS9073

MFS17263

MFS18769

MFS21078

MFS21937

RN14

__Campo codAnaCont__

Inicialmente esse campo será gerado como nulo, sem informação\.

MFS9073

MFS13897

- __Registro nfs – Detalhamento da receita bruta por nota fiscal emitida pelo contribuinte\. __

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN15

- __Origem das informações__: SAFX07\.
- __Regra de seleção__: Este registro servirá para demonstrar o Detalhamento da receita bruta por nota fiscal emitida pelo contribuinte\.
- __Campos\-Chave__: serie, numDocto 
- __Nível hierárquico do registro__: filho do registro tipoCom
- __Ordenação__: não se aplica\. 
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: Para cada tipoCom poderá existir “N” nfs\.

MFS9073

MFS13897

RN16

__Campo serie__

Informação será recuperada do campo SERIE\_DOCFIS da SAFX07\. Caso não preenchido gravar “0”\.

MFS9073

MFS13897

RN17

__Campo numDocto__

Informação será recuperada do campo NUM\_DOCFIS da SAFX07\.

MFS9073

MFS13897

RN18

__Campo dtEmissaoNF__

Informação será recuperada do campo DATA\_EMISSAO da SAFX07\.

MFS9073

MFS13897

RN19

__Campo vlrBruto__

Informação será recuperada do campo VLR\_PRODUTO da SAFX07\.

MFS9073

MFS13897

- __Registro__ __infoProc – Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN17

- __Origem das informações__: 

       \- SAFX263: Processos Administrativos/Judiciais \(Botão “R\-2050/S1250” da tela de “Documento Fiscal de Mercadoria”\);

       \- Ajustes da Comercialização \(menu “*Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria*”\);

- __Regra de seleção__: Este registro servirá para informar os Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte
- __Campos\-Chave__: nrProc
- __Nível hierárquico do registro__: filho do registro tipoCom
- __Ordenação__: não se aplica\. 
- __Agrupamento__: Não se aplica\.
- __Ocorrência__: para cada tipoCom poderá existir “50” infoProc

Para geração deste registro é feita a totalização dos valores da SAFX263 referentes ao Tipo de Comercialização do registro “pai” \(tipoCom\), e por Processo\. Para cada Processo, será gerado um registro infoProc com seus respectivos valores\. 

__\[MFS27483\]__ A geração do infoProc foi alterada para considerar os ajustes de processos cadastrados na manutenção dos ajustes do R\-2050 \(menu “Ajustes da Comercialização da Produção por Produtor Rural PJ/Agroindústria”, opção “*Processos*”\)\.

Ao gerar os registros filhos infoProc para um determinado tipo de comercialização \(registro “pai” tipoCom\), além de totalizar os valores da SAFX263, também será verificada a existência de ajustes de adição e/ou dedução para o tipo de comercialização e processo em questão\. Caso existam ajustes, os valores a serem gravados *para cada processo* serão:

 

            Valores apurados na SAFX263 __\+__ Valores do ajuste de adição __\-__ Valores do ajuste de dedução

Importante: Quando o registro “pai” tipoCom for gravado apenas com base em ajuste de adição \(conforme descrito na RN16 para geração do tipoCom\), os ajustes de processo, caso existam, também serão consideradas para geração do infoProc\.  

MFS17448

__MFS27483__

RN18

__Campo tpProc__

Será gerado com o conteúdo do campo “IND\_TIP\_PROC” da SAFX263

MFS17448

RN19

__Campo nrProc__

Será gerado com o conteúdo do campo “NUM\_PROC” da SAFX263

MFS17448

RN20

__Campo codSusp__

Será gerado com o conteúdo do campo “COD\_SUSP” da SAFX263\. 

Obs:

Caso a informação do campo seja diferente de numérico deverá apresentar a seguinte mensagem no log de pré\-geração:

Evento R2050 \- Registro: Informações de Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte 

“Campo Código do Indicativo da Suspensão deve ser numérico\." 

Informações do Processo: Tipo Processo: XXXXX / Numero Processo: XXXX

Estabelecimento: XXXX / Data Movimento: XXXX

MFS17448

RN21

__Campo vlrCPSusp__

Será gerado com o valor da Contribuição Previdenciária não retida informado nas notas fiscais \(SAFX263\), mais/menos os ajustes de adição/dedução que possam existir para o Período, Tipo de Comercialização e Processo em questão \(ver RN17\):

   Total apurado do campo “VLR\_PREV\_EXIG\_SUSP” da SAFX263 __\(\+\)__

   Valor CP não Retida do ajuste de adição \(caso exista\) __\(\-\) __

   Valor CP não Retida do ajuste de adição \(caso exista\)  

Caso o resultado obtido seja um valor negativo, o campo será gravado com zeros, e no log será gravada a seguinte mensagem de erro: 

Evento R2050 \- Registro: Informações de Processos \(infoProc\) 

Campo: Valor CP com Exigibilidade Suspensa negativo 

Estabelecimento: XXXX / Período: 99/99 / Indicativo Comercialização: X / Tipo Processo: X / Numero Processo: XXXXXXXXXX

__OBS__\.: O registro infoProc só será gravado quando pelo menos um dos três valores a serem gerados tiver valor > zeros \(vlrCPSusp, vlrRatSusp ou vlrSenarSusp\)\. Quando os três valores forem = zero, o registro *não* será gravado\.

  

MFS17448

__MFS27483__

RN22

__Campo vlrRatSusp__

Será gerado com o valor da Contribuição GILRAT não retida informado nas notas fiscais \(SAFX263\), mais/menos os ajustes de adição/dedução que possam existir para o Período, Tipo de Comercialização e Processo em questão \(ver RN17\):

   Total apurado do campo “VLR\_GILRAT\_EXIG\_SUSP” da SAFX263 __\(\+\)__

   Valor GILRAT não Retida do ajuste de adição \(caso exista\) __\(\-\)__

   Valor GILRAT não Retida do ajuste de adição \(caso exista\)  

Caso o resultado obtido seja um valor negativo, o campo será gravado com zeros, e no log será gravada a seguinte mensagem de erro: 

Evento R2050 \- Registro: Informações de Processos \(infoProc\) 

Campo: Valor GILRAT com Exigibilidade Suspensa negativo 

Estabelecimento: XXXX / Período: 99/99 / Indicativo Comercialização: X / Tipo Processo: X / Numero Processo: XXXXXXXXXX

__OBS__\.: O registro infoProc só será gravado quando pelo menos um dos três valores a serem gerados tiver valor > zeros \(vlrCPSusp, vlrRatSusp ou vlrSenarSusp\)\. Quando os três valores forem = zero, o registro *não* será gravado\.

MFS17448

__MFS27483__

RN23

__Campo vlrSenarSusp__

Será gerado com o valor da Contribuição SENAR não retida informado nas notas fiscais \(SAFX263\), mais/menos os ajustes de adição/dedução que possam existir para o Período, Tipo de Comercialização e Processo em questão \(ver RN17\):

   Total apurado do campo “VLR\_SENAR\_EXIG\_SUSP” da SAFX263 __\(\+\)__

   Valor SENAR não Retida do ajuste de adição \(caso exista\) __\(\-\)__

   Valor SENAR não Retida do ajuste de adição \(caso exista\)  

Caso o resultado obtido seja um valor negativo, o campo será gravado com zeros, e no log será gravada a seguinte mensagem de erro: 

Evento R2050 \- Registro: Informações de Processos \(infoProc\) 

Campo: Valor SENAR com Exigibilidade Suspensa negativo 

Estabelecimento: XXXX / Período: 99/99 / Indicativo Comercialização: X / Tipo Processo: X / Numero Processo: XXXXXXXXXX

__OBS__\.: O registro infoProc só será gravado quando pelo menos um dos três valores a serem gerados tiver valor > zeros \(vlrCPSusp, vlrRatSusp ou vlrSenarSusp\)\. Quando os três valores forem = zero, o registro *não* será gravado\.

MFS17448

__MFS27483__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


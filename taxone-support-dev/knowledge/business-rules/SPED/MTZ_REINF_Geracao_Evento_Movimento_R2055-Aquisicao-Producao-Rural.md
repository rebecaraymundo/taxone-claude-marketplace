# MTZ_REINF_Geracao_Evento_Movimento_R2055-Aquisicao-Producao-Rural

> Fonte: MTZ_REINF_Geracao_Evento_Movimento_R2055-Aquisicao-Producao-Rural.docx






THOMSON REUTERS

Módulo REINF

Geração do Evento R-2055

(Aquisição de Produção Rural)


Localização: Menu SPED, módulo EFD-REINF, menu Geração à Geração do Evento R-2055



DOCUMENTO DE REQUISITO



Sumário

1.	Parâmetros da Tela	3
2.	Recuperação dos Dados e Processamento	3
3.	Verificação do Status de Eventos já Gerados	7
4.	Gravação dos Dados	9


## Parâmetros da Tela


Este documento é específico das regras de geração do evento R-2055.

Para consultar a tela da geração e o funcionamento dos parâmetros, ver documento “MTZ_REINF_Tela_Geracao_Previa_Evento_R2055.docx”.

Nesta geração os dados serão armazenados em tabelas, já com o formato e hierarquia exigidos no layout do REINF, para posterior conferência do usuário, e geração dos arquivos XML.


## Recuperação dos Dados e Processamento


Origem dos dados: - Parametrização “Dados Iniciais” do Módulo REINF;
- Cadastro do Estabelecimento;
- SAFX04 - Arquivo de Cadastro de Pessoas Físicas/Jurídicas;
- SAFX07 - Arquivo de Notas Fiscais;
- SAFX263 - Processos Administrativos/Judiciais com decisão/sentença favorável ao contribuinte;
- SAFX271 - Processos Judiciais com decisão/sentença – Produtor Rural;
- SAFX63 - Funrural

Critérios para a recuperação dos dados da parametrização “Dados Iniciais”:

Esta parametrização é por estabelecimento centralizador, e para recuperar os dados, considerar:

- Estabelecimento – estabelecimento selecionado na tela da geração no caso desse ser o centralizador ou estabelecimento selecionado na tela da geração no caso desse estar centralizado ao estabelecimento centralizador parametrizado nos Dados Iniciais;

[ALTERAÇÃO-MFS-70639] Tratamento da regra para considerar o Campo MOVTO_E_S igual à 4

Critérios para a recuperação dos registros dependerá da seleção do parâmetro ‘Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais.

- Se ‘Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ estiver marcado, então:
A recuperação será pela tabela SAFX63. Veja os critérios:
- Empresa – Empresa do estabelecimento selecionado na geração;
- Estabelecimento – Estabelecimento selecionado na geração;
- Data Movimento – O campo DATA_MOVTO deve compreender o período de geração da tela (campo “Período”);
- Movimento Entrada/Saída – O campo TIP_MOV_ES seja igual “1” ou "2" ou “4”;
- Produtor
- Tipo de Aquisição/Comercialização da Produção – O campo IND_TIPO_AQUIS – SAFX63 deve ser “1” ou “2” ou “3” ou ”4” ou “5” ou “6” ou “7”.

[ALTERAÇÃO- MFS67713] Inclusão da regra para considerar data de emissão quando a origem for documento fiscal (SAFX07) -Parâmetro ‘Geração por Data de Emissão (SAFX07 – Arquivo de Notas Fiscais)’ em Dados Iniciais.

- Se ‘ Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ estiver desmarcado, então:
A recuperação será pela tabela SAFX07 como padrão. Os critérios são:
- Empresa – Empresa do estabelecimento selecionado na geração;
- Estabelecimento – Estabelecimento selecionado na geração;
- Data Fiscal – O campo DATA_FISCAL deve compreender o período de geração da tela (campo “Período”), se o parâmetro “Geração por Data de Emissão (SAFX07 – Arquivo de Notas Fiscais)” estiver desmarcado. Caso contrário, consideraremos a DATA_EMISSAO (que deve estar compreendida no período de geração do evento);
- Movimento Entrada/Saída – O campo MOVTO_E_S seja igual “1” ou "2" ou “4”;
- Situação – O campo SITUACAO deve ser diferente de "S";
- Classificaçao Fiscal – O campo COD_CLASS_DOC_FIS deve ser igual a "1" ou "3";
- Produtor
- Tipo de Aquisição/Comercialização da Produção – O campo IND_TIPO_AQUIS – SAFX07 deve ser “1” ou “2” ou “3” ou ”4” ou “5” ou “6” ou “0”.



Agrupamento dos dados:

[ALTERAÇÃO- MFS67713] – Alterada a forma de geração do evento, anteriormente, seguimos o e-Social que gerava o evento S-1250 por estabelecimento e a partir desta demanda, o evento será gerado como os demais eventos do REINF (centralizado)

A geração desse evento R-2055 é diferente dos outros eventos que já geramos nesse módulo, visto que para os outros eventos geramos por estabelecimento Centralizador e esse evento R-2055 é por estabelecimento, ou seja, um evento para cada estabelecimento seja ele centralizador ou centralizado, de acordo com o estabelecimento escolhido na tela de geração.

Para cada estabelecimento adquirente e produtor rural será gerado um evento R-2055, que pode conter até 6 tipos de aquisição, com as informações descritas no item “Gravação dos Dados”.

- As aquisições recuperadas para cada estabelecimento e produtor, serão agrupadas e totalizadas pelas seguintes informações:

- Estabelecimento Adquirente
- Produtor Rural
- Tipo de Aquisição (campo 276-Tipo de Aquisição/Comercialização da Produção-SAFX07/campo 32-Tipo de Aquisição-SAFX63);

Cada produtor irá gerar pelo menos um registro IndAquis, podendo existir de 1 a 6 tipo de aquisição diferentes.

Para cada Tipo de Aquisição do produtor recuperado (de cada estabelecimento adquirente), serão agrupados e totalizados pelas seguintes informações:

- Tipo de Aquisição (campo 276-Tipo de Aquisição/Comercialização da Produção/ campo 32-Tipo de Aquisição-SAFX63);
- Tipo Inscrição Produtor: CNPJ ou CPF
- Produtor: (06- CPF-CGC/69 - CPF do Proprietário da Fazenda SP (São Paulo)-SAFX04 ou 289 - CPF/CNPJ do Consumidor)
- Campo a ser totalizado: 22-Valor do Produto-SAFX07 ou 20-Valor do Produto-SAFX63, 243-Valor Contrib Previd s/ Rural Sub-rogação-SAFX07 ou 24-Valor da Contribuição-SAFX63, 287-Valor da GILRAT-SAFX07 ou 30-Valor da GILRAT-SAFX63, 288-Valor da Contribuição Destinada ao SENAR-SAFX07 ou 26-Valor do Senar-SAFX63.

Sobre o desconto das devoluções (Parâmetros > Devoluções de Aquisição de Produtor Rural (R-2055):

O valor total das aquisições (registro IndAquis), assim como os valores de cada produtor rural (registro ideProdutor), passaram a ter uma dedução referentes às devoluções que possam existir no período. As devoluções também são contabilizadas por produtor rural, da mesma forma feita para as aquisições, com objetivo de garantir que a dedução seja feita nos valores do produtor rural correto.

Este procedimento sobre as devoluções é realizado apenas para os produtores rurais = pessoa física.

[ALTERAÇÃO - MFS71799] Tratamento para considerar Nota Fiscal de Devolução se o Campo 69 -  CPF_SP estiver preenchido.

Considerar a Nota de Devolução SE o Campo 69 - CPF_SP da tabela definitiva da SAFX04 estiver preenchido.

Obs.: Se o Campo 69 - CPF_SP, estiver preenchido, significa que o Produtor Rural é uma Pessoa Física (mesmo tratamento quando o Campo 06 - CPF-CGC estiver preenchido com CNPJ).

Para produtor = pessoa jurídica não é possível deduzir as devoluções, pois neste caso teríamos uma inconsistência entre os valores das notas (registro “nfs”), e os registros “pai”. Lembrando que, o detalhamento das notas das aquisições no registro “nfs” é feito apenas quando o produtor rural é pessoa jurídica.



Critérios da recuperação das notas de devolução:

[ALTERAÇÃO- MFS67737] Inclusão dos demais códigos de Tipo de Aquisição (opções usadas para compra de produtor pessoa física).
[ALTERAÇÃO- MFS67713] Inclusão da regra para considerar data de emissão quando a origem for documento fiscal (SAFX07) -Parâmetro ‘Geração por Data de Emissão (SAFX07 – Arquivo de Notas Fiscais)’ em Dados Iniciais.



- Se ‘Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ estiver desmarcado:

A recuperação será pela tabela SAFX07. Veja os critérios:
- Notas de saída (MOVTO_E_S = 9);
- Notas de Devolução (NORM_DEV = 2);
- Data Fiscal no período da geração, se o parâmetro ‘Geração por Data de Emissão (SAFX07 – Arquivo de Notas Fiscais)’ estiver desmarcado, caso contrário, considerar a DATA_EMISSAO das notas compreendida no período da geração do evento;
- O CFOP da capa (SAFX07) deve constar na parametrização das devoluções (menu Parâmetros > Devoluções de Aquisição de Produtor
Rural (R-2055));
- O campo 276-IND_TIPO_AQUIS da SAFX07 deve ser = “1” ou “2” ou “4” ou “5” ou “0” (opções usadas para compra de produtor pessoa física);


- Se ‘Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ estiver marcado:
A recuperação será pela tabela SAFX63. Veja os critérios:
- Notas de saída (campo 05 - Movimento Entrada/Saída TIP_MOV_ES = 9 da SAFX63);
- Data Movimento no período da geração (campo 03 - DATA_MOVTO da SAFX63);
- O CFOP (campo 13 - Código Fiscal da SAFX63) deve constar na parametrização das devoluções (menu Parâmetros > Devoluções de Aquisição de Produtor Rural (R-2055));

- O Tipo de Aquisição (campo 32- IND_TIPO_AQUIS) deve ser = “1” ou “2” ou ”4” ou “5” ou “7”(opções usadas para compra de produtor pessoa física);



## Eventos


Original/Retificação: Os critérios para identificar se o evento a ser gerado será original ou retificador serão os seguintes:

Se não houver ocorrência de geração de evento anterior, criar nova ocorrência de arquivo original.

Se houver ocorrência de geração anterior com status “Evento Enviado” exibir a seguinte mensagem no log de geração:

Evento R2055 – Aquisição de produção rural
Evento não gerado. Existe evento anterior enviado aguardando retorno.
Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

Se houver ocorrência de geração anterior com status “Evento REINF Recebido com Sucesso ou Advertência” verificar se há evento de exclusão, então:

- Se não existir evento de exclusão então, criar ocorrência de arquivo de retificação.
- Se existir, evento de exclusão considerar os status, então:

Evento de exclusão com status de “Evento REINF Enviado” exibir a seguinte mensagem no log de geração:

Evento R2055 – Aquisição de produção rural
Evento não gerado. Existe evento de exclusão anterior enviado aguardando retorno.
Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

Evento de exclusão com status “Evento Recebido com sucesso ou Advertência” então, verificar se há ocorrência
anterior de evento periódico com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova
ocorrência de arquivo de retificação, se não houver, criar original.

- Se existir evento de exclusão com status “Evento REINF Recebido com Erro” ou “Cancelado” ou “Erro na Geração do                          XML” então, criar nova ocorrência de retificação.

- Se existir evento de exclusão com status “Aguardando Geração do XML” então exibir a seguinte mensagem no log de      geração:

Evento R2055 – Aquisição de produção rural
Evento não gerado. Existe evento anterior não enviado.
Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

Se houver ocorrência de geração anterior com status “Evento REINF Recebido com erro”, então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova ocorrência de arquivo de retificação, se não houver, criar original.

Se houver ocorrência de geração anterior com status “Aguardando Geração do XML” ou “Cancelado” ou “Erro na Geração do XML” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, criar nova ocorrência de arquivo de retificação, se não houver, criar original.


Importante: Na tela Geração Prévia do Evento R-2055, serão gerados APENAS os eventos Originais, os eventos de Retificação deverão ser gerados diretamente pelo Painel de Controle de Eventos pela opção ‘Reprocessar Evento’. Caso os eventos encontrados na tela de Geração Prévia dos Movimentos sejam identificados nos critérios acima como Retificação esses deverão ser desconsiderados e não gerados, pela tela de Geração Prévia dos Movimentos serão gerados apenas os eventos que se enquadrarem como ‘Original’.



Fechamento/Reabertura: Critérios de geração do evento considerando a situação do período.

Se não houver ocorrência de geração de evento de fechamento, prosseguir com a geração.

Se houver ocorrência de geração de evento de fechamento considerar os status então:

- Evento de fechamento com status de “Evento Reinf Enviado” exibir a seguinte mensagem no log de geração:

R2055 – Aquisição de produção rural
Evento não gerado. Existe evento de fechamento do período enviado aguardando retorno.
Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

- Evento de fechamento com status de “Evento REINF Recebido com Sucesso ou Advertência” exibir a seguinte
mensagem no log de geração:


R2055 – Aquisição de produção rural
Evento não gerado. Período Fechado.
Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

Se houver ocorrência de geração de evento de reabertura correspondente, com status “Evento REINF Recebido com
Sucesso ou Advertência”, prosseguir com a geração.


- Evento de fechamento com status de “Evento REINF Recebido com erro” ou “Cancelado” ou “Erro na Geração do
XML” ou “Evento Excluído na Mensageria” então, verificar se há ocorrência de evento anterior com status “Evento REINF Recebido com Sucesso ou Advertência”, se houver, exibir a seguinte mensagem no log de geração:

R2055 – Aquisição de produção rural
Evento não gerado. Período Fechado.
Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX

Se não houver evento de fechamento com status “Evento REINF Recebido com Sucesso ou Advertência”,
prosseguir com a geração.

- Evento de Fechamento com status de “Aguardando Geração do XML”, exibir a seguinte mensagem no log de
geração:

R2055 – Aquisição de produção rural
Evento não gerado. Existe evento de fechamento do período não enviado.
Empresa/Estabelecimento: XX / XXXXX / Identificação do Evento: XXXXXX



.


## Gravação dos Dados


Conforme descrito acima (“Agrupamento dos dados”), será gerado um evento R-2055 para cada estabelecimento, com as seguintes informações:

(os registros não citados não serão gerados)


Reinf – EFD - Reinf
evtAqProd – Evento aquisição de produção
ideEvento – Informações de Identificação do Evento
ideContri – Informações de Identificação do Contribuinte
infoAquisProd– Informações da aquisição de produção
ideEstabAdquir – Identificação do estabelecimento adquirente da produção
ideProdutor – Identificação do produtor rural
detAquis - Detalhamento da aquisição de produção rural
infoProcJud– Informação de processo judicial do produtor rural


Observar orientações existentes no arquivo “TR_REINF_DEXPARA_V2.1.1.xlsx".

Detalhamento das Regras:

Registro evtAqProd – Evento Aquisição de Produção



Registro ideEvento - Informações de Identificação do evento.




Registro ideContri - Informações de identificação do contribuinte.



Registro ideEstabAdquir- Informações do estabelecimento adquirente da produção.

Este registro servirá para identificar a qual estabelecimento se referem as notas que serão demonstradas. Como vamos gerar um arquivo por estabelecimento, demonstrará o CNPJ do estabelecimento de geração.




Registro ideProdutor - Informações de identificação do produtor.

As informações do produtor serão recuperadas no seu cadastro na SAFX04, através dos campos “06-Indicador da Pessoa Fis/Jur” e “07-Código da Pessoa Fis/Jur” da SAFX07 ou dos campos “06- Indicador Pessoa Física/Jurídica” e “07- Código/Destinatário/Emitente/Remetente” da SAFX63.

Havendo mais de um registro da pessoa fis/jur na SAFX04, será considerado o registro de > data de validade cujo mês/ano seja <= ao mês/ano do período informado na tela da geração.





Registro detAquis - Detalhamento da aquisição de produção rural.

Caso o parâmetro ‘Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado as informações da aquisição serão recuperadas no seu cadastro na SAFX63, sempre que:
- O campo Movimento Entrada/Saída (MOVTO_E_S) esteja preenchido com o conteúdo igual a “1”;
- O campo Tipo de Aquisição (IND_TIPO_AQUIS) da SAFX63 esteja preenchido com o conteúdo igual a “1” ou “2” ou “3”;
- A Data do Movimento compreenda o período parametrizado na geração;

OU

- O campo Movimento Entrada/Saída (MOVTO_E_S) esteja preenchido com o conteúdo igual a “2”;
- O campo Tipo de Aquisição (IND_TIPO_AQUIS) da SAFX63 esteja preenchido com o conteúdo igual a “1” ou “2” ou “3” ou ”4” ou “5” ou “6”, ou “7”;
- A Data do Movimento compreenda o período parametrizado na geração.


Caso o parâmetro ‘Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais NÃO esteja selecionado as informações da aquisição serão recuperadas no seu cadastro na SAFX07, sempre que:
- O campo Movimento Entrada/Saída (MOVTO_E_S) esteja preenchido com o conteúdo igual a “1”;
- O campo Tipo de Aquisição/Comercialização da Produção (IND_TIPO_AQUIS) da SAFX07 esteja preenchido com o conteúdo igual a “1” ou “2” ou “3”;
- A Data Fiscal compreenda o período parametrizado na geração se o parâmetro “Geração por Data de Emissão (SAFX07 – Arquivo de Notas Fiscais)” estiver desmarcado. Caso contrário, consideraremos a data de emissão (que deve estar compreendida no período de geração do evento);


OU

- O campo Movimento Entrada/Saída (MOVTO_E_S) esteja preenchido com o conteúdo igual a “2”;
- O campo Tipo de Aquisição/Comercialização da Produção (IND_TIPO_AQUIS) da SAFX07 esteja preenchido com o conteúdo igual a “1” ou “2” ou “3” ou ”4” ou “5” ou “6”, ou “0”;
- A Data Fiscal compreenda o período parametrizado na geração se o parâmetro “Geração por Data de Emissão (SAFX07 – Arquivo de Notas Fiscais)” estiver desmarcado. Caso contrário, consideraremos a data de emissão (que deve estar compreendida no período de geração do evento).



Poderão existir até 6 registros de aquisição, e para cada registro recuperado, será gerado um registro IndAquis, com as informações descritas abaixo:




Registro infoProcJud - Informações referentes à processo judicial

Se o parâmetro ‘Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais estiver desmarcado:
Este registro será gerado apenas quando o Produtor Rural possuir processo judicial do produtor (campo 12 - IND_TP_PROC_ADJ igual a ‘2 – Judicial’ e campo 21 – Indicador Tipo do Processo Judicial for igual a ‘1 - Processo Judicial do Produtor’). Para isso será verificado o preenchimento dos campos “12 - IND_TP_PROC_ADJ”,  21 – Indicador Tipo do Processo Judicial”, “13 - Número do Processo” e “14 - Código do Indicativo da Suspensão de Exigibilidade de Tributos” da SAFX263, da seguinte forma:

Esse registro infoProcJud será gerado apenas se o campo 12 - IND_TP_PROC_ADJ igual a ‘2 – Judicial’, campo 21 – Indicador Tipo do Processo Judicial for igual a ‘1 - Processo Judicial do Produtor’ E os campos “13 - Número do Processo” e “14 - Código do Indicativo da Suspensão de Exigibilidade de Tributos” estiverem preenchidos.

Caso o parâmetro ‘Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado, será verificado o preenchimento dos campos “18 – Indicador Tipo do Processo Judicial”, “13 - Número do Processo” e “14 - Código do Indicativo da Suspensão” da SAFX271, da seguinte forma:

Esse registro infoProcJud será gerado quando o campo 18 – Indicador Tipo do Processo Judicial for igual a ‘1 - Processo Judicial do Produtor’ E os campos “13 - Número do Processo” e “14 - Código do Indicativo da Suspensão” estiverem preenchidos.

OU

Esse registro infoProcJud será gerado quando o campo 18 – Indicador Tipo do Processo Judicial for igual a ‘3 - Indicador de Autoria do Processo’ E os campos “13 - Número do Processo” e “14 - Código do Indicativo da Suspensão” estiverem preenchidos.  Além de verificar o campo 18 da SAFX271, também deve ser verificado o campo 01 - IND_TP_PROC_ADJ igual a ‘2 – Judicial’ e campo 8 - Indicador de Autoria da SAFX2058, que deve estar igual a “1 - Próprio contribuinte”;

O registro infoProcJud será gerado com a seguinte informação:




= = = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-58346 | Alessandra Cristina Navatta | Criação da geração do Evento R-2055 (a especificação foi baseada na documentação existente do Evento S-1250, do produto e-Social).   Pontos ajustados com relação ao Evento S-1250:  Retirado o campo PerApur do Registro ideEvento  Inclusão de opção no campo tipo aquisição (campo 32 - IND_TIPO_AQUIS da SAFX63, opção 7 e campo 276 - IND_TIPO_AQUIS da SAFX07, opção 0 ). Para a origem de documentos fiscais, houve um tratamento no campo, para exibir o domínio correto no evento, uma vez que a opção 7 já existia na SAFX07. Agrupamento por Produtor Rural e não mais por Tipo de Aquisição (alteração de hierarquia). Os valores passam a estar no Registro IndAquis Excluído o campo vlrTotAquis Excluído o Registro nfs Excluído o Registro infoProcJ Ajustes nas regras do Registro infoProcJud, para considerar o campo IND_TP_PROC_ADJ (campo 12 da SAFX263 e campo 01 da SAFX2058)  Inclusões de validações nos campos (indAquis, vlrBruto, vlrCPDescPR, vlrRatDescPR e vlrSenarDesc) do registro Registro detAquis e nos campos (vrCPNRet, vrRatNRet e vrSenarNRet) do registro infoProcJud. | 04/02/2021 |
| MFS64383 | Alessandra Cristina Navatta | Alteração na regra do campo <indOpcCP> (para origem SAFX07) | 30/04/2021 |
| MFS66875 | Rogério Ohashi | Alteração na regra do campo <nrInscProd> (para origem SAFX07, também considerar a informação do Campo 69 – CPF-SP da tabela SAFX04). | 09/06/2021 |
| MFS67737 | Rogério Ohashi | Alteração da regra referente recuperação do desconto das devoluções (Parâmetros > Devoluções de Aquisição de Produtor Rural (R-2055), que devem considerar também os Códigos de Tipo de Aquisição “4” e “5”, para origem SAFX07 e SAFX63. | 24/06/2021 |
| MFS-67713 | Alessandra Cristina Navatta | Inclusão das regras para o parâmetro “Geração por Data de Emissão (SAFX07 – Arquivo de Notas Fiscais)”.  Ajuste nas regras que utilizam o parâmetro “Gerar evento R-2055 a partir da SAFX63 – Arquivo de Contribuição Rural – INSS” para “Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS”(apenas ajuste de label) Alteração na forma de geração do evento, inicialmente, o mesmo era gerado por estabelecimento (seguindo o formato do e-Social) e nesta demanda, a geração passa a ser centralizada. O campo retifS1250, do Registro ideEvento, não está sendo tratado atualmente pelo FISCO, mas também não foi retirado do layout. Diante disso, estamos desativando a regra criada (apenas atualizando a especificação, pois a tela criada mencionada na regra deste campo, já estava oculta do Menu) | 03/08/2021 |
| MFS69255 | Rogério Ohashi | Alteração na regra do campo <nrInscProd> (para origem SAFX07, retirar o filtro pelo Campo movto_e_s = ‘2’ e considerar a informação do Campo 69 – CPF-SP da tabela SAFX04 se estiver preenchido | 04/08/2021 |
| MFS70413 | Rogério Ohashi | Retirar regra de obrigatoriedade, p/ possibilitar geração dos Campos Valor da Contribuição Previdenciária Não Retida, GILRAT Não Retida ou SENAR Não Retido igual à “Zero”. | 11/08/2021 |
| MFS70639 | Rogério Ohashi | Tratamento na geração à partir da SAFX63 e à partir da SAFX07 para considerar também o campo MOVTO_E_S igual à 4 | 18/08/2021 |
| MFS71799 | Rogério Ohashi | Tratamento para considerar Notas de Devolução para Produtor Rural com CNPJ, se o Campo 69 – CPF-SP da tabela SAFX04  estiver preenchido. | 08/09/2021 |
| MFS-79878 | Alessandra Cristina Navatta | Exclusão do campo ‘retifS1250’ para atendimento do layout V2.1 do REINF. | 31/01/2022 |
| MFS-90001 | Alessandra Cristina Navatta | Alteração da versão 2.1 para 2.1.1 e referência do arquivo de de_para  Obs. Os ajustes mapeados nesta demanda, referem-se a atualização funcional. Não há impactos na implementação | 02/08/2022 |
| MFS-90387 | Rogério Ohashi | Inclusão do parâmetro “Considerar para composição da Receita Bruta” na tela de Dados Iniciais no quadro “Evento R-2055 – Aquisição do Produtor Rural”. | 02/08/2022 |
| MFS-98132 | Rogério Ohashi | Alterar a recuperação do Campo 85 - VLR_BASE_INSS para o Campo 241 – VLR_BASE_INSS_RURAL, do parâmetro “Considerar para composição da Receita Bruta” na tela de Dados Iniciais no quadro “Evento R-2055 – Aquisição do Produtor Rural”. | 05/12/2022 |


| id | Identificação do evento, conforme REGRA_VALIDA_ID_EVENTO:   “ID” + “1” + CNPJ do estabelecimento + data da geração (AAAAMMDD) + hora da geração (HHMMSS) + sequencial  CNPJ – 8 primeiras posições do CNPJ, completando com zeros à direita; Sequencial (99999) - Número sequencial da chave. Deve ser incrementado apenas quando houver a geração de eventos na mesma data/hora. |
| --- | --- |


| indRetif | Este campo será gerado de acordo com a verificação de status descrita no item “3-Verificação do Status de Eventos já Gerados”:  Se for a primeira geração do evento do contribuinte no período:       O campo será gerado com “1” (Arquivo Original); Senão       Neste caso o preenchimento do campo depende do status do evento gerado anteriormente:        Se status do evento original = 8 ou = 9 à O campo será gerado com “2” (Retificação);       Se status do evento original <> 8 e <> 9 à O campo será gerado com “1” (Arquivo Original); |
| --- | --- |
| nrRecibo | Este campo será gerado de acordo com o conteúdo do campo anterior (indRetif), da seguinte forma:  Se indRetif = “1” (Arquivo Original)       Nesse caso este campo não será gerado;  Se indRetif = “2” (Retificação)       Nesse caso este campo será gravado com o número do recibo do arquivo a ser retificado. Ou seja, com o conteúdo      do campo nrRecibo que consta no evento original; |
| perApur | Mês e ano do período informado na tela da geração, no formato AAAA-MM (conforme orientação do layout) |
| tpAmb | Campo “Tipo de ambiente” da parametrização “Dados Iniciais” (ver acima a regra para a recuperação dos dados desta parametrização) |
| procEmi | Conteúdo fixo = “1” (= Aplicativo do contribuinte) |
| verProc | Versão do sistema DW. Esta informação é gerada de forma fixa = “V2R010”.   Obs: A princípio, a definição previa informar neste campo a versão do produto informada na tela da geração. No entanto, este entendimento é equivocado, pois como descreve o manual trata-se da versão do aplicativo (do empregador ou governamental) utilizado para gerar o evento. No caso, trata-se da versão do próprio DW. O REINF já trabalha desta forma. |
| retifS1250 | Este campo só pode ser preenchido se indRetif for igual a “1” e se perApur anterior 202105.   Este campo deve ser preenchido se atender a regra acima e se na tela ‘Evento R-2055 - Indicação sobre Retificação dos Eventos S-1250’, para o período de apuração em questão, o produtor estiver com o flag ‘Retificação do Evento S-1250’, selecionado. Quando marcado, este campo deve ser gerado com ‘S’   Obs. Esse campo será sempre null (exceto na criação do XSD), se o registro possuir o flag ‘Retificação do Evento S-1250’ marcado (tela Evento R-2055 - Indicação sobre Retificação dos Eventos S-1250’).  [ALTERAÇÃO- MFS67713] Atenção: Este campo retifS1250, do Registro ideEvento, não está sendo tratado atualmente pelo FISCO, mas também não foi retirado do layout. Diante disso, estamos desativando a regra criada (apenas atualizando a especificação, pois a tela criada mencionada na regra deste campo, já estava oculta do Menu). Gerar branco.  [ALTERAÇÃO MFS-90001]- Alteração de versão [ALTERAÇÃO MFS-79878] Este campo não deve ser gerado a partir da versão 2.1 2.1.1 do REINF |


| tpInsc | Conteúdo fixo = “1” |
| --- | --- |
| nrInsc | CNPJ do estabelecimento, considerando apenas as 8 primeiras posições do CNPJ, completando com zeros à direita. |


| tpInscAdq | Conteúdo fixo = “1” |
| --- | --- |
| nrInscAdq | CNPJ do estabelecimento |


| tpInscProd | Gravar ‘1’ - CNPJ ou ‘2’ - CPF. | MFS-58346 |
| --- | --- | --- |
| nrInscProd | Se o parâmetro ‘Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado:  Caso existir informação no campo CPF_SP da tabela definitiva da SAFX04, gerar o campo com a informação desse campo CPF_SP, caso contrário:  Gerar o campo com a informação do campo CPF-CGC (CPF_CGC) da tabela definitiva da SAFX04.  [MFS66875-MFS69255] Tratamento para Produtor Rural para considerar o Campo CPF_SP (Origem SAFX07)  Se o parâmetro ‘Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais NÃO esteja selecionado:  Gerar o campo com a informação do campo CPF_SP da tabela definitiva da SAFX04, SE o campo CPF_SP da tabela definitiva da SAFX04 estiver preenchido. OU  Gerar o campo com a informação do campo CPF/CNPJ do Consumidor/ Produtor (CPF_CNPJ) da tabela definitiva da SAFX07, SE o campo Movimento Entrada/Saída (MOVTO_E_S) estiver preenchido com o conteúdo igual a “2” e SE o campo CPF/CNPJ do Consumidor/ Produtor (CPF_CNPJ) da tabela definitiva da SAFX07 estiver preenchido. OU  Gerar o campo com a informação do campo CPF-CGC (CPF_CGC) da tabela definitiva da SAFX04, SE o campo Movimento Entrada/Saída (MOVTO_E_S) da tabela definitiva da SAFX07 estiver preenchido com o conteúdo igual a “1” e o campo Indicador do Conteúdo do Código (IND_CONTEM_COD) da tabela definitiva da SAFX04 estiver preenchido com o conteúdo igual a “2”.   SE NÃO gerar o campo com a informação do campo CPF-CGC (CPF_CGC) da tabela definitiva da SAFX04.   Tratamento:  Se for CPF (preenchimento com 11 posições) não deve ser considerado zeros à esquerda e nem à direita para completar o tamanho do campo; Se houver espaços em branco no campo da tabela SAFX04/SAFX07 deve ser desconsiderado, pois esse campo quando for CPF deve vir apenas com os 11 dígitos. | MFS-58346 MFS-66875 |
| indOpcCP | Se o parâmetro ‘Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ esteja selecionado nos Dados Iniciais:  Se o campo 33-IND_TRIB_PRODUTOR_CP da SAFX63, estiver preenchido, considerar a informação indicada neste campo, gerando ‘S’ se a opção for ‘2 - Sobre a folha de pagamento’ e não gerar o campo se a opção do registro for ‘1 - Sobre a comercialização da sua produção’, caso o campo da tabela esteja sem informação, verificar as regras abaixo:  Se campo 24-Valor da Contribuição da SAFX63 estiver sem valor informado (0-zero) E  Não existir vinculação de processo na SAFX271 que zera o campo por liminar (processo judicial) OU  caso exista, os campos 15 - Valor da Contribuição Previdenciária Não Retida(VLR_CONT_PREV_N_RET) e 16 - Valor da contribuição para o GILRAT Não Retido(VLR_GILRAT_N_RET) da SAFX271 estiverem sem valor informado (0-zero), então:        Gravar ‘S’  Senão:         Não gerar o campo.  Se geração normal a partir das notas (SAFX07):  Se o campo 303-IND_TRIB_PRODUTOR_CP da SAFX07, estiver preenchido, considerar a informação indicada neste campo, gerando ‘S’ se a opção for ‘2 - Sobre a folha de pagamento’ e não gerar o campo se a opção do registro for ‘1 - Sobre a comercialização da sua produção’. Caso o campo não esteja preenchido, não gerar este campo. | MFS-58346 MFS-64383 |


| indAquis | Campo 276-Tipo de Aquisição/Comercialização da Produção da SAFX07. Caso a opção ‘0 - Aquisição de produção de produtor rural pessoa física ou segurado especial para fins de exportação’ esteja selecionada, preencher o campo com ‘7’.  Caso o parâmetro ‘Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado o campo a ser recuperado será:  Campo 32-Tipo de Aquisição da SAFX63   Validações:  Se o campo {tpInscProd} = [1], só deve existir IndAquisição igual a [3, 6], caso seja gerada outras opções, exibir a mensagem: “Quando o tipo de inscrição do contribuinte for igual a 1 – CNPJ, só devem existir Indicador de Aquisição igual a 3 ou 6”.    Se o campo {tpInscProd} = [2], só deve existir IndAquisição igual a [1, 2, 4, 5, 7], caso exista outras opções exibir a mensagem: “Quando o tipo de inscrição do contribuinte for igual a 2 – CPF, só devem existir Indicador de Aquisição igual a 1, 2, 4, 5 ou 7”. | MFS-58346 |
| --- | --- | --- |
| vlrBruto | [ALTERAÇÃO-MFS90387/MFS98132] Readequar a regra de preenchimento do campo o valor Bruto, para considerar o parâmetro “Considerar para composição da Receita Bruta” na tela do Dados Iniciais (Geração à partir da SAFX07). Alterar a recuperação do Campo de Base de INSS para o Campo 241 – VLR_BASE_INSS_RURAL.  Se caso o parâmetro “Geração a partir da SAFX63” estiver desmarcado o valor a ser gravado nesse campo deverá seguir conforme regra abaixo:  1 – Para correta gravação do campo será necessário verificar qual opção o usuário informou no parâmetro ‘Considerar para composição da Receita Bruta’ nos Dados Iniciais, sendo que:  Caso selecionado Valor Contábil, recuperar a informação do campo VLR_TOT_NOTA da SAFX07; Caso selecionado Valor Total, recuperar a informação do campo VLR_PRODUTO da SAFX07; Caso selecionado Base de Cálculo do INSS RURAL, recuperar a informação do campo 241- VLR_BASE_INSS_RURAL da SAFX07; Caso selecionado Base de Cálculo do INSS, recuperar a informação do campo VLR_BASE_INSS da SAFX07;  Campo 23 -Valor Total do Documento Fiscal da SAFX07 (total agrupado por Tipo de aquisição e Produtor)  Caso o parâmetro ‘Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais estiver marcado o campo a ser recuperado será:  Campo 19 - Valor do Documento Fiscal da SAFX63 (total agrupado por Tipo de aquisição e Produtor)  Quando se tratar de produtor rural pessoa física, será deduzido deste valor o correspondente ao mesmo valor das notas fiscais de devolução.  O valor resultante das aquisições menos as devoluções não pode ser menor ou igual a zero. Neste caso, exibir mensagem no log:  O Valor Bruto das Aquisições do produtor rural no período é menor ou igual a zero. Nesse caso, não geramos  as informações das aquisições. Dados do Registro: Indicativo da Aquisição: XX' - Inscrição do Produtor: XXXXXXXXXXX   (ver regra geral sobre as devoluções na Recuperação dos Dados e Processamento). | MFS-58346 MFS-90387 MFS-98132 |
| vlrCPDescPR | Campo 243 - Valor Contrib Previd s/ Produção Rural Sub-rogação da SAFX07 (total agrupado por Tipo de aquisição e Produtor)  Caso o parâmetro ‘Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado o campo a ser recuperado será:  Campo 24-Valor da Contribuição da SAFX63 (total agrupado por Tipo de aquisição e Produtor)  Quando se tratar de produtor rural pessoa física, será deduzido deste valor o correspondente ao mesmo valor das notas fiscais de devolução.  Atenção: Se não existir valor retido, gerar zero  O valor resultante das aquisições menos as devoluções não pode ser menor que zero. Neste caso, gerar o campo com zero e exibir mensagem no log: O Valor da Contribuição Previdenciária referente às Devoluções excede ao das aquisições do produtor rural no período. Nesse caso será gerado o valor 0 - zero. Dados do Registro: Indicativo da Aquisição: XX' - Inscrição do Produtor: XXXXXXXXXXX   (ver regra geral sobre as devoluções na Recuperação dos Dados e Processamento). | MFS-58346 |
| vlrRatDescPR | Campo 287 - Valor da GILRAT da SAFX07 (total agrupado por Tipo de aquisição e Produtor)  Caso o parâmetro ‘Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado o campo a ser recuperado será:  Campo 30-Valor da GILRAT da SAFX63 (total agrupado por Tipo de aquisição e Produtor)  Quando se tratar de produtor rural pessoa física, será deduzido deste valor o correspondente ao mesmo valor das notas fiscais de devolução.  Atenção: Se não existir valor retido, gerar zero   O valor resultante das aquisições menos as devoluções não pode ser menor que zero. Neste caso, gerar o campo com zero e exibir mensagem no log: O Valor da Contribuição Destinada ao RAT referente às Devoluções excede ao das aquisições do produtor rural no período. Nesse caso será gerado o valor 0 - zero. Dados do Registro: Indicativo da Aquisição: XX' - Inscrição do Produtor: XXXXXXXXXXX  (ver regra geral sobre as devoluções na Recuperação dos Dados e Processamento). | MFS-58346 |
| vlrSenarDesc | Campo 288 - Valor da Contribuição Destinada ao SENAR da SAFX07 (total agrupado por Tipo de aquisição e Produtor)  Caso o parâmetro ‘Geração a partir da SAFX63 – Arquivo de Contribuição Rural – INSS’ nos Dados Iniciais esteja selecionado o campo a ser recuperado será:  Campo 26-Valor do Senar da SAFX63 (total agrupado por Tipo de aquisição e Produtor)  Quando se tratar de produtor rural pessoa física, será deduzido deste valor o correspondente ao mesmo valor das notas fiscais de devolução.  Atenção: Se não existir valor retido, gerar zero   O valor resultante das aquisições menos as devoluções não pode ser menor que zero. Neste caso, gerar o campo com zero e exibir mensagem no log: O Valor da Contribuição Destinada ao SENAR referente às Devoluções excede ao das aquisições do produtor rural no período. Nesse caso será gerado o valor 0 - zero. Dados do Registro: Indicativo da Aquisição: XX' - Inscrição do Produtor: XXXXXXXXXXX  (ver regra geral sobre as devoluções na Recuperação dos Dados e Processamento). | MFS-58346 |


| nrProcJud | Campo 13-Número do Processo (SAFX263) ou 13-Número do Processo (SAFX271) | MFS-58346 |
| --- | --- | --- |
| codSusp | Campo 14 - Código do Indicativo da Suspensão de Exigibilidade de Tributos (SAFX263) ou 14- Código do Indicativo da Suspensão (SAFX271) | MFS-58346 |
| vrCPNRet | Campo 15-Valor da Contribuição Previdenciária Não Retida (SAFX263) ou 15- Valor da Contribuição Previdenciária Não Retida (SAFX271)  Validações:  [MFS70413] Retirar regra de obrigatoriedade, p/ o Campo Valor da Contribuição Previdenciária Não Retida Retida igual à “Zero” (Não gravar Tag com zero). Informação obrigatória se ‘vlrRatNRet’ e/ou ‘vlrSenarNRet’ não tiver(em) sido informado(s). Caso contrário, exibir a mensagem: “O campo Valor da Contribuição Previdenciária Não Retida deve ser preenchido, quando os campos ‘Valor da Contribuição GILRAT Não Retida’ e/ou ‘Valor da Contribuição SENAR Não Retida’ não estiverem preenchidos.”   Validar quando o campo ‘indAquis’ igual a ‘1’ e/ou ‘2’, se a soma dos valores informados neste campo (‘vlrCPNRet’), menos os processos cujo ‘indSusp’ seja igual a ‘92’, é superior ao resultado da expressão: 0,012 * valor informado no campo ‘vlrBruto’ do registro superior (Registro detAquis). Se for superior, exibir a mensagem no log: “Valor da Contribuição Previdenciária Não Retida está superior ao valor permitido. Valor informado: (apresentar o valor deste campo), Valor Máximo Permitido: (apresentar o resultado da expressão mencionada na regra)”.    Validar quando o campo ‘indAquis’ igual a ‘3’, se a soma dos valores informados neste campo (‘vlrCPNRet’), menos os processos cujo ‘indSusp’ seja igual a ‘92’, é superior ao resultado da expessão: 0,017 * valor informado no campo ‘vlrBruto’ do registro superior (Registro detAquis). Se for superior, exibir a mensagem no log: “Valor da Contribuição Previdenciária Não Retida está superior ao valor permitido. Valor informado: (apresentar o valor deste campo), Valor Máximo Permitido: (apresentar o resultado da expressão mencionada na regra)”.   Não gravar a Tag se o valor for igual à zero. | MFS-58346 |
| vrRatNRet | Campo 16-Valor da contribuição para GILRAT Não Retida (SAFX263) ou 16-Valor da Contribuição para GILRAT Não Retido (SAFX271)  Validações:  [MFS70413] Retirar regra de obrigatoriedade, p/ o Campo GILRAT Não Retida igual à “Zero” (Não gravar Tag com zero). Informação obrigatória se ‘vlrCPNRet’ e/ou ‘vlrSenarNRet’ não tiver(em) sido informado(s). Caso contrário, exibir a mensagem: “O campo Valor da Contribuição GILRAT Não Retida deve ser preenchido, quando os campos ‘Valor da Contribuição Previdenciária Não Retida e/ou ‘Valor da Contribuição SENAR Não Retida’ não estiverem preenchidos. “  Validar se a soma dos valores informados neste campo (‘vlrRatNRet’), menos os valores dos processos cujo ‘indSusp’ seja igual a ‘92’, é superior ao resultado da expressão: 0,001* valor informado no campo ‘vlrBruto’ do registro superior (Registro detAquis). Se for superior, exibir a mensagem no log: “Valor da contribuição para GILRAT Não Retida está superior ao valor permitido. Valor informado: (apresentar o valor deste campo), Valor Máximo Permitido: (apresentar o resultado da expressão mencionada na regra)”.  Não gravar a Tag se o valor for igual à zero. | MFS-58346 |
| vrSenarNRet | Campo 17-Valor da contribuição para o SENAR Não Retido (SAFX263) ou 17-Valor da Contribuição para SENAR Não Retido (SAFX271)  Validações:  [MFS70413] Retirar regra de obrigatoriedade, p/ o Campo SENAR Não Retido igual à “Zero” (Não gravar Tag com zero). Informação obrigatória se ‘vlrCPNRet’ e/ou ‘vlrRatNRet’ não tiver(em) sido informado(s). Caso contrário, exibir a mensagem: “O campo Valor da Contribuição SENAR Não Retida deve ser preenchido, quando os campos ‘Valor da Contribuição Previdenciária Não Retida’ e/ou ‘Valor da Contribuição GILRAT Não Retida’ não estiverem preenchidos. “  Validar se a soma dos valores informados neste campo (‘vlrSenarNRet’), menos os valores dos processos cujo ‘indSusp’ seja igual a ‘92’, é superior ao resultado da expressão: 0,002* do valor informado no campo ‘vlrBruto’ do registro superior (Registro detAquis). Se for superior, exibir a mensagem no log: “Valor da contribuição para SENAR Não Retida está superior ao valor permitido. Valor informado: (apresentar o valor deste campo), Valor Máximo Permitido: (apresentar o resultado da expressão mencionada na regra)”.  Não gravar a Tag se o valor for igual à zero. | MFS-58346 |

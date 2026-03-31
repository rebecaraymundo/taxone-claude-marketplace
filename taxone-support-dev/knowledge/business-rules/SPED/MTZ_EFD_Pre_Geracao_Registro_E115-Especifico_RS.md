# MTZ_EFD_Pre_Geracao_Registro_E115-Específico RS

> Fonte: MTZ_EFD_Pre_Geracao_Registro_E115-Específico RS.docx






THOMSON REUTERS

Pré-Geração do Registro E115
EFD-Escrituração Fiscal Digital



DOCUMENTO DE REQUISITO




Localização: Menu Sped, Módulo EFD - Escrituração Fiscal Digital, item Pré-Geração à Registro E115 (Específico RS)

REGRAS DE NEGÓCIO









Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:



| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-13074 | Julyana Perrucini | Essa MFS tem como objetivo criar a rotina de geração do Registro E115 para alimentar a tabela de Valores Declaratórios. |
| CH5484_2018 (MFS-17456) | João Henrique | Essa MFS tem como objetivo gerar o registro E115 quebrando por CFOP. |
| CH16505_2018 (MFS-19588) | Julyana Perrucini | Essa MFS tem como objetivo ajustar a geração do Anexo V.A para considerar a redução de base de cálculo à soma dos valores. |
| MFS-23315 | Julyana Perrucini | Essa MFS tem como objetivo alterar a geração dos Anexos V.A e V.B. |
| MFS-24916 | Liliane Assaf | Reestruturação de Menu (Específico RS) |
| MFS-40746 | Liliane Assaf | Inclusão das notas de classificação = 4 - Conhecimentos Fretes - SAFX 51, nos Anexos V.A, V.B e V.C |
| MFS-57858 | Rogério Ohashi | Regra para bloquear pré-geração de um CFOP para mais de um Código de Informação Adicional, para evitar duplicidade na geração dos Registros E115.E criar Log de Erro de Geração. |
| MFS-59693 | Rogério Ohashi | Alteração na Regra para utilizar o Parâmetro “Considerar campo Código do Benefício” para considerar ou não o Campo 255 – Código do Benefício da Tabela SAFX08 na geração do Registro E115. Esse ajuste se faz necessário para os clientes que utilizaram esse campo como critério de geração, conforme informação do campo no Manual Layout. |
| MFS-67999 | Rogério Ohashi | Inclusão de Regra de tratamento para Geração de Estabelecimentos com Inscrição Estadual Única. |
| MFS-80289 | Rogério Ohashi | Regra para desbloquear a pré-geração de um CFOP para mais de um Código de Informação Adicional, e correção nas duplicidades na geração do Registros E115. E criar Log de Erro de Geração. |


| CÓD | DESCRIÇÃO | MFS/CH |
| --- | --- | --- |
| RN00 | Regra Específica p/ RS:  Regras Gerais  Esta geração foi criada na MFS-13074 com objetivo de fazer a geração dos dados do Registro E115 para a UF do Rio Grande do Sul (RS).  Essa geração é especifica para os itens da Tabela 5.2 - Informações Adicionais da Apuração - Valores Declaratórios disponibilizados no site da Receita Federal no Portal do SPED – EFD ICMS/IPI.  A UF do Rio Grande do Sul (RS) está obrigada a entrega deste registro desde 2016, no entanto o módulo só possuía a possibilidade de informar manualmente os registros para geração no arquivo magnético, nem todos os estados estão obrigados e nem todos possuem uma definição para declarar essas informações.  Como o validador da GIA-RS teve modificação para entrega do arquivo magnético, que agora é através da EFD e não mais na estrutura da GIA, foram definidos os códigos dos valores declaratórios relacionando-os ao amparo legal de forma com quê consigamos gerar as informações necessárias via parametrização de CFOP ou CFOP/ Natureza de Operação.  Trataremos os Anexos I.C, V.A, V.B e V.C.  [ALTERAÇÃO-MFS-67999] Tratamento p/ Geração por Inscrição Estadual Única. Não terá geração por IEU no momento.  Tratamento:  Foi disponibilizado o Parâmetro “Geração p/Inscrição Estadual Única” na tela de Pré-Geração do Registro E115 – Específico RS, para tratamento de Geração para Estabelecimentos por Inscrição Estadual Única, sendo assim deverá seguir a seguinte regra:   Se a opção selecionada for “Sim”: Serão consideradas as Notas Fiscais de todos os estabelecimentos envolvidos, o centralizador (estabelecimento selecionado em tela), e os centralizados (conforme parametrização do módulo de controle das obrigações estaduais, menu  “Obrigações >  Empresas/Estabelecimentos com Ins. Estadual Única”), onde:                Selecionar todas as Notas Fiscais dos Estabelecimentos envolvidos na centralização, identificados a partir do campo “COD_ESTAB” da tabela “ICP_INSC_EST_CENTR”, do Estabelecimento Centralizador.  Tabela ICP_INSC_EST_CENTR:  Campo COD_ESTAB: Estabelecimentos Centralizados; Campo COD_ESTAB_CENTR: Estabelecimento Centralizador.      Se a opção selecionada for “Não”:  Será considerado somente as Notas Fiscais do estabelecimento selecionado em tela.                         [MFS57858] Regra para Bloquear Geração de um CFOP, para códigos adicionais diferentes. [MFS80289] Regra para Desbloquear Geração de um CFOP, para códigos adicionais diferentes.  Verificar se o CFOP está parametrizado para mais de um código adicional para os Anexos V.A e V.B         SE sim criar log de aviso:  Aviso: CFOP “XXXX” parametrizado para códigos adicionais diferentes, para o Anexo V.A ou V.B, para evitar duplicidades preencher o Campo 255 - COD_BENEFICIO da Tabela SAFX08 ou utilizar o Parâmetro de CFOP/Natureza de Operação.                                     SE sim bloquear geração do CFOP.           Criar log de erro:  Aviso: CFOP “XXXX” parametrizado para códigos adicionais diferentes, para evitar duplicidade utilizar o Parâmetro de CFOP/Natureza de Operação.   Alteração MFS-59693: Criado o parâmetro “Considerar campo de Código do Benefício - SAFX08 (campo 255)” na tela dos Dados Iniciais do Sped Fiscal:       - Parâmetro desmarcado – A geração do Registro E115 permanecerá conforme regra original, desconsiderando a regra do Campo 255 – Código do Benefício.      - Parâmetro marcado – A geração do Registro E115 passará a considerar o Campo 255 – Código do Benefício da tabela SAFX08, conforme regra abaixo:  - Campo Código do Benefício (SAFX08, Campo 255 – COD_BENEFICIO):                SE o Campo 255 – COD_BENEFICIO da tabela DWT_ITENS_MERC estiver preenchido;                     E o código do benefício estiver cadastrado no módulo EFD-Escrituração Fiscal Digital >> Informações Adicionais da Apuração (Registro E115/1925). (Tabela/Campo do Parâmetro: Tabela EFD_INF_ADIC_APUR, Campo COD_INF_ADIC);                                             (Relacionamento entre as tabelas:  DWT_ITENS_MERC.COD_BENEFICIO = EFD_INF_ADIC_APUR.COD_INF_ADIC);                                     Então seguir com a sequência das próximas regras;                             Senão desconsiderar o item na geração do Registro E115. | MFS-13074 MFS-57858 MFS-59693 MFS-67999 |
| RN01 | Critério p/ Recuperação dos Dados – Anexo I.C  Origem: SAFX07/08, SAFX2013, TACES51, TACES86, TACES87.   Seleção das notas fiscais (SAFX07/SAFX08):   Empresa – empresa do login Estabelecimento – estabelecimento da geração No caso de geração por I.E.U, se o indicador da “Geração p/ Inscrição Estadual Única” estiver igual a SIM, serão considerados os documentos de todos os estabelecimentos envolvidos na centralização, (centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle das Obrigações Estaduais; Somente notas fiscais de entrada (campo MOVTO_E_S da SAFX07 <> 9); Data fiscal referente ao período inicial e final preenchido na tela de geração; Classificação do documento = ‘1’ ou ‘3’ (campo COD_CLASS_DOC_FIS da SAFX07); Situação da nota <> S (campo SITUACAO da SAFX07); Somente notas fiscais com item; Somente notas fiscais com CFOP ou CFOP/Natureza de Operação parametrizado no menu “Parâmetros  Registros E115 e 1925  Registro E115”, exceto os CFOP que estiverem cadastrados na TACES51 com o campo Excluída igual a “Não”, pois esses devem ser ignorado da geração; | MFS-13074 |
| RN02 | Processamento dos Dados – Anexo I.C  As informações não serão agrupadas porque o campo sequencial é campo chave na tabela, para cada código parametrizado gravar o registro na tabela.  Por ser uma pré-geração, as informações precisam ser alimentadas na tabela Registro E115/1925 (Valores Declaratórios) do menu  “Geração  Manutenção  Registro E115/1925 (Valores Declaratórios)”. | MFS-13074 CH_5484_2018 (MFS-17456) |
| RN03 | Critério p/ Recuperação dos Dados – Anexo V.A  [ALTERADA – MFS-23315] [MFS-40746: inclusão da classificação do documento = ‘4’] Origem: SAFX07/08/09, TACES51.   Seleção das notas fiscais (SAFX07/SAFX08/SAFX09):   Empresa – empresa do login Estabelecimento – estabelecimento da geração No caso de geração por I.E.U, se o indicador da “Geração p/ Inscrição Estadual Única” estiver igual a SIM, serão considerados os documentos de todos os estabelecimentos envolvidos na centralização, (centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle das Obrigações Estaduais; Somente notas fiscais de saída (campo MOVTO_E_S da SAFX07 = 9); Data fiscal referente ao período inicial e final preenchido na tela de geração; Classificação do documento = ‘1’ ou ‘3’ ou ‘4’ (campo COD_CLASS_DOC_FIS da SAFX07); Situação da nota <> S (campo SITUACAO da SAFX07); Somente notas fiscais com item; Somente notas fiscais com CFOP ou CFOP/Natureza de Operação parametrizado no menu “Parâmetros  Registros E115 e 1925  Registro E115”, exceto os CFOP que estiverem cadastrados na TACES51 com o campo Isentas igual a “Não”, pois esses devem ser ignorados da geração;  Atenção: Notas fiscais sem item deverão ser considerados os conteúdos informados na capa. | MFS-13074 MFS-23315 |
| RN04 | Processamento dos Dados – Anexo V.A  As informações não serão agrupadas porque o campo sequencial é campo chave na tabela, para cada código parametrizado gravar o registro na tabela.  Por ser uma pré-geração, as informações precisam ser alimentadas na tabela Registro E115/1925 (Valores Declaratórios) do menu  “Geração  Manutenção  Registro E115/1925 (Valores Declaratórios)”. | MFS-13074 CH_5484_2018 (MFS-17456) MFS-23315 |
| RN05 | Critério p/ Recuperação dos Dados – Anexo V.B  [ALTERADA – MFS-23315] [MFS-40746: inclusão da classificação do documento = ‘4’]  Origem: SAFX07/08/09, TACES51.   Seleção das notas fiscais (SAFX07/SAFX08/SAFX09):   Empresa – empresa do login Estabelecimento – estabelecimento da geração No caso de geração por I.E.U, se o indicador da “Geração p/ Inscrição Estadual Única” estiver igual a SIM, serão considerados os documentos de todos os estabelecimentos envolvidos na centralização, (centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle das Obrigações Estaduais; Somente notas fiscais de saída (campo MOVTO_E_S da SAFX07 = 9); Data fiscal referente ao período inicial e final preenchido na tela de geração; Classificação do documento = ‘1’ ou ‘3’ ou ‘4’ (campo COD_CLASS_DOC_FIS da SAFX07); Situação da nota <> S (campo SITUACAO da SAFX07); Somente notas fiscais com item; Somente notas fiscais com CFOP ou CFOP/Natureza de Operação parametrizado no menu “Parâmetros  Registros E115 e 1925  Registro E115”, exceto os CFOP que estiverem cadastrados na TACES51 com o campo Outras igual a “Não”, pois esses devem ser ignorados da geração;  Atenção: Notas fiscais sem item deverão ser considerados os conteúdos informados na capa. | MFS-13074 MFS-23315 |
| RN06 | Processamento dos Dados – Anexo V.B  As informações não serão agrupadas porque o campo sequencial é campo chave na tabela, para cada código parametrizado gravar o registro na tabela.  Por ser uma pré-geração, as informações precisam ser alimentadas na tabela Registro E115/1925 (Valores Declaratórios) do menu  “Geração  Manutenção  Registro E115/1925 (Valores Declaratórios)”. | MFS-13074 CH_5484_2018 (MFS-17456) MFS-23315 |
| RN07 | Critério p/ Recuperação dos Dados – Anexo V.C  [MFS-40746: inclusão da classificação do documento = ‘4’]  Origem: SAFX07/08, SAFX2013, TACES51, TACES86, TACES87.   Seleção das notas fiscais (SAFX07/SAFX08):   Empresa – empresa do login Estabelecimento – estabelecimento da geração No caso de geração por I.E.U, se o indicador da “Geração p/ Inscrição Estadual Única” estiver igual a SIM, serão considerados os documentos de todos os estabelecimentos envolvidos na centralização, (centralizador e centralizados), de acordo com a parametrização da centralização por Inscrição Estadual Única do Módulo de Controle das Obrigações Estaduais; Somente notas fiscais de saída (campo MOVTO_E_S da SAFX07 = 9); Data fiscal referente ao período inicial e final preenchido na tela de geração; Classificação do documento = ‘1’ ou ‘3’ ou ‘4’ (campo COD_CLASS_DOC_FIS da SAFX07); Situação da nota <> S (campo SITUACAO da SAFX07); Somente notas fiscais com item; Somente notas fiscais com CFOP ou CFOP/Natureza de Operação parametrizado no menu “Parâmetros  Registros E115 e 1925  Registro E115”, exceto os CFOP que estiverem cadastrados na TACES51 com o campo Excluída igual a “Não”, pois esses devem ser ignorado da geração; | MFS-13074 |
| RN08 | Processamento dos Dados – Anexo V.C  As informações não serão agrupadas porque o campo sequencial é campo chave na tabela, para cada código parametrizado gravar o registro na tabela.  Por ser uma pré-geração, as informações precisam ser alimentadas na tabela Registro E115/1925 (Valores Declaratórios) do menu  “Geração  Manutenção  Registro E115/1925 (Valores Declaratórios)”. | MFS-13074 CH_5484_2018 (MFS-17456): |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | MFSNNNN |
| --- | --- | --- |

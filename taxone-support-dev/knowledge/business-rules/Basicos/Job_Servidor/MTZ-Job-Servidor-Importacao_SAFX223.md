# MTZ-Job-Servidor-Importacao_SAFX223

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX223.docx
- **Modificado:** 2022-07-22
- **Tamanho:** 74 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX223

Tabela das Guias de Recolhimento do ICMS Diferencial de Alíquota UF Orig/Dest \(EC 87/15\) 

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS2132

Atendimento ao Ato Cotepe/ICMS 44/2015

Criação da nova tabela SAFX223 para a importação das guias de recolhimento da Apuração do ICMS Diferencial de Alíquota UF Origem/Destino \(EC 87/15\)\. 

MFS2824

Atendimento a Portaria DF 228/2015

Este documento tem como objetivo incluir o campo Observação em atendimento a Portaria 228/2015 para geração do Registro E350 referente à EC 87/2015\.

MFS2109

Ajustes para tratar a apuração por I\.E\.U\.

Ajustes para tratar a apuração por Inscrição Estadual Única\.

CH6619\_2016

Inclusão de campo chave

Este documento tem como objetivo incluir o campo Código Obrigação como chave na tabela para aceitar que a mesma Guia receba códigos de obrigação diferentes\.

MFS90023

Sped Fiscal 2023

Aumento do tamanho do campo Número do Processo para 60 posições \(RN13\)

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

Estrutura da tabela SAFX223 🡪 vide manual de layout

__\[ALTERADA – CH6619\_2016\]__

Campos que compõe a chave da tabela:

__Código da Empresa__ \+ __Código do Estabelecimento__ \+ __Obrigação Fiscal__ \+ __Data da Apuração__ \+ __UF__ \+ __Número da Guia de Recolhimento \+ Código Obrigação__

Tabela definitiva:

Tabela das guias de recolhimento da aba “Guias de Recolhimento” da rotina de manutenção dos lançamentos complementares específica da Apuração do ICMS Diferencial de Alíquota UF Origem/Destino, localizada no módulo ICMS, menu Apuração 🡪 Apuração do ICMS 🡪 Lançamentos Complementares 🡪 Apuração do ICMS Dif\. Aliq\. UF Origem/Destino \(EC 87/15\)\.

 

*\(ver estrutura da tabela definitiva no documento de regras da manutenção citada acima\)*

Conforme padrão, a tabela definitiva tem os campos de controle da importação de tabelas SAFX:

\- Indicador de Gravação \(IND\_GRAVACAO\) 

\- Número do Processo da Importação \(NUM\_PROCESSO\) 

Para as guias importadas 🡪 o IND\_GRAVACAO será gravado com “1” 

Para as guias alteradas pela importação 🡪 o IND\_GRAVACAO será gravado com “2” 

Mensagens de erro:

Sempre que o registro a ser importado for rejeitado, será gerada uma mensagem no log, e os dados de identificação da guia \(campos chave\) serão demonstrados corretamente, para possibilitar ao usuário identificar o registro rejeitado\.   

 

MFS2132

CH6619\_2016

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

Quando o campo não estiver preenchido,* *o registro não será importado e no log de erros será gravada mensagem de erro padrão:

*                                                      “O código da empresa deve ser preenchido”*

MFS2132

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

Quando o campo não estiver preenchido,* *o registro não será importado e no log de erros será gravada mensagem de erro padrão:

*                                                      “O código do estabelecimento deve ser preenchido”*

MFS2132

__RN03__

__Campo Obrigação Fiscal__

Campo de preenchimento obrigatório\.

Deve ser preenchido com o código do livro fiscal “108” \(Livro de Apuração\)\.

Alteração da __MFS2901__: Incluído tratamento do livro “165”\.

Deve ser preenchido com o código do livro fiscal “108” \(Livro de Apuração\) ou “165” \(Livro de Apuração por Inscrição Estadual Única\)\.

 

Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “O código da obrigação fiscal deve ser 108 *__*ou 165*__*”*

MFS2132

__RN04__

__Campo Data da Apuração__

Campo de preenchimento obrigatório\.

Quando não preenchido, ou quando for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “Data da apuração não preenchida ou inválida”*

Serão consideradas apenas as apurações agendadas \(CALEN\_OBRIGACAO\) e já registradas na tabela APURACAO, e ainda não validadas\. Por isso serão realizadas as seguintes críticas:

Crítica da existência da apuração: Será verificada a existência da apuração em questão, ou seja, se já existe uma apuração gerada para a Empresa, Estabelecimento, Obrigação Fiscal e Data da Apuração\. 

Caso não exista, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                   “Não existe apuração gerada p/o estabelecimento e data informados”*

Crítica do status da apuração: Se o status da apuração for = “Válido”, então o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                       “Não é permitida a importação de guias para apurações já validadas”*

MFS2132

__RN05__

__Campo UF __

Campo de preenchimento obrigatório\.

O conteúdo deve ser uma UF válida, de acordo com a lista das UF’s da tabela ESTADOS\. 

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                   * *“Código da Unidade da Federação não preenchido ou inválido”*

MFS2132

__RN06__

__Campo Número da Guia de Recolhimento __

Campo de preenchimento obrigatório\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                  * *“O número da guia de recolhimento é de preenchimento obrigatório\. Consultar orientações no manual de layout”*

MFS2132

__RN07__

__Campo Valor __

Campo de preenchimento obrigatório\.

Quando não preenchido ou = zero, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                         “Valor da guia não informado ou igual à zero”*

MFS2132

__RN08__

__Campo Data Vencimento __

Campo de preenchimento obrigatório\.

Quando não preenchido, ou quando for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                        “Data do vencimento não preenchida ou inválida”*

MFS2132

__RN09__

__Campo Mês/Ano Referência __

Campo de preenchimento __*não*__ obrigatório\.

Se preenchido, será verificada a validade do mês e do ano informados, e quando a informação for inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                                                                     “Mês/Ano Referência inválido”*

MFS2132

__RN10__

__Campo Código Obrigação __

Campo de preenchimento obrigatório\.

__\[ALTERADA – MFS 2898\]__

Deve ser um código válido de acordo com a tabela “5\.4\-Tabela de Códigos do ICMS a Recolher” do Sped Fiscal:

   000\-ICMS a Recolher

   001\-ICMS da substituição tributária pelas entradas

   002\-ICMS da substituição tributária pelas saídas p/o estado

   003\-Antecipação do diferencial de alíquota do ICMS

   004\-Antecipação do ICMS da importação

   005\-Antecipação tributária

   006\- ICMS resultante da alíquota adicional dos itens incluídos no Fundo de Combate a Pobreza

<a id="OLE_LINK152"></a><a id="OLE_LINK153"></a>   020\-ICMS \- Diferença de Alíquota referente à EC 87/2015

   090\-Outras obrigações do ICMS 

   999\-ICMS da substituição tributária pelas saídas p/outro estado

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*     “O Código Obrigação deve ser preenchido de acordo com a tabela “5\.4\-Tabela de Códigos do ICMS a Recolher” do Sped Fiscal”*

MFS2824

__RN11__

__Campo Código da Receita__

Campo de preenchimento obrigatório\.

Deve ser um código válido de acordo com a Tabela de Códigos de Receita Estadual \(SAFX2080\)\.

O código informado deve atender as seguintes condições:

  \- Deve ser da mesma UF informada na guia, ou seja, a UF da SAFX2080 deve ser a mesma informada no campo “05\-UF” da guia;

  \- Deve ser um código válido para o período da apuração em questão, ou seja, a data de validade da SAFX2080 deve ser < = data da

    apuração informada no campo “04\-Data da Apuração” da guia;\.

Quando o código não for preenchido, ou não atender as regras descritas acima, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*                              “Código da Receita não preenchido, inexistente para a UF, ou inválido para a data da apuração”*

MFS2132

__RN12__

__Campo Descrição Complementar __

Campo de preenchimento __*não*__ obrigatório\.

MFS2132

__RN13__

__Campo Número do Processo__

Campo de preenchimento __*não*__ obrigatório\.

Quando o número do processo é preenchido, a origem do processo também deve ser informada\. Caso o número seja informado e a origem não, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

                                    *“Ao informar o número do processo, a origem do processo também deve ser informada”*

MFS2132

__RN14__

__Campo Origem do Processo __

Campo de preenchimento __*não*__ obrigatório\.

Se preenchido, deve ser uma das opções descritas abaixo\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem: *“Origem do Processo inválida \(deve ser = 0, 1, 2 ou 9\)”*

                    = “0” \(Sefaz\)

                    = “1” \(Justiça Federal\)

                    = “2” \(Justiça Estadual\)

                    = “9” \(Outros\)

 

Quando a origem do processo é preenchida, o número do processo também deve ser informado\. Caso a origem seja informada e o número não, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

                                    *“Ao informar a origem do processo, o número do processo também deve ser informado”*

MFS2132

__RN15__

__Campo Descrição do Processo __

Campo de preenchimento __*não*__ obrigatório\.

MFS2132

__RN16__

__Campo Classe de Vencimento \(SC\) __

Campo de preenchimento __*não*__ obrigatório\.

Quando preenchido, serão feitas as seguintes críticas:

   \- Este campo deve ser utilizado apenas quando a UF da Guia for = SC\. Quando a UF não for SC, o registro não será importado, e 

     no log de erros será gravada a seguinte mensagem:

*                     “O campo Classe de Vencimento \(SC\) deve ser utilizado apenas quando a UF informada for SC”*

   \- O código informado deve existir na TACES80 \(Tabela das Classes de Vencimento\), e ser um código da UF de SC\. Caso o código

     não exista na tabela, não seja de SC, ou tenha data de validade incompatível com a data da apuração da Guia __\(\*\)__, o registro não 

     será importado, e no log de erros será gravada a seguinte mensagem:

*                                       “Classe de Vencimento \(SC\) inexistente ou inválida p/a data da apuração”*

__\(\*\)__ A data de validade inicial da TACES80 deve ser menor ou igual à data da apuração da guia, e a data de validade final deve ser maior ou igual à data da apuração da guia\.

MFS2132

__RN17__

__Campo Código de Identificação do Débito \(RJ\) __

Campo de preenchimento __*não*__ obrigatório\.

Quando preenchido, serão feitas as seguintes críticas:

   \- Este campo deve ser utilizado apenas quando a UF da Guia for = RJ\. Quando a UF não for RJ, o registro não será importado, e 

     no log de erros será gravada a seguinte mensagem:

*                   “O campo Código de Identificação do Débito \(RJ\) deve ser utilizado apenas quando a UF informada for RJ”*

   \- O código informado deve existir na TACES60 \(Tabela de Identificação de Débitos de ICMS\-RJ\)\. Caso o código não exista na 

     tabela, ou tenha data de validade incompatível com a data da apuração da Guia __\(\*\)__, o registro não será importado, e no log de erros

     será gravada a seguinte mensagem:

*                                       “Código de Identificação do Débito \(RJ\) inexistente ou inválido p/a data da apuração”*

__\(\*\)__ A data de validade da TACES60 deve ser menor ou igual à data da apuração da guia\.

MFS2132

__RN18__

__Campo Observação __

Campo de preenchimento __*não*__ obrigatório, aceitar conteúdo informado inclusive nulo\.

Quando preenchido, serão feitas as seguintes críticas:

  \- Este campo, se informado, deve ter cadastro na SAFX2009 \- Cadastro de Observações \- Ato Cotepe/ICMS 35/05, caso não esteja cadastrado não será importado, e no log de erros será grava a seguinte mensagem:

*                                                                 “A Observação não foi cadastrada na SAFX2009”*

__Tratamento:__

Se o código de observação estiver cadastrado na SAFX2009 deve ser preenchido na guia com o código \+ descrição\.

MFS2824

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


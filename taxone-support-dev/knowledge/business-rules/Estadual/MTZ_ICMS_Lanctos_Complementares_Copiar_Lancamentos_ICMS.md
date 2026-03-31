# MTZ_ICMS_Lanctos_Complementares_Copiar_Lançamentos_ICMS

> Fonte: MTZ_ICMS_Lanctos_Complementares_Copiar_Lançamentos_ICMS.docx






THOMSON REUTERS

Módulo ICMS
Menu: Apuração >> Apuração do ICMS >> Lançamentos Complementares ICMS
Botão > Copiar Lançamentos



DOCUMENTO DE REQUISITO



REGRAS DE NEGÓCIO







Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:



| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS1943 | Criação do documento | Cópia das parametrizações já efetuadas nos Lançamentos Complementares para apuração e livro corrente. |


| CÓD | DESCRIÇÃO | MFS/CH |
| --- | --- | --- |
| RN00 |  |  |
| RN01 | Processamento dos Dados  Origem dos dados da aba Lançamentos de Valores dos Lançamentos Complementares:  - Módulo ICMS > menu “Apuração > Apuração do ICMS > Lançamentos Complementares > Apuração ICMS > Ajuste SINIEF > Aba Lançamentos de Valores”, campos  “Data Apuração, Operação Apuração, Descrição, Classe Lançamento, Amparo/Texto/Ocorrencia, Subitem Amp./Texto/Ocor. e Código de Ajuste (Sped Fiscal – Reg E11/E220).” - Tabela Discriminação Item de Apuração (ITEM_APURAC_DISCR) para o Tipo de Livro = ‘108’ - Apuração Normal (COD_TIPO_LIVRO = ‘108’)  O processamento é por Estabelecimento. | MFS1943 |
| RN02 | Critérios para a recuperação dos Lançamentos:  Para cada Estabelecimento e Período selecionado em tela:   Passo 1: Recuperação dos parâmetros da aba Lançamentos de Valores: Serão recuperados os dados da parametrização (ITEM_APURAC_DISCR) do estabelecimento: DAT_APURACAO, COD_OPER_APUR, DSC_ITEM_APURACAO, COD_CLASSE, COD_AMPARO_LEGAL, COD_SUB_ITEM_OCORR, COD_AJUSTE_ICMS considerando os seguintes critérios:      COD_EMPRESA  código da Empresa do login      COD_ESTAB  código do estabelecimento selecionado      DAT_APURACAO  de acordo com o mês/ano informado em tela  Caso todos os campos sejam iguais deverá ser consolidado e apresentado apenas um lançamento para seleção.   Passo 2: Gravar na tabela de Item de Apuração (ITEM_APURAC_DISCR) e efetuar um novo lançamento a cada registro de lançamento selecionado em tela, com os seguintes dados: | MFS1943 |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | MFSNNNN |
| --- | --- | --- |

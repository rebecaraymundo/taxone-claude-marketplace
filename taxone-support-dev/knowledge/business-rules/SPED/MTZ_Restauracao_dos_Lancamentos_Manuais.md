# MTZ_Restauracao_dos_Lancamentos_Manuais

> Fonte: MTZ_Restauracao_dos_Lancamentos_Manuais.docx



## (EFD-PIS/PASEP – COFINS) – Restauração dos Lançamentos Manuais




DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO






| DR | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| OS3169-GE22 | Restauração dos Lançamentos Manuais | Será criado o processo de Restauração dos Lançamentos Manuais  para o Módulo do SPED PIS/PASEP – COFINS | 10/01/2012 |
| OS3619 | Restauração dos Lançamentos Manuais | Incluir no processo de restauração, os registros M220 e M620 que forem incluídos na base através da opção Upload criada na tela de ‘Apuração PIS/PASEP’ e ‘Apuração COFINS’ | 25/05/2012 |
| OS3554 | Restauração dos Lançamentos Manuais | Incluir no processo de restauração, os registros M230/M630 e M300/M700 que forem incluídos na base através da opção Upload criada na tela de ‘Apuração PIS/PASEP’ e ‘Apuração COFINS’ | 28/06/2012 |
| OS4594 | Elenilson Coutinho | Incluir no processo de restauração, os registros M115/M515, M205/M605 e M225/M625, que forem incluídos na base através da opção Upload criada na tela de ‘Apuração PIS/PASEP’ e ‘Apuração COFINS’. | 21/08/2014 |


| Cód. |  | DR |
| --- | --- | --- |
| RN00 | Criar um processo de Restauração dos Lançamentos Manuais no Menu: Obrigações do Módulo: SPED / EFD – Escrituração Fiscal Digital – PIS/PASEP-COFINS    Estrutura do Menu:  Automação de Devolução/Vendas Canceladas  Geração dos Registros Restauração dos Lançamentos Manuais – Após Reabertura da Apuração Manutenção Demonstrativos Geração do Meio Magnético  Status da Obrigação | OS3169-GE22 |
| RN01 | Vinculação Automática dos Registros de Manutenção Após o reprocesso da geração dos registros ( devido alguma alteração ou reabertura  do período), se o usuário desejar manter as manutenções existentes, será necessário executar o Processo de Restauração dos Lançamentos Manuais.  Esta rotina  irá recuperar os registros de manutenção que possuírem os mesmos campos chaves do registro pai (que foi processado novamente), gravando as manutenções nas tabelas definitivas. As manutenções que não forem vinculadas automaticamente pelo processo (por terem sofrido alguma alteração no tipo de credito, por exemplo), serão desconsideradas na geração e neste caso, o usuário deverá revisar se há ou não a necessidade de incluir/alterar as manutenções. IMPORTANTE: Esta rotina foi criada (para ser executada depois de reprocessar a geração dos registros), evitando  a perda das manutenções existentes, de uma Apuração Realizada ou Reaberta. LOG DO PROCESSO:  1 - Ao executar o processo, caso não seja encontrada nenhuma manutenção existente para os registros selecionados, estabelecimento e período, deverá ser exibida a seguinte msg por registro: “Não foi encontrada nenhuma manutenção para o estabelecimento/período informado.” 2 - Ao executar o processo, caso exista manutenção para os registros selecionados, estabelecimento e período, mas se o sistema não conseguir vincular nenhuma manutenção com o registro pai, deverá ser exibida a seguinte msg por registro: “Não foi possível, vincular nenhuma manutenção, efetuada anteriormente a última geração dos registros, a um registro pai correspondente”  3 - Ao executar o processo, caso todas as manutenções tenham sido vinculadas, para os registros selecionados,  estabelecimento e período, deve ser emitida a seguinte msg por registros: “Todas as manutenções efetuada anteriormente a última geração dos registros foram vinculadas a um registro pai correspondente”  4 - Relatório de Conferência disponível na tela de Restauração dos Lançamentos Manuais : Ao executar o processo e alguma  manutenção não foi identificada pela nova rotina, deverá ser criado um relatório mostrando os registros que não foram vinculados pelo processo ao registro pai correspondente e um totalizador informando quantas manutenções foram associadas. Devem ser criados 5 relatórios, um para cada dupla de registros (M110/M510, M115/M515, M205/M605, M211/M611, M220/M620, M225/M625, M230/M630 e M300/M700). Cada relatório irá demonstrar detalhadamente, os registros que foram restaurados e  os não restaurados, com seus respectivos totais. Se na vinculação do registro que está sendo lido da tabela temporária, já existir na tabela definitiva (M110, M115, M205 M211, M220, M225, M230, M300), o registro não será vinculado. Dar mensagem de aviso. | OS3169-GE22 |
| RN02 | Os registros que foram identificados pela nova rotina são excluídos da tabela temporária e os registros que permanecerem na tabela por não terem sido associados automaticamente pelo sistema (para seu respectivo pai), serão desconsiderados, assim que o status da apuração for FECHADA. | OS3169-GE22 |
| RN03 | Incluir no processo de restauração, os registros M220 e M620 que forem incluídos na base através da opção Upload criada na tela de ‘Apuração PIS/PASEP’ e ‘Apuração COFINS’  no Módulo: SPED EFD – Escrituração Fiscal Digital das Contribuições, Menu: Obrigações   Manutenção, dentro das opções ‘Contribuição para PIS/PASEP no Período – M200 / Detalhamento da Contribuição – M210’ e ‘Contribuição para COFINS no Período – M600 / Detalhamento da Contribuição – M610’ | OS3619 |
| RN04 | Incluir no processo de restauração, os registros M230/M630 e M300/M700 que forem incluídos na base através da opção Upload criada na tela de ‘Apuração PIS/PASEP’ e ‘Apuração COFINS’  no Módulo: SPED EFD – Escrituração Fiscal Digital das Contribuições, Menu: Obrigações   Manutenção, dentro das opções ‘Contribuição para PIS/PASEP no Período – M200 / Detalhamento da Contribuição – M210’ e ‘Contribuição para COFINS no Período – M600 / Detalhamento da Contribuição – M610’ | OS3554 |
| RN05 | Incluir no processo de restauração, os registros M115/M515, M205/M605 e M225/M625 que forem incluídos na base através da opção Upload criada na tela de ‘Apuração PIS/PASEP’ e ‘Apuração COFINS’ no Módulo: SPED EFD – Escrituração Fiscal Digital das Contribuições, Menu: Obrigações   Manutenção, dentro das opções ‘Contribuição para PIS/PASEP no Período – M200 / Detalhamento da Contribuição – M210’ e ‘Contribuição para COFINS no Período – M600 / Detalhamento da Contribuição – M610’ | OS4594 |

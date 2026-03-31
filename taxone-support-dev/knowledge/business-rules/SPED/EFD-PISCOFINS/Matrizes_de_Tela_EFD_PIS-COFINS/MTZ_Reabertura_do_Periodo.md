# MTZ_Reabertura_do_Periodo 

- **Fonte:** MTZ_Reabertura_do_Periodo .docx
- **Modificado:** 2020-03-11
- **Tamanho:** 37 KB

---

    

#  \(EFD\-PIS/PASEP – COFINS\) – Reabertura de Período

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3169\-GE22

Reabertura de Período

Será criado o processo para a Reabertura de Período para o Módulo do SPED PIS/PASEP – COFINS – Tela Status da Obrigação

27/10/2011

OS3169\-GE22

Reabertura de Período

Serão consideradas as manutenções no processo da Reabertura do Período\.

27/10/2011

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__ Reabertura da Apuração__

__Passo 1 – Cópia dos dados inseridos através de manutenção__

Este passo será efetuado com intuito de armazenarmos os registros M110, M211, M220, M230, M300, M350, M510, M611, M620, M630 e  M700 para uso futuro, portanto, devemos fazer uma cópia destes registros para que após um novo reprocessamento os mesmos estejam disponíveis para serem lançados novamente na apuração\.

O sistema deverá manter em uma tabela temporária todos os registros de manutenção citados acima dos meses que foram reabertos/excluídos\.

OS3169\-GE22A

__RN00__

__Passo 2 – Restaurar créditos utilizados para desconto na apuração__

Este passo tem por objetivo restaurar os valores dos créditos que tenham sido utilizados para desconto na apuração a ser reaberta\. Os créditos utilizados estarão informados através da opção de menu “*Obrigações  Manutenção  Controle dos Créditos Fiscais \(PIS/PASEP e COFINS\)  Créditos Disponíveis*” do módulo SPED – EFD\-PIS/PASEP\-COFINS\. 

__COFINS __

Neste passo, no campo Crédito Disponível, somar os valores dos campos Crédito Disponível, Crédito Utilizado para Desconto, Crédito Utilizado por  Pedido de Ressarcimento, Crédito Utilizado por  Compensação Intermediária, Crédito Utilizado por  Transferência \(cisão, fusão ou incorporação\), Outros Créditos Utilizados\.

Zerar os campos: Crédito Utilizado para Desconto, Crédito Utilizado por  Pedido de Ressarcimento, Crédito Utilizado por  Compensação Intermediária, Crédito Utilizado por  Transferência \(cisão, fusão ou incorporação\), Outros Créditos Utilizados  \(se utilizado em um dos meses que foram reabertos\)\.

Manter o valor do campo Crédito Extemporâneo\.

Manter o Status \(do mês anterior ao período que está sendo reaberto\)\.

__PIS/PASEP__

Neste passo, no campo Crédito Disponível, somar os valores dos campos Crédito Disponível, Crédito Utilizado para Desconto, Crédito Utilizado por  Pedido de Ressarcimento, Crédito Utilizado por  Compensação Intermediária, Crédito Utilizado por  Transferência \(cisão, fusão ou incorporação\), Outros Créditos Utilizados\.

Zerar os campos: Crédito Utilizado para Desconto, Crédito Utilizado por  Pedido de Ressarcimento, Crédito Utilizado por  Compensação Intermediária, Crédito Utilizado por  Transferência \(cisão, fusão ou incorporação\), Outros Créditos Utilizados  \(se utilizado em um dos meses que foram reabertos\)\.

Manter o valor do campo Crédito Extemporâneo\.

Manter o Status \(do mês anterior ao período que está sendo reaberto\)\.

OS3169\-GE22

__RN00__

__Passo 3 – Restaurar retenções utilizadas para dedução na apuração__

Este passo tem por objetivo restaurar os valores das deduções que tenham sido utilizadas para desconto na apuração a ser reaberta\. As deduções utilizados estarão informados através da opção de menu “*Obrigações  Manutenção  Controle das Retenções na Fonte \(PIS/PASEP e COFINS\)  Retenções Disponíveis*” do módulo SPED – EFD\-PIS/PASEP\-COFINS\. 

__COFINS __

Neste passo, no campo Retenção Disponível, somar os valores dos campos Retenção Deduzida da Contribuição, Retenção Utilizada por Pedido da Restituição, Retenção Utilizada por Declaração de Compensação\.

Zerar os campos: Retenção Deduzida da Contribuição, Retenção Utilizada por Pedido da Restituição, Retenção Utilizada por Declaração de Compensação 

__PIS/PASEP__

Neste passo, no campo Retenção Disponível, somar os valores dos campos Retenção Deduzida da Contribuição, Retenção Utilizada por Pedido da Restituição, Retenção Utilizada por Declaração de Compensação\.

Zerar os campos: Retenção Deduzida da Contribuição, Retenção Utilizada por Pedido da Restituição, Retenção Utilizada por Declaração de Compensação 

__Passo 4 – Exclusão dos créditos utilizados__

Neste passo realizar a exclusão dos registros de créditos utilizados contidos na opção de menu “*Obrigações  Manutenção  Controle dos Créditos Fiscais \(PIS/PASEP e COFINS\)  Créditos a Utilizar na Apuração*” do módulo SPED – EFD\-PIS/PASEP\-COFINS, quadro “*Crédito\(s\) a ser\(em\) Utilizado\(s\) nesse período*”\.

OS3169\-GE22

__RN00__

__Passo 5 – Exclusão das retenções utilizadas__

Neste passo realizar a exclusão dos registros de retenções utilizadas contidos na opção de menu “*Obrigações  Manutenção  Controle das Retenções na Fonte \(PIS/PASEP e COFINS\)  Retenções a Utilizar na Apuração*” do módulo SPED – EFD\-PIS/PASEP\-COFINS, quadro “*Retenções\(s\) a ser\(em\) Utilizada\(s\) nesse período*”\.

__Passo 6 – Apagar os registros de Apuração gerados automaticamente pela a funcionalidade Geração dos Registros __

\- Para o processo de reabertura de período apagar todos os registros M100, M105,M200,M210,M500,M505,M600 e M610, até chegar no mês \(período\) que o cliente precisar reabrir\. 

\- Apagar todos os registros 1100 que foram gerados com base no registro M100 \(ind\_desc\_cred = 1 \) 

\- Apagar todos os registros 1500 que foram gerados com base no registro M500 \(IND\_DESC\_CRED = ‘’1’’\) 

\- Apagar todos os registros 1300  e 1700\.

Exemplo: Existem gerações até o mês de novembro/2011 e o cliente precisa reabrir fevereiro/2011, neste caso, o sistema deverá apagar todos os registros citados, dos meses de novembro/11 à fevereiro/11\.

OS3169\-GE22

__RN01__

__Processo Exclusão __

O processo de exclusão \(que só é permitido para apurações com Status__ ‘Apuração__ __Reaberta’ e ‘Apuração Realizada’__\) deve seguir o mesmo fluxo da reabertura, partindo do passo 2\. 

OS3169\-GE22

__RN02__

__Vinculação dos Registros de Manutenção__

A partir do momento que for reprocessada a geração dos registros \( do período que foi reaberto\), o sistema deve vincular os registros de manutenção que possuírem os mesmos campos chaves do registro pai \(que estarão armazenados em uma tabela temporária\), gravando esses registros nas tabelas definitivas novamente\. 

Os registros que forem identificados são excluídos da tabela temporária e os registros que permanecerem na tabela por não terem sido associados automaticamente pelo sistema \(para seu respectivo pai\), ficarão disponíveis para o usuário efetuar as associações na tela de Apuração PIS/PASEP e COFINS \(se necessário\)\. 

Quando o status da apuração for __FECHADA__, se existir algum registro nas tabelas temporárias, os dados serão excluídos\.

 

No log da geração do meio magnético deverá ser exibida a seguinte msg para os registros de manutenção que não foram identificados automaticamente pelo sistema: Existe manutenções que não foram associadas ao registro XXX, favor efetuar a associação desses registros, através das telas de Apuração ou essas manutenções serão desconsideradas na geração do meio magnético\.

OS3169\-GE22A


# MTZ-OTF-Relatório de Tributos Federais-Por Empresa

> Fonte: MTZ-OTF-Relatório de Tributos Federais-Por Empresa.docx


## Obrigações de Tributos Federais – Relatório de Tributos Federais >> Por Empresa





DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO





Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:


Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:



| DR | Nome | Descrição |
| --- | --- | --- |
| CH95931 | Campo Valor dedução do relatório | Na geração do relatório de Tributos Federais o dado do campo Valor Dedução deve ser gravado considerando o total dos campos 29,30,41 e 42 da SAFX53, |
| OS3753-E | Obrigações de Tributos Federais - Desconsiderar Retenções com Estorno do Relatório de Tributos Federais e do Relatório de Rastreabilidade de Retenções | O cliente Caixa Seguradora possui um processo interno de estorno de retenções. O conceito de estorno de retenções é quando o cliente deseja reaver o valor de uma retenção indevida. Isso pode ocorrer em três momentos distintos no produto:  Retenção sem DARF Gerado: esse é o caso mais simples, o cliente importou uma retenção no produto, porém antes mesmo de gerar o DARF referente a essa retenção, o cliente percebeu o erro.  Retenção com DARF Gerado e Não Pago: esse caso é o cenário principal do cliente, pois ele envia o DARF para pagamento e por motivos de erro no sistema bancário – exemplo: conta inválida ou encerrada, CPF inválido, entre outros – o pagamento não é processado. Nesse caso o cliente tem que estornar o valor no ERP (SAP) para que essa retenção não seja considerada em nenhuma obrigação acessória. Retenção com DARF Gerado e Pago: esse cenário já está resolvido dentro do sistema, pois se o cliente pagou um DARF indevidamente – a maior ou a menor – o cliente pode resolver essa situação através da funcionalidade de Tributos Ajustados já disponibilizada no produto.  A solução proposta foi a criação de dois campos de identificação na tabela de Controle de Tributos: “Estorno” e “Data do Estorno”. Esses campos identificam a retenção estornada e não permitem que a mesma seja considerada nas obrigações acessórias federais e relatórios de conferência do sistema. Vale salientar que esses campos citados anteriormente foram criados na OS3753. As rotinas do sistema que deverão ser alteradas são:  Obrigações Acessórias DARF DCTF DIRF Informe de Rendimentos Relatórios Gerenciais Relatório de Tributos Federais – OS3753-E Relatório de Rastreabilidade – OS3753-E  Hoje a rotina de importação do produto não permite a importação de uma retenção que tenha um DARF vinculado à mesma e que esteja Gerado/Não Pago ou Pago. Isso é um controle do sistema para garantir que um DARF fique diferente da retenção, ocasionando erros críticos para o cliente. Esse controle funciona assim de longa data e no passado já foram dados NO GO para que isso fosse permitido.  Com esse cenário do cliente, o sistema deverá permitir que na rotina de importação da tabela de Controle de Tributos – SAFX53 – o sistema ao identificar os campos “Estorno” e “Data do Estorno” preenchidos, o sistema deverá fazer a seguinte identificação:  Retenção sem DARF Gerado: nesse caso a retenção será atualizada sem maiores ônus.  Retenção com DARF Gerado e Não Pago: nesse caso, o sistema irá identificar o DARF dessa retenção e irá à tabela X75_DCTF apagar esse DARF. Essa retenção e as outras associadas ao DARF que foi deletado, terão seu status alterado para “Não Gerado”. Essas retenções terão o campo “Estorno” e “Data do Estorno” informados. Retenção com DARF Pago: nesse caso o cliente deverá utilizar o sistema de acordo com a funcionalidade de Tributos Ajustados já existente no sistema.   É importante que no segundo ponto o DARF seja deletado, porque as retenções com Estorno não serão consideradas nas obrigações federais. Se isso não for desenvolvido ao gerar a DCTF o cliente irá ter uma Ficha de Pagamento (R11) sem uma Ficha de Débito vinculada.  O escopo da OS3753-E é permitir que os relatórios de Tributos Federais e Rastreabilidade de Retenções/DARF’s desconsiderem as retenções da tabela de Controle de Tributos que estejam estornadas. |
| OS4155 | Criação de um filtro na tela”Emissão de Tributos-Empresa.    Conforme Chamado nº 7452/2013, o cliente solicitou a inclusão de um campo “Data Vencimento”, no “Relatório de Tributos Federais – Por Empresa” | Conforme Chamado nº 7452/2013, o cliente solicitou a inclusão de um filtro na tela abaixo:  Tela “Emissão de Tributos – Empresa”. A inclusão de um fitro solucionará o tempo em que o cliente passa selecionando os código DARF que hoje é relizado pela barra de rolagem. Um botão “Pesquisar” faria o processo do filtro da tela acima.   O objetivo do campo “Data Vencimento” irá detalhar o “Relatório de Tributos Federais-Por Empresa”, com o novo campo “Data Vencimento”. |


| Cód. | Descrição | DR |
| --- | --- | --- |
| RN00 | Campo Valor Dedução  Deve se recuperar a soma dos campos da tabela SAFX53:  29 Valor de Previdência Privada (campo VLR_PREV_PRIVADA), 30 Valor de Pensão Alimentícia	(campo VLR_PENS_ALIMENT), 41 Valor de Deduções de INSS Terceiros (campo VLR_DED_INSS_TERC), 42 Valor da Dedução de Dependentes Terceiros (campo VLR_DED_DEP_TERC) | CH95931 |
| RN01 | Deve haver no relatório um aviso informando aos usuários que o campo valor dedução é a soma dos valores de Previdência Privada, Pensão Alimentícia, Deduções de INSS Terceiros e Dedução de Dependentes Terceiros. | CH95931 |
| RN02 | As Retenções da tabela X53_RETENCAO_IRRF, cujos campos “Estorno” e “Data do Estorno” estiverem preenchidos, não deverão ser consideradas para a geração do Relatório de Tributos Federais. Vale salientar que essas retenções não possuem registros de retificação. | OS3753-D |
| RN03 | Criar um botão “Pesquisar” para fazer o filtro dos códigos DARF no campo “Código Retenção” na tela de “Emissão de Tributos – Empresa”, de forma que o usuário possa fazer a seleção do código desejado. | OS4155 |
| RN04 | Após selecionar o código DARF no filtro, o campo “Código de Retenção” na tela “Emissão de Tributos-Empresa” receberá o código DARF selecionado pelo usuário. Obs: “Os criterios de recuperação do código DARF continuam o mesmo”. | OS4155 |
| RN05 | Criar um novo campo “Data Vencimento” para o “Relatório de Tributos Federais – Por Empresa”. | OS4155 |
| RN06 | A “Data Vencimento” receberá as informações do campo “Data Vencimento”, tela “Controle de Tributos”. | OS4155 |
| RN07 | O novo campo “Data Vencimento” deverá estar no “Relatório de Tributos Federais – Por Empresa”, ao lado do campo “Data Movimento”.  O campo Data Vencimento será exibido no formato normal – DD/MM/AAAA. | OS4155 |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |


| RN01 | [ALTERADA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |

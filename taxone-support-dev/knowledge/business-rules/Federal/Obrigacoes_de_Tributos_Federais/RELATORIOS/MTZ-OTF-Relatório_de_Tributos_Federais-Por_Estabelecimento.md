# MTZ-OTF-Relatório de Tributos Federais-Por Estabelecimento

- **Fonte:** MTZ-OTF-Relatório de Tributos Federais-Por Estabelecimento.docx
- **Modificado:** 2020-08-31
- **Tamanho:** 35 KB

---

# Obrigações de Tributos Federais – Relatório de Tributos Federais >> Por Estabelecimento

##### DOCUMENTO DE REQUISITO 

###### DR

###### Nome

__Descrição__

CH95931

Campo Valor dedução do relatório

Na geração do relatório de Tributos Federais o dado do campo Valor Dedução  deve ser gravado considerando o total dos campos 29,30,41 e 42 da SAFX53, 

CH115077

Exibição do Total da Alíquota e não do Arredondamento da mesma

O objetivo dessa alteração de regra de negócio é permitir que no campo descritivo “Total da Alíquota” do relatório  por Estabelecimento seja exibido o total da Alíquota e não um arredondamento\.

OS3753\-E

Obrigações de Tributos Federais \- Desconsiderar Retenções com Estorno do Relatório de Tributos Federais e do Relatório de Rastreabilidade de Retenções

O cliente Caixa Seguradora possui um processo interno de estorno de retenções\. O conceito de estorno de retenções é quando o cliente deseja reaver o valor de uma retenção indevida\. Isso pode ocorrer em três momentos distintos no produto:

- __Retenção sem DARF Gerado:__ esse é o caso mais simples, o cliente importou uma retenção no produto, porém antes mesmo de gerar o DARF referente a essa retenção, o cliente percebeu o erro\. 
- __Retenção com DARF Gerado e Não Pago:__ esse caso é o cenário principal do cliente, pois ele envia o DARF para pagamento e por motivos de erro no sistema bancário – exemplo: conta inválida ou encerrada, CPF inválido, entre outros – o pagamento não é processado\. Nesse caso o cliente tem que estornar o valor no ERP \(SAP\) para que essa retenção não seja considerada em nenhuma obrigação acessória\.
- __Retenção com DARF Gerado e Pago: __esse cenário já está resolvido dentro do sistema, pois se o cliente pagou um DARF indevidamente – a maior ou a menor – o cliente pode resolver essa situação através da funcionalidade de Tributos Ajustados já disponibilizada no produto\.

A solução proposta foi a criação de dois campos de identificação na tabela de Controle de Tributos: “Estorno” e “Data do Estorno”\. Esses campos identificam a retenção estornada e não permitem que a mesma seja considerada nas obrigações acessórias federais e relatórios de conferência do sistema\. Vale salientar que esses campos citados anteriormente foram criados na OS3753\. As rotinas do sistema que deverão ser alteradas são:

- Obrigações Acessórias
	- DARF
	- DCTF
	- DIRF
	- Informe de Rendimentos
- Relatórios Gerenciais
	- __Relatório de Tributos Federais – OS3753\-E__
	- __Relatório de Rastreabilidade – OS3753\-E__

Hoje a rotina de importação do produto não permite a importação de uma retenção que tenha um DARF vinculado à mesma e que esteja Gerado/Não Pago ou Pago\. Isso é um controle do sistema para garantir que um DARF fique diferente da retenção, ocasionando erros críticos para o cliente\. Esse controle funciona assim de longa data e no passado já foram dados NO GO para que isso fosse permitido\.

Com esse cenário do cliente, o sistema deverá permitir que na rotina de importação da tabela de Controle de Tributos – SAFX53 – o sistema ao identificar os campos “Estorno” e “Data do Estorno” preenchidos, o sistema deverá fazer a seguinte identificação:

- __Retenção sem DARF Gerado:__ nesse caso a retenção será atualizada sem maiores ônus\. 
- __Retenção com DARF Gerado e Não Pago:__ nesse caso, o sistema irá identificar o DARF dessa retenção e irá à tabela X75\_DCTF apagar esse DARF\. Essa retenção e as outras associadas ao DARF que foi deletado, terão seu status alterado para “Não Gerado”\. Essas retenções terão o campo “Estorno” e “Data do Estorno” informados\.
- __Retenção com DARF Pago:__ nesse caso o cliente deverá utilizar o sistema de acordo com a funcionalidade de Tributos Ajustados já existente no sistema\. 

É importante que no segundo ponto o DARF seja deletado, porque as retenções com Estorno não serão consideradas nas obrigações federais\. Se isso não for desenvolvido ao gerar a DCTF o cliente irá ter uma Ficha de Pagamento \(R11\) sem uma Ficha de Débito vinculada\.

O escopo da OS3753\-E é permitir que os relatórios de Tributos Federais e Rastreabilidade de Retenções/DARF’s desconsiderem as retenções da tabela de Controle de Tributos que estejam estornadas\.

OS4155

- Criação de um filtro na tela”Emissão de Tributos\-Estabelecimento\.
- Conforme Chamado nº 7452/2013, o cliente solicitou a inclusão de um campo “Data Vencimento”, no “Relatório de Tributos Federais – Por Estabelecimento”

- Conforme Chamado nº 7452/2013, o cliente solicitou a inclusão de um filtro na tela abaixo:

Tela “Emissão de Tributos – Estabalecimento”\.

A inclusão de um fitro solucionará o tempo em que o cliente passa selecionando os código DARF que hoje é relizado pela barra de rolagem\.

Um botão “Pesquisar” faria o processo do filtro da tela acima\.

- O objetivo do campo __“Data Vencimento”__ irá detalhar o “Relatório de Tributos Federais\-Por Estabelecimento”, com o novo campo “Data Vencimento”\.

OS4323

Criação de parâmetro “Considerar Estabelecimentos Sem Movimento”

<a id="OLE_LINK30"></a><a id="OLE_LINK31"></a><a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK51"></a><a id="OLE_LINK52"></a>Este documento tem como objetivo atender uma melhoria no Relatório de Tributos Federais por Estabelecimento, disponibilizando a parametrização “Considerar Estabelecimentos Sem Movimento” na geração, para que o usuário tenha a opção de demonstrar no relatório os estabelecimentos “Sem Movimento” no período\.

CH11726\_2015

Alteração do preenchimento do campo Nº AP \(<a id="OLE_LINK4"></a><a id="OLE_LINK5"></a>Número de Autorização do Pagamento\)

<a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a><a id="OLE_LINK17"></a><a id="OLE_LINK18"></a>Este documento tem como objetivo alterar o tamanho do campo Nº AP \(Número de Autorização do Pagamento\) de 08 para 10 posições\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Campo Valor Dedução

Deve se recuperar a soma dos campos da tabela SAFX53:

- 29 Valor de Previdência Privada \(campo VLR\_PREV\_PRIVADA\),
- 30 Valor de Pensão Alimentícia	\(campo VLR\_PENS\_ALIMENT\),
- 41 Valor de Deduções  de INSS Terceiros \(campo VLR\_DED\_INSS\_TERC\),
- 42 Valor da Dedução de Dependentes Terceiros \(campo VLR\_DED\_DEP\_TERC\)

CH95931

__RN01__

Deve haver no relatório um aviso informando aos usuários que o campo valor dedução é a soma dos valores de Previdência Privada, Pensão Alimentícia, Deduções de INSS Terceiros e Dedução de Dependentes Terceiros\.

CH95931

__RN02__

O totalizador da Alíquota do Relatório de Tributos Federais por Estabelecimento deverá exibir o Total da Alíquota de acordo com o contido no campo “Alíquota” da tela de Controle de Tributos\. Exemplo: no caso se a alíquota informada for 4,15, deverá ser informado no relatório 4,1500, assim como é gerado hoje no relatório de tributos federais por Empresa\.

O arredondamento não deverá existir mais\.

CH115077

__RN03__

As Retenções da tabela X53\_RETENCAO\_IRRF, cujos campos “Estorno” e “Data do Estorno” estiverem preenchidos, não deverão ser consideradas para a geração do Relatório de Tributos Federais\. Vale salientar que essas retenções não possuem registros de retificação\.

OS3753\-D

# RN04

Criar um botão “Pesquisar” para fazer o filtro dos códigos DARF no campo “Código Retenção” na tela de “Emissão de Tributos – Estabelecimento”, de forma que o usuário possa fazer a seleção do código desejado\.

OS4155

# RN05

Após selecionar o código DARF no filtro, o campo “Código de Retenção” na tela “Emissão de Tributos\-Estabelecimento” receberá o código DARF selecionado pelo usuário\.

Obs: “Os criterios de recuperação do código DARF continuam o mesmo”\.

OS4155

__RN06__

Criar um novo campo “Data Vencimento” para o “Relatório de Tributos Federais – Por Estabelecimento”\.

OS4155

__RN07__

<a id="OLE_LINK13"></a><a id="OLE_LINK14"></a><a id="OLE_LINK15"></a><a id="OLE_LINK16"></a>A “Data Vencimento” receberá as informações do campo “Data Vencimento”, tela “Controle de Tributos”\.

OS4155

__RN08__

O novo campo “Data Vencimento” deverá estar no “Relatório de Tributos Federais – Por Estabelecimento”, ao lado do campo “Data Movimento”\.

O campo Data Vencimento será exibido no formato normal – DD/MM/AAAA\.

OS4155

__RN09__

__Rotina parâmetro __<a id="OLE_LINK45"></a><a id="OLE_LINK46"></a><a id="OLE_LINK47"></a>__“Considerar Estabelecimentos Sem Movimento”:__

Através do parâmetro “Considerar Estabelecimentos Sem Movimento” será possível demonstrar estabelecimentos sem movimentação no período\.

__Tratamento:__

- __Parâmetro desmarcado:__ <a id="OLE_LINK48"></a><a id="OLE_LINK49"></a><a id="OLE_LINK50"></a>Gerar o relatório conforme tratamento atual \(a geração emite apenas os estabelecimentos com movimentação e quando não há movimentação não apresenta o estabelecimento no relatório\)\.
- __Parâmetro marcado:__ Gerar o relatório conforme tratamento atual, mas verificar quando um determinado estabelecimento marcado na tela de geração não apresentar movimentação dentro do período preenchido, podendo ser por data de movimento, fato gerador ou data de competência, e ainda para qualquer Pessoa Fis/Jur e Situação de DARF selecionada, então emitir apresentando no corpo a descrição “Sem Movimento”, além disso, levar os dados do estabelecimento conforme é feito quando há movimentação \(Filial, CNPJ e Inscrição Estadual\)\.

__Observação:__ A mensagem deve ser demonstrada no relatório mesmo se o usuário selecionar vários estabelecimentos que contenham alguns com movimento e outros não, na ordem de estabelecimento conforme a geração padrão, ou seja, sem p parâmetro marcado\.

OS4323

__RN10__

__Campo Nº AP:__

__\[ALTERADA – CH11726\_2015\]__

O campo “Nº AP” receberá as informações, com até  10 posições, do campo “19\-Nº Autorização de Pagamento” da tela “Controle de Tributos \(SAFX53\)”\.

CH11726\_2015

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


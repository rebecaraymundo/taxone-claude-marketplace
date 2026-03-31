# MTZ_Relatorio_Consistencia_REINF

> Fonte: MTZ_Relatorio_Consistencia_REINF.docx






THOMSON REUTERS

Módulo SPED >> EFD-REINF

Consistências - REINF


Localização:

SPED >> EFD-REINF>> Relatórios>> Federais >> Consistências








DOCUMENTO DE REQUISITO

Sumário

1. Regras Gerais	3
2.  Definição da tela	3
3. Abas Geradas	6
4. Cenários	8
5. Layout do Relatório	10






















## 1. Regras Gerais


Este relatório tem por objetivo consistir algumas informações de cadastros e dos registros da tabela de Controle de tributos, validando natureza de rendimento, Códigos dos DARFs, Códigos de Receitas, valores dos tributos, entre outras situações, que são solicitadas e exigidas para o REINF. O usuário poderá escolher pelo menos uma das seguintes consistências:

CADASTRO (X04_PESSOA_FIS_JUR)
Classe de Pessoa Física Jurídica não Preenchida para Beneficiários do Exterior
CONTROLE DE TRIBUTOS (X53_RETENCAO_IRRF)
Natureza de Rendimento não Preenchida
Resultado do Valor Bruto x Alíquota Diferente do Valor de Imposto
Código do DARF Diferente de 0000 e Valor de Tributo não Preenchido
Valor de Tributo Menor do que R$10,00
CONTROLE DE TRIBUTOS (X53_RETENCAO_IRRF) x TACES109 (CAD_NAT_REND_COD_RECEITA)
Código do DARF x Natureza de Rendimento
Código de Receita x Natureza de Rendimento
Tributação não Permitida para o Exterior


Este relatório, será disponibilizado no módulo SPED/ EFD-REINF


## 2.  Definição da tela









Campos de Preenchimento Obrigatório:
Período, pelo menos uma consistência e um estabelecimento, devem ser selecionados.

## 3. Abas Geradas



## 4. Cenários



O Relatório deve apresentar as informações de acordo com a consistência escolhida na tela de geração.

Se marcada a opção ‘Classe de Pessoa Física Jurídica não Preenchida para Beneficiários do Exterior’:

Exibir todos os registros da tabela Arquivo de Controle de Tributos (X53_RETENCAO_IRRF) da empresa, estabelecimento, que estão compreendidos no período indicado na tela de geração do relatório, quando os registros possuírem beneficiários do exterior (campo 05 - Código do Fornecedor (COD_FIS_JUR) da X53, que possuam o campo 19- UF da X04_PESSOA_FIS_JUR preenchidos com ‘EX’) e que não estejam com o campo 26 - Classe de Pessoa Física Jurídica (Ind_Class_PFJ), preenchido na tabela de cadastro de pessoa física/jurídica (X04_PESSOA_FIS_JUR).


Se marcada a opção ‘Natureza de Rendimento não Preenchida’:

Exibir todos os registros da tabela Arquivo de Controle de Tributos (X53_RETENCAO_IRRF) da empresa, estabelecimento, que estão compreendidos no período indicado na tela de geração do relatório, que não estejam com o campo 67 – Natureza de Rendimentos (COD_NAT_REND) preenchido.

Se marcada a opção ‘Resultado do Valor Bruto x Alíquota Diferente de Valor de Imposto’:
Exibir todos os registros da tabela Arquivo de Controle de Tributos (X53_RETENCAO_IRRF) da empresa, estabelecimento, que estão compreendidos no período indicado na tela de geração do relatório, cujo resultado da expressão:  [campo 14– Valor Bruto (VLR_BRUTO) x (campo 17 – Alíquota (ALIQUOTA)/100)] seja diferente do valor informado no campo 15 – Valor do Tributo (VLR_IR_RETIDO)

Se marcada a opção ‘Código do DARF Diferente de 0000 e Valor de Tributo não Preenchido’:

Exibir todos os registros da tabela Arquivo de Controle de Tributos (X53_RETENCAO_IRRF) da empresa, estabelecimento, que estão compreendidos no período indicado na tela de geração do relatório, que possuam o campo 40 - Indicador de Tipo de Lançamento na DIRF da X53 igual a "0", "1" ou "2", que não estejam com o campo 11 – Código do DARF (COD_DARF) igual a ‘0000’ e que não possuam valores em todos os campos indicados abaixo:
- Campo 15 - Valor do Tributo da X53, Campo 47 - Valor Tributo 13º. Salário da X53 e Campo 43 - Valor Outros de Tributação Exclusiva da X53.

Se marcada a opção ‘Valor de Tributo Menor do que R$10,00’:

Exibir todos os registros da tabela Arquivo de Controle de Tributos (X53_RETENCAO_IRRF) da empresa, estabelecimento, que estão compreendidos no período indicado na tela de geração do relatório, que possuam o campo 40 - Indicador de Tipo de Lançamento na DIRF da X53 igual a "0", "1" ou "2", o campo 11 – Código do DARF (COD_DARF) diferente de ‘0000’ e o valor informado nos campos abaixo sejam menores que R$10,00:

- Campo 15 - Valor do Tributo da X53, Campo 47 - Valor Tributo 13º. Salário da X53 e Campo 43 - Valor Outros de Tributação Exclusiva da X53.

Com relação aos campos acima, se em um mesmo registro existir valores para mais de um desses campos, considerar o resultado do somatório dos campos para consistir se o valor é maior ou não que R$10,00. Ou seja, o registro deve ser apresentado no relatório, quando o somatório dos três campos não atingir R$10,00.


Se marcada a opção ‘Código do DARF x Natureza de Rendimento’:

Exibir todos os registros da tabela Arquivo de Controle de Tributos (X53_RETENCAO_IRRF) da empresa, estabelecimento, que estão compreendidos no período indicado na tela de geração do relatório, que não possuam código de receita, que não estejam cadastrados no campo código do DARF com ‘0000’ e quando a combinação dos campos 11 – Código do DARF (COD_DARF) e 67 – Natureza de Rendimentos (COD_NAT_REND), não correspondem a uma combinação válida e existente em uma linha da TACES109 (Campos Código de Natureza de Receita e Código de Receita*).

*Considerar os 4 primeiros dígitos do campo Código de Receita da TACES109 (campos Código da Natureza de Rendimento), para verificar a combinação.
* Considerar apenas os registros da TACES109 que estão cadastrados com os eventos R-4010 (confrontando com os registros da X53 de pessoa física, inclusive as pessoas do exterior (UF igual a EX, PAÍS diferente de ‘105 e IND_CLASSE_PFJ da safx04 estiver preenchido com informação igual a ‘01-Pessoa Física’)) e R-4020(confrontando com os registros da X53 de pessoa jurídica, inclusive as pessoas do exterior (UF igual a EX, PAÍS diferente de ‘105 e IND_CLASSE_PFJ da safx04 estiver preenchido com informação diferente de‘01-Pessoa Física’))

Se marcada a opção ‘Código de Receita x Natureza de Rendimento’:

Exibir todos os registros da tabela Arquivo de Controle de Tributos (X53_RETENCAO_IRRF) da empresa, estabelecimento, que estão compreendidos no  período indicado na tela de geração do relatório, que possuam código de receita,  que não tenham no campo código de DARF o código ‘0000’ e quando a combinação dos campos 23 – Código de Receita (COD_RECEITA) e 67 – Natureza de Rendimentos (COD_NAT_REND), não correspondem a uma combinação válida e existente em uma linha da TACES109 (Campos Código de Natureza de Receita e Código de Receita*).

*Considerar todos os dígitos do campo Código de Receita da TACES109 (campos Código da Natureza de Rendimento), para verificar a combinação.
* Considerar apenas os registros da TACES109 que estão cadastrados com os eventos R-4010 (confrontando com os registros da X53 de pessoa física e pessoa do Exterior (UF igual a EX, PAÍS diferente de ‘105  e IND_CLASSE_PFJ da safx04 estiver preenchido com informação igual a ’01-Pessoa Física’) e R-4020(confrontando com os registros da X53 de pessoa jurídica e pessoa do Exterior (UF igual a EX, PAÍS diferente de ‘105 e IND_CLASSE_PFJ da safx04 estiver preenchido com informação diferente de ’01-Pessoa Física’))




Se marcada a opção ‘Tributação não Permitida para o Exterior’:


Exibir todos os registros da tabela Arquivo de Controle de Tributos (X53_RETENCAO_IRRF) da empresa, estabelecimento, que estão compreendidos no período indicado na tela de geração do relatório e que não tenham no campo código de DARF o código ‘0000’:

Quando Fornecedor for do Exterior*, com o Campo Código de Receita sem Preenchimento e:
Não existir na TACES109 uma combinação (linha) com as mesmas informações dos campos 11 – Código do DARF* (COD_DARF), 67 – Natureza de Rendimentos (COD_NAT_REND), permitindo a Tributação no Exterior (campo ‘Tributação no Exterior ‘com ‘Sim’)

*Considerar apenas os registros da TACES109 que estão cadastrados com os eventos R-4010 (confrontando com os registros de pessoa do Exterior (UF igual a EX, PAÍS diferente de ‘105 e IND_CLASSE_PFJ da safx04 estiver preenchido com informação igual a ‘01-Pessoa Física’) e R-4020(confrontando com os registros do Exterior (UF igual a EX, PAÍS diferente de ‘105 e IND_CLASSE_PFJ da safx04 estiver preenchido com informação diferente de ‘01-Pessoa Física’))

*Considerar os 4 primeiros dígitos do campo Código de Receita da TACES109 (campos Código da Natureza de Rendimento), para verificar a combinação
*



Quando Fornecedor for do Exterior*, com o Campo Código de Receita preenchido e:
Não existir na TACES109 uma combinação (linha) com as mesmas informações dos campos 23 – Código de Receita (COD_RECEITA), 67 – Natureza de Rendimentos (COD_NAT_REND), permitindo a Tributação no Exterior (campo ‘Tributação no Exterior ‘com ‘Sim’)

* Considerar apenas os registros da TACES109 que estão cadastrados com os eventos R-4010 (confrontando com os registros de pessoa do Exterior (UF igual a EX, PAÍS diferente de ‘105 e IND_CLASSE_PFJ da safx04 estiver preenchido com informação igual a ‘01-Pessoa Física’) e R-4020(confrontando com os registros do Exterior (UF igual a EX , PAÍS diferente de ‘105 e IND_CLASSE_PFJ da safx04 estiver preenchido com informação diferente de ‘01-Pessoa Física’))


## 5. Layout do Relatório


Deverá ser gerado relatório em formato Excel (extensão .xls), contendo as colunas:






Modelo do relatório, disponível no arquivo ‘layout_relatorio_consitencia_REINF.xlsx’




| MFS | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-542765 | Alessandra Cristina Navatta | Criação do Relatório | 09/08/2023 |


| Campo | Regra | Demanda |
| --- | --- | --- |
| Período | Formato: MM/AAAA Onde, MM, só é aceito meses de 01 a 12, caso contrário, exibir a mensagem: “Mês inválido” | MFS-542765 |
| Consistências | Opções Válidas: CADASTRO PESSOA FÍSICA/JURÍDICA (X04_PESSOA_FIS_JUR) Classe de Pessoa Física Jurídica não Preenchida para Beneficiários do Exterior’ CONTROLE DE TRIBUTOS (X53_RETENCAO_IRRF) Natureza de Rendimento não Preenchida Resultado do Valor Bruto x Alíquota Diferente do Valor de Imposto Código do DARF Diferente de 0000 e Valor de Tributo não Preenchido Valor de Tributo Menor do que R$10,00 CONTROLE DE TRIBUTOS (X53_RETENCAO_IRRF) x TACES109 (CAD_NAT_REND_COD_RECEITA) Código do DARF x Natureza de Rendimento  Código de Receita x Natureza de Rendimento  Tributação não Permitida para o Exterior | MFS-542765 |
| Multiempresas | Se selecionado, será apresentado todos os estabelecimentos de todas as empresas que o usuário tem acesso na grid de estabelecimentos. Caso desmarcado, apenas os estabelecimentos da empresa logada será demonstrado na grid estabelecimentos. | MFS-542765 |
| Grid Estabelecimentos | Exibir todos os estabelecimentos que estão cadastrados na tela de Dados Iniciais do REINF, da empresa logada ou que o usuário tem acesso, de acordo com o parâmetro Multiempresas estar ou não marcado.  Quando o parâmetro Multiempresas estiver desmarcado, será apresentado todos os estabelecimentos da empresa logada. Caso o parâmetro esteja marcado, será exibido todos os estabelecimentos de todas as empresas que o usuário tem acesso. | MFS-542765 |
| Selecionar | Permite que o usuário selecione os Estabelecimentos que serão gerados o relatório.   Tratamentos:  Modal 'Selecionar Estabelecimentos‘ Ao ser acionado abrir o Modal 'Selecionar Estabelecimentos‘. Apresentando os campos Cód. Estab e Descrição Botões do Modal 'Selecionar Estabelecimentos': Critério, Cancelar, OK e Salvar...   Botões Critério, Cancelar, OK e Salvar  - Ao selecionar o botão 'Cancelar', nada será feito e o Modal 'Selecionar Estabelecimentos‘ será fechado.  - Ao selecionar o botão 'Critério', os estabelecimentos poderão ser filtrados e no novo modal serão exibidos habilitado os botões Pesquisar e Cancelar.  -Ao confirmar a seleção dos registros, acionando o botão ‘OK’, apresentar os estabelecimentos no componente “Estabelecimentos” da tela Principal - Permite a seleção de vários registros por vez. - Ao entrar no modal, pelo menos um registro deve ser selecionado, se for selecionado o botão 'Ok', caso contrário, exibir a mensagem “Selecionar pelo menos um registro”. -Ao selecionar o botão ’Salvar’, o sistema salva as informações recuperadas dos estabelecimentos (no diretório local e formato que o usuário informar). | MFS-542765 |
| Marcar Todos | Permite ao usuário selecionar ou desmarcar todos os registros da grid Estabelecimentos. | MFS-542765 |
| Executar | O período deve ser informado, caso contrário, será apresentado a mensagem: “Informe o período!” Pelo menos um estabelecimento deve ser selecionado, caso contrário, será apresentado a mensagem: “Informe o estabelecimento!” Apenas serão realizadas as consistências que o usuário marcar na tela. Pelo menos uma consistência deve ser selecionada, caso não esteja marcado, exibir a mensagem: “Informe pelo menos uma consistência!” | MFS-542765 |


| Processos | Esta aba será gerada sempre que for criado um processo. Deve conter o número do processo, os parâmetros, a situação do processo, as datas Início Execução e Fim Execução, além da informação do Usuário que fez a execução do processo. | MFS-542765 |
| --- | --- | --- |
| Logs | Esta aba deve demonstrar os logs do processo.   Na parte superior da tela exibir os parâmetros que foram indicados na tela de geração, seguindo o formato abaixo: | MFS-542765 |
| Arquivos | Esta aba deve demonstrar o arquivo que foi gerado durante a execução.  O título do arquivo: ‘Relatorio Consistencia_REINF.xls’ Além disso, o usuário poderá salvar os arquivos com ou sem o nº do processo, escolher se o arquivo será salvo em Local/Rede ou Servidor (Banco de Dados). | MFS-542765 |


| Campo | Formato / Default | Regra | Demanda |
| --- | --- | --- | --- |
| Empresa | Código. | Exibir o código da empresa. Campo 01 – Código da Empresa da X53 | MFS-542765 |
| Estabelecimento | Código | Exibir o código do estabelecimento. Campo 03 – Código do Estabelecimento da X53. | MFS-542765 |
| Período | MM/AAAA | Exibir o a informação do campo período da tela de Geração. | MFS-542765 |
| Data do Movimento | DD/MM/AAAA | Exibir a data do movimento.  Campo 03 – Data do Movimento da X53. | MFS-542765 |
| Beneficiário | ‘Indicador de Pessoa Física/Jurídica’/’Código do Fornecedor’ | Exibir o indicador de Pessoa Física/Jurídica e o Código do Fornecedor.  Campo 04 – Indicador de Pessoa Física/Jurídica e 05 - Código do Fornecedor da X53. | MFS-542765 |
| Razão Social |  | Exibir a Razão Social da SAFX04 (campo 05 – Razão Social), da pessoa física/jurídica recuperada | MFS-542765 |
| CPF/CNPJ | XXX.XXX.XXX-XX OU  XX.XXX.XXX\XXXX-XX | Exibir o  CPF-CGC da SAFX04 (campo 06 – CPF-CGC), da pessoa física/jurídica recuperada. | MFS-542765 |
| UF | XX | Exibir a UF do Fornecedor. Campo 19 – UF da X04. | MFS-542765 |
| Classe de Pessoa Física Jurídica | Código - Descrição | Exibir a Classe de Pessoa Física Jurídica. Campo da X04. | MFS-542765 |
| Tipo do Documento |  | Exibir o tipo de documento. Campo 06 – Tipo do Documento da X53. | MFS-542765 |
| Documento (Número/Série/Subsérie) | Xxxx/xxx/xxxx | Exibir o número, série e subsérie do documento. Campos 07 – Número do Documento, 08 – Série do Documento e 09 – Subsérie do Documento da X53. | MFS-542765 |
| Operação (Código/Descrição) | Código - Descrição | Exibir o código de operação. Campo 10 – Código de Operação da X53 e a descrição de operação. Campo 03 - Descrição do Código Operação –da X2001. . | MFS-542765 |
| Código do DARF |  | Exibir o código do DARF. Campo 11 – Código do DARF da X53. | MFS-542765 |
| Código de Receita |  | Exibir o código de Receita. Campo 23 – Código de RECEITA da X53. | MFS-542765 |
| Tipo de Lançamento na DIRF | Código - Descrição | Exibir o Tipo de Lançamento da DIRF. Campo 40 – Indicador de Tipo de Lançamento da DIRF da SAFX53 | MFS-542765 |
| Natureza de Rendimento |  | Exibir a Natureza de Rendimento. Campo 67 – Natureza de Rendimento da SAFX53. | MFS-542765 |
| Serviço Atribuição Natureza Rendimento |  | Exibir a informação do Campo 103 - Serviço para Atribuição da Natureza da X53 | MFS-542765 |
| Valor Bruto | 9,99 | Exibir o valor bruto. Campo 14 – Valor Bruto da X53 | MFS-542765 |
| Valor do Tributo | 9,99 | Exibir o valor do tributo. Campo 15 - Valor do Tributo da X53. | MFS-542765 |
| Valor Tributo 13º. Salário | 9,99 | Exibir o valor tributo 13 º salário. Campo 47 – Valor Tributo 13º. Salário da SAFX53 | MFS-542765 |
| Valor Outros de Tributação Exclusiva | 9,99 | Exibir o valor outros de tributação exclusiva.  Campo 43 - Valor Outros de Tributação Exclusiva da X53. | MFS-542765 |
| Alíquota |  | Exibir a alíquota. Campo 17 – Alíquota da X53 | MFS-542765 |
| Advertência |  | Exibir as mensagens indicadas abaixo (maior detalhamento das regras para cada cenário, considerar as informações do item 3. Cenários:  Se marcada a opção ‘Classe de Pessoa Física Jurídica não Preenchida  para Beneficiários do Exterior’ e existir registro sem o campo ‘Classe de Pessoa Física Jurídica preenchido, exibir em cada registro (nesta condição) a mensagem: “O Fornecedor do Exterior <<indicador – Código do Fornecedor>> não possui a informação do campo   26 - Classe de Pessoa Física Jurídica (Ind_Class_PFJ), preenchido na tabela de cadastro (X04_PESSOA_FIS_JUR).”   Se marcada a opção ‘Natureza de Rendimento não Preenchida’ e existir registro sem o campo ‘Natureza de Rendimento’ preenchido, exibir em cada registro (nesta condição) a mensagem: “Campo 67 – Natureza de Rendimentos (COD_NAT_REND) não está preenchido na X53.“  Se marcada a opção ‘Resultado do Valor Bruto x Alíquota Diferente de Valor de Imposto’ e for encontrada diferenças no valor do Imposto, exibir em cada registro (nesta condição) a mensagem: “O resultado da multiplicação do Valor Bruto x Alíquota não está igual ao valor informado no campo Valor do Tributo.  <<Valor da Multiplicação: 99,99 Valor Informado: 99,99 >>”   Se marcada a opção ‘Código do DARF Diferente de 0000 e Valor de Tributo não Preenchido’ e existir registros com informação de código do DARF diferente de 0000 sem o Valor de Tributo informado, exibir em cada registro (nesta condição) a mensagem: “Não foi informado o Valor de Tributo.   Se marcada a opção ‘Valor de Tributo Menor do que R$10,00’. Se for encontrado valor do tributo menor do que R$10,00, exibir em cada registro (nesta condição) a mensagem: “Valor do tributo menor que R$10,00.<<Exibir APENAS o(s)campo(s) com os valor(es) menores que 10,00, exemplo: Valor Tributo: 5,00;  Valor Outros de Tributação Exclusiva: 2,00 >>”    Se marcada a opção ‘Código do DARF x Natureza de Rendimento’ e existir registros que não atendam a combinação existente na TACES109, exibir em cada registro (nesta condição), a mensagem: Não existe esta combinação de código do DARF e natureza de rendimento na TACES109. <<Código do DARF: XXXX e Natureza de Rendimento:99999>>  Se marcada a opção ‘Código de Receita x Natureza de Rendimento’ e existir registros que não atendam a combinação existente na TACES109, exibir em cada registro (nesta condição), a mensagem: Não existe esta combinação de código de receita e natureza de rendimento na TACES109. <<Código de Receita: XXXXXX e Natureza de Rendimento:99999>>   Se marcada a opção ‘Tributação não Permitida para o Exterior’ e existir registros de fornecedores do exterior com natureza de rendimento que não permitam tributação no exterior (conforme registros disponibilizados na TACES109), exibir em cada registro (nesta condição), a mensagem: “Esta natureza de rendimento não aceita Tributação no Exterior. << Fornecedor: Indicador – Código fornecedor, Natureza de Rendimento:99999>>  Obs. Se um registro se enquadrar em mais de uma advertência/inconsistência, o mesmo deve ser exibido N vezes no relatório (considerando as validações escolhidas na tela de geração). | MFS-542765 |

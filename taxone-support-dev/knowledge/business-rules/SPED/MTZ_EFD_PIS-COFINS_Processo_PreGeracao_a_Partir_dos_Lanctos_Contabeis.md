# MTZ_EFD PIS-COFINS_Processo_PreGeracao_a_Partir_dos_Lanctos_Contabeis

> Fonte: MTZ_EFD PIS-COFINS_Processo_PreGeracao_a_Partir_dos_Lanctos_Contabeis.docx







THOMSON REUTERS

Módulo Sped Contribuições

Pré-Geração a Partir dos Lanctos Contábeis (PROCESSO)


Localização: Menu Sped, Módulo: EFD Escrituração Fiscal Digital das Contribuições  Manutenção Registro do Bloco F  Demais Documentos e Operações Geradoras de Contribuição e Créditos (F100) Pré-Geração a Partir dos Lanctos Contábeis
Sumário

1.	CONTROLE DE ALTERAÇÕES	2
2.	INTRODUÇÃO	3
3.	DOCUMENTOS DE REFERÊNCIA	3
4.	DEFINIÇÃO DAS REGRAS	4







## CONTROLE DE ALTERAÇÕES










## INTRODUÇÃO

Criar o processamento de geração automática das informações da x147_oper_cred. Esse processo será acionado através da tela Pré-Geração a Partir dos Lantos Contábeis, no módulo de SPED/ EFD-Escrituração Fiscal Digital das Contribuições.
A pré-geração é uma opção para os clientes que não querem carregar as informações através da importação da tabela SAFX147- Demais documentos e Operações Geradoras de Crédito, pois possuem carregados dados na X01 e utilizam na tela de Dados Iniciais, a opção ‘‘Utilizar a parametrização da
‘Conta Contábil X Centro de Custo/CST/Operação/Nat. Base de Crédito’, para a geração do registro F100.

As informações que foram processadas por essa rotina, serão utilizadas para a geração do registro F100 do SPED Contribuições.

## DOCUMENTOS DE REFERÊNCIA

MTZ_Tela_Parâmetros_Dados_Iniciais.docx
MTZ_SPED_EFD_CONTRIBUICOES_Tela_Parametrizacao_F100_Conta_ContabilxCentro_de_Custo_CST_Oper_Nat.docx
MTZ_EFD PIS-COFINS_Tela_PreGeracao_a_Partir_dos_Lanctos_Contabeis.docx.docx
## DEFINIÇÃO DAS REGRAS




| Data | Demanda | Descrição | Autor |
| --- | --- | --- | --- |
| 19/05/2021 | MFS-64743 | Criação do processo que será acionado na tela ‘Pré-Geração a Partir dos Lanctos Contábeis’, que a partir dos lançamentos contábeis existente na base e a parametrização definida para a geração do registro F100 do SPED Contribuições (em dados iniciais do módulo), grava as informações na x147_oper_cred. | Alessandra Cristina Navatta |
| 21/05/2021 | MFS-64744 | Criação do processo de limpeza dos registros gerados pelo sistema. | Alessandra Cristina Navatta |


| Número | Regra | Demanda |
| --- | --- | --- |
| RP00 | Esta funcionalidade tem o propósito de preencher as informações na tabela x147_oper_cred, considerando as informações de lançamentos contábeis, existente na base, compreendidos no período da geração do processo, levando em consideração a opção ‘Utilizar a parametrização da  Conta Contábil X Centro de Custo/CST/Operação/Nat. Base de Crédito’ definida em Dados Iniciais para a geração do registro F100 do produto Sped Contribuições.  Este processo será executado através da tela Pré-Geração a Partir dos Lanctos Contábeis, localizada no Menu: SPED, Módulo: Escrituração Fiscal Digital das Contribuições Manutenção Registro do Bloco F  Demais Documentos e Operações Geradoras de Contribuição e Créditos (F100) Pré-Geração a Partir dos Lanctos Contábeis.  Para o processamento, serão consideradas as informações dos parâmetros da tela (Período,  Informações para o Registro F100, Empresa/Estabelecimento), além da recuperação dos  lançamentos contábeis, quando a configuração da empresa/estabelecimento possuir na tela de Dados Iniciais, a opção ‘‘Utilizar a parametrização da Conta Contábil X Centro de Custo/CST/Operação/Nat. Base de Crédito’, marcada,  para a geração do registro F100.  Vale ressaltar que as informações da tabela x147_oper_cred, são utilizadas para a geração do SPED Contribuições registro F100.  Caso já exista informações nas tabelas (registros importados através da SAFX147- Demais Documentos e Operações Geradoras de Crédito e ou digitados), para o período processado, não iremos executar o processo. A rotina apenas será executada se não houver registro no período ou se o registro existente foi gerado pelo próprio processo de pré-geração (neste caso, todos os registros serão sobrepostos).   Todos os registros criados por este processo, ficaram identificados que foram criados pelo sistema (campo ind_gravação igual a 7). | MFS-64743 |
| RP01 | Processo de Geração: O objetivo é recuperar os registros de lançamentos contábeis que possuem direito a crédito de PIS/COFINS, consolidando os valores dos lançamentos por período, conta contábil e centro de custo. Serão gravados registros na x147_oper_cred, quando essa consolidação de valores for um valor a crédito. Os registros gravados, posteriormente, serão considerados na geração do registro F100 - Demais documentos e Operações Geradoras de crédito), no SPED Contribuições.  O processo será realizado caso o campo ‘Informações para Registro F100’ na tela de pré-geração, esteja com a opção ‘Gerar’ marcado  Atenção: Consideraremos  lançamentos contábeis com direito ao crédito, os lançamentos que se enquadrarem nos filtros das parametrizações indicadas pelo usuário (SPED> EFD- Escrituração Fiscal Digital das Contribuições > Parâmetros > Registro F100 > Conta Contábil X Centro de Custo/CST/Operação/Nat. Base de Crédito).   Critérios da recuperação:  Empresa/Estabelecimento selecionado na tela de pré-geração;  Período (mês/ano) indicado na tela de pré-geração; Configuração do parâmetro ‘Registro F100 – Demais Documentos e Operações Geradoras de Contribuição e Crédito’ com a opção igual a ‘Utilizar a parametrização da Conta Contábil X Centro de Custo/CST/Operação/Nat. Base de Crédito’ em Dados Iniciais para a empresa/estabelecimento indicado na tela de pré-geração; Parametrização por ‘Conta Contábil X Centro de Custo/CST/Operação/Nat. Base de Crédito’ para a empresa/estabelecimento, indicado na tela de pré-geração; Lançamentos Contábeis (SAFX01 - Arquivo Contábil-), com o campo 17-TIPO_LANCTO diferente de ‘E-Encerramento’ da empresa/estabelecimento indicado na tela de pré-geração.  Recuperando os lançamentos contábeis com direito ao crédito de PIS/COFINS:  Dados Iniciais e Parametrização  A partir do período indicado na tela da pré-geração, verificar se há, para a empresa/estabelecimento que estamos executando o processo, parametrização configurada em dados iniciais igual a ‘Utilizar a parametrização da Conta Contábil X Centro de Custo/CST/Operação/Nat. Base de Crédito’, para o parâmetro  Registro F100 – Demais Documentos e Operações Geradoras de Contribuição e Crédito:  Dados Iniciais: Se o parâmetro estiver marcado com: ‘Utilizar a parametrização do Tipo de Documento X CST/Operação/Nat. Base de Crédito’, o processo será interrompido e exibiremos a mensagem no log (indicada na regra do botão executar do documento ‘MTZ_EFD PIS-COFINS_Tela_PreGeracao_a_Partir_dos_Lanctos_Contabeis.docx’);  Caso o parâmetro esteja marcado com ‘Utilizar a parametrização da Conta Contábil X Centro de Custo/CST/Operação/Nat. Base de Crédito’, consideraremos a parametrização que está no caminho: ‘ SPED> EFD- Escrituração Fiscal Digital das Contribuições > Parâmetros > Registro F100>  Conta Contábil X Centro de Custo/CST/Operação/Nat. Base de Crédito’. Neste caso, verificar a parametrização, conforme regras abaixo:   Parametrização Se não existir parametrização por ‘Conta Contábil X Centro de Custo/CST/Operação/Nat. Base de Crédito’  Localizada em SPED> EFD- Escrituração Fiscal Digital das Contribuições > Parâmetros > Registro F100> Conta Contábil X Centro de Custo/CST/Operação/Nat. Base de Crédito, o processo será interrompido e exibiremos a mensagem no log (indicada na regra do botão executar do documento ‘MTZ_EFD PIS-COFINS_Tela_PreGeracao_a_Partir_dos_Lanctos_Contabeis.docx’). Encontrando a parametrização, seguir para o item 2 desta regra.  Lançamentos Contábeis  Após verificar a existência da parametrização atendida por este processo, indicada nesta regra no item 1, deve ser verificado se existem lançamentos contábeis na base (com o campo 17-TIPO_LANCTO diferente de ‘E-Encerramento’), para o período e empresa/estabelecimento indicados na tela de pré geração, conforme abaixo:  Caso não exista lançamentos contábeis no período, o processo será interrompido e exibiremos a mensagem no log (indicada na regra do botão executar do documento ‘MTZ_EFD PIS-COFINS_Tela_PreGeracao_a_Partir_dos_Lanctos_Contabeis.docx’). Encontrando a parametrização, seguir para o item 3 desta regra.  Possíveis Lançamentos Contábeis elegíveis para x147_oper_cred  Após verificar a existência da parametrização e dos lançamentos contábeis na base, indicados nesta regra nos itens 1 e 2 desta regra, devemos filtrar os lançamentos que serão considerados para o PIS/COFINS, de acordo com a parametrização criada pelo usuário.  Apenas os lançamentos enquadrados pela parametrização serão considerados na gravação da x147_oper_cred. Vale ressaltar que serão desprezados lançamentos do tipo de encerramento.   Consolidação dos Lançamentos Contábeis e criação do registro na x147_oper_cred  Considerando os lançamentos enquadrados pela parametrização (item 3 desta regra), consolidar os valores dos lançamentos contábeis por conta e centro de custo (este último, quando existir), referente ao período da geração e da empresa/estabelecimento selecionado na tela de pré-geração. Para a consolidação, efetuar a soma de todos os lançamentos a crédito MENOS a soma de todos os lançamentos a débito, se o resultado for um valor a crédito, um registro será gravado na x147_oper_cred (as regras da criação do registro, estão disponíveis na RP02), se o resultado for um valor a débito, nenhum registro desta conta e centro de custo será gravado pelo processo.    Validações  Considerar as validações na RP04 (Mensagens que devem ser apresentadas no Log do processamento e as (indicadas na regra do botão executar do documento ‘MTZ_EFD PIS-COFINS_Tela_PreGeracao_a_Partir_dos_Lanctos_Contabeis.docx’). | MFS-64743 |
| RP02 | Conforme informado anteriormente, após a consolidação dos valores dos lançamentos por conta e centro de custo, se o valor do lançamento consolidado for um valor a crédito, um registro será criado na x147_oper_cred.  Gravar os registros na tabela x147_oper_cred, conforme regras indicadas nos respectivos campos indicado na tabela abaixo. Os dados gravados podem ser consultados na tela:   Menu Sped, Módulo: EFD Escrituração Fiscal Digital das Contribuições > Manutenção> Registro do Bloco F > Demais Documentos e Operações Geradoras de Contribuição e Créditos (F100) > Manutenção dos Registros.    (Tabela de Gravação dos Registros) | MFS-64743 |
| RP03 | Todos os registros gravados na tabela x147_oper_cred , através deste processo (RP02), devem ser identificados que foram gerados pelo sistema, pois os registros importados ( SAFX147- Demais Documentos e Operações Geradoras de Crédito ) não podem ser alterados (por esse processo).   Sugestão: utilizar o campo ind_gravacao, com os domínios  6.  Gerado pelo Sistema 7.  Gerado pelo Sistema / Atualizado por Digitação 8. Gerado pelo Sistema / Atualizado por Importação   O domínio 7 deve ser considerado, quando o usuário ajustar uma informação que foi gerada pelo sistema.  Domínio completo do campo ind_gravacao: 		 Tipo/tamanho: CHAR(1)  Valores padrão do campo: 1.  Incluído por Importação 2.  Atualizado por Importação 3.  Incluído por Importação / Atualizado por Digitação 4.  Incluído por Digitação 5.  Incluído por Digitação / Atualizado por Digitação 6.  Gerado pelo Sistema 7.  Gerado pelo Sistema  / Atualizado por Digitação 8. Gerado pelo Sistema  / Atualizado por Importação 9. Atualizado pelo Sistema   Serão considerados registros oriundos de Importação os domínios:  1.  Incluído por Importação 2.  Atualizado por Importação 3.  Incluído por Importação / Atualizado por Digitação    Serão considerados registros oriundos de Digitação os domínios:  4. Incluído por Digitação 5.  Incluído por Digitação / Atualizado por Digitação | MFS-64743 |
| RP04 | Mensagens que devem ser apresentadas no Log do processamento:  Se existir informações no período para a tabela x147_oper_cred (registros de origem via importação ou digitação), o processo não será realizado. Exibir a mensagem: “Existem dados importados através da SAFX147- Demais documentos e Operações Geradoras de crédito, ou que foram digitados, para o período por isso, o processo não será realizado”. Atenção: Para identificarmos que um registro foi importado pela SAFX147 ou inserido via manutenção, consideraremos a regra a seguir: Tipo de Documento deve ser diferente de ‘NF100’ e o ind_gravação diferente de 6,7, e 8. | MFS-64743 |
| RP05 | Processo de Exclusão:  O processo será realizado caso o campo ‘Informações para Registro F100’ na tela de pré-geração, esteja com a opção ‘Gerar’ ou ‘Limpar’ marcado. Quando a opção gerar estiver selecionada, a exclusão ficará transparente para o usuário. Esta funcionalidade será necessária, para evitarmos eventuais divergências de informações.  O processo consiste em apagar da base, todos os registros que foram gerados automaticamente por este processo, considerando o período e a empresa/estabelecimento indicado na tela de pré-geração. | MFS-64744 |
|  |  |  |

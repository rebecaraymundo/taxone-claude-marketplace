# Relatorio_Conferencia_Lucro_Real_LALUR_LACS

> Fonte: Relatorio_Conferencia_Lucro_Real_LALUR_LACS.docx


Atenção: Para recuperar a versão, considerar a versão compatível com o período ‘01/01 do ano anterior’ até ‘01/01 do ano informado no exercício’.




THOMSON REUTERS

Relatório de Conferência do Lucro Real – LALUR/LACS



DOCUMENTO DE REQUISITO


Sumário

1.	INTRODUÇÃO	3
2.	DOCUMENTOS DE REFERÊNCIA	3
3.	Tela de Parâmetros	3
4.	LEIAUTE	9
4.1.	Regras dos campos do Relatório (Leiaute)	11
4.2.	Exemplos do Relatório	22

## INTRODUÇÃO


Objetivo desta especificação é criar uma tela para permitir ao usuário parametrizar dados e gerar o relatório de Conferência dos registros exibidos na tela Lucro Real – Demonstração, dos registros do bloco M.

## DOCUMENTOS DE REFERÊNCIA


- Layout_ECF.xlsx
- Tela_Lucro_Real-Registros_de_Tabela_Dinamica.doc


## Tela de Parâmetros

Localização da tela:  ECF - Escrituração Contábil Fiscal >>Relatórios >> Conferência do Lucro Real >> LALUR/LACS

Título da tela: Conferência do Lucro Real – LALUR/LACS

As regras destacadas em amarelo (e com fonte vermelha), não serão implementadas neste momento.



## LEIAUTE


Origem das informações para geração do relatório:

Tela Lucro Real, registros oriundos de Tabela Dinâmica (todos os registros processados da tabela dinâmica do bloco M).
Registros M300, M350


Tela Lucro Real, demais registros
Registros M410, M500

Tipos de Relatórios:

Sintético
Analítico

Os registros M410 e M500 não consideram esse parâmetro (serão gerados com o mesmo leiaute, independentemente do tipo de relatório escolhido) .

Regra de agrupamento:

Agrupar por Informação do ECF, por registro e período de apuração.


Ordenação:
Ordenar por código do estabelecimento, data inicial Informação ECF, período de apuração, código do registro (seguindo a hierarquia dos registros de acordo com o arquivo Layout_ECF.xlsx) e

Se registro oriundo de Tabelas Dinâmicas:

Código da linha da tabela dinâmica. Todos de forma crescente.

Nos relatórios analíticos, ordenar os campos Conta Contábil e Centro de Custo, se houver, de forma crescente.

Para o registro M410:

Ordenar por CNPJ da empresa, data inicial Informação ECF, período de apuração, código do registro, grupo da conta, conta da parte b, tributo, data do lançamento e
Apresentar inicialmente os registros que possuem o campo Conta da Parte B Origem da Contrapartida, sem preenchimento.

Busca de Registros:

Considerar as informações que foram processadas e exibidas na tela do Lucro Real, de acordo com as informações de filtro indicadas na tela de geração do relatório. Não será possível selecionar a apuração anual nos períodos Inicial e Final, na tela de geração do relatório, se existir dados referente a apuração Anual (A00), a mesma deve ser exibida no relatório.
Para os demais registros (M410, M500), não será considerado o tipo de relatório, ou seja, se marcados esses registros serão gerados sempre em um único leiaute.



#### Regras dos campos do Relatório (Leiaute)



(*)Não exibir a descrição na tela/relatório.

#### Exemplos do Relatório



Registros de Tabela Dinâmica – Sintético



Registros de Tabela Dinâmica – Analítico






DEMAIS REGISTROS

Registro M410 – M415



Registro M500







| Data | MFS | Descrição | Autor |
| --- | --- | --- | --- |
| 27/08/2018 | MFS-20624 | Criação do documento | Alessandra Cristina Navatta |


| Campo | Tipo | Formato/Default | Obrig. | Editável | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- |
| Exercício | Texto | AAAA | Sim | Sim | Informar o exercício que será utilizado para recuperar as Informações ECF.  Tratamentos:  Trazer o campo preenchido, com o ano atual. Se o campo exercício, for alterado, os demais campos devem ser limpos (inclusive os campos de opções definidas com default), para serem novamente definidos. | MFS-20624 |
| Versão | Lista | Código - Descrição | Sim | Sim | Permite ao usuário indicar a versão que será utilizada para recuperar as Informações ECF.  Lista de Opções Válidas:  Exibir a lista de versões da RNG00004 – Versão de layout.  Atenção: Para recuperar a versão, considerar a versão compatível com o período ‘01/01 do ano anterior’ até ‘01/01 do ano informado no exercício’.   Tratamentos:  Se este campo for alterado, os demais campos, exceto o campo exercício, devem ser limpos (inclusive os campos de opções definidas com default), para serem novamente definidos | MFS-20624 |
| Apuração | Lista | S | N | Default: Anual  Formato: Descrição | Permite que o usuário informe o tipo de Apuração.  Valores válidos:  Anual Trimestral | MFS-20624 |
| Data Inicial | Data | S | S | DD/MM/AAAA | Permite que o usuário escolha uma data inicial para gerar o relatório. | MFS-20624 |
| Data Final | Data | S | S | DD/MM/AAAA | Permite que o usuário escolha uma data final para gerar o relatório. | MFS-20624 |
| Tipo do Relatório: | Radiobutton | S | S | Default: Sintético | Permite que o usuário selecione o tipo do relatório.  Conteúdos Válidos: Sintético  Analítico | MFS-20624 |
| Apenas Registros com Movimento | Check-box |  |  | Default: Marcado | Permite que o usuário escolha a forma de exibição das informações no relatório, se deseja visualizar apenas os registros que possuam movimento ou todos os registros.  Tratamentos:  Quando o usuário selecionar a opção “Apenas Registros com Movimento”, apresentar no relatório apenas os registros cujo campo “Valor” seja diferente de zero.  Atenção para o relatório Sintético: Devido à quebra do relatório em mais de uma página, a linha que possuir valor diferente de zero, em pelo menos um mês/trimestre (dentro da escrituração), a mesma deve sair em todas as páginas do relatório.  Esta regra acima não se aplica ao relatório Analítico, que possui estrutura diferente de exibição de valor.  Quando o usuário desmarcar a opção “Apenas Registros com Movimento”, apresentar no relatório todos os registros. | MFS-20624 |
| Relatório Analítico – Exibir os lançamentos associados dos registros do Bloco M | Checkbox | S | S | Desabilitado | Permite que o usuário escolha se na geração do relatório analítico dos registros do Bloco M, seja exibido os lançamentos das associações das contas contábeis caso existam.  Tratamento:  Habilitar esse campo apenas quando o “Tipo do Relatório” for igual a “Analítico”   Ao habilitar, apresentar com marcação selecionada.  Se o usuário desmarcar essa opção, não exibir nenhum lançamento associado às contas contábeis, caso existam, na geração do relatório analítico dos registros do Bloco M. | MFS-20624 |
| Gravar Arquivos | Radio-Button | Arquivo Único | Sim | Sim | Opções Válidas:  Quebra por Informações ECF Arquivo Único  Tratamentos:  Se selecionada a opção ‘Quebra por Estabelecimentos’, será gerado um relatório por Informações ECF, com todos os registros selecionados. Se selecionada a opção ‘Arquivo Único’, será gerado em um único relatório, contendo todas as Informações ECF recuperadas, com os dados de todos os registros selecionados. Se este campo for alterado, os demais campos não devem ser limpos. | MFS-20624 |
| Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos |
| Informações ECF(*) | Check-box | Código Estab - CGC - Exercício -  Data Inicial da Escrituração  (076 - XXXXXXXXXXXXXX -  01/03/2017) | - | - | Permite ao usuário selecionar um ou mais registros de Informações ECF.  Tratamentos:  Recuperar apenas as Informações ECF que estão compatíveis com as opções de filtro preenchidas na tela de parametrização do relatório. | MFS-20624 |
| Marcar Todos | Check-box | Desmarcado | - | - | Permite ao usuário selecionar todas ou desmarcar todas as Informações ECF.  Tratamentos:  Se selecionar o check-box, todos os registros exibidos no componente de Informações serão marcados.  Se desmarcar o check-box, o sistema deve desmarcar todos os registros de Informações ECF selecionados. | MFS-20624 |
| Registros | Registros | Registros | Registros | Registros | Registros | Registros |
| Registros (*) | Check-box | Cód. - Descrição | - | - | Permite ao usuário selecionar um ou mais registros do Lucro Real do Bloco M , da Tela Demonstraçãopara gerar o relatório.  Tratamentos:  Só deve ser exibido os registros, quando o campo versão estiver preenchido. Recuperar os registros do bloco M, compatível com a versão que foi indicada na tela de parâmetros do relatório   Lista de Registros Válidos: M300  M350  M410 M500 | MFS-20624 |
| Marcar Todos | Check-box | Desmarcado | - | - | Permite ao usuário selecionar todos ou desmarcar todos os registros de tabela dinâmica.  Tratamentos:  Se selecionar o check-box, todos os registros exibidos no componente de Registros serão marcados.  Se desmarcar o check-box, o sistema deve desmarcar todos os registros do componente de Registros. | MFS-20624 |
| OK | Botão |  | - | - | Permite ao usuário gerar um relatório de conferência dos registros selecionados.  Tratamentos: Se o usuário clicar em OK, sem ter selecionado pelo menos uma Informação ECF, exibir a mensagem DW00057. Aplicar RNG00010 – Campo Obrigatório Se não houver dados para a composição do relatório, exibir a mensagem DW00274. Se a “Data Inicial” for posterior ao “Data Final”, exibir a mensagem DW00212. Aplicar a regra RNG00010 - Campo Obrigatório.  Gerar o relatório conforme tópico “4. LEIAUTE”.   Atenção: Será recuperada e exibida nos relatórios as apurações que estão compreendidas integralmente entre as datas inicial e final indicadas na tela de geração do relatório. | MFS-20624 |
| Cancelar | Botão |  | - | - | Permite ao usuário fechar a tela e não executar o relatório. | MFS-20624 |


| Campo/Coluna | Tipo | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- |
| Cabeçalho(*) | Cabeçalho(*) | Cabeçalho(*) | Cabeçalho(*) | Cabeçalho(*) |
| Empresa(*) | Texto | Código - Descrição | Apresenta no lado superior esquerdo do cabeçalho, a empresa do estabelecimento, que está sendo gerado os dados do relatório. | MFS-20624 |
| Página X de Y | Texto | Página X de Y | Apresenta no lado superior direito do cabeçalho, o número da página atual (X) e a quantidade total de páginas do relatório (Y). | MFS-20624 |
| Data | Data | DD/MM/AAAAA às HH:MM:SS hs | Apresenta no lado superior direito do cabeçalho, a data, hora, minuto e segundo em que o relatório foi gerado. | MFS-20624 |
| Corpo do Relatório (*) | Corpo do Relatório (*) | Corpo do Relatório (*) | Corpo do Relatório (*) | Corpo do Relatório (*) |
| Título1: (*) Relatório de Conferência do Lucro Real- LALUR/LACS - Sintético  Título 2: (*) Relatório de Conferência do Lucro Real - LALUR/LACS - Analítico   Exibir somente um dos títulos de acordo com o tipo de relatório parametrizado na tela de geração.(*) | Título1: (*) Relatório de Conferência do Lucro Real- LALUR/LACS - Sintético  Título 2: (*) Relatório de Conferência do Lucro Real - LALUR/LACS - Analítico   Exibir somente um dos títulos de acordo com o tipo de relatório parametrizado na tela de geração.(*) | Título1: (*) Relatório de Conferência do Lucro Real- LALUR/LACS - Sintético  Título 2: (*) Relatório de Conferência do Lucro Real - LALUR/LACS - Analítico   Exibir somente um dos títulos de acordo com o tipo de relatório parametrizado na tela de geração.(*) | Título1: (*) Relatório de Conferência do Lucro Real- LALUR/LACS - Sintético  Título 2: (*) Relatório de Conferência do Lucro Real - LALUR/LACS - Analítico   Exibir somente um dos títulos de acordo com o tipo de relatório parametrizado na tela de geração.(*) | Título1: (*) Relatório de Conferência do Lucro Real- LALUR/LACS - Sintético  Título 2: (*) Relatório de Conferência do Lucro Real - LALUR/LACS - Analítico   Exibir somente um dos títulos de acordo com o tipo de relatório parametrizado na tela de geração.(*) |
| Estabelecimento | Texto | Código - Descrição | Exibe o estabelecimento de cada Informações ECF que foi recuperada. | MFS-20624 |
| Exercício | Texto | AAAA | Exibe o exercício correspondente a cada Informações ECF, que foi recuperada. | MFS-20624 |
| Data Inicial | Texto | DD/MM/AAAA | Exibe a data inicial correspondente a cada Informações ECF que foi recuperada. | MFS-20624 |
| Versão | Texto | - | Exibe a versão correspondente a cada Informações ECF recuperada. | MFS-20624 |
| Forma de Tributação | Texto | - | Exibe a forma de tributação correspondente a cada Informações ECF que foi recuperada. | MFS-20624 |
| Apuração | Texto | - | Exibe a apuração correspondente a cada Informação ECF que foi recuperada. | MFS-20624 |
| Relatório Sintético – Registros de Origem de Tabela Dinâmica (*) Registros Atendidos: M300, M350 (*)  Cód. Registro - Descrição do Registro | Relatório Sintético – Registros de Origem de Tabela Dinâmica (*) Registros Atendidos: M300, M350 (*)  Cód. Registro - Descrição do Registro | Relatório Sintético – Registros de Origem de Tabela Dinâmica (*) Registros Atendidos: M300, M350 (*)  Cód. Registro - Descrição do Registro | Relatório Sintético – Registros de Origem de Tabela Dinâmica (*) Registros Atendidos: M300, M350 (*)  Cód. Registro - Descrição do Registro | Relatório Sintético – Registros de Origem de Tabela Dinâmica (*) Registros Atendidos: M300, M350 (*)  Cód. Registro - Descrição do Registro |
| Período (*) | Texto | Descrição | Exibe a descrição de cada período informado, conforme as apurações que foram recuperadas, baseadas nos campos de data inicial e final na geração do relatório.   Tratamento:  Se existir mais de um período a ser exibido, os mesmos devem ser demonstrados em ordem crescente, um abaixo do outro, (após a exibição de todos os códigos de linha do registro).  Valores Válidos:  Se apuração = Anual: Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro Anual  Se apuração  =  Trimestral 1º Trimestre 2º Trimestre 3º Trimestre 4º Trimestre    Registro M410 | MFS-20624 |
| LINHAS DA TABELA DINÂMICA | Texto | Código - Descrição | Exibe o código e a descrição das linhas da tabela dinâmica de cada registro gerado.  Tratamentos:  Exibir as linhas da tabela dinâmica, de acordo com a informação indicada no campo ‘Exibição dos Dados’ da tela de geração deste relatório.  As linhas da tabela dinâmica, devem ser exibidas em ordem crescente. | MFS-20624 |
| VALOR | Texto | XX,XX ou  - XX,XX | Exibe o valor de cada linha da tabela dinâmica que foi recuperada.  Tratamento:  Essa coluna irá exibir o saldo de cada linha e por período processado. | MFS-20624 |
| DETALHAMENTO | Texto | Descrição | Exibe o tipo de detalhamento da linha da tabela dinâmica que foi recuperada.  Tratamento:  Valores Válidos:  Conta Contábil Entrada Manual Fórmula Exibir com o texto ‘Fórmula’, se o tipo da linha igual a ‘CA’ e não existir associação ou se tipo da linha igual a ‘CNA’,  Exibir ‘Entrada Manual’, se o tipo da linha igual a ‘E’ e existir entrada manual na linha. exibir ‘Conta Contábil’, se o tipo da linha igual a ‘E’, ou tipo da linha igual a ‘CA’ e existir associação.   Para os registros do Bloco M:  Valores Válidos: Fórmula ‘nulo’ Exibir com o texto ‘Fórmula’, se o tipo da linha igual a ‘CA’ e não existir associação ou se tipo da linha igual a ‘CNA’, nos demais casos, deixar o campo nulo. | MFS-20624 |
| Relatório Analítico –  Registros de Origem de Tabela Dinâmica(*)  Cód. Registro - Descrição do Registro | Relatório Analítico –  Registros de Origem de Tabela Dinâmica(*)  Cód. Registro - Descrição do Registro | Relatório Analítico –  Registros de Origem de Tabela Dinâmica(*)  Cód. Registro - Descrição do Registro | Relatório Analítico –  Registros de Origem de Tabela Dinâmica(*)  Cód. Registro - Descrição do Registro | Relatório Analítico –  Registros de Origem de Tabela Dinâmica(*)  Cód. Registro - Descrição do Registro |
| Para os registros M300, M350(*) | Para os registros M300, M350(*) | Para os registros M300, M350(*) | Para os registros M300, M350(*) | Para os registros M300, M350(*) |
| LINHAS DA TABELA DINÂMICA | Texto | Cód - Descrição | Tratamentos:  Exibir as linhas da tabela dinâmica, de acordo com a informação indicada no campo ‘Exibição dos Dados’ da tela de geração deste relatório.  As linhas da tabela dinâmica, devem ser exibidas em ordem crescente.  As linhas do tipo R, não terão detalhamento. Os demais tipos, estão detalhados abaixo. | MFS-20624 |
| VALOR | Texto | X,XX ou -XX,XX | Exibe o valor da linha da tabela dinâmica recuperada. | MFS-20624 |
| Detalhamento das linhas da tabela dinâmica com tipos E (*) | Detalhamento das linhas da tabela dinâmica com tipos E (*) | Detalhamento das linhas da tabela dinâmica com tipos E (*) | Detalhamento das linhas da tabela dinâmica com tipos E (*) | Detalhamento das linhas da tabela dinâmica com tipos E (*) |
| CONTA CONTÁBIL | Texto | Cód - Descrição | Exibir o código e a descrição da conta contábil associada à linha da tabela dinâmica.  Tratamentos: As contas devem ser apresentadas por ordem de código. | MFS-20624 |
| CENTRO DE CUSTO | Texto | Cód - Descrição | Exibe o código e a descrição do centro de custo associado, caso exista.   Tratamentos: As contas devem ser apresentadas por ordem de código. | MFS-20624 |
| VALOR | Texto | X,XXC ou X,XXD | Exibir o valor da conta contábil e centro de custo (este último, se existir), referente a linha da tabela dinâmica.  Tratamento: Concatenar o valor com o indicador. | MFS-20624 |
| Para os registros M300 e M350 (*) | Para os registros M300 e M350 (*) | Para os registros M300 e M350 (*) | Para os registros M300 e M350 (*) | Para os registros M300 e M350 (*) |
| Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas da parte B(*)  Registros M305 | Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas da parte B(*)  Registros M305 | Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas da parte B(*)  Registros M305 | Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas da parte B(*)  Registros M305 | Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas da parte B(*)  Registros M305 |
| CONTA DA PARTE B | Texto | Cód - Descrição | Exibir o código e a descrição da conta da parte B.  Tratamentos: As contas devem ser apresentadas por ordem de código. | MFS-20624 |
| VALOR | Texto | XX,XX | Exibir o valor da conta da parte B, referente a linha da tabela dinâmica. | MFS-20624 |
| Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas contábeis(*)  Registros M310M360(*)  Cód. Registro - Descrição do Registro | Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas contábeis(*)  Registros M310M360(*)  Cód. Registro - Descrição do Registro | Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas contábeis(*)  Registros M310M360(*)  Cód. Registro - Descrição do Registro | Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas contábeis(*)  Registros M310M360(*)  Cód. Registro - Descrição do Registro | Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas contábeis(*)  Registros M310M360(*)  Cód. Registro - Descrição do Registro |
| CONTA CONTÁBIL | Texto | Cód - Descrição | Exibir o código e a descrição da conta contábil associada à linha da tabela dinâmica.  Tratamentos: As contas devem ser apresentadas por ordem de código. | MFS-20624 |
| CENTRO DE CUSTO | Texto | Cód - Descrição | Exibe o código e a descrição do centro de custo associado, caso exista.  Tratamentos: As contas devem ser apresentadas por ordem de código. | MFS-20624 |
| VALOR | Texto | X,XXC ou X,XXD | Exibir o valor da conta contábil e centro de custo (este último, se existir), referente a linha da tabela dinâmica.  Tratamento: Concatenar o valor com o indicador. | MFS-20624 |
| RECUPERAÇÃO DE VALORES | Texto | Cód. - Descrição | Exibe a informação utilizada para a recuperação dos valores (de cada conta contábil). | MFS-20624 |
| Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas contábeis M312/M362(*)  Cód. Registro - Descrição do Registro | Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas contábeis M312/M362(*)  Cód. Registro - Descrição do Registro | Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas contábeis M312/M362(*)  Cód. Registro - Descrição do Registro | Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas contábeis M312/M362(*)  Cód. Registro - Descrição do Registro | Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas contábeis M312/M362(*)  Cód. Registro - Descrição do Registro |
| LANÇAMENTO | Texto | Descrição | Exibe a informação de número de lançamento (se existir)  Tratamento:  Apresentar os lançamentos, ordenado pelo campo número, se existir lançamentos e o parâmetro ‘Relatório Analítico – Exibir os lançamentos associados dos registros do Bloco M’, estiver selecionado na tela de geração do relatório. | MFS-20624 |
| VALOR | Texto | XX,XXC ou XX,XXD | Exibe o valor do lançamento contábil.  Tratamento: Concatenar o valor com o indicador. | MFS-20624 |
| DEMAIS REGISTROS (*)  M410, M500 (*) | DEMAIS REGISTROS (*)  M410, M500 (*) | DEMAIS REGISTROS (*)  M410, M500 (*) | DEMAIS REGISTROS (*)  M410, M500 (*) | DEMAIS REGISTROS (*)  M410, M500 (*) |
| Relatório do Registro M410 (independente se tipo do Relatório = Sintético ou Analítico) (*) Cód. Registro - Descrição do Registro | Relatório do Registro M410 (independente se tipo do Relatório = Sintético ou Analítico) (*) Cód. Registro - Descrição do Registro | Relatório do Registro M410 (independente se tipo do Relatório = Sintético ou Analítico) (*) Cód. Registro - Descrição do Registro | Relatório do Registro M410 (independente se tipo do Relatório = Sintético ou Analítico) (*) Cód. Registro - Descrição do Registro | Relatório do Registro M410 (independente se tipo do Relatório = Sintético ou Analítico) (*) Cód. Registro - Descrição do Registro |
| PERÍODO (*) | Texto | Descrição | Ver regra do campo Período | MFS-20624 |
| GRUPO DA CONTA | Texto | Cód. | Exibe o código e a descrição do grupo da Conta da Parte B  Tratamentos:  Ordenar pelo campo código. | MFS-20624 |
| CONTA DA PARTE B | Texto | Cód. - Descrição | Exibe o código e a descrição da Conta da Parte B  Tratamentos:  Ordenar as contas pelo campo código. | MFS-20624 |
| TRIBUTO | Texto | Cód. - Descrição | Exibe o código e a descrição do tributo da conta da parte B  Tratamentos:  Ordenar pelo campo código. | MFS-20624 |
| DATA LANÇAMENTO | Texto | DD/MM/AAAA | Exibe a data do Lançamento do ajuste da Conta da Parte B.  Tratamentos:  Ordenar pelo campo data lançamento. | MFS-20624 |
| VALOR | Texto | x.xxx,xxCR, ou x.xxx,xxDB | Exibe o valor do lançamento da Conta da Parte B e o indicador | MFS-20624 |
| CONTRAPARTIDA | Texto | Cód. - Descrição | Exibe a Conta da Parte B, que será gerado o lançamento de Contrapartida. | MFS-20624 |
| CONTA DA PARTE B ORIGEM DA CONTRAPARTIDA | Texto | Cód. - Descrição | Exibe a Conta da Parte B, que originou o lançamento de Contrapartida. | MFS-20624 |
| HISTÓRICO | Texto | Descrição | Exibe o valor do lançamento da Conta da Parte B. | MFS-20624 |
| AJUSTE COM ORIGEM NA PARTE B | Texto | Cód. - Descrição | Exibe se o ajuste é incremental ou cumulativo. | MFS-20624 |
| TRIBUTAÇÃO DIFERIDA | Texto | Descrição | Exibe se há ou não Tributação Diferida. | MFS-20624 |
| Registro M415 – Processos (*)  Cód. Registro - Descrição do Registro | Registro M415 – Processos (*)  Cód. Registro - Descrição do Registro | Registro M415 – Processos (*)  Cód. Registro - Descrição do Registro | Registro M415 – Processos (*)  Cód. Registro - Descrição do Registro | Registro M415 – Processos (*)  Cód. Registro - Descrição do Registro |
| TIPO | Texto | Cód. - Descrição | Exibe o tipo de processo do ajuste.  Tratamentos:  Ordenar pelo tipo de processo. | MFS-20624 |
| NÚMERO | Texto | Descrição | Exibe o número do processo.  Tratamentos:  Ordenar pelo número de processo. | MFS-20624 |
| Relatório do Registro M500 (independente se tipo do Relatório = Sintético ou Analítico) (*) Cód. Registro - Descrição do Registro | Relatório do Registro M500 (independente se tipo do Relatório = Sintético ou Analítico) (*) Cód. Registro - Descrição do Registro | Relatório do Registro M500 (independente se tipo do Relatório = Sintético ou Analítico) (*) Cód. Registro - Descrição do Registro | Relatório do Registro M500 (independente se tipo do Relatório = Sintético ou Analítico) (*) Cód. Registro - Descrição do Registro | Relatório do Registro M500 (independente se tipo do Relatório = Sintético ou Analítico) (*) Cód. Registro - Descrição do Registro |
| GRUPO DA CONTA | Texto | Cód. | Exibe o código e a descrição do grupo da Conta da Parte B  Tratamentos:  Ordenar pelo campo código. | MFS-20624 |
| CONTA DA PARTE B | Texto | Cód. - Descrição | Exibe o código e a descrição da Conta da Parte B  Tratamentos:  Ordenar as contas pelo campo código. | MFS-20624 |
| TRIBUTO | Texto | Cód. - Descrição | Exibe o código e a descrição do tributo da conta da parte B  Tratamentos:  Ordenar pelo campo código. | MFS-20624 |
| SALDO INICIAL | Texto | x.xxx,xxC ou x.xxx,xxD | Exibe o Saldo Inicial da Conta da Parte B. | MFS-20624 |
| LANÇAMENTOS DA PARTE A | Texto | x.xxx,xxC ou x.xxx,xxD | Exibe o valor do Lançamento da parte A para a Conta da Parte B. | MFS-20624 |
| LANÇAMENTOS DA PARTE B | Texto | x.xxx,xxC ou x.xxx,xxD | Exibe o valor do Lançamento da Parte B para a Conta da Parte B. | MFS-20624 |
| LANÇAMENTOS DA PARTE B - CONTRAPARTIDA | Texto | x.xxx,xxC ou x.xxx,xxD | Exibe o valor do Lançamento de Contrapartida da parte B para a Conta da Parte B. | MFS-20624 |
| SALDO FINAL | Texto | x.xxx,xxC ou x.xxx,xxD | Exibe o Saldo Final da Conta da Parte B. | MFS-20624 |
| Relatório do Registro N615 (independente se tipo do Relatório = Sintético ou Analítico) (*) Cód. Registro - Descrição do Registro | Relatório do Registro N615 (independente se tipo do Relatório = Sintético ou Analítico) (*) Cód. Registro - Descrição do Registro | Relatório do Registro N615 (independente se tipo do Relatório = Sintético ou Analítico) (*) Cód. Registro - Descrição do Registro | Relatório do Registro N615 (independente se tipo do Relatório = Sintético ou Analítico) (*) Cód. Registro - Descrição do Registro | Relatório do Registro N615 (independente se tipo do Relatório = Sintético ou Analítico) (*) Cód. Registro - Descrição do Registro |
| BASE DE CÁLCULO | Texto | x.xxx,xx | Exibe o valor da base de cálculo do incentivo. | MFS-20624 |
| PERCENTUAL FINOR | Texto | x,xxxx | Exibe o valor do percentual do incentivo. | MFS-20624 |
| VALOR LÍQUIDO FINOR | Texto | x.xxx,xx | Exibe o valor líquido do incentivo. | MFS-20624 |
| PERCENTUAL FINAM | Texto | x,xxxx | Exibe o valor do percentual do incentivo. | MFS-20624 |
| VALOR LÍQUIDO FINAM | Texto | x.xxx,xx | Exibe o valor líquido do incentivo. | MFS-20624 |
| VALOR TOTAL | Texto | x.xxx,xx | Exibe o valor do incentivo. | MFS-20624 |
| Rodapé(*) | Rodapé(*) | Rodapé(*) | Rodapé(*) | Rodapé(*) |
| MasterSaf – Atendimento Fiscal | Texto | - | Apresentar o texto do lado inferior esquerdo. | MFS-20624 |
| ECF – Escrituração Contábil Fiscal | Texto | - | Apresentar o texto do lado inferior direito. | MFS-20624 |

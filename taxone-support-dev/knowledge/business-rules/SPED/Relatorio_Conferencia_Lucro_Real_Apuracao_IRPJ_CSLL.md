# Relatorio_Conferencia_Lucro_Real_Apuracao_IRPJ_CSLL

> Fonte: Relatorio_Conferencia_Lucro_Real_Apuracao_IRPJ_CSLL.docx






THOMSON REUTERS

Relatório de Conferência do Lucro Real – Apuração IRPJ/CSLL



DOCUMENTO DE REQUISITO


Sumário

1.	INTRODUÇÃO	3
2.	DOCUMENTOS DE REFERÊNCIA	3
3.	Tela de Parâmetros	3
4.	LEIAUTE	9
4.1.	Regras dos campos do Relatório (Leiaute)	10
4.2.	Exemplos do Relatório	21

## INTRODUÇÃO


Objetivo desta especificação é criar uma tela para permitir ao usuário parametrizar dados e gerar o relatório de Conferência dos registros exibidos na tela Lucro Real – Demonstração, dos registros do bloco N.

## DOCUMENTOS DE REFERÊNCIA


- Layout_ECF.xlsx
- Tela_Lucro_Real-Registros_de_Tabela_Dinamica.doc


## Tela de Parâmetros

Localização da tela:  ECF - Escrituração Contábil Fiscal >>Relatórios >> Conferência do Lucro Real >> Apuração IRPJ/CSLL

Título da tela: Conferência do Lucro Real - Apuração IRPJ/CSLL


As regras destacadas em amarelo (e com fonte vermelha), não serão implementadas neste momento.



## LEIAUTE


Origem das informações para geração do relatório:

Tela Lucro Real, registros oriundos de Tabela Dinâmica (todos os registros processados da tabela dinâmica do bloco N).
Registros N500, N600, N610, N620, N630, N650, N660 e N670

Tela Lucro Real, demais registros
RegistroN615

Tipos de Relatórios:

Sintético
Analítico

O registro N615  não considera esse parâmetro (será gerado com o mesmo leiaute, independentemente do tipo de relatório escolhido) .

Regra de agrupamento:

Agrupar por Informação do ECF, por registro e período de apuração.


Ordenação:
Ordenar por código do estabelecimento, data inicial Informação ECF, período de apuração, código do registro (seguindo a hierarquia dos registros de acordo com o arquivo Layout_ECF.xlsx) e

Se registro oriundo de Tabelas Dinâmicas:

Código da linha da tabela dinâmica. Todos de forma crescente.

Se registro oriundo do Plano Referencial:

Código da conta referencial. Todos de forma crescente.

Nos relatórios analíticos, ordenar os campos Conta Contábil e Centro de Custo, se houver, de forma crescente.



Busca de Registros:

Considerar as informações que foram processadas e exibidas na tela do Lucro Real, de acordo com as informações de filtro indicadas na tela de geração do relatório. Não será possível selecionar a apuração anual nos períodos Inicial e Final, na tela de geração do relatório, se existir dados referente a apuração Anual (A00), a mesma deve ser exibida no relatório.
Para os demais registros (N615), não será considerado o tipo de relatório, ou seja, se marcados esses registros serão gerados sempre em um único leiaute.

#### Regras dos campos do Relatório (Leiaute)



(*)Não exibir a descrição na tela/relatório.

#### Exemplos do Relatório



Registros de Tabela Dinâmica – Sintético



Registros de Tabela Dinâmica – Analítico




N500 – linha 2 (com percentual de receita e entrada manual nos percentuais)



N650 – linha 2 (com percentual de receita e entrada manual nos percentuais)



N620 – linha 8 e N630 – linha 9 (PAT)

DEMAIS REGISTROS
Registro N615

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
| Apenas Registros com Movimento | Check-box |  |  | Default: Marcado | Permite que o usuário escolha a forma de exibição das informações no relatório, se deseja visualizar apenas os registros que possuam movimento ou todos os registros.  Tratamentos:   Quando o usuário selecionar a opção “Apenas Registros com Movimento”, apresentar no relatório apenas os registros cujo campo “Valor” seja diferente de zero.  Atenção para o relatório Sintético: Devido à quebra do relatório em mais de uma página, a linha que possuir valor diferente de zero, em pelo menos um mês/trimestre (dentro da escrituração), a mesma deve sair em todas as páginas do relatório.  Esta regra acima não se aplica ao relatório Analítico, que possui estrutura diferente de exibição de valor.  Quando o usuário desmarcar a opção “Apenas Registros com Movimento”, apresentar no relatório todos os registros. | MFS-20624 |
| Gravar Arquivos | Radio-Button | Arquivo Único | Sim | Sim | Opções Válidas:  Quebra por Informações ECF Arquivo Único  Tratamentos:  Se selecionada a opção ‘Quebra por Estabelecimentos’, será gerado um relatório por Informações ECF, com todos os registros selecionados. Se selecionada a opção ‘Arquivo Único’, será gerado em um único relatório, contendo todas as Informações ECF recuperadas, com os dados de todos os registros selecionados. Se este campo for alterado, os demais campos não devem ser limpos. | MFS-20624 |
| Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos | Informações ECF dos Estabelecimentos |
| Informações ECF(*) | Check-box | Código Estab - CGC - Exercício -  Data Inicial da Escrituração  (076 - XXXXXXXXXXXXXX -  01/03/2017) | - | - | Permite ao usuário selecionar um ou mais registros de Informações ECF.  Tratamentos:  Recuperar apenas as Informações ECF que estão compatíveis com as opções de filtro preenchidas na tela de parametrização do relatório. | MFS-20624 |
| Marcar Todos | Check-box | Desmarcado | - | - | Permite ao usuário selecionar todas ou desmarcar todas as Informações ECF.  Tratamentos:  Se selecionar o check-box, todos os registros exibidos no componente de Informações serão marcados.  Se desmarcar o check-box, o sistema deve desmarcar todos os registros de Informações ECF selecionados. | MFS-20624 |
| Registros | Registros | Registros | Registros | Registros | Registros | Registros |
| Registros (*) | Check-box | Cód. - Descrição | - | - | Permite ao usuário selecionar um ou mais registros do Lucro Real, do bloco N, da Tela Demonstração,) para gerar o relatório.  Tratamentos:  Só deve ser exibido os registros, quando o campo versão estiver preenchido. Recuperar os registros do bloco N, compatível com a versão que foi indicada na tela de parâmetros do relatório.  Lista de Registros Válidos: N500 N600 N610 N615 N620 N630 N650 N660 N670 | MFS-20624 |
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
| Título1: (*) Relatório de Conferência do Lucro Real – Apuração IRPJ/CSLL - Sintético  Título 2: (*) Relatório de Conferência do Lucro Real – Apuração IRPJ/CSLL - Analítico   Exibir somente um dos títulos de acordo com o tipo de relatório parametrizado na tela de geração.(*) | Título1: (*) Relatório de Conferência do Lucro Real – Apuração IRPJ/CSLL - Sintético  Título 2: (*) Relatório de Conferência do Lucro Real – Apuração IRPJ/CSLL - Analítico   Exibir somente um dos títulos de acordo com o tipo de relatório parametrizado na tela de geração.(*) | Título1: (*) Relatório de Conferência do Lucro Real – Apuração IRPJ/CSLL - Sintético  Título 2: (*) Relatório de Conferência do Lucro Real – Apuração IRPJ/CSLL - Analítico   Exibir somente um dos títulos de acordo com o tipo de relatório parametrizado na tela de geração.(*) | Título1: (*) Relatório de Conferência do Lucro Real – Apuração IRPJ/CSLL - Sintético  Título 2: (*) Relatório de Conferência do Lucro Real – Apuração IRPJ/CSLL - Analítico   Exibir somente um dos títulos de acordo com o tipo de relatório parametrizado na tela de geração.(*) | Título1: (*) Relatório de Conferência do Lucro Real – Apuração IRPJ/CSLL - Sintético  Título 2: (*) Relatório de Conferência do Lucro Real – Apuração IRPJ/CSLL - Analítico   Exibir somente um dos títulos de acordo com o tipo de relatório parametrizado na tela de geração.(*) |
| Estabelecimento | Texto | Código - Descrição | Exibe o estabelecimento de cada Informações ECF que foi recuperada. | MFS-20624 |
| Exercício | Texto | AAAA | Exibe o exercício correspondente a cada Informações ECF, que foi recuperada. | MFS-20624 |
| Data Inicial | Texto | DD/MM/AAAA | Exibe a data inicial correspondente a cada Informações ECF que foi recuperada. | MFS-20624 |
| Versão | Texto | - | Exibe a versão correspondente a cada Informações ECF recuperada. | MFS-20624 |
| Forma de Tributação | Texto | - | Exibe a forma de tributação correspondente a cada Informações ECF que foi recuperada. | MFS-20624 |
| Apuração | Texto | - | Exibe a apuração correspondente a cada Informação ECF que foi recuperada. | MFS-20624 |
| Relatório Sintético – Registros de Origem de Tabela Dinâmica (*) Registros Atendidos: N500, N600, N610, N620, N630, N650, N660 e N670 (*)  Cód. Registro - Descrição do Registro | Relatório Sintético – Registros de Origem de Tabela Dinâmica (*) Registros Atendidos: N500, N600, N610, N620, N630, N650, N660 e N670 (*)  Cód. Registro - Descrição do Registro | Relatório Sintético – Registros de Origem de Tabela Dinâmica (*) Registros Atendidos: N500, N600, N610, N620, N630, N650, N660 e N670 (*)  Cód. Registro - Descrição do Registro | Relatório Sintético – Registros de Origem de Tabela Dinâmica (*) Registros Atendidos: N500, N600, N610, N620, N630, N650, N660 e N670 (*)  Cód. Registro - Descrição do Registro | Relatório Sintético – Registros de Origem de Tabela Dinâmica (*) Registros Atendidos: N500, N600, N610, N620, N630, N650, N660 e N670 (*)  Cód. Registro - Descrição do Registro |
| Período (*) | Texto | Descrição | Exibe a descrição de cada período informado, conforme as apurações que foram recuperadas, baseadas nos campos de data inicial e final na geração do relatório.   Tratamento:  Se existir mais de um período a ser exibido, os mesmos devem ser demonstrados em ordem crescente, um abaixo do outro, (após a exibição de todos os códigos de linha do registro).  Valores Válidos:  Se apuração = Anual: Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro Anual  Se apuração  =  Trimestral 1º Trimestre 2º Trimestre 3º Trimestre 4º Trimestre | MFS-20624 |
| LINHAS DA TABELA DINÂMICA | Texto | Código - Descrição | Exibe o código e a descrição das linhas da tabela dinâmica de cada registro gerado.  Tratamentos:  Exibir as linhas da tabela dinâmica, de acordo com a informação indicada no campo ‘Exibição dos Dados’ da tela de geração deste relatório.  As linhas da tabela dinâmica, devem ser exibidas em ordem crescente. | MFS-20624 |
| VALOR | Texto | XX,XX ou  - XX,XX | Exibe o valor de cada linha da tabela dinâmica que foi recuperada.  Tratamento:  Essa coluna irá exibir o saldo de cada linha e por período processado. | MFS-20624 |
| DETALHAMENTO | Texto | Descrição | Exibe o tipo de detalhamento da linha da tabela dinâmica que foi recuperada.  Tratamento:  Valores Válidos:  Conta Contábil Entrada Manual Fórmula Exibir com o texto ‘Fórmula’, se o tipo da linha igual a ‘CA’ e não existir associação ou se tipo da linha igual a ‘CNA’,  Exibir ‘Entrada Manual’, se o tipo da linha igual a ‘E’ e existir entrada manual na linha. exibir ‘Conta Contábil’, se o tipo da linha igual a ‘E’, ou tipo da linha igual a ‘CA’ e existir associação.   Para as linhas 8 do N620 e 9 do N630:  Valores Válidos: Fórmula ‘nulo’ Exibir com o texto ‘Fórmula’, se o tipo da linha igual a ‘CA’ e não existir associação ou se tipo da linha igual a ‘CNA’, nos demais casos, deixar o campo nulo. | MFS-20624 |
| Relatório Analítico –  Registros de Origem de Tabela Dinâmica(*)  Cód. Registro - Descrição do Registro | Relatório Analítico –  Registros de Origem de Tabela Dinâmica(*)  Cód. Registro - Descrição do Registro | Relatório Analítico –  Registros de Origem de Tabela Dinâmica(*)  Cód. Registro - Descrição do Registro | Relatório Analítico –  Registros de Origem de Tabela Dinâmica(*)  Cód. Registro - Descrição do Registro | Relatório Analítico –  Registros de Origem de Tabela Dinâmica(*)  Cód. Registro - Descrição do Registro |
| Para os registros N500, N600, N610, N620, N630, N650, N660 e N670 (*) | Para os registros N500, N600, N610, N620, N630, N650, N660 e N670 (*) | Para os registros N500, N600, N610, N620, N630, N650, N660 e N670 (*) | Para os registros N500, N600, N610, N620, N630, N650, N660 e N670 (*) | Para os registros N500, N600, N610, N620, N630, N650, N660 e N670 (*) |
| LINHAS DA TABELA DINÂMICA | Texto | Cód - Descrição | Tratamentos:  Exibir as linhas da tabela dinâmica, de acordo com a informação indicada no campo ‘Exibição dos Dados’ da tela de geração deste relatório.  As linhas da tabela dinâmica, devem ser exibidas em ordem crescente.  As linhas do tipo R, não terão detalhamento. Os demais tipos, estão detalhados abaixo. | MFS-20624 |
| VALOR | Texto | X,XX ou -XX,XX | Exibe o valor da linha da tabela dinâmica recuperada. | MFS-20624 |
| Detalhamento das linhas da tabela dinâmica com tipos E (*) | Detalhamento das linhas da tabela dinâmica com tipos E (*) | Detalhamento das linhas da tabela dinâmica com tipos E (*) | Detalhamento das linhas da tabela dinâmica com tipos E (*) | Detalhamento das linhas da tabela dinâmica com tipos E (*) |
| CONTA CONTÁBIL | Texto | Cód - Descrição | Exibir o código e a descrição da conta contábil associada à linha da tabela dinâmica.  Tratamentos: As contas devem ser apresentadas por ordem de código. | MFS-20624 |
| CENTRO DE CUSTO | Texto | Cód - Descrição | Exibe o código e a descrição do centro de custo associado, caso exista.   Tratamentos: As contas devem ser apresentadas por ordem de código. | MFS-20624 |
| VALOR | Texto | X,XXC ou X,XXD | Exibir o valor da conta contábil e centro de custo (este último, se existir), referente a linha da tabela dinâmica.  Tratamento: Concatenar o valor com o indicador. | MFS-20624 |
| Detalhamento para os registros N500 e N650, linha 2 com percentual de receita bruta e sem entrada manual nos percentuais (*) | Detalhamento para os registros N500 e N650, linha 2 com percentual de receita bruta e sem entrada manual nos percentuais (*) | Detalhamento para os registros N500 e N650, linha 2 com percentual de receita bruta e sem entrada manual nos percentuais (*) | Detalhamento para os registros N500 e N650, linha 2 com percentual de receita bruta e sem entrada manual nos percentuais (*) | Detalhamento para os registros N500 e N650, linha 2 com percentual de receita bruta e sem entrada manual nos percentuais (*) |
| Subtítulo: (*)  DEMONSTRAÇÃO DO CÁLCULO DA ESTIMATIVA DA RECEITA BRUTA | Subtítulo: (*)  DEMONSTRAÇÃO DO CÁLCULO DA ESTIMATIVA DA RECEITA BRUTA | Subtítulo: (*)  DEMONSTRAÇÃO DO CÁLCULO DA ESTIMATIVA DA RECEITA BRUTA | Subtítulo: (*)  DEMONSTRAÇÃO DO CÁLCULO DA ESTIMATIVA DA RECEITA BRUTA | Subtítulo: (*)  DEMONSTRAÇÃO DO CÁLCULO DA ESTIMATIVA DA RECEITA BRUTA |
| CONTA CONTÁBIL | Texto | Cód - Descrição | Exibir o código e a descrição da conta contábil associada à linha da tabela dinâmica.  Tratamentos: As contas devem ser apresentadas por ordem de código. | MFS-20624 |
| CENTRO DE CUSTO | Texto | Cód - Descrição | Exibe o código e a descrição do centro de custo associado, caso exista.  Tratamentos: As contas devem ser apresentadas por ordem de código. | MFS-20624 |
| VALOR | Texto | XX,XXC ou X,XXD | Exibir o valor da conta contábil e centro de custo (este último, se existir), referente a linha da tabela dinâmica, antes da aplicação do percentual de receita.  Tratamento: Concatenar o valor com o indicador. | MFS-20624 |
| PERCENTUAL DA RECEITA BRUTA | Texto | XX,XXXX | Exibe o valor do percentual de receita bruta que foi utilizado. | MFS-20624 |
| Detalhamento para os registros N500, linha 2 com percentual de receita bruta e com entrada manual nos percentuais (*) | Detalhamento para os registros N500, linha 2 com percentual de receita bruta e com entrada manual nos percentuais (*) | Detalhamento para os registros N500, linha 2 com percentual de receita bruta e com entrada manual nos percentuais (*) | Detalhamento para os registros N500, linha 2 com percentual de receita bruta e com entrada manual nos percentuais (*) | Detalhamento para os registros N500, linha 2 com percentual de receita bruta e com entrada manual nos percentuais (*) |
| VALOR DA RECEITA BRUTA SUJEITA A 1,6% | Texto | XX,XX | Exibe o valor da receita sujeita ao percentual referido. | MFS-20624 |
| VALOR CALCULADO | Texto | XX,XX | Exibe o valor calculado da receita com o percentual aplicado. | MFS-20624 |
| VALOR DARECEITA BRUTA SUJEITA A 8% | Texto | XX,XX | Exibe o valor da receita sujeita ao percentual referido. | MFS-20624 |
| VALOR CALCULADO | Texto | XX,XX | Exibe o valor calculado da receita com o percentual aplicado. | MFS-20624 |
| VALOR DARECEITA BRUTA SUJEITA A 16% | Texto | XX,XX | Exibe o valor da receita sujeita ao percentual referido. | MFS-20624 |
| VALOR CALCULADO | Texto | XX,XX | Exibe o valor calculado da receita com o percentual aplicado. | MFS-20624 |
| VALOR DARECEITA BRUTA SUJEITA A 32% | Texto | XX,XX | Exibe o valor da receita sujeita ao percentual referido. | MFS-20624 |
| VALOR CALCULADO | Texto | XX,XX | Exibe o valor calculado da receita com o percentual aplicado. | MFS-20624 |
| VALOR DARECEITA BRUTA SUJEITA A 100% | Texto | XX,XX | Exibe o valor da receita sujeita ao percentual referido. | MFS-20624 |
| VALOR CALCULADO | Texto | XX,XX | Exibe o valor calculado da receita com o percentual aplicado. | MFS-20624 |
| VALOR TOTAL DA RECEITA BRUTA | Texto | XX,XX | Exibe o valor total das receitas. | MFS-20624 |
| SOMATÓRIO DO VALOR CALCULADO | Texto | XX,XX | Exibe o valor total calculado da receita (valor aplicado ao percentual). | MFS-20624 |
| Detalhamento para os registros N650, linha 2 com percentual de receita bruta e com entrada manual nos percentuais (*) | Detalhamento para os registros N650, linha 2 com percentual de receita bruta e com entrada manual nos percentuais (*) | Detalhamento para os registros N650, linha 2 com percentual de receita bruta e com entrada manual nos percentuais (*) | Detalhamento para os registros N650, linha 2 com percentual de receita bruta e com entrada manual nos percentuais (*) | Detalhamento para os registros N650, linha 2 com percentual de receita bruta e com entrada manual nos percentuais (*) |
| VALOR DA RECEITA BRUTA SUJEITA A 12% | Texto | XX,XX | Exibe o valor da receita sujeita ao percentual referido. | MFS-20624 |
| VALOR CALCULADO | Texto | XX,XX | Exibe o valor calculado da receita com o percentual aplicado. | MFS-20624 |
| VALOR DA RECEITA BRUTA SUJEITA A 32% | Texto | XX,XX | Exibe o valor da receita sujeita ao percentual referido. | MFS-20624 |
| VALOR CALCULADO | Texto | XX,XX | Exibe o valor calculado da receita com o percentual aplicado. | MFS-20624 |
| VALOR DARECEITA BRUTA SUJEITA A 100% | Texto | XX,XX | Exibe o valor da receita sujeita ao percentual referido. | MFS-20624 |
| VALOR CALCULADO | Texto | XX,XX | Exibe o valor calculado da receita com o percentual aplicado. | MFS-20624 |
| VALOR TOTAL DA RECEITA BRUTA | Texto | XX,XX | Exibe o valor total das receitas. | MFS-20624 |
| SOMATÓRIO DO VALOR CALCULADO | Texto | XX,XX | Exibe o valor total calculado da receita (valor aplicado ao percentual). | MFS-20624 |
| Detalhamento para as linhas 9 do registro N620 e 8 do registro N630A, N630B ou N630C. (*) | Detalhamento para as linhas 9 do registro N620 e 8 do registro N630A, N630B ou N630C. (*) | Detalhamento para as linhas 9 do registro N620 e 8 do registro N630A, N630B ou N630C. (*) | Detalhamento para as linhas 9 do registro N620 e 8 do registro N630A, N630B ou N630C. (*) | Detalhamento para as linhas 9 do registro N620 e 8 do registro N630A, N630B ou N630C. (*) |
| Agrupamento (*)  ANTES DA ATUALIZAÇÃO | Texto |  | Agrupar os campos VALOR DO PAT e LIMITE DE 15% SOBRE O PAT | MFS-20624 |
| VALOR DO PAT | Texto | XX,XX | Exibe o valor da linha 9 do registro N620 ou 8 do registro N630A, N630B ou N630C antes de realizar o cálculo do PAT. Obs.: Mesmo valor após o processamento da importação dos saldos. | MFS-20624 |
| LIMITE DE 15% SOBRE O PAT | Texto | XX,XX | Exibe o limite de 15% calculado sobre o PAT antes da atualização. | MFS-20624 |
| VALOR DO IMPOSTO DEVIDO | Texto | XX,XX | Exibe o valor do imposto, ou seja, valor da linha 3 do registro N620 ou 8 do registro N630A, N630B ou N630C. | MFS-20624 |
| LIMITE DE 4% SOBRE O IMPOSTO DEVIDO | Texto | XX,XX | Exibe o limite de 4% calculado sobre o imposto devido. | MFS-20624 |
| VALOR DO PDTI/PDTA | Texto | XX,XX | Exibe o valor do PDTI/PDTA, ou seja, valor da linha 10 do registro N620 e linha 9 do registro N630A, N630B ou N630C | MFS-20624 |
| LIMITE DE 4% COM PDTI/PDTA | Texto | XX,XX | Exibe o limite de 4% com a dedução do incentivo PDTI/PDTA. | MFS-20624 |
| VALOR DO PAT DE PERÍODOS ANTERIORES | Texto | XX,XX | Exibe o valor de PAT que foi utilizado de períodos anteriores. | MFS-20624 |
| VALOR DO PAT ATUALIZADO | Texto | XX,XX | Exibe o valor do PAT após o cálculo.  Obs.: Mesmo valor da linha 9 do registro N620 ou 8 do registro N630A, N630B ou N630C após a realização do cálculo de registros e fórmulas. | MFS-20624 |
| DEMAIS REGISTROS (*)  N615 (*) | DEMAIS REGISTROS (*)  N615 (*) | DEMAIS REGISTROS (*)  N615 (*) | DEMAIS REGISTROS (*)  N615 (*) | DEMAIS REGISTROS (*)  N615 (*) |
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

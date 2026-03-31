---
source: "MTZ_Tela de Guia Complementar.docx"
category: Tax Payments
converted: auto
---





THOMSON REUTERS

Matriz da tela Contabilização

Tela de Guia Complementar e Geração Arquivos - JSON



DOCUMENTO DE REQUISITO


Sumário

**1.	Introdução	3**
2.	Documento de Referência	3
3.	Fluxo Principal Seleção de dados:	3
4.	Tela Guia Complementar:	4
4..1.	Parâmetros:	6
4..2.	Calcular valor da Diferença a pagar	9
4..3.	Estrutura de Dados JSON:	11
4..4.	Botão – Gerar JSON	11
4..5.	Campos para geração do JSON:	12
4..6.	Controle de Geração	13
4..7.	Processos:	15
4..8.	Regras de negócio:	16


# Introdução

Disponibilizar uma tela específica para cálculo e emissão de guias complementares em situações em que houver diferença a pagar resultante da reapuração dos impostos ICMS-Próprio, ICMS-ST, IPI, PIS-Cumulativo, COFINS-Cumulativo, PIS–Não Cumulativo e COFINS–Não Cumulativo. Essa tela tem como objetivo principal identificar e consolidar as diferenças entre o valor reapurado e o valor originalmente apurado/pago, possibilitando a geração do arquivo JSON contendo os valores de diferença a pagar para cada tributo contemplado.



# Documento de Referência



# Fluxo Principal Seleção de dados:

Este caso de uso descreve o processo para a geração de arquivos – Lançamentos Contábeis





**Localização da Tela:**

- Agrupamentos: Básico
- Módulo: Manutenção >> Guia de Pagamento >> Guia Complementar
- Menu: Acesso Principal >> Guia de Pagamentos

Prótotipo







# Tela Guia Complementar:






# Parâmetros:



# Calcular valor da Diferença a pagar

Teremos dois Tooltips para incluir informações para usuário visualizar para o campo Status da Guia e Diferença de valor a pagar



# Estrutura de Dados JSON:
A estrutura de dados JSON foi projetada para armazenar e organizar informações relevantes às operações realizadas pelo usuário. As operações incluem lançamentos contábeis relacionados às seguintes categorias de lançamentos Contábeis:
ICMS-Próprio Complementar
ICMS-ST Complementar
IPI Complementar
PIS-Cumulativo Complementar
COFINS – Cumulativo Complementar
PIS-Não Cumulativo Complementar
COFINS – Não Cumulativo Complementar

# Botão – Gerar JSON

Permitir ao usuário gerar um arquivo JSON contendo os dados consolidados da guia complementar, respeitando os parâmetros e cálculos realizados na tela.

**Pré-condições**
Todos os campos obrigatórios devem estar preenchidos e validados:


# Campos para geração do JSON:

A seguir, apresentamos os campos essenciais para a APIs que facilita a interação com as estruturas de dados JSON, incluindo requisitos de obrigatoriedade.








# Controle de Geração






# Processos:




# Tela de Status
Os arquivos gerados serão enviados via Tela de Status, após revisão e execução do usuário

# Relatório de Status
Os dados da guia Complementar farão parte do relatório de Status

# Regras de Negócio

---

| OS/CH | Nome | Descrição |
| --- | --- | --- |
| ADO | Millys Lopes | Tela de Geração – Lançamentos Contábeis arquivo JSON |
|  |  |  |


---

| Documentação do Caso de Uso | Documentação do Caso de Uso |
| --- | --- |
| Ator Principal | Usuário do sistema |
| Pré- Condições | A guia original já foi emitida e paga, e seu status deve estar registrado no sistema como “Guia Pagar” -Recuperado via SAFX-Retorno   A reapuração dos impostos no Tax One foi concluída, gerando valores reapurados para os tributos ICMS-Próprio, ICMS-ST, IPI, PIS-Cumulativo, COFINS-Cumulativo, PIS-Não Cumulativo e COFINS-Não Cumulativo.  Os dados  apuração reapurada estão disponíveis e consistentes para comparação com a guia pagar |
| Pós-Condições | Os dados são processados e armazenados, ficando disponíveis para uso nas etapas subsequentes, exibidos na tela de Status para envio do JSON e Relatório de Conferência e para geração de uma nova guia. |


---

| Ações do Ator | Ações do Sistema |
| --- | --- |
| O usuário acessa a Tela de Guia Complementar | O sistema carrega a tela e apresenta os filtros/parametrizações necessárias (Empresa, UF, Estabelecimento e Periodo) |
| O usuário preencher os parâmetros | O sistema valida os parâmetros preenchidos (formato, obrigatoriedade e consistência).  O sistema consulta as apurações  e reapurada correspondentes. Ao Periodo e Guias Pagas |
| Visualização de Resultado | O sistema processa as informações e apresenta, na grade de resultados, a comparação entre valores originais, reapurados e diferença a pagar para cada tributo. |
| Usuário Analisar e visualizar o valor da diferença | O sistema disponibiliza ações por tributo: visualizar detalhes, emitir guia, gerar JSON |


---

|  | Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RN01 | Empresa | Campo | S | S | Código Descrição | Exibe o código e a descrição da empresa selecionada no Tax One |  |
| RN02 | Estabelecimento | Checkbox | S | S | Default: Não selecionado | Lista os códigos e descrições dos estabelecimentos vinculados à empresa selecionada. |  |
| RN03 | UF | Checkbox | Não | S | Default: Não selecionado | Lista as UFs dos estabelecimentos vinculados ou todas as UFs. |  |
| RN04 | Grupo Imposto | Dropdown | Sim | Sim | Default: Não preenchido | O campo "Grupo Imposto" será apresentado como um dropdown contendo uma lista de impostos disponíveis. O usuário poderá selecionar apenas uma opção por vez. Opções disponíveis: ICMS-Próprio Complementar ICMS-ST Complementar IPI Complementar PIS-Cumulativo Complementar COFINS – Cumulativo Complementar PIS-Não Cumulativo Complementar COFINS – Não Cumulativo Complementar |  |
| RN05 | Periodo | Campo | Sim | Sim | DD/MM/AAAA | Regra de Preenchimento do Campo: Este campo deve ser preenchido pelo usuário no formato 'DD/MM/AAAA' (Mês/Ano do Exercício). Esse formato é essencial para identificar o período específico relacionado à apuração dos impostos previamente selecionados. A data inserida é fundamental, pois define o intervalo necessário para a busca e o processamento dos dados fiscais. Para cada período informado, a busca será associada aos seguintes campos: empresa, estabelecimento, UF, grupo de imposto, imposto selecionado. Esses elementos serão utilizados para identificar a regra de negócio correspondente, conforme descrito abaixo:  Regra de Negócio (RN): |  |
| RN06 | Número de documento de gerado | Campo | Sim | Sim | Numérico | O sistema deverá buscar na tabela "Guia de Pagamento" o valor do campo NUM_DOC_ORIGEM, considerando os seguintes filtros: Empresa, Estabelecimento, UF, Período, Grupo de Imposto |  |
| RN07 | Código da Arrecadação | Campo | Sim | Sim | Numérico | O sistema deverá buscar na tabela "Guia de Pagamento" o valor do campo COD_ARRECADACAO, considerando os seguintes filtros: Empresa, Estabelecimento, UF, Período, Grupo de Imposto, NUM_DOC_ORIGEM |  |
| RN08 | Código Da Receita | Campo | Sim | Sim | Numérico | O sistema deverá buscar na tabela "Guia de Pagamento" o valor do campo COD_RECEITA, considerando os seguintes filtros: Empresa, Estabelecimento, UF, Período, Grupo de Imposto, NUM_DOC_ORIGEM, COD_ARRECADACAO |  |
| RN09 | Detalhamento da Receita | Campo | Sim | Sim | Numérico | O sistema deverá buscar na tabela "Guia de Pagamento" o valor do campo DET_RECEITA, considerando os seguintes filtros: Empresa, Estabelecimento, UF, Período, Grupo de Imposto, NUM_DOC_ORIGEM, COD_ARRECADACAO, COD_RECEITA |  |
| RN10 | Status da Guia |  |  |  |  | Descrição: O sistema deve buscar na SAFX de Retorno Nº 346 o valor do campo STATUS, aplicando os seguintes filtros: Empresa, Estabelecimento, UF, Período, Grupo de Imposto, NUM_DOC_ORIGEM, COD_ARRECADACAO, COD_RECEITA Observação: Para este campo, será considerado apenas o preenchimento do STATUS referente às guias pagas. Tooltip: Será exibido na tela um tooltip com a seguinte mensagem para auxiliar o usuário: "A diferença será recalculada apenas se o status da guia gerada estiver como 'Guia Pagar'." |  |


---

|  | Campo | Tipo | Obrig | Ed | Formato/Default | Regra |
| --- | --- | --- | --- | --- | --- | --- |
| RN11 | Valor da Apuração Atual(Reapurada) | Campo | Sim | Sim | Numérico | Consulta de Apurações: O sistema deve consultar o valor atual da apuração para o período.  Regra de Negócio (RN): |
| RN12 | Valor da Guia (original/Status Guia Pagar) | Campo | Sim | Sim | Numérico | O sistema deve buscar na SAFX de Retorno Nº 346 o valor do campo VALOR_PRINCIPAL_DO_TÍTULO, aplicando os seguintes filtros: Empresa, Estabelecimento, UF, Período, Grupo de Imposto, NUM_DOC_ORIGEM, COD_ARRECADACAO, COD_RECEITA Observação: Para este campo, será considerado apenas o preenchimento do STATUS referente às guias pagas. Tooltip: Será exibido na tela um tooltip com a seguinte mensagem para auxiliar o usuário: O valor principal da diferença será informado. O sistema Tax Payments realizará automaticamente o cálculo de juros e multas. |
| RN13 | Diferença de Valor a Pagar | Campo | Sim | Sim | Numérico | Cálculo da Diferença a Pagar: A diferença deve ser calculada individualmente por tributo, aplicando a seguinte fórmula: Diferença = Valor Reapurado – Valor Pago da Guia (Status “Guia Pagar”)preencher o campo VALOR enviado para Tax Payments |
| RN14 | Data de Vencimento | Campo | Sim | Sim | DATA | Deve ser carregada automaticamente do registro da guia original na SAFX Retorno Nº 346, utilizando o campo DATA_VENCIMENTO. Empresa, Estabelecimento, UF, Período, Grupo de Imposto, NUM_DOC_ORIGEM, COD_ARRECADACAO, COD_RECEITA |
| RN15 | Informação Complementar | Campo | Não | Não | Alfanumérico | Este campo é opcional e serve para o usuário incluir observações ou detalhes adicionais sobre a guia complementar.  O conteúdo informado será incorporado ao JSON no atributo CAMPO_EXTRA, garantindo que informações complementares sejam transmitidas. |


---

| CAMPO | NOME | FORMATO | TAMANHO | OBRIG. | CHAVE |
| --- | --- | --- | --- | --- | --- |
| Grupo de Imposto | GRUPO_IMPOSTO | Texto | 014 | SIM | (*) |
| Código da Empresa | COD_EMPRESA | N | 003 | SIM | (*) |
| Código Do Estabelecimento | COD_ESTABELECIMENTO | N | 006 | SIM | (*) |
| Periodo da Apuração | PERIODO | DD/MM/AAAA | 008 | SIM | (*) |
| Código de Arrecadação | COD_ARRECADACAO | N | 020 | SIM | (*) |
| Código da Receita | COD_RECEITA | N | 020 | SIM | (*) |
| UF | UF | TEXTO | 002 | NÃO |  |
| Documento de Origem | NUM_DOC_ORIGEM | A | 019 | SIM |  |
| Detalhamento da Receita | DET_RECEITA | N | 020 | NÃO |  |
| Data de Vencimento | DATA_VENCIMENTO | DD/MM/AAAA | 008 | NÃO |  |
| Valor | VL_PRINCIPAL | N | 15,2 | SIM |  |
| Campos extras | campos_extras | C | 500 | N |  |


---

| Campo | Regra |
| --- | --- |
| Grupo de Imposto | Recuperar dados da RN01 |
| Código da Empresa | Recuperar dados da RN02 |
| Código Do Estabelecimento | Recuperar dados da RN03 |
| Periodo da Apuração | Recuperar dados da RN04 |
| Código de Arrecadação | Recuperar dados da RN05 |
| Código da Receita | Recuperar dados da RN0 |
| UF | Recuperar dados da RN04 |
| Documento de Origen |  |
| Data de Vencimento | Recuperar dados da RN0 |
| Valor | Recuperar dados da RN0 |


---

| Campo | Regra | OS/CH |
| --- | --- | --- |
| Tratamento de campos sem dados (JSON) | Não enviar campos opcionais quando seu valor for null. Não permitir null em campos obrigatórios. Não enviar propriedades fora do layout |  |
| Controle de geração | Cada arquivo, considerando seus campos-chave, só poderá ser gerado uma única vez para a combinação dos seguintes campos: Empresa, Grupo_Imposto,  Cod_Empresa, Cod_Estabelecimento, Período, num O arquivo poderá ser gerado novamente apenas se: ainda não tiver sido enviado pela tela de status; e seu status não estiver como "Enviado"  Caso o status esteja "Aguardando envio", o usuário deverá acessar a tela de status e cancelar o arquivo antes de gerar uma nova versão. Observações adicionais Após o envio, qualquer nova tentativa de geração exige o cancelamento da versão anterior (quando permitido) e, em seguida, uma nova geração do arquivo. A cada geração de arquivo, devem ser registrados data/hora da geração e o usuário responsável. Obs: Já existe um arquivo gerado para esta combinação de campos (Empresa, Estabelecimento, Grupo de Imposto, Período,). Mensagens: Para gerar um novo arquivo: verifique o status na tela de Status de Arquivos; e se o status estiver como 'Aguardando envio', cancele o arquivo antes de tentar gerar novamente. Arquivos com status 'Enviado' ou 'Contabilizado' não podem ser regenerados." |  |
| Cancelamento | O cancelamento só é permitido quando o arquivo estiver com status "Aguardando envio". Arquivos com status "Enviado" ou "Contabilizado" não podem ser cancelados por esta rotina. |  |
| Usuário | Deve ser exibido e registrado o nome do usuário que realizou a geração do arquivo. Esta informação é obrigatória |  |
| Data da geração | Registrar a data e hora exatas da geração do arquivo exemplo  (ex.: 2025-11-12T10:30) O carimbo de data/hora  para cada versão gerada. |  |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Processos Gerados nos últimos | Campo | Sim | Sim | Númerico |  |  |
| Nº Processo | Lista | Sim | Sim | Númerico | Um número único de processo deve ser gerado automaticamente toda vez que uma operação de geração for realizada. Esse número servirá para controle interno e dará visibilidade ao usuário, permitindo que ele visualize todos os processos gerados ou pesquise por um processo específico. |  |
| Descrição | Lista | Sim | Sim | Alfanúmerico | A descrição deve detalhar informações como a data de apuração, o imposto envolvido e o estabelecimento ao qual o processo está vinculado. Essa descrição ajudará o usuário a identificar rapidamente os dados relacionados a cada processo. |  |
| Situação | Lista | Sim | Sim | Dropdown | Esta regra deve mostrar ao usuário o status atual do arquivo gerado, indicando se a execução está "Iniciada" ou "Encerrada". Essa informação proporciona transparência e permite que o usuário acompanhe o progresso das operações. |  |
| Início Execução | Data/Hora | Sim | Sim | DD/MM/AAAA HH:MM | A tela deve exibir a data e a hora em que a execução do processo foi iniciada. Essa informação é crucial para que o usuário possa monitorar e gerenciar as operações em tempo real, assegurando que esteja ciente do início das atividades. |  |
| Fim Execução | Data/Hora | Sim | Sim | DD/MM/AAAA HH:MM | Deve-se mostrar a data e a hora em que a execução do processo foi concluída. Essa informação é importante para o usuário avaliar a duração da operação e para documentação de quando os processos são finalizados. |  |
| Usuário | Lista | Sim | Sim | Texto | Esta regra deve exibir o nome do usuário  que realizou a geração do arquivo. A apresentação dessa informação é essencial para rastrear a responsabilidade pelas operações executadas |  |

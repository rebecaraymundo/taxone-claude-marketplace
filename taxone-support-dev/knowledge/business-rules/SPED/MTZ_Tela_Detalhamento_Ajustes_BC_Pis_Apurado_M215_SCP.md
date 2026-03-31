# MTZ_Tela_Detalhamento_Ajustes_BC_Pis_Apurado_M215_SCP

> Fonte: MTZ_Tela_Detalhamento_Ajustes_BC_Pis_Apurado_M215_SCP.docx






THOMSON REUTERS

Matriz da tela Detalhamento dos Ajustes da BC da Contribuição para o Pis/Pasep Apurada - M215



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Sugestão de Layout	6

## Regras dos Campos


Localização da tela:
Módulo: SPED >> EFD-Escrituração Fiscal Digital das Contribuições
Menu: Obrigações SCP >> Manutenção >> Apuração PIS/PASEP

Deverá ser criada a tela “Detalhamento dos Ajustes da BC da Contribuição para o Pis/Pasep Apurada - M215” para que seja possível realizar a geração do registro M215 da EFD-Contribuições.

Esta tela será acessada através de nova aba inserida na tela de Apuração PIS/PASEP. Estará em um nível abaixo do nível das abas de Detalhamento por Código de Receita (Visão Débito DCTF) – M205 e Detalhamento da Contribuição – M210. Na estrutura dos registros da EFD-Contribuições este é um registro filho do M210 – Detalhamento da Contribuição para o PIS/Pasep do Período.

Deverá ser criada a tela de lista, permitindo a visualização das informações gravadas e a tela de detalhe, que será acessada na inserção de novas informações ou a partir de uma linha da tela de listagem.

Botões:
- Incluir: Ao clicar nesse botão, deve abrir a tela para inserção dos dados.
- Excluir: Ao clicar nesse botão, deve fazer a exclusão do registro selecionado.
- Pesquisar: Ao clicar nesse botão, deve abrir a tela padrão do Mastersaf mostrando os campos chave para seleção.
- Relatório: Ao clicar nesse botão, deve apresentar a seguinte mensagem: “Atenção: Você deseja emitir o relatório de todos os registros?”; incluir a opção de botões “Yes”, “No” e “Cancel” padronizados dos relatórios em comum na apuração e para apresentar o relatório deverão ser demonstrados os campos de dados do estabelecimento, data de geração, página, título e período da apuração. Após, abaixo, demonstrar o Registro e os campos dos dados informados em tela.

Tratamento:
- Não será possível repetir o mesmo valor para os campos: “Tipo de Ajuste”, “Código do Ajuste” e “Número do processo , documento ou ato concessório”; e se houver, emitir a mensagem na tela: “Atenção, já existe registro com a chave informada, favor corrigir manutenção.”;
- Para os campos chave que não forem preenchidos, emitir a mensagem na tela: “Atenção, Dados que compõem a chave do registro não estão preenchidos, favor corrigir: ?”.


* Descrição não disponível em tela


## Sugestão de Layout






| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS-20225 | Julyana Perrucini | Criação da tela de Detalhamento dos Ajustes da Base de Cálculo da Contribuição para o Pis/Pasep Apurada - M215. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Tipo de Ajuste | Texto | S | S | Formato: ComboBox  Default: Não Informado | Nesse campo o usuário deverá informar o indicador do tipo de ajuste da base de cálculo.  Conteúdo: 0 - Ajuste de redução; 1 - Ajuste de acréscimo. | MFS-20225 |
| Valor do Ajuste | Numérico | S | S | Formato: 0,00  Default: Não Informado | Nesse campo o usuário deverá informar o valor do ajuste de base de cálculo. | MFS-20225 |
| Código do Ajuste | Texto | S | S | Formato: ComboBox  Default: Não Informado | Nesse campo o usuário deverá selecionar um Código do ajuste, conforme a Tabela disponibilizada pela Receita Federal de item 4.3.18.  Conteúdo: 01-Vendas canceladas de receitas tributadas em períodos anteriores; 02-Devoluções de vendas tributadas em períodos anteriores; 21-ICMS a recolher sobre Operações próprias; 41-Outros valores a excluir, vinculados a decisão judicial; 42-Outros valores a excluir, não vinculados a decisão judicial. | MFS-20225 |
| Número do processo, documento ou ato concessório | Texto | N | S | Formato: Text input  Default: Não Informado | Nesse campo o usuário deverá informar o número do processo, documento ou ato concessório ao qual o ajuste está vinculado, se houver.  Tratamento: Aceitar inclusive nulo. | MFS-20225 |
| Descrição Resumida | Texto | N | S | Formato: Text input  Default: Não Informado | Nesse campo o usuário deverá informar a descrição resumida do ajuste na base de cálculo. | MFS-20225 |
| Data Referência | Data | N | S | Formato: DD/MM/AAAA  Default: Não Informado | Nesse campo o usuário deverá informar a data de referência do ajuste. | MFS-20225 |
| Conta Analítica | Texto | N | S | Formato: Pasta de Seleção (SAFX2002)  Default: Não Informado | Nesse campo o usuário deverá informar o código da conta analítica contábil debitada/creditada. É importante que a tabela definitiva da SAFX2002 – Plano de Contas  esteja devidamente cadastrada.  Campo padrão do Mastersaf com pasta de seleção, campo de grupo, campo de código, campo de data de validade e descrição. | MFS-20225 |
| CNPJ | Texto | S | S | Formato: 99.999.999/9999-99  Default: Não Informado | Nesse campo o usuário deverá informar o CNPJ do estabelecimento da empresa, a que se refere o ajuste informado no campo “Código do Ajuste”. Caso o ajuste não se refira a um estabelecimento específico, poderá ser informado pela empresa o CNPJ do estabelecimento matriz.  Tratamento: Se o campo não for preenchido, emitir a seguinte mensagem na tela: “O campo CNPJ deve ser informado.”. | MFS-20225 |
| Informação Complementar | Texto | N | S | Formato: Text Input  Default: Não Informado | Nesse campo o usuário poderá utilizar para acrescentar informações complementares do registro. | MFS-20225 |

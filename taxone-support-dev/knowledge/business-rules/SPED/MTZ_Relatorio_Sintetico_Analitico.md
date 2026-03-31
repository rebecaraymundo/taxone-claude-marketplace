# MTZ_Relatorio_Sintetico_Analitico

> Fonte: MTZ_Relatorio_Sintetico_Analitico.docx


THOMSON REUTERS

Módulo SPED

Relatórios Sintético e Analítico



Localização: MastersafDW >> SPED >> ECD – Escrituração Contábil Digital >> Relatórios >> Relatório Sintético/Analítico






DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	3
2.	Definição da tela	3
2.1 – Processos:	9
2.2 – Layout dos relatórios:	9
2.2.1 – Visão Sintética:	10
2.2.1.1 – Layout Relatório Sintético: Periodicidade Mensal	11
2.2.1.2 – Layout Relatório Sintético: Periodicidade Anual	12
2.2.1.3 – Layout Relatório Sintético: Periodicidade Diária	14
2.2.2 – Visão Analítica:	16
2.2.2.1 – Layout Relatório Analítico:	18
2.3 Salvar Relatórios	20



## Regras Gerais


Este relatório tem por objetivo exibir as informações de valores dos saldos de acordo com as parametrizações criadas em “Plano de contas Referencial x Plano de contas da Empresa”. Será permitido a geração de relatórios na visão sintético e analítico.



## Definição da tela




Ao selecionar a tela pelo Menu Relatórios, exibir a mensagem:








### 2.1 – Processos:


Por conta de performance, os relatórios não serão mantidos nos processos. Foi criada uma tabela temporária para guardar as informações dos relatórios, até que a tela do relatório emitida após o processamento, seja fechada.


### 2.2 – Layout dos relatórios:



#### 2.2.1 – Visão Sintética:


Visão Sintética será apresentada em tela, conforme regras:

De acordo com a parametrização criada na tela ‘Plano Referencial X Plano Empresa', será exibido relatório considerando o plano referencial escolhido pelo estabelecimento que está sendo gerado (indicação em Dados Iniciais do Menu Paramentos do módulo Sped ECD – Escrituração Fiscal Digital). Devem ser demonstradas todas as contas referenciais da TFIX64 (respeitando a ordenação e o plano escolhido para o estabelecimento. Devem ser exibidas inclusive as contas referenciais que não tenham associação com as contas da empresa).
Para a geração do relatório sintético (com Periodicidade Mensal e Anual), deverá ser recuperado os saldos (finais) da SAFX02 de todos os estabelecimentos que foram marcados na geração do relatório. Ao processar a geração de um estabelecimento CENTRALIZADOR, no caso de haver mais de uma SAFX02 (por estabelecimento) os saldos deverão ser sumarizados para a obtenção dos valores demonstrados. Caso na tela de Dados Iniciais for indicado que o estabelecimento utilize saldos por centro de custo (SAFX80), estes registros, também deverão ser considerados no relatório (sumarizando as informações por conta referencial e centralizador, se for o caso).
Para a geração do relatório sintético (com Periodicidade Diária), deverá ser recuperado os valores dos lançamentos da SAFX01 de todos os estabelecimentos que foram marcados na geração do relatório. Ao processar a geração de um estabelecimento CENTRALIZADOR, no caso de haver mais de uma SAFX01 (por estabelecimento, conta e dia) os lançamentos deverão ser sumarizados para a obtenção dos valores demonstrados.


Campos que devem ser apresentados no Relatório :

(*) Não apresentar no relatório.

#### 2.2.1.1 – Layout Relatório Sintético: Periodicidade Mensal




#### 2.2.1.2 – Layout Relatório Sintético: Periodicidade Anual


Atenção: Se a periodicidade for anual, o layout do relatório é o mesmo, porém há uma quebra por ano:




#### 2.2.1.3 – Layout Relatório Sintético: Periodicidade Diária


Apresentar as informações ordenadas por conta referencial e dia.





#### 2.2.2 – Visão Analítica:


Visão Analítica será apresentada em tela, conforme regras:

De acordo com a parametrização criada na tela ‘Plano Referencial X Plano Empresa’, será exibido relatório considerando o plano referencial escolhido pelo estabelecimento que está sendo gerado (indicação em Dados Iniciais do Menu Paramentos do módulo Sped ECD – Escrituração Fiscal Digital). Devem ser demonstradas as contas referenciais da TFIX64 (respeitando a ordenação, o plano escolhido pelo estabelecimento e apenas as contas referenciais que foram associadas a SAFX2101, com as contas da empresa e que foram movimentadas no período da geração do relatório).
Para a geração do relatório analítico (periodicidade mensal ou anual), deverá ser recuperado o saldo final do período solicitado de todos os estabelecimentos que foram marcados em tela. Ao processar a geração de um estabelecimento CENTRALIZADOR, no caso de haver mais que uma SAFX02 (além do CENTRALIZADOR) os saldos deverão ser sumarizados para a obtenção dos valores demonstrados na conta referencial, porém mostrando a quebra por conta contábil. Caso na tela de Dados Iniciais for indicado que o estabelecimento utilize saldos por centro de custo (SAFX80), estes registros também deverão ser considerados no relatório (neste caso, além da quebra por conta contábil, deverá ser considerada a quebra por centro de custo), sumarizando inclusive as informações por conta referencial e centralizador, este último, se for o caso do estabelecimento ser centralizador.
Para a geração do relatório analítico de periodicidade diária, deverá ser recuperado os lançamentos contábeis do período solicitado de todos os estabelecimentos que foram marcados em tela. Ao processar a geração de um estabelecimento CENTRALIZADOR, no caso de haver mais que uma SAFX01 (além do CENTRALIZADOR) os lançamentos deverão ser sumarizados para a obtenção dos valores demonstrados na conta referencial, porém mostrando a quebra por conta contábil e centro de custo (este último quando for o caso).

Campos que devem ser apresentados no Relatório:


(*) Não apresentar no relatório.



#### 2.2.2.1 – Layout Relatório Analítico:











Atenção: Se a periodicidade for anual, o layout do relatório é o mesmo, porém há uma quebra por ano (conforme já detalhado no relatório sintético). Assim, como se a periodicidade for diária, há uma quebra dia (conforme já detalhado no relatório sintético).


### 2.3 Salvar Relatórios


Ao salvar os relatórios (em qualquer extensão) considerar a exibição de todas as colunas (inclusive na mesma ordem) apresentada na tela.


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-41870 | Alessandra Cristina Navatta | Este relatório já está disponível no módulo. Esta demanda tem o objetivo apenas de documentá-lo (engenharia reversa). | 21/08/2020 |
| MFS-41257 | Alessandra Cristina Navatta | Alterações em tela: Opção Default da Versão do Plano Referencial (sempre a última versão); Mudar Label na tela (não precisa repetir o texto Plano de Contas Referencial X Plano de Contas da Empresa; Validar se pelo menos um tipo de demonstrativo foi selecionado;  Na geração do Relatório Não bloquear geração do relatório se inscrição estadual não estiver preenchida;  Layout do Relatório  No demonstrativo analítico apresentar o indicador do saldo da conta referencial. Mudar o layout do relatório analítico (usando agrupadores) Ordenar as informações do layout do relatório diário, por conta referencial e dia.  Salvar Relatórios  Ao salvar os relatórios (em qualquer extensão) considerar a exibição de todas as colunas (inclusive na mesma ordem) apresentada na tela. | 16/09/2020 |
| MFS-81170 | Alessandra Cristina Navatta | Atualização da versão do plano de contas referencial. Inclusão das versões 7.00 e 8.00 | 28/02/2022 |
| MFS-511450 | Elisabete Costa | Atualização da versão do plano de contas referencial. Inclusão das versões 9.00 | 24/02/2023 |
|  |  |  |  |
| MFS-749696 | Rosemeire Santos | Atualização da versão do plano de contas referencial. Inclusão das versões 11.00 | 20/01/2025 |
| MFS-1035615 | Rosemeire Santos | Atualização da versão do plano de contas referencial. Inclusão das versões 12.00 | 05/03/2026 |


| Campo | Regra | Demanda |
| --- | --- | --- |
| Livro | Lista de Valores Válidos  G – Livro Diário (Completa sem Escrituração Auxiliar) R – Livro Diário com Escrituração Resumida (com Escrituração Auxiliar)  Opção Default : G – Livro Diário (Completa sem Escrituração Auxiliar) | MFS-41870 |
| Periodicidade | Lista de Valores Válidos:  Anual  Diária  Mensal  Opção Default: Mensal | MFS-41870 |
| Versão do Plano Referencial | Lista de Valores Válidos:  1.00 2.00 3.00 4.00 5.00 6.00 7.00 8.00 9.00  11.00 12.00  Opção Default: Exibir a versão mais atual | MFS-41870 MFS-41257 MFS-81170 MFS-511450  MFS-749696 MFS-1035615 |
| Tipo do Demonstrativo | Opções Válidas:  Sintético Analítico  Default : Marcado a opção Sintético | MFS-41870 |
| Grid Estabelecimentos | Exibir todos os estabelecimentos da empresa selecionada no menu (Header), que possuem os livros selecionados na tela. | MFS-41870 |
| Selecionar | Permite que o usuário selecione os Estabelecimentos que serão gerados os relatórios  Tratamentos:  Modal 'Selecionar Estabelecimentos‘ Ao ser acionado abrir o Modal 'Selecionar Estabelecimentos‘. Apresentando os campos Cód. Estab e Descrição Botões do Modal 'Selecionar Estabelecimentos': Critério, Cancelar, OK e Salvar...   Botões Critério, Cancelar, OK e Salvar  - Ao selecionar o botão 'Cancelar', nada será feito e o Modal 'Selecionar Estabelecimentos‘ será fechado.  - Ao selecionar o botão 'Critério', os estabelecimentos poderão ser filtrados e no novo modal serão exibidos habilitado os botões Pesquisar e Cancelar.  -Ao confirmar a seleção dos registros, acionando o botão ‘OK’, apresentar os estabelecimentos no componente “Estabelecimentos” da tela Principal - Permite a seleção de vários registros por vez. - Ao entrar no modal, pelo menos um registro deve ser selecionado, se for selecionado o botão 'Ok', caso contrário, exibir a mensagem “Selecionar pelo menos um registro”. -Ao selecionar o botão ’Salvar’, o sistema salva as informações recuperadas dos estabelecimentos (no diretório local e formato que o usuário informar). | MFS-41870 |
| Marcar Todos | Permite ao usuário selecionar ou desmarcar todos os registros da grid Estabelecimentos. | MFS-41870 |
| Executar | Validar se período final é maior que período inicial, caso contrário exibir a mensagem: “Data final deve ser maior ou igual a data inicial”   Verificar se o campo período inicial está preenchido, caso contrário exibir a mensagem: “Informe o Período Inicial.”  Verificar se o campo período final está preenchido, caso contrário exibir a mensagem: “Informe Final.”  Se nenhum estabelecimento estiver selecionado, exibir a mensagem: “Selecione pelo menos um estabelecimento.”   A informação de inscrição estadual, não deve ser impeditivo para gerar o relatório (independentemente do tipo de demonstração).   Verificar se pelo menos um tipo de demonstrativo está selecionado, caso contrário exibir a mensagem: “Informe pelo menos um tipo de demonstrativo.” | MFS-41870 MFS-41257 |


| Campo | Tipo | Formato / Default | Regra | Regra |
| --- | --- | --- | --- | --- |
| Cabeçalho | Cabeçalho | Cabeçalho | Cabeçalho | Cabeçalho |
| Empresa | Texto | Cód. – Razão Social | Cód. – Razão Social | Exibir o código e a razão social da empresa. |
| Período | Texto | DD/MM/AAAA a DD/MM/AAAA | DD/MM/AAAA a DD/MM/AAAA | Exibir o período inicial e final que está sendo processado |
| Data | Data | DD/MM/AAAA | DD/MM/AAAA | Exibir a data da geração do relatório |
| Página | Texto | 999999 | 999999 | Exibir o número da página do relatório |
| Filial | Texto | Cód. – Razão Social | Cód. – Razão Social | Exibir o código e a razão social do estabelecimento. |
| Insc. Estadual | Texto |  |  | Exibir a inscrição estadual do estabelecimento. |
| CNPJ | Texto | 00.000.000/0000-00 | 00.000.000/0000-00 | Exibir o CNPJ do estabelecimento. |
| Título (*) | Texto |  |  | Demonstrativo Sintético do Plano Referencial X Plano da Empresa |
| Periodicidade (*) | Texto | Mensal: MM/AAAA Ou Data: DD/MM/AAAA | Mensal: MM/AAAA Ou Data: DD/MM/AAAA | A periodicidade deve ser indicada, de acordo com o parâmetro em tela.  Se escolhido mensal ou anual na tela, apresentar: “Mensal: MM/AAAA” Se escolhido diária, apresentar “Data: DD/MM/AAAA” |
| Conteúdo do Relatório – Movimento(*) | Conteúdo do Relatório – Movimento(*) | Conteúdo do Relatório – Movimento(*) | Conteúdo do Relatório – Movimento(*) | Conteúdo do Relatório – Movimento(*) |
| Conta Referencial | Texto | Código | Código | Exibir o código da conta referencial. |
| Descrição | Texto | Descrição | Descrição | Exibir a descrição da conta referencial |
| Valor | Texto | 0,00 | 0,00 | Exibir o valor do saldo da conta referencial se a periodicidade for anual ou mensal. Se a periodicidade for diária, considerar os lançamentos contábeis, ordenados por conta referencial e data. |
| Indicador D/C | Texto | C/D | C/D | Exibir o indicador do saldo. Opções válidas: C,D |


| Campo | Tipo | Formato / Default | Regra | Regra |
| --- | --- | --- | --- | --- |
| Cabeçalho | Cabeçalho | Cabeçalho | Cabeçalho | Cabeçalho |
| Empresa | Texto | Cód. – Razão Social | Cód. – Razão Social | Exibir o código e a razão social da empresa. |
| Período | Texto | DD/MM/AAAA a DD/MM/AAAA | DD/MM/AAAA a DD/MM/AAAA | Exibir o período inicial e final que está sendo processado |
| Data | Data | DD/MM/AAAA | DD/MM/AAAA | Exibir a data da geração do relatório |
| Página | Texto | 999999 | 999999 | Exibir o número da página do relatório |
| Filial | Texto | Cód. – Razão Social | Cód. – Razão Social | Exibir o código e a razão social do estabelecimento. |
| Insc. Estadual | Texto |  |  | Exibir a inscrição estadual do estabelecimento. |
| CNPJ | Texto | 00.000.000/0000-00 | 00.000.000/0000-00 | Exibir o CNPJ do estabelecimento. |
| Título (*) | Texto |  |  | Demonstrativo Analítico do Plano Referencial X Plano da Empresa |
| Periodicidade (*) | Texto | Mensal: MM/AAAA Ou Data: DD/MM/AAAA | Mensal: MM/AAAA Ou Data: DD/MM/AAAA | A periodicidade deve ser indicada, de acordo com o parâmetro em tela.  Se escolhido mensal ou anual na tela, apresentar: “Mensal: MM/AAAA” Se escolhido diária, apresentar “Data: DD/MM/AAAA” |
| Conteúdo do Relatório – Movimento(*) | Conteúdo do Relatório – Movimento(*) | Conteúdo do Relatório – Movimento(*) | Conteúdo do Relatório – Movimento(*) | Conteúdo do Relatório – Movimento(*) |
| Conta Referencial | Texto | Código – Descrição | Código – Descrição | Exibir o código e descrição da conta referencial. |
| Valor Total | Texto | 0,00 | 0,00 | Exibir o valor do saldo da conta referencial (para a periodicidade anual e ou mensal). Para a periodicidade diária, exibir o valor dos lançamentos contábeis, das contas que estão associados à conta referencial |
| Indicador D/C | Texto | C/D | C/D | Exibir o indicador do saldo da conta referencial. Opções válidas: C,D |
| Conta Empresa | Texto | Código – Descrição | Código – Descrição | Exibir todas as contas da empresa, que estão vinculadas à conta referencial |
| Centro de Custo | Texto | Código – Descrição | Código – Descrição | Exibir todos os centros de custos que estão vinculados à contas da empresa e que estão vinculadas à conta referencial |
| Indicador D/C | Texto | C/D | C/D | Exibir o indicador do saldo. Opções válidas: C,D |

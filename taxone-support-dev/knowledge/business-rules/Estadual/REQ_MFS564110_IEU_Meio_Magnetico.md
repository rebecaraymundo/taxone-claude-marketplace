# REQ_MFS564110_IEU_Meio_Magnético

> Fonte: REQ_MFS564110_IEU_Meio_Magnético.docx






THOMSON REUTERS


MFS564110

Scanc

Scanc – Refinaria – Geração Meio Magnético








Revisões





















Sumário

1.	INTRODUÇÃO	3
1.1	Documentos e Base Legal para a Solução	3
2.	SOLUÇÃO FUNCIONAL / ESCOPO	3
2.1	Procedimentos para Fábrica	3
2.1.1	Inclusão da opção de Filtro por Inscrição Estadual Única:	3
2.1.2	Inclusão da opção de Filtro por UF:	3
2.2	Procedimentos para Interface	4
3.	PROCEDIMENTOS PARA CONTEÚDO	4
3.1	Criação / Alteração – Tabelas (Manual de Layout)	4
3.1.1	Manual de Layout	4
3.2	Criação / Alteração em telas e relatórios (manual operacional, roteiro e help)	4
3.2.1	Geração dos Arquivos Magnéticos - Scanc	4
Anexos VI, VI-M, VII e VII-M	5
3.3	Criação / Alteração de Tabelas (Fixas, Acessórias, Básicas)	6
3.4	Criação / Alteração de Roteiro Operacional	6
3.5	Outras informações que necessitarão ser atualizadas (help, manual operacional etc)	6
3.6	Informações p/ Carta do Patch	6
4.	TESTES	7



## INTRODUÇÃO

Ajuste no Filtro de Parametrização da Rotina de Geração dos Arquivos Magnéticos dos Movimentos de Refinaria do modulo de Combustíveis e Derivados de Petróleo:
- Inclusão da opção de filtro por Estabelecimento com Inscrição Estadual Única
- Inclusão de Filtro por UF
### Documentos e Base Legal para a Solução


## SOLUÇÃO FUNCIONAL / ESCOPO


### Procedimentos para Fábrica


#### Inclusão da opção de Filtro por Inscrição Estadual Única:


Localização no DW: Menu Específicos  Combustíveis e Derivados de Petróleo,
Menu -> Movimento Refinaria -> Geração dos Arquivos Magnéticos – Scanc -> Anexos VI e VII

Inclusão de um Check-Box com filtro de nome “Inscrição Estadual Única” que ao ser marcado filtre os estabelecimentos de centralizados por inscrição estadual única e também os descentralizados.

Exemplo de Tela:



#### Inclusão da opção de Filtro por UF:


Localização no DW: Menu Específicos  Combustíveis e Derivados de Petróleo,
Menu -> Movimento Refinaria -> Geração dos Arquivos Magnéticos – Scanc -> Anexos VI e VII

Inclusão de uma Lista com filtro de nome “Pesquisa UF (Estabelecimento)” contendo todas as UF´s constantes na tabela “Estado” mais a opção “Todos”.

Na seleção do estado correspondente deve-se verificar na tabela “Estabelecimento” a UF correspondente e apresentar na lista de seleção todos os Estabelecimentos do estado selecionado.

Exemplo de Tela:



### Procedimentos para Interface

Não há
## PROCEDIMENTOS PARA CONTEÚDO


### Criação / Alteração – Tabelas (Manual de Layout)




#### Manual de Layout


Não há
### Criação / Alteração em telas e relatórios (manual operacional, roteiro e help)


Alteração no Manual Operacional do módulo Combustíveis e Derivados de Petróleo.


#### Geração dos Arquivos Magnéticos - Scanc


Localização no DW: Menu Específicos  Combustíveis e Derivados de Petróleo,
Menu -> Movimento Refinaria -> Geração dos Arquivos Magnéticos – Scanc -> Anexos VI e VII

Incluir o texto marcado em Verde:

Esta rotina possibilita a geração dos arquivos referentes aos Anexos VI, VI-M, VII e VII-M, e Notas Fiscais.
#### Anexos VI, VI-M, VII e VII-M

Nesta rotina o usuário pode fazer a geração do arquivo magnético no layout definido pelo aplicativo SCANC - Refinarias. O arquivo conterá os dados dos Anexos VI, VI-M, VII e VII-M de um determinado período (mês/ano), e de um ou vários estabelecimentos.
Obs.: Os anexos VI, VI-M, VII e VII-M gerados deverão ser importados pelo aplicativo SCANC - Refinarias, acompanhado do relatório de conferência, que demonstra os dados gravados no arquivo.
Inicialmente esta tela de geração só apresenta as opções de Parâmetros e Processos, após a execução, são disponibilizadas as demais opções: Log, Arquivos e Conferência do Meio Magnético.
Para a correta geração, o usuário deve preencher nas respectivas abas, as seguintes informações:
- Parâmetros:
Tipo de Execução: Informar o tipo de execução, podendo ser: Imediata ou Programada.
Data/Hora de Execução: Informar a data e hora que deseja fazer a execução da geração do arquivo.
Obs.: Este campo está disponível, caso o usuário tenha selecionado a opção "Programada" no campo Tipo de Execução.
Mês/Ano Referência: Informar o período (mês/ano) para geração.
Local: Informar o município de execução do arquivo.

Pesquisa UF (Estabelecimento): lista contendo todas as UF’s mais a opção “Todos”.
Inscrição Estadual Única: caso essa opção seja selecionada, serão apresentados apenas os estabelecimentos Centralizadores e Descentralizados.

Estabelecimentos: Lista todos os estabelecimentos cadastrados, para que o usuário selecione quais estabelecimentos que deseja fazer a geração. Tendo a opção de selecionar todos e desmarcar todos automaticamente.
### Criação / Alteração de Tabelas (Fixas, Acessórias, Básicas)


### Criação / Alteração de Roteiro Operacional


### Outras informações que necessitarão ser atualizadas (help, manual operacional etc)



### Informações p/ Carta do Patch


Carta do Patch – DW e TAXONE:

Módulo: Combustíveis e Derivados de Petróleo

Resumo da alteração: Inclusão de novas opções de filtros na tela de parametrização da Rotina de Geração dos Arquivos Magnéticos do Scanc Refinaria Anexos VI e VII.

Foram disponibilizadas opções adicionais de Filtro na tela de Parametrização da Rotina de Geração dos Arquivos Magnéticos do Scanc Anexos VI e VII dos Movimentos de Refinaria do módulo de Combustíveis e Derivados de Petróleo:
- Inclusão da opção de filtro por Estabelecimento com Inscrição Estadual Única
- Inclusão de Filtro por UF

Funcionalidades atualizadas:

Módulo Impactado: Combustíveis e Derivados de Petróleo

Menu -> Movimento Refinaria -> Geração dos Arquivos Magnéticos – Scanc -> Anexos VI e VII

## TESTES

= = = = =


| Data | OS/Chamado | Descrição | Autor |
| --- | --- | --- | --- |
| 11/09/2023 | MFS 564110 | Inclusão da opção IEU e Filtro de UF na parametrização da Rotina de Geração do Meio Magnético – Refinaria - Scanc | Graciela Soares |

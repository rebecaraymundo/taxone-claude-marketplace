# Tela_Perfil_de_Geracao

> Fonte: Tela_Perfil_de_Geracao.docx






THOMSON REUTERS

Tela Perfil de Geração

DOCUMENTO DE REQUISITO




Sumário

1.	INTRODUÇÂO	3
2.	DOCUMENTOS DE REFERÊNCIAS	3
3.	TELA/MODAIS	3
3.1	Pesquisa de Registros	3
3.2 Regras dos Campos Tela Principal	3

## INTRODUÇÂO


Objetivo desta especificação é permitir o cadastro/visualizaçãodo perfil de geração.

## DOCUMENTOS DE REFERÊNCIAS


- Regras_Gerais_DWECF.docx

- Layout_ECF.xlsx

## TELA/MODAIS


### Pesquisa de Registros


Localização da tela: ECF - Escrituração Contábil Fiscal >> Parâmetros

Título da tela:   Perfil de Geração


Obs. As opções dos campos de pesquisa e suas opções, podem ter alguma divergência na escrita e tipo, pois serão apresentados como cadastradas no banco.


### 3.2 Regras dos Campos Tela Principal

Localização da tela: ECF - Escrituração Contábil Fiscal >> Parâmetros
Título da tela:   Perfil de Geração



| Data | MFS | Descrição | Autor |
| --- | --- | --- | --- |
| 18/06/2018 | MFS-12684 | Criação da documentação | Alessandra Cristina Navatta |


| Campo | Tipo | Regra |
| --- | --- | --- |
| VERSÃO | Lista  (Descrição) | Permite o usuário buscar o registro pela versão do perfil. |
| CÓDIGO | Texto | Permite o usuário buscar o registro pelo código do perfil. |
| Descrição | Texto | Permite o usuário buscar o registro pela descrição do perfil. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- |
| Cabeçalho (*) | Cabeçalho (*) | Cabeçalho (*) | Cabeçalho (*) | Cabeçalho (*) | Cabeçalho (*) | Cabeçalho (*) |
| Leiaute | Lista | S | S | Descrição | Permite ao usuário informar um leiaute Válido.  Lista de Valores:  Aplicar RNG00004 - Versão de Layout | MFS-12684 |
| Perfil | Texto | S | S | Código - Descrição | Permite ao usuário indicar um código e descrição do perfil. | MFS-12684 |
| Descrição dos Blocos | Descrição dos Blocos | Descrição dos Blocos | Descrição dos Blocos | Descrição dos Blocos | Descrição dos Blocos | Descrição dos Blocos |
| Blocos(*) | Texto | S | N | Código Descrição | Apresentar a lista de blocos compatível com a versão selecionada.  Tratamentos  Considerar as informações do arquivo Layout_ECF.xlsx Os blocos não gerados pelo Sistema, devem ficar desabilitados. Exibir somente após informado o campo: leiaute, quando não informado, a grid deverá ficar em branco. | MFS-12684 |
| Definição dos Registros | Definição dos Registros | Definição dos Registros | Definição dos Registros | Definição dos Registros | Definição dos Registros | Definição dos Registros |
| Checkbox |  |  |  |  | Tratamentos: Exibir em todas as linhas da grid que houver registros. | MFS-12684 |
| Registros(*) |  |  |  | Registro Nível Descrição | Ao selecionar um bloco (grid Descrição dos Blocos), o sistema deverá trazer “todos” os registros referente a este bloco selecionado, na criação de um novo perfil de geração. Neste caso, poderá ser desmarcado pelo usuário, os registros que não são obrigatórios (conforme campo obrigatoriedade de saída).  Os registros obrigatórios (Campo Obrigatoriedade Saída = O) devem ser apresentados sempre marcados e desabilitados.  Ao desmarcar um registro PAI, deve-se automaticamente desmarcar todos os FILHOS. Ao marcar um registro FILHO cujo PAI esteja desmarcado, deve-se marcar automaticamente o PAI, anteriores a ele;  A relação de dependência entre os registros deve ser observada através da informação do nível hierárquico do documento “Layout_ECF.xlsx”.  Apenas os registros com Campo Obrigatoriedade Saída = O) devem ser apresentados marcados, os demais desmarcados. Os registros dos Blocos C e E e o registro M500 devem ser apresentados sempre desabilitados e desmarcado na tela (pois não são gerados pelo produto). | MFS-12684 |

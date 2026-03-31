# MTZ-Tela_Parametros_Cadastro das Séries_Modelos das Obrigações_Cadastro_Serie

> Fonte: MTZ-Tela_Parametros_Cadastro das Séries_Modelos das Obrigações_Cadastro_Serie.docx






THOMSON REUTERS
TAXONE
Parâmetros para Município

Cadastro de Série

Localização: TAXONE, Menu Municipal, módulo Parâmetros para Município à Parâmetros à Série Cadastro das Séries/Modelos das Obrigações à Cadastro de Série


DOCUMENTO DE REQUISITO


Sumário

1.	Objetivo	3
2.	Layout da Tela	3
3.	Regras dos Campos	5























## Objetivo


Criar a tela de parametrização de cadastro de séries, no produto TAXONE, para dar a possibilidade de ser feita a manutenção/inclusão das informações oriundas da TFIX83 – Cadastros de Séries/Modelos das Obrigações, PRT_SERIE_OBRIG.

## Layout da Tela







Botões da barra de menu:



## Regras dos Campos


Localização: Menu Municipal, módulo Parâmetros para Município à Parâmetros àSérie Cadastro das Séries/Modelos das Obrigações à Cadastro de Série
Título: Cadastro de Série (Município – UF)

Ao abrir a tela, será exibida a tela de Seleção de Municípios, onde o usuário, deverá indicar a UF e o município que será consultado/manutenido.
As informações serão recuperadas da tabela ESTADO, desde que exista na tabela PRT_VALIDADOR_MUNIC (TFIX105), campo cod_modulo.



| MFS | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-758271 | Alessandra Cristina Navatta | Criação da tela de Parâmetro Cadastro de Série (TFIX83), para o produto TAXONE. | 17/03/2025 |
| MFS-844235 | Rosemeire Santos | Ajuste na nomenclatura do menu | 07/07/2025 |


| Município | Exibe a tela de Seleção de Município. |
| --- | --- |
| Novo | Ao clicar nesta opção será inserida uma nova linha para cadastrar uma nova série |
| Exclui | Opção para excluir a série. |
| Confirma | Opção para salvar os dados |
| Relatório | Esta opção permite exibir o relatório com os dados das séries. |
| Fecha | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/ Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Código Série | Texto | S | S |  | Informar o código da série. |
| Descrição Série | Texto | S | S |  | Informar a descrição da série. |
| Confirma | Botão | - | - | - | Validações:  Ao confirmar, se Código Série se não tiver preenchido, exibir a mensagem: Código Série deve ser informado!  Ao confirmar, se já existir na base o mesmo Código Série, exibir a mensagem:  Série já cadastrada: <<Série>> |

# MTZ-Tela_Parametros_Tipos de Documento das Obrigações _Cadastro_Tipo_Documento

> Fonte: MTZ-Tela_Parametros_Tipos de Documento das Obrigações _Cadastro_Tipo_Documento.docx






THOMSON REUTERS
TAXONE
Parâmetros para Município

Cadastro de Modelo Tipo de Documento

Localização: TAXONE, Menu Municipal, módulo Parâmetros para Município à Parâmetros à Modelo Cadastro dos Tipos de Documento das Obrigações àCadastro de Modelo Cadastro Tipo de Documento



DOCUMENTO DE REQUISITO


Sumário

1.	Objetivo	3
2.	Layout da Tela	3
3.	Regras dos Campos	4























## Objetivo


Criar a tela de parametrização de cadastro de modelo Cadastro Tipo de Documento, no produto TAXONE, para dar a possibilidade de ser feita a manutenção/inclusão das informações oriundas das TFIX84 – Cadastros dos Tipos dos Documentos das Obrigações, PRT_TP_DOCTO_OBRIG

## Layout da Tela






Botões da barra de menu:



## Regras dos Campos


Localização: Menu Municipal, módulo Parâmetros para Município à Parâmetros à Modelo Cadastro dos Tipos de Documento das Obrigações à Cadastro de Modelo  Cadastro Tipo de Documento
Título: Cadastro de Modelo (Descrição do Município - UF)

Ao abrir a tela, será exibida a tela de Seleção de Municípios, onde o usuário, deverá indicar a UF e o município que será consultado/manutenido.
As informações serão recuperadas da tabela ESTADO, desde que exista na tabela PRT_VALIDADOR_MUNIC (TFIX105), campo cod_modulo.




| MFS | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS-758271 | Alessandra Cristina Navatta | Criação da tela de Parâmetro Cadastro de Modelo (TFIX84), para o produto TAXONE. | 17/03/2025 |
| MFS-844235 | Rosemeire Santos | Ajuste na nomenclatura do menu e submenu | 07/07/2025 |


| Município | Exibe a tela de Seleção de Município. |
| --- | --- |
| Novo | Ao clicar nesta opção será inserida uma nova linha para cadastrar um novo modelo documento. |
| Exclui | Opção para excluir o modelo documento. |
| Confirma | Opção para salvar os dados |
| Relatório | Esta opção permite exibir o relatório com os dados dos modelos documentos. |
| Fecha | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/ Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Tipo Documento | Texto | S | S |  | Informar o tipo de modelo de documento. |
| Descrição Documento | Texto | N | S |  | Informar a descrição do documento. |
| Confirma | Botão | - | - | - | Validações:  Ao confirmar, se já existir na base o mesmo tipo de documento, exibir a mensagem: Tipo de documento já cadastrado: <<tipo de documento>>  Ao confirmar, se Tipo documento não tiver preenchido, exibir a mensagem: Tipo documento deve ser informado! |

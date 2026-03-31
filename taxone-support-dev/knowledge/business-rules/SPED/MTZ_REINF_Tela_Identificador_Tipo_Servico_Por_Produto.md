# MTZ_REINF_Tela_Identificador_Tipo_Servico_Por_Produto

> Fonte: MTZ_REINF_Tela_Identificador_Tipo_Servico_Por_Produto.docx






THOMSON REUTERS

Módulo EFD Reinf
Tela de Identificação do Tipo de Serviço > Por Produto

Localização: Menu SPED / EFD Reinf / Retenções Previdenciárias >> Parametros >> Identificação do Tipo de Serviço >> Por Produto


DOCUMENTO DE REQUISITO

Sumário

TELA A SER DESENVOLVIDA	3
1.	REGRAS DOS CAMPOS	3

## TELA A SER DESENVOLVIDA


## REGRAS DOS CAMPOS


Localização: Menu SPED / EFD Reinf / Retenções Previdenciárias >> Parametros >> Identificação do Tipo de Serviço >> Por Produto

- Título da tela: Parametrização de Identificação do Tipo de Serviço – Por Produto








| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS14463 | Lara Aline | Definição das regras de criação da parametrização por produto. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Grupo Produto | ComboBox | S | S | Default: Em Branco | Neste campo é apresentado o código do grupo selecionado através da tela padrão de seleção de Estabelecimento/Grupo/Validade. | MFS14463 |
| Estabelecimento | ComboBox | S | S | Default: Em Branco | Nesse campo, o usuário poderá selecionar o estabelecimento. O Estabelecimento será exibido exibindo o Código do Estabelecimento e a Descrição do mesmo. Exemplo: 001 – Estabelecimento 001, onde “001” é o Código do Estabelecimento e “Estabelecimento 001” é a Descrição do mesmo.   Por default esse campo irá exibir o estabelecimento informado no Manager, caso no Manager não exista nenhum estabelecimento informado, esse campo será exibido vazio.   Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento dever ser Selecionado”. | MFS14463 |
| Tipo de Serviço | ComboBox | S | S | Default: Em Branco | - Local onde deve exibir uma lista com código e descrição dos tipos serviços, que constam na tabela TACES85.  - Quando um Tipo de Serviço (TACES85)  já estiver associado com  um “Código de Produto”, não pode ser exibido para associação com outro “código de produto”;  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Tipo de Serviço deve ser Escolhido”. | MFS14463 |
| Informar Código/Descrição para Pesquisa | ComboBox | N | S | Default: não selecionado | Este campo é destinado para pesquisa de Código do Produto via código ou descrição.  Campos Código e Descrição são Checkbox. | MFS14463 |
| Códigos de Produtos | CheckBox | S | S | Default: não selecionado | Este campo exibe a relação de códigos de produto do estabelecimento, registrados na SAFX2013 para associação;  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS14463 |
| Replicar para os Estabelecimentos | CheckBox | S | S | Default: não selecionado | Este campo permiti replicar a parametrização para outros estabelecimentos. | MFS14463 |

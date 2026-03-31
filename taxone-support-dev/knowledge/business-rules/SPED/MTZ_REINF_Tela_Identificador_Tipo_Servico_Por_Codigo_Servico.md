# MTZ_REINF_Tela_Identificador_Tipo_Servico_Por_Codigo_Servico

> Fonte: MTZ_REINF_Tela_Identificador_Tipo_Servico_Por_Codigo_Servico.docx






THOMSON REUTERS

Módulo EFD Reinf
Tela de Identificação do Tipo de Serviço

Localização: Menu SPED / EFD Reinf / Retenções Previdenciárias >> Parametros >> Identificação do Tipo de Serviço >> Por Código de Serviço


DOCUMENTO DE REQUISITO


Sumário

1.	REGRAS DE GERAÇÃO DO RELATÓRIO	3
1.1.	Layout do Relatório	6

## TELA A SER DESENVOLVIDA


## REGRAS DOS CAMPOS


Localização: Menu SPED / EFD Reinf / Retenções Previdenciárias >> Parametros >> Identificação do Tipo de Serviço >> Por Código de Serviço

- Título da tela: Parametrização de Identificação do Tipo de Serviço



### LAYOUT DA TELA:









| OS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS7084 | Jefferson Mota | Definição das regras de criação dos Relatórios Previdenciários para o EFD Reinf. |
| MFS8958 | Elenilson Coutinho | Inclusão do Campo “Indicador de Aposentadoria Especial” na tela de “Indicador de Tipo de Serviço”. |
| MFS13857 | Lara Aline | Inclusão campo Informar Código/Descrição para Pesquisa |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | ComboBox | S | S | Default: Em Branco | Nesse campo, o usuário poderá selecionar o estabelecimento. O Estabelecimento será exibido exibindo o Código do Estabelecimento e a Descrição do mesmo. Exemplo: 001 – Estabelecimento 001, onde “001” é o Código do Estabelecimento e “Estabelecimento 001” é a Descrição do mesmo.   Por default esse campo irá exibir o estabelecimento informado no Manager, caso no Manager não exista nenhum estabelecimento informado, esse campo será exibido vazio.   Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento dever ser Selecionado”. | MFS7084 |
| Tipo de Serviço | ComboBox | S | S | Default: Em Branco | - Local onde deve exibir uma lista com código e descrição dos tipos serviços, que constam na tabela TACES85.  - Quando um Tipo de Serviço (TACES85)  já estiver associado com  um “Código de Serviço”, não pode ser exibido para associação com outro “código de serviço”;  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Tipo de Serviço deve ser Escolhido”. | MFS7084 |
| Informar Código/Descrição para Pesquisa | ComboBox | N | S | Default: não selecionado | Este campo é destinado para pesquisa de Código de Serviço via código ou descrição.  Campos Código e Descrição são Checkbox. | MFS13857 |
| Códigos de Serviços | CheckBox | S | S | Default: não selecionado | Este campo exibe a relação de códigos de serviço do estabelecimento, registrados na SAFX2018 para associação;  Como facilitador, poderão ser utilizadas as opções “Marcar todos” e “Desmarcar todos”. | MFS7084 |
| Ind. Aposentadoria Especial | Dropdown | N | S | Default: “Não se aplica” | Exibir as opções:  - Não se aplica - 15 anos - 20 anos - 25 anos | MFS8958 |
| Replicar para os Estabelecimentos | CheckBox | S | S | Default: não selecionado | Este campo permiti replicar a parametrização para outros estabelecimentos. | MFS7084 |

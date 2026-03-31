---
source: "MTZ_Tela_Relatorio_Venda_SAT.docx"
category: Report_Fiscal
converted: auto
---





THOMSON REUTERS


Report Fiscal
Relatório Analítico Vendas Cupom SAT



DOCUMENTO DE REQUISITO



Sumário

**1.	Regras dos Campos	3**
2.	Leiaute da Tela	5



# Regras dos Campos

**Localização da tela:**

**Módulo: Básicos >> Report Fiscal**
**Menu: Gerenciais >> Documentos Fiscais >> Analíticos >> Vendas Cupom Fiscal SAT**

Título da tela: Relatório de Vendas do SAT

Funcionamento da tela: Esta tela tem como objetivo definir os critérios de seleção, para a geração do Relatório de Vendas de Cupom Fiscal SAT. Será possível definir o período do relatório, o Estabelecimento a ser gerado, e opcionalmente um número de equipamento para filtro (parâmetro incluído na MFS11117). O relatório possui um filtro para o usuário visualizar os documentos cancelados (parâmetro incluído na MFS17603).





# Leiaute da Tela





Para futuras alterações acessar o objeto do mockup abaixo, realizar alterações e salvar;

O print da tela foi incluído para que as outras áreas possam visualizar, visto que não possuem o programa do balsamiq.


---

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS1932 | Jefferson Mota | Definição das regras da tela de Relatório Analítico Vendas Cupom SAT |  |
| MFS11117 | Vânia Mattos | Alteração do relatório das vendas com Cupom Fiscal SAT para inclusão de filtro por Número do Equipamento. | 10/08/2017 |
| MFS17603 | João Henrique | Alteração do relatório das vendas com Cupom Fiscal SAT para inclusão de filtro de documentos cancelados. | 26/11/2018 |


---

| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimentos | ComboBox | S | S | Default: não selecionado | Este campo exibe todos os estabelecimentos da empresa que acessou o módulo do Report Fiscal.   Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser preenchido”. | MFS1932 |
| Período Inicial | Data | S | S | DD/MM/AAAA | Local para digitação do período inicial de referencia da geração do relatório, no formato de DD/MM/AAAA. Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório. | MFS1932 |
| Período Final | Data | S | S | DD/MM/AAAA | Local para digitação do período final de referência da geração do relatório, no formato de DD/MM/AAAA. Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório. Obs: No campo do Período final, o usuário deverá informar um período maior ou igual ao período inicial. Caso informe um período menor do que o período inicial retornar a mensagem:  “O período final informado deve ser maior ou igual ao período inicial”. | MFS1932 |
| Número do Equipamento SAT   (campo incluído na MFS11117) | Numérico | N | S |  | Neste campo o usuário poderá informar um número de equipamento. O campo é de preenchimento não obrigatório. Campo numérico de 9 posições (corresponde ao campo “03-Número do Equipamento” da SAFX201). | MFS11117 |
| Somente Lançamentos Cancelados | Checkbox | N | S | Não possui default | Este campo estará desmarcado por default. Quando selecionado, o sistema exibirá na geração do relatório os documentos SAT cancelados. Campo: 07-Situação do Documento = “02 – Documento Cancelado” da SAFX201.  O campo não é obrigatório.  Ao gerar essa rotina com a opção “Somente Lançamentos Cancelados”, o título do relatório será apresentado como: “Relatório Analítico de Vendas Canceladas do SAT”. | MFS17603 |

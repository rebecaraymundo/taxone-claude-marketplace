---
source: "MTZ-DW-Manutencao_Combustiveis_Grupos de Combustíveis e Derivados.docx"
category: Especificos
converted: auto
---


# Módulo DW – Manutenção – Grupos de Combustíveis e Derivados


Localização: Menu Básicos, Módulo: Data Warehouse
Menu Manutenção >> Combustíveis (Não Varejistas) >> Grupos de Combustíveis e Derivados


Localização: Menu Específicos, Módulo: Combustíveis e Derivados de Petróleo
Menu Parâmetros >> Grupos de Combustíveis e Derivados



DOCUMENTO DE REQUISITO


## REGRAS DE NEGÓCIO












---

| MFS | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| MFS540746 | Liliane Assaf | Disponibilizar manutenção no módulo Data Warehouse | 15/06/2023 |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |


---

| Cód. |  | DR |
| --- | --- | --- |
| RN00 | Regras gerais Tela de manutenção disponível em dois módulos Data Warehouse e Combustíveis e Derivados de Petróleo.  Nesta opção é possível fazer a manutenção dos Grupos de combustíveis e derivados, devendo informar para cada grupo quais os anexos que são emitidos   Tabela: CBT_GRP_COMB |  |
| RN01 | Campo  – Grupo Combustível  Campo obrigatório. Texto de livre digitação. |  |
| RN02 | Campo – Descrição Campo não obrigatório Texto de livre digitação. |  |
| RN03 | Campo – Produto SEF Campo não obrigatório Texto de livre digitação. Este código deve estar de acordo com os códigos de produtos relacionados na tabela 4.3 do manual de orientação do SCANC (Sistema de Captação e Auditoria dos Anexos de Combustíveis). Obs: A informação deste campo é utilizada na geração dos Registros 40, 45, 60, 62 e 70 do SCANC Distribuidoras  Veja como deve ficar a parametrização dos Grupos Combustíveis: |  |
| RN04 | Campo – Anexos: Para cada anexo existe um check-box. Os anexos com final “M” devem ser marcados para os combustíveis sujeitos à tributação monofásica. |  |
| RN05 |  |  |
| RN06 |  |  |
|  |  |  |
|  |  |  |

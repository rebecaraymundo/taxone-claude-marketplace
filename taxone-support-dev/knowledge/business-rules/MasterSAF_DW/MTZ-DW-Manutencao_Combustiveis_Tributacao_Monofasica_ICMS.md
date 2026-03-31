---
source: "MTZ-DW-Manutencao_Combustiveis_Tributação Monofásica ICMS.docx"
category: MasterSAF_DW
converted: auto
---


# Módulo DW – Manutenção – Tabela Produtos Sujeitos à Tributação Monofásica ICMS   (TACES112)


Localização: Menu Básicos, Módulo: Data Warehouse
Menu Manutenção >> Combustíveis (Não Varejistas) >> Produtos Sujeitos à Tributação Monofásica ICMS

Localização: Menu Específicos, Módulo: Combustíveis e Derivados de Petróleo
Menu Parâmetros >> Produtos Sujeitos à Tributação Monofásica ICMS


DOCUMENTO DE REQUISITO


## REGRAS DE NEGÓCIO












---

## Tabelas

| MFS | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| MFS540746 | Liliane Assaf | Criação da tela de manutenção | 15/06/2023 |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

| Cód. |  | DR |
| --- | --- | --- |
| RN00 | Regras gerais Tela de manutenção disponível em dois módulos Data Warehouse e Combustíveis e Derivados de Petróleo.  Nesta opção é possível fazer a manutenção dos Códigos de combustíveis sujeitos à tributação monofásica do ICMS, cuja carga inicial se dá através da TACES112.  Base Legal: Portal da Nota Fiscal Eletrônica (fazenda.gov.br) - Tabela de códigos de combustíveis sujeitos à tributação monofásica de ICMS.  Tabela: CBT_PRD_ICMS_MONO  Os tratamentos relacionados ao regime de tributação monofásica do ICMS aplicados na geração do Sped Fiscal, Livros de Apuração do ICMS e ICMS-ST e SCANC dependem das seguintes definições: - Os tratamentos são aplicados para as notas fiscais cuja data fiscal se enquadre na vigência da monofasia do combustível, ou seja, a data fiscal >= Data de Validade Inicial aqui informada para o combustível. - Produto movimentado na nota fiscal deve ser um Combustível Sujeito à Tributação Monofásica. Para isso, o campo “Código do Produto Oficial” presente na parametrização dos Produtos x Grupos de Combustíveis e Derivados (SAFX96) deve estar preenchido de acordo com os códigos aqui informados.  Módulo: Combustíveis e Derivados de Petróleo, menu Parâmetros >> Produtos x Grupos de Combustíveis e Derivados Módulo: Data Warehouse menu Manutenção >> Combustíveis (Não Varejistas) >> Produtos x Grupos de Combustíveis e Derivados - Parâmetro 94 marcado, presente na tela de manutenção dos Parâmetros p/ UF no módulo ICMS. - SAFX325 – Informações de Tributação do ICMS Monofásico carregada - CST movimentado na nota fiscal igual a 02, 25, 53, 61 | MFS540746 |
| RN01 | Campo  – Código Produto Oficial:  Campo obrigatório. Texto de livre digitação. Campo COD_PROD_OFICIAL da tabela CBT_PRD_ICMS_MONO | MFS540746 |
| RN02 | Campo – Validade Inicial  Campo obrigatório. Texto formatado com DD/MM/AAAA Campo DAT_VALID_INI da tabela CBT_PRD_ICMS_MONO | MFS540746 |
| RN03 | Campo – Descrição Campo não obrigatório Texto de livre digitação. Campo DSC_PROD_OFICIAL da tabela CBT_PRD_ICMS_MONO | MFS540746 |
| RN04 | Campo – Alíquota ad Rem ICMS: Campo não obrigatório. Campo numérico com 4 casas decimais. Campo ALIQ_AD_REM_ICMS da tabela CBT_PRD_ICMS_MONO | MFS540746 |
| RN05 | Campo –Validade Final Campo não obrigatório. Texto formatado com DD/MM/AAAA Campo DAT_VALID_FIM da tabela CBT_PRD_ICMS_MONO | MFS540746 |
| RN06 | Campo - Biocombustível Campo não obrigatório Lista fixa ou check-box. Se marcado sim, gravar ‘S’ no campo IND_BIOCOMB da tabela CBT_PRD_ICMS_MONO. Se não, gravar ‘N’. | MFS540746 |
|  |  |  |
|  |  |  |

# MTZ-DW-Manutencao_Combustiveis_Tributação Monofásica ICMS

- **Fonte:** MTZ-DW-Manutencao_Combustiveis_Tributação Monofásica ICMS.docx
- **Modificado:** 2023-06-15
- **Tamanho:** 33 KB

---

    

# Módulo DW – Manutenção – Tabela Produtos Sujeitos à Tributação Monofásica ICMS   \(TACES112\)

__Localização__: Menu Básicos, Módulo: Data Warehouse

Menu Manutenção >> Combustíveis \(Não Varejistas\) >> Produtos Sujeitos à Tributação Monofásica ICMS

__Localização__: Menu Específicos, Módulo: Combustíveis e Derivados de Petróleo

Menu Parâmetros >> Produtos Sujeitos à Tributação Monofásica ICMS

* *

##### DOCUMENTO DE REQUISITO

###### MFS

###### Nome

__Descrição__

__Data Alteração__

MFS540746

Liliane Assaf

Criação da tela de manutenção

15/06/2023

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

Tela de manutenção disponível em dois módulos Data Warehouse e Combustíveis e Derivados de Petróleo\.

Nesta opção é possível fazer a manutenção dos Códigos de combustíveis sujeitos à tributação monofásica do ICMS, cuja carga inicial se dá através da TACES112\.

Base Legal:

[Portal da Nota Fiscal Eletrônica \(fazenda\.gov\.br\)](https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/NJarYc9nus=) \- Tabela de códigos de combustíveis sujeitos à tributação monofásica de ICMS\.

Tabela: CBT\_PRD\_ICMS\_MONO

Os tratamentos relacionados ao regime de tributação monofásica do ICMS aplicados na geração do Sped Fiscal, Livros de Apuração do ICMS e ICMS\-ST e SCANC dependem das seguintes definições:

\- Os tratamentos são aplicados para as notas fiscais cuja data fiscal se enquadre na vigência da monofasia do combustível, ou seja, a data fiscal >= Data de Validade Inicial aqui informada para o combustível\.

\- Produto movimentado na nota fiscal deve ser um Combustível Sujeito à Tributação Monofásica\. Para isso, o campo “Código do Produto Oficial” presente na parametrização dos Produtos x Grupos de Combustíveis e Derivados \(SAFX96\) deve estar preenchido de acordo com os códigos aqui informados\. 

Módulo: Combustíveis e Derivados de Petróleo, menu Parâmetros >> Produtos x Grupos de Combustíveis e Derivados

Módulo: Data Warehouse menu Manutenção >> Combustíveis \(Não Varejistas\) >> Produtos x Grupos de Combustíveis e Derivados

\- Parâmetro 94 marcado, presente na tela de manutenção dos Parâmetros p/ UF no módulo ICMS\.

\- SAFX325 – Informações de Tributação do ICMS Monofásico carregada

\- CST movimentado na nota fiscal igual a 02, 25, 53, 61

MFS540746

__RN01__

__Campo  – Código Produto Oficial:__

Campo obrigatório\.

Texto de livre digitação\.

Campo COD\_PROD\_OFICIAL da tabela CBT\_PRD\_ICMS\_MONO

MFS540746

__RN02__

__Campo – Validade Inicial__

Campo obrigatório\.

Texto formatado com DD/MM/AAAA

Campo DAT\_VALID\_INI da tabela CBT\_PRD\_ICMS\_MONO

MFS540746

__RN03__

__Campo – Descrição__

Campo não obrigatório

Texto de livre digitação\.

Campo DSC\_PROD\_OFICIAL da tabela CBT\_PRD\_ICMS\_MONO

MFS540746

__RN04__

__Campo – Alíquota ad Rem ICMS:__

Campo não obrigatório\.

Campo numérico com 4 casas decimais\.

Campo ALIQ\_AD\_REM\_ICMS da tabela CBT\_PRD\_ICMS\_MONO

MFS540746

__RN05__

Campo –Validade Final

Campo não obrigatório\.

Texto formatado com DD/MM/AAAA

Campo DAT\_VALID\_FIM da tabela CBT\_PRD\_ICMS\_MONO

MFS540746

__RN06__

Campo \- Biocombustível

Campo não obrigatório

Lista fixa ou check\-box\.

Se marcado sim, gravar ‘S’ no campo IND\_BIOCOMB da tabela CBT\_PRD\_ICMS\_MONO\. Se não, gravar ‘N’\.

MFS540746


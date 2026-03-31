# MTZ-DW-Manutencao_Combustiveis_Grupos de Combustíveis e Derivados

- **Fonte:** MTZ-DW-Manutencao_Combustiveis_Grupos de Combustíveis e Derivados.docx
- **Modificado:** 2023-06-15
- **Tamanho:** 33 KB

---

    

# Módulo DW – Manutenção – Grupos de Combustíveis e Derivados

__Localização__: Menu Básicos, Módulo: Data Warehouse

Menu Manutenção >> Combustíveis \(Não Varejistas\) >> Grupos de Combustíveis e Derivados

__Localização__: Menu Específicos, Módulo: Combustíveis e Derivados de Petróleo

Menu Parâmetros >> Grupos de Combustíveis e Derivados

* *

##### DOCUMENTO DE REQUISITO

###### MFS

###### Nome

__Descrição__

__Data Alteração__

MFS540746

Liliane Assaf

Disponibilizar manutenção no módulo Data Warehouse

15/06/2023

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

Tela de manutenção disponível em dois módulos Data Warehouse e Combustíveis e Derivados de Petróleo\.

Nesta opção é possível fazer a manutenção dos Grupos de combustíveis e derivados, devendo informar para cada grupo quais os anexos que são emitidos 

Tabela: CBT\_GRP\_COMB

__RN01__

__Campo  – Grupo Combustível__

Campo obrigatório\.

Texto de livre digitação\.

__RN02__

__Campo – Descrição__

Campo não obrigatório

Texto de livre digitação\.

__RN03__

__Campo – Produto SEF__

Campo não obrigatório

Texto de livre digitação\.

Este código deve estar de acordo com os códigos de produtos relacionados na tabela 4\.3 do manual de orientação do SCANC \(Sistema de Captação e Auditoria dos Anexos de Combustíveis\)\. Obs: A informação deste campo é utilizada na geração dos Registros 40, 45, 60, 62 e 70 do SCANC Distribuidoras

Veja como deve ficar a parametrização dos Grupos Combustíveis:

Cód Grupo

Descrição

AEA

ÁLCOOL ETÍLICO ANIDRO COMBUSTÍVEL

DSL

ÓLEO DIESEL A

DSM

ÓLEO DIESEL MARÍTIMO \(DMA\-MGO, DMB\-MDO\)

B00

BIODIESEL B100

BXD

ÓLEO DIESEL B \(MISTURA DIESEL\-B100\)

GSL

GASOLINA A

GSP

GASOLINA A PREMIUM

GSC

GASOLINA C

GCP

GASOLINA C PREMIUM

GSV

GASOLINA DE AVIAÇÃO

__RN04__

__Campo – Anexos:__

Para cada anexo existe um check\-box\. Os anexos com final “M” devem ser marcados para os combustíveis sujeitos à tributação monofásica\.

__RN05__

__RN06__


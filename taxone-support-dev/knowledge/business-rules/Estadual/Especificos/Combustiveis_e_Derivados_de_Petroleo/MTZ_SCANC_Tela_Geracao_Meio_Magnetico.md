# MTZ_SCANC_Tela_Geracao_Meio_Magnetico

- **Fonte:** MTZ_SCANC_Tela_Geracao_Meio_Magnetico.docx
- **Modificado:** 2023-05-19
- **Tamanho:** 63 KB

---

THOMSON REUTERS

Distribuidora – Geração dos Arquivos Magnéticos – SCANC

Módulo Combustível e Derivados de Petróleo \(SCANC\)

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-11111

Julyana Perrucini

Este documento não modifica a estrutura de geração do meio magnético do SCANC que está desenvolvida desde 2012, porém será necessário incluir novos grupos de combustíveis para serem considerados na geração\.

MFS\-535195

Aline Melo

Atendimento a Nota Técnica 2023\.001 \- v\.1\.00\.

Sumário

[1\.	Regras dos Campos	3](#_Toc494804515)

# <a id="_Toc350763252"></a><a id="_Toc494804515"></a>Regras dos Campos 

__Localização da tela:__ Específicos\\ Combustível e Derivados de Petróleo\\ Movimento\\ Distribuidora\\ Geração dos Arquivos Magnéticos \- SCANC

__Título da tela: __Geração do Meio Magnético \- SCANC

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Registros 

Texto

N

S

Formato:

Check Box

Default:

Todas as opções selecionadas

Permite que o usuário selecione os registros para a geração no arquivo magnético:

Lista:

10 – Estabelecimento

20 – Fornecedor / Cliente

40 – Nota Fiscal

45 – Nota Fiscal Óleo Diesel e Biodiesel Tributação Monofásica

60 – Estoque

62 – Estoque por Fornecedor

70 – Variação de Estoque

80 – GNRE

90 – Totalização dos Registros 

MFS\-535195

Grupos de Combustíveis

Texto

N

S

Formato:

Check Box

Default:

Todas as opções selecionadas

Permite que o usuário selecione os grupos de combustíveis para geração no arquivo magnético\.

Lista:

DSL – Diesel A

DSM \- Diesel Marítimo

GSL – Gasolina A

GSV – Gasolina de Aviação

GLP – GLP

OCB – Óleo Combustível

QAV – Querosene Aviação

QRS – Querosene

AEA – Álcool Anidro

S10 – Diesel A S10

B100 – Biodiesel B100

BXD – Óleo Diesel B

BDX – Biodiesel B02

GSP – Gasolina A Premium

GSC – Gasolina C

GLN – GLN

É importante que esse mesmo código selecionado na geração seja preenchido no campo Produto SEF do parâmetro Grupos de Combustíveis e Derivados\.

*Exemplo:*

Grupo Combustível: GA

Descrição: Gasolina A

Anexos: I

Anexos RO Decreto 10886\-A: nulo

Produto SEF: GSL

MFS\-11111

MFS\-535195


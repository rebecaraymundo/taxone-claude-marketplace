# MTZ_SCANC_Tela_Geracao_Meio_Magnetico

- **Fonte:** MTZ_SCANC_Tela_Geracao_Meio_Magnetico.docx
- **Modificado:** 2025-02-28
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

MFS698396

Andréa Rocha

Inclusão de um parâmetro para definir a regra geração do campo Informação do ICMS do registro Tipo 45\.

MFS760481

Liliane Assaf

Inclusão do registro 47, alteração na descrição do registro 45, inclusão do Grupo Combustível “GPN” e ordenar a lista de Grupos Combustíveis\.

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

45 – Nota Fiscal Óleo Diesel, Biodiesel, Gasolina e Etanol Anidro Tributação Monofásica

47 \- Nota Fiscal GLP/GLGN Tributação Monofásica

60 – Estoque

62 – Estoque por Fornecedor

70 – Variação de Estoque

80 – GNRE

90 – Totalização dos Registros 

MFS\-535195

MFS760481

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

AEA – Álcool Anidro

B00 – Biodiesel B100

BXD – Óleo Diesel B

BXS – Óleo Diesel B S10

BDX – Biodiesel B02

DSL – Diesel A

DSM \- Diesel Marítimo

S10 – Diesel A S10

GLP – GLP

GLN – GLN

GPN\- GLP/GLGN

GSL – Gasolina A

GSP – Gasolina A Premium

GSC – Gasolina C

GCP – Gasolina C Premium

GSV – Gasolina de Aviação

OCB – Óleo Combustível

QAV – Querosene Aviação

QRS – Querosene

É importante que esse mesmo código selecionado na geração seja preenchido no campo Produto SEF do parâmetro Grupos de Combustíveis e Derivados\.

*Exemplo:*

Grupo Combustível: GA

Descrição: Gasolina A

Anexos: I

Anexos RO Decreto 10886\-A: nulo

Produto SEF: GSL

MFS\-11111

MFS\-535195

MFS760481

Gerar o Campo 24\-Informação do ICMS a partir do CST \(Registro 45\)

Texto

N

S

Formato:

Check Box

Default:

Desmarcado

Esse parâmetro vai definir a forma de gerar o campo 24\-Informação do ICMS do registro Tipo 45\.

MFS698396


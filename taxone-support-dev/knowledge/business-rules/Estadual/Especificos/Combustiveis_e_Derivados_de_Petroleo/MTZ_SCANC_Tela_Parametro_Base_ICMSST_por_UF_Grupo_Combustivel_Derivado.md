# MTZ_SCANC_Tela_Parametro_Base_ICMSST_por_UF_Grupo_Combustivel_Derivado

- **Fonte:** MTZ_SCANC_Tela_Parametro_Base_ICMSST_por_UF_Grupo_Combustivel_Derivado.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 67 KB

---

THOMSON REUTERS

Base ICMS\-ST p/ UF/Grupo Combustível e Derivados

Módulo Combustível e Derivados de Petróleo \(SCANC\)

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-11111

Julyana Perrucini

Este documento tem como objetivo alterar a tela de manutenção da SAFX111, que tem como intuito cadastrar Base de ICMS\-ST por UF/Grupo Combustível e Derivados\. Será incluído o campo para informar o valor da regra de redução da base de cálculo e do campo para informar o fator de conversão do volume\.

Sumário

[1\.	Regras dos Campos	3](#_Toc494448785)

# <a id="_Toc350763252"></a><a id="_Toc494448785"></a>Regras dos Campos 

__Localização da tela:__ Específicos\\ Combustível e Derivados de Petróleo\\ Parâmetros\\ Base ICMS\-ST p/ UF/Grupo Combustível e Derivados

__Título da tela: __Base ICMS\-ST p/ UF/Grupo Combustível e Derivados

__\[ALTERADA – MFS\-11111\]__

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Grupo Combustível

Texto

S

N

Formato: 

Text Input com opção de selecionar a informação na tela Grupos de Combustíveis e Derivados 

Default: 

Habilitado

Neste campo o usuário deverá informar o código do grupo de combustível, de acordo com o cadastro realizado na tela Grupos de Combustíveis e Derivados\.

MFS\-11111

UF

Texto

S

N

Formato: 

Combo Box

Default: 

Habilitado

Neste campo o usuário deverá informar a unidade de federação, que deseja fazer a parametrização\.

*Observação:* Para correta seleção deste código, o usuário deverá ter importado a tabela TFIX04 através do Módulo Básicos \- Ferramentas ou cadastrado manualmente\.

MFS\-11111

Validade Base ST

Data

S

N

Formato: 

Text Input DD/MM/AAAA

Default: 

Habilitado

Neste campo o usuário deverá informar a data de validade da base de substituição tributária\.

MFS\-11111

Regra Base ST

Numérico

N

S

Formato:

Combo Box

Default:

Habilitado

Neste campo o usuário deverá informar qual a regra que será utilizada na base da substituição tributária\.

__Conteúdo:__

1 \- MVA \(Margem Valor Agregado\);

2 \- PMPF \(Preço Médio Ponderado Consumidor Final\);

3 \- ANP \(Valor Unitário de Partida\)\.

MFS\-11111

Vlr\. Regra Base ST

Numérico

N

S

Formato:

Text Input 0,000000

Default:

Habilitado

Neste campo o usuário deverá informar o valor da regra da base de substituição tributária\.

MFS\-11111

Vlr\. Regra Redução BC

Numérico

N

S

Formato:

Text Input 0,000000

Default:

Habilitado

Alguns estados trabalham com a redução da base de cálculo, então deve ser informada a regra que determina o valor da Redução da Base de Cálculo \(Porcentagem\) do combustível na UF informada\.

MFS\-11111

Fator de Conv\. De Volume

Numérico

N

S

Formato:

Text Input 0,000000

Default:

Habilitado

O FCV deve ser considerado apenas nas compras de Gasolina A e Diesel A de refinarias, embora para este caso o mesmo já esteja embutido nos valores informados em campo próprio na nota fiscal, e importadoras/equiparadas\.

MFS\-11111


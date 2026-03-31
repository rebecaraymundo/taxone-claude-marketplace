# MTZ-GIAM-TO-Manutencao_do_Diferencial_de_Aliquota

- **Fonte:** MTZ-GIAM-TO-Manutencao_do_Diferencial_de_Aliquota.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Módulo GIAM\-TO – Manutenção do Diferencial de Alíquota

__Localização__: Menu Estadual,  Módulo: GIAM\-TO, Item Obrigações 🡪 Diferencial de Alíquota 🡪 Manutenção 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS6415

Alterações da GIAM\-TO p/a versão 10\.0 \(Portaria n\. 748, de 07/08/2016\)

Inclusão do campo “Alíquota”

07/10/2016

\(criação do doc\)

MFS31876

Andréa Rocha

Inclusão do campo “Alíquota” na chave da tabela

19/12/2019

Sumário

[1\.	Regras Gerais	2](#_Toc463622453)

[2\.	Layout da Tela	2](#_Toc463622454)

[3\.	Regras de Funcionamento dos Campos	2](#_Toc463622455)

# <a id="_Toc463622453"></a>Regras Gerais

# <a id="_Toc463622454"></a>Layout da Tela

# <a id="_Toc463622455"></a>Regras de Funcionamento dos Campos

Alteração da __MFS6415__: Inclusão do campo “Alíquota” 

\(OBS: esta informação foi incluída na geração dos dados da tabela auxiliar da GIAM\-TO que armazena as informações sobre diferencial de alíquota para posterior geração do Segmento P\)

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

UF

Domicílio Fiscal

Valor Contábil

Base de Cálculo

Diferencial de Alíquota

Alíquota

    Numérico     

    \(003v004\)

__    N__

__    S__

 

Este campo exibe o conteúdo da alíquota do diferencial referente à UF demonstrada no campo “UF”\.  

O campo não será obrigatório, por causa dos dados já existentes na base antes de sua inclusão\. Mas quando não preenchido, será exibida a seguinte mensagem ao salvar a operação:

*O preenchimento da alíquota é obrigatório a partir da versão 10\.0 da GIAM\-TO\.  Deseja salvar a operação?*

*                                   <Sim>  <Não>*

Opção = Sim 🡪 salva os dados incluídos/alterados;

Opção = Não 🡪 não salva os dados incluídos/alterados;

__\[MFS31876\]__

Obs\.:  O campo passará a fazer parte da chave mas não será obrigatório, Quando o campo não for preenchido, será gravado com zero\.

       = = = = = =


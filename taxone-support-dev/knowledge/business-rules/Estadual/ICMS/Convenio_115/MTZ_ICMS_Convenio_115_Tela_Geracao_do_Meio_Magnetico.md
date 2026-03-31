# MTZ_ICMS_Convenio_115_Tela_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_ICMS_Convenio_115_Tela_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2024-07-11
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Geração dos Arquivos Magnéticos para o Convênio 115

Convênio ICMS 115

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4281

Julyana Perrucini

Criação de parâmetro para quantidade de documento fiscal por volume \(quebra de arquivo\)

OS4413\-A

Vânia Dias Mattos

Tratamento dos itens negativos da nova tabela SAFX431

OS4786

Vânia Dias Mattos

Inclusão de parâmetro para filtro do Modelo

MFS\-4969

Marcos G\. de Paula

Inclusão da opção de Formato do Convênio ICMS 60

MFS\-6572

Julyana Perrucini

Criação do parâmetro para sequencial do formato do Convênio ICMS 60

MFS\-15387

Julyana Perrucini

Criação do parâmetro para gerar arquivo auxiliar

MFS\-16140

Julyana Perrucini

Alteração do parâmetro para gerar arquivo auxiliar

MFS\-20889

João Henrique

Criação do parâmetro para gerar o Arquivo dos Dados Cadastrais com a descrição do município conforme tabela do IBGE\.

MFS24491

Andréa Rocha

Criação do parâmetro para desconsiderar os itens de desconto da SAFX43\.

MFS91802

Rogério Ohashi

Criação do parâmetro para desconsiderar os itens de desconto da SAFX431 p/ Arquivo Mestre\.

Sumário

[1\.	Regras dos Campos	3](#_Toc372814288)

# <a id="_Toc350763252"></a><a id="_Toc372814288"></a>Regras dos Campos 

__Localização da tela:__ Estadual >> ICMS >> DATA MART >> Convênio ICMS 115 >> Geração do Meio Magnético\.

__Título da tela: __Geração dos Arquivos Magnéticos para o Convênio 115

__Considerações: __

- Foi criado o parâmetro nessa tela com o nome Quantidade de NFs p/ arquivos com movimentação menor que 1\.000\.000, respeitando a seleção “Qtde Documentos Fiscais por Volume:”
- Alteração da __OS4786__: criado o campo “Modelo de documento para geração”;
- Alteração da __MFS\-6572__: criado o campo “Sequencial”;

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Sequencial

Texto

N

S

Default:

Desabilitado

Permite o usuário incluir o número de sequência do arquivo magnético gerado para substituição do arquivo original entregue à SEFAZ\.

__Tratamento:__

- Deverá ser habilitado apenas quando o campo “Formato do Convênio ICMS” estiver marcado com Convênio ICMS 60 e o campo “Status” estiver marcado com a opção Substituta;
- Quando habilitado, o preenchimento será obrigatório, caso não for preenchido emitir a mensagem de erro na tela: *“Arquivo Conv ICMS 60 substituto, favor preencher o campo Sequencial do arquivo\.”*\.

__MFS\-6572__

Arquivo com qtde de cem mil

Radio Button

S

S

Default: 

Selecionado

Permitir o usuário selecionar essa opção para gerar o arquivo magnético dividindo os arquivos de cem em cem mil, quando este atingir 1\.000\.000 de registros\.

__OS4281__

Arquivo com qtde específica

Radio Button

N

S

Default: 

Não Selecionado

Permitir o usuário selecionar essa opção caso o arquivo magnético tenha que ser entregue dividido diferente de cem mil, isso também quando atingir 1\.000\.000 de registros\.

Esta opção habilita o campo “Qtde Específica:” para o usuário colocar a quantidade que deve ser quebrado o arquivo\.

__OS4281__

Qtde Específica

Texto

N

S

Default:

Desabilitado

Nesse campo o usuário deve informar a quantidade necessária de registros e quando atingir essa quantidade informada será dividido os arquivos, isso também quando atingir 1\.000\.000 de registros\.

__Tratamento:__

- Deverá ser habilitado apenas quando a opção “Arquivo com qtde específica” estiver selecionada, caso contrário não habilitar;
- Deve ser obrigatória a quantidade informada pelo usuário maior que zero, se não obedecer a essa regra, ou seja, preenchimento com “0”, enviar uma mensagem na tela: *“Deve ser preenchido o campo Qtde Específica\. Favor verificar\.”*;
- Se o usuário colocar essa opção citada anteriormente e não preencher a quantidade específica \(campo Qtde Específica\), enviar uma mensagem na tela: *“Deve ser preenchido o campo Qtde Específica\. Favor verificar\.”\.*

__OS4281__

Gravar os itens negativos no arquivo \(itens da SAFX431\)

Checkbox 

N

S

Default: desmarcado 

As regras da utilização deste parâmetro estão descritas no documento de regras da geração do arquivo, regra __RN18__\. 

Quando no campo “Formato do Convênio ICMS” for selecionado a opção “Convênio ICMS 60”, este campo será desabilitado para edição\.

__OS4413\-A__

__MFS\-4969__

Modelo de documento para geração

Listbox

N

S

Default: “Todos”

Este campo é uma lista com as seguintes opções:

\- Todos

\- 01

\- 06

\- 21

\- 22

 

Obs: o modelo “01” também será tratado, pois é o modelo usado pelo cliente CEG p/geração do Conv\. 115\.

__OS4786__

Formato do Convênio ICMS

RadioButton

S

S

Default: Convênio ICMS 113

Exibir as opções:

\- Convênio ICMS 115

\- Convênio ICMS 133

\- Convênio ICMS 60

__MFS\-4969__

Gerar Arquivo Auxiliar

Checkbox

N

S

Default: Opções desmarcadas

__\[ALTERADA – MFS16140\]__

Exibir as opções:

\- Ato COTEPE/ICMS 74

\- Conv\. ICMS 201 – Fatura

\- Conv\. ICMS 201 – Pré\-Pago

__MFS\-15387__

__MFS\-16140__

Geração para Empresas c/ Insc\. Estadual Única

Checkbox 

N

S

Default: desmarcado 

Quando no campo “Formato do Convênio ICMS” for selecionado a opção “Convênio ICMS 60”, este campo será desabilitado para edição\.

__MFS\-4969__

<a id="_Hlk525031071"></a>*Preenchimento da Descrição*

Geração Descrição de Município por Cód\. IBGE

Checkbox 

N

S

Default: desmarcado

Permitir o usuário marcar essa opção para gerar os Arquivos dos Dados Cadastrais com a descrição do município através da TACES06\.

__MFS\-20889__

Desconsiderar Itens de Desconto \(SAFX43\)

Checkbox 

N

S

Default: desmarcado

Permitir o usuário marcar essa opção para desconsiderar os itens de desconto na geração\.

__MFS\-24491__

Desconsiderar Itens de Desconto \(SAFX431\) p/ Arquivo Mestre

Checkbox 

N

S

Default: desmarcado

Permitir o usuário marcar essa opção para desconsiderar os itens de desconto na geração para o Arquivo Mestre de Documento Fiscal\.

__Obs\.:__ Este parâmetro deverá estar liberado para ser __marcado__, somente se o parâmetro “Desconsiderar Itens de Desconto \(SAFX43\)”  estiver marcado\.

__MFS\-91802__


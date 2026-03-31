# MTZ_Relatorios_Acessorios_Resumo_da_Apuracao_do_ICMS

- **Fonte:** MTZ_Relatorios_Acessorios_Resumo_da_Apuracao_do_ICMS.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Relatório Resumo da Apuração do ICMS

Resumo da Apuração do ICMS – Livro Modelo 108

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

CH21826\_2016

Julyana Perrucini

Este documento tem como objetivo definir o funcionamento do Relatório Resumo da Apuração do ICMS\.

Sumário

[1\.	REGRAS DOS CAMPOS	3](#_Toc463958508)

[2\.	REGRAS DE GERAÇÃO DO RELATÓRIO	5](#_Toc463958509)

# <a id="_Toc463958508"></a>REGRAS DOS CAMPOS

__Localização da tela:__ Estadual\\ ICMS\\ Relatórios\\ Acessórios\\ Resumo da Apuração do ICMS

__Título da tela: __Relatório Resumo da Apuração do ICMS

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Estabelecimento

Texto

S

S

Formato: 

Combo Box

Default: 

Habilitado

Nesse campo o usuário poderá informar o estabelecimento para qual deseja emitir o resumo\.

__Tratamento:__

- O usuário somente poderá selecionar este campo, caso não tenha informado o código do estabelecimento na tela de login do sistema, caso contrário será exibido o estabelecimento que o usuário se logou;
- Caso o usuário tenha selecionado primeiramente uma UF, neste campo serão exibidos todos os estabelecimentos cadastrados com a unidade de federação selecionada\. Podendo emitir o resumo com todos os estabelecimentos com essa UF;
- Se o usuário não selecionar um estabelecimento, emitir a seguinte mensagem na tela: *“Estabelecimento Deve Ser Escolhido”\.*

CH21826\_2016

Data Apuração

Data

S

S

Formato: 

DD/MM/AAAA

Default: 

Habilitado

Nesse campo o usuário deverá informar a data da apuração, que o usuário deseja emitir o relatório\.

__Tratamento:__

- Se o usuário não preencher a data de apuração, emitir a seguinte mensagem na tela: *“Data da Apuração Inválida”\.*

CH21826\_2016

UF

Texto

N

S

Formato: 

Combo Box

Default: 

Habilitado

Nesse campo o usuário poderá selecionar a unidade de federação, que deseja emitir o resumo\. 

__Tratamento:__

- O usuário somente poderá selecionar este campo, caso não tenha informado o código do estabelecimento na tela de login do sistema, caso contrário será exibido a UF do estabelecimento que o usuário se logou\.

CH21826\_2016

OK

Texto

S

N

Formato: 

Button

Default: 

Habilitado

Esse botão servirá para processamento do relatório\.

CH21826\_2016

Cancelar

Texto

S

N

Formato: 

Button

Default: 

Habilitado

Esse botão servirá para cancelar a operação caso o usuário não desejar gerar o relatório\.

CH21826\_2016

# <a id="_Toc396483621"></a><a id="_Toc463958509"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Origem das informações para geração:__ 

Estadual >> Controle das Obrigações Estaduais >> Obrigações: Registro do Livro de modelo 108 no item de menu Obrigações Fiscais\.

__Regra de seleção: __

__Ordenar por CNPJ/ Data Emissão: __

__Regra de agrupamento: __

__Ordenação: __

__Campo/Coluna__

__Tipo__

__Formato/Default__

__Regra__

__OS/CH__

Dados do Cabeçalho

Corpo do Relatório


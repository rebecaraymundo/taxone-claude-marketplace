# MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_EFD Fiscal

- **Fonte:** MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_EFD Fiscal.docx
- **Modificado:** 2022-09-30
- **Tamanho:** 89 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 087/2020\) 

Transferência dos Movimentos para EFD Fiscal 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\), itens:

Geração à IN\-RE 087/20 à Transferência dos Movimentos para EFD Fiscal

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS48753__

Liliane Videira Assaf

Criação da funcionalidade

12/01/2021

__MFS65137__

Liliane Videira Assaf

Tratamento dos Cupom Fiscal \(Mod\. 02, 2D e 60\) para geração do registro C480 do Sped Fiscal\.

Os cupons devem ser lidos da tabela EST\_ST\_RS\_ECF e gravados na tabela X297\_INF\_COMP\_ST\_CUPOM\_ECF, de onde o registro C480 é gerado no Sped Fiscal\.

13/05/2021

__MFS72958__

Liliane Videira Assaf

Tratamento de produtos novos sem inventário\.

Atualizar o Resumo de “Quantidade Total de Registros Gravados” para demonstrar o total de registros lidos e inseridos do H030\.

21/09/2021 

Sumário

[1\.	Introdução	1](#_Toc62057632)

[2\.	Parâmetros da Tela	1](#_Toc62057633)

[3\.	Críticas	1](#_Toc62057634)

[4\.	Processamento	1](#_Toc62057635)

[1º Passo: Atualizar o Inventário do Último dia do Mês Anterior	1](#_Toc62057636)

[2º Passo: Atualizar Tabelas SAFX p/ Gerar os registros do Sped Fiscal	1](#_Toc62057637)

[3º Passo \- Geração Registros de Saldo Consolidado de Ressarcimento e Complemento \(1255\)	1](#_Toc62057638)

[4º Passo: Gerar Relatórios de Conferência	1](#_Toc62057639)

#  

# <a id="_Toc62057632"></a>Introdução

O objetivo dessa funcionalidade é recuperar os registros gerados pelo processo de “Geração dos Movimentos” a partir das tabelas específicas do módulo, e gravar as tabelas definitivas relacionadas as “SAFX”, que são base para geração dos registros C180, C181, C185, C480, C186, 1250, 1255, H030 do Sped Fiscal\. 

Como __Pré\-Requisito__ para esta execução, não pode existir registro na tabela definitiva, oriundo da importação da SAFX\.

__Tabelas Específicas da Geração do Movimento__

__Tabelas definitivas relacionadas as SAFX__

__Registro do SPED FISCAL__

EST\_ST\_RS\_NF\_ENT

x296\_info\_compl\_st\_itens\_merc

C180

EST\_ST\_RS\_NF\_DEV\_ENT

X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV

C186

EST\_ST\_RS\_NF\_DEV\_SAI

X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV

C181

EST\_ST\_RS\_NF\_SAI

x296\_info\_compl\_st\_itens\_merc

C185

EST\_ST\_RS\_NF\_SAI

x296\_info\_compl\_st\_itens\_merc

C380

EST\_ST\_RS\_ECF

X297\_INF\_COMP\_ST\_CUPOM\_ECF

C480 \[__MFS65137\]__

EST\_ST\_RS\_MEDIA\_POND

X52\_INVENT\_PRODUTO

H030

X304\_SALDO\_CONS\_RES\_COMP\_ICMS

1255

__Artefatos gerados pela Transferência do Movimento__:

O resultado dessa geração pode ser conferido através dos Relatórios:

- Relatório de Conferência do Saldo Consolidado de Ressarcimento e Complemento – registro 1255, gerado em arquivo Excel\. 
- Relatório Demonstrando o total de Registros Lidos e Gravados em cada tabela definitiva relacionada a SAFX\.

__Base Legal:__

\- IN\-RE 087/20

\- IN\-RE 096/20

# <a id="_Toc62057633"></a>Parâmetros da Tela 

Período: MM/AAAA

Estabelecimentos

\[ \] xxxxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[ \] xxxxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[ \] xxxxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Funcionamento dos campos:

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

<a id="_Hlk517437550"></a>Período 

Data

\(mês e ano\)

S

S

\(MM/AAAA\)

Neste campo será informado o período \(mês e ano\) para a geração dos dados\.

Deve ser um mês válido\.

Estabelecimentos

Alfanumérico 

S

S

Neste campo é exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário\.

Serão disponibilizados para seleção apenas os estabelecimentos de RS \(UF do estabelecimento = RS\)\.

Selecionar

N

N

Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos\.

O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”:

\- Somente Estabelecimentos da empresa do login;

\- Somente Estabelecimentos da UF de RS;

Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos” já marcados\. 

   

Marcar todos

N

N

Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”\.

# <a id="_Toc62057634"></a>Críticas 

Como pré\-requisito, não pode existir registro importado nas tabelas SAFX\. Caso exista, o processo será abortado\.

Existência de Movimento de Entradas e Saídas importados pela SAFX296

Caso exista Movimento de Entradas e Saídas importados pela SAFX296, para o estabelecimento e período informados na tela de geração, exibir a seguinte mensagem no log:

“*Existem dados importados através da SAFX296 – Informações Complementares das Operações Sujeitas ao ST \(C180, C185 e C380\) para o estabelecimento e período informados\. Nesta rotina os movimentos de entradas e saídas a serem apresentados nos registros C180, C185 e C380 são gerados na tabela definitiva da SAFX296\. Como pré\-requisito não pode existir movimentos oriundos da Importação da SAFX296\. Favor realize a limpeza dessa tabela no módulo Ferramentas, opção Exclusão de Tabelas Definitivas\.”*	

__\[MFS65137\]__

__Existência de Movimento de Cupom Fiscal importado pela SAFX297__

Caso exista Movimento de Cupom Fiscal importados pela SAFX297, para o estabelecimento e período informados na tela de geração, exibir a seguinte mensagem no log:

“*Existem dados importados através da SAFX297 –* *Informações Complementares das Operações Sujeitas ao ST \(C480\) para o estabelecimento e período informados\. Nesta rotina os movimentos de cupons fiscais a serem apresentados no registro C480 são gerados na tabela definitiva da SAFX297\. Como pré\-requisito não pode existir movimentos oriundos da Importação da SAFX297\. Favor realize a limpeza dessa tabela no módulo Ferramentas, opção Exclusão de Tabelas Definitivas\.”	*

__Existência de Movimento de Devoluções de Entradas e Saídas importados pela SAFX308__

Caso exista Movimento de Devoluções de Entradas e Saídas importados pela SAFX308, para o estabelecimento e período informados na tela de geração, exibir a seguinte mensagem no log:

“*Existem dados importados através da SAFX308 – Informações Complementares das Operações de Devolução Sujeitas ao ST \(C181 e C186\) para o estabelecimento e período informados\. Nesta rotina os movimentos de devoluções a serem apresentados nos registros C181 e C186 são gerados na tabela definitiva da SAFX308\. Como pré\-requisito não pode existir movimentos oriundos da Importação da SAFX308\. Favor realize a limpeza dessa tabela no módulo Ferramentas, opção Exclusão de Tabelas Definitivas\.”*

__Existência de Saldo Consolidado da Restituição/Complemento importado pela SAFX304__

Caso exista Saldo Consolidado da Restituição/Complemento ST importados pela SAFX304, para o estabelecimento e período informados na tela de geração, exibir a seguinte mensagem no log:

“*Existem dados importados através da SAFX304 – Saldo Consolidado da Restituição/Complemento ST \(1250 e 1255\) para o estabelecimento e período informados\. Nesta rotina os saldos a serem apresentados nos registros 1250 e 1255 são gerados na tabela definitiva da SAFX304\. Como pré\-requisito não pode existir movimentos oriundos da Importação da SAFX304*

*\. Favor realize a limpeza dessa tabela no módulo Ferramentas, opção Exclusão de Tabelas Definitivas\.”*

Acontecendo qualquer erro, finalizar a geração com status = “\-1” – Erro\.

# <a id="_Toc62057635"></a>Processamento

__Visão resumida do Processamento__

O processamento requer uma ordem na geração dos movimentos já que algumas etapas dependem do resultado da execução anterior\.

Sendo assim vamos executar o processamente seguindo os passos abaixo:

1º Passo: Atualizar o Inventário do Último dia do Mês Anterior

2º Passo: Atualizar Tabelas SAFX p/ Gerar os registros do Sped Fiscal

3º Passo: Gerar os Registros de Saldo Consolidado de Ressarcimento e Complemento \(1255\)

4º Passo: Gerar Relatórios de Conferência

Segue detalhamento de cada passo do processamento

## <a id="_Toc62057636"></a>1º Passo: Atualizar o Inventário do Último dia do Mês Anterior

Recupera os Valores Unitários do ICMS, ICMS\-ST, Base de Cálculo do ICMS\-ST e FECEP\-ST da tabela EST\_ST\_RS\_MEDIA\_POND do último dia do mês anterior e atualiza a Tabela do Inventário \(X52\_INVENT\_PRODUTO\) para o registro do último dia do mês anterior com IND\_MOT\_INV = 06\. Gera uma crítica caso o os valores médios tenham sido importados e estejam diferentes dos calculados\.

Para maiores detalhes ver documento matriz:

\- MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_Inventário\_H030\.docx

## <a id="_Toc62057637"></a>2º Passo: Atualizar Tabelas SAFX p/ Gerar os registros do Sped Fiscal

Gravação das tabelas definitivas relacionadas as “SAFX”, base para geração dos registros C180, C181, C185, C186, C380 e \[__MFS65137\] __C480 do SPED FISCAL, a partir da leitura das tabelas específicas da Geração do Movimento\.

Para maiores detalhes ver documento matriz:

MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_Tabelas SAFX\_C180\_C181\_C185\_C186\_C380\_C480\.docx

## <a id="_Toc62057638"></a>3º Passo \- Geração Registros de Saldo Consolidado de Ressarcimento e Complemento \(1255\)

Geração dos registros de Saldo Consolidado de Ressarcimento e Complemento \(1255\)\.

O registro 1255 é uma consolidação dos valores de complemento e ressarcimento por Código de Motivo da Restituição/Complementação \(RS100, RS300, \.\.\.\) apresentados nos registros C181, C185, C330, C380, C430, \[__MFS65137\] __C480, C815 e C880 do Sped Fiscal\.

Os registros gerados são gravados na tabela de “Saldo Consolidado da Restituição/Complemento de ICMS” \- X304\_SALDO\_CONS\_RES\_COMP\_ICMS, base para geração do registro 1255 no Sped Fiscal\.

Os dados calculados e gravados podem ser consultados na tela SPEDàEFD – Escrituração Fiscal Digital àGeração àManutenção àRegistro 1255\.

Tabela Destino

Registros do SPED FISCAL

X304\_SALDO\_CONS\_RES\_COMP\_ICMS

1255

Para maiores detalhamentos ver documentos matrizes: 

\- MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_Saldo Ressarcimento Complemento\_1255\.docx

## <a id="_Toc62057639"></a>4º Passo: Gerar Relatórios de Conferência

Geração do Relatório de Conferência em arquivos Excel para conferência do registro 1255\.

Geração do Resumo demonstrando o total de registros lidos e gravados em tela, na aba “Quantidade Total de Registros Gravados”

- Relatório de Conferência do Saldo Consolidado de Ressarcimento e Complemento \(1255\)\. 

ver: MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_Saldo Ressarcimento Complemento\_1255\.docx

- Resumo “Quantidade Total de Registros Gravados”: 

    Layout do relatório:

Registro

Total Lidos

Total Inseridos

Total Atualizados

C180

C181

C185

C186

C380

C480 \[__MFS65137\]__

H030

__MFS72958__

Não se aplica ao H030

__MFS72958__

Não se aplica ao H030

1255

Não se aplica ao 1255

= = = = = =

 


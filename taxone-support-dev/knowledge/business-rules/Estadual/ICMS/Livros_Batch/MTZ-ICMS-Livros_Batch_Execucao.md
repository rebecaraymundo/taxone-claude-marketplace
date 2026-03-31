# MTZ-ICMS-Livros_Batch_Execucao

- **Fonte:** MTZ-ICMS-Livros_Batch_Execucao.docx
- **Modificado:** 2021-04-07
- **Tamanho:** 73 KB

---

THOMSON REUTERS

Módulo ICMS – Geração Batch dos Livros Fiscais

__Localização__: Menu Estadual, Módulo: ICMS, menu Livros Batch 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS2131

Atendimento ao Ato Cotepe ICMS 44/2015

Criação da nova apuração do ICMS Diferencial de Alíquota UF Origem/Destino, para atendimento ao Ato Cotepe ICMS 44/2015 \(ver item “3\-Processamento”\)\.

16/11/2015 \(criação do documento\)

MFS62601

Liliane Assaf

Na tela de programação foram realizadas as seguintes alterações:

__Troca__ do label __Data Inicial__ para __Programação Válida a partir de__

__Troca__ do label __Dias Específicos__ por __Gerar nos dias__

__Troca__ do label __Eventual__ por __Executar Programação em Qualquer Dia__

__Remoção__ do campo __Período__\.

Atualmente a execução da programação com opção Eventual, considera o período informado na tela de programação como sendo o período para geração do Livro\.

Com essa MFS, o campo Período está sendo removido\. E a apuração do livro passa a considerar o período que está em aberto no calendário fiscal\. Esse tratamento já é feito quando a programação possui Periodicidade = Dias Específicos\.

07/04/2021

Sumário

[1\.	Parâmetros da Tela	2](#_Toc432604677)

[2\.	Origem e Recuperação dos Dados	4](#_Toc432604678)

[3\.	Processamento	5](#_Toc432604679)

# <a id="_Toc432604677"></a>Parâmetros da Tela 

Empresa:  \[ xxx\- xxxxxxxxxxxxxx\]

Código da Programação: \[ xxx\- xxxxxxxxxxxxxx\]

Data Processamento:   \[ dd/mm/aaaa\]

# <a id="_Toc350763252"></a><a id="_Toc432604678"></a>Origem e Recuperação dos Dados

 

# Processamento

Se Data Processamento MAIOR OU IGUAL a Data Inicial da Programação, informada no campo “*Programação Válida a partir de” *da tela de Programação do Livro Batch, então:

Se a Periodicidade da Programação for Eventual “Executar Programação em Qualquer Dia” \(IND\_PERIOD = 2 da tabela ICT\_PROG\) então:

	Realizar a geração do livro para cada estabelecimento especificado na Programação\.

	Se a Periodicidade da Programação for Dias Específicos “Gerar nos Dias” \(IND\_PERIOD = 7 da tabela ICT\_PROG\) então:

		Se o dia da Data Processamento for um dia que estiver programado \(vide campo “Prog Dias Específicos da tela de Programação\), então:

			Realizar a geração do livro para cada estabelecimento especificado na Programação\.

 A geração do livro deve considerar:

- Período = período informado na Programação 
- Período = período em aberto do calendário\. Para isso:

\- Recuperar Periodicidade do livro \(tabela OBRIGACAO\_FISCAL \- IND\_PERIODICIDADE\) ;

\- Recuperar o período em aberto no calendário \(tabela CALEND\_OBRIGACAO \- DAT\_APURACAO\);

\- Calcular data Inicial do período de apuração, considerando Periodicidade e data fim do período em aberto\.

- Modelo = modelo informado na Programação
- Parâmetros informados no item de menu Manutenção >> Parâmetros p/ UF\.

Ao final da execução atualizar a tabela de Histórico da Programação \(ICT\_HISTORICO\), que servirá de base para o Relatório de Listagem de Histórico de Programação de Processos, disponível no menu Livros Batch >> Relatório >> Histórico:

Campos

Campo na tabela ICT\_HISTORICO

Regra de preenchimento

Código da Programação

COD\_PROG

Preencher com o código da programação executada\.

Código da Empresa

COD\_EMPRESA

Empresa de login\.

Código do Estabelecimento 

COD\_ESTAB

Estabelecimento pertencente a programação executada\.

Código do Tipo de Livro

COD\_TIPO\_LIVRO

Tipo do livro pertencente a programação executada\.

Modelo

MODELO

Modelo do livro da programação executada\.

Data Início do Período

DAT\_INI\_PERIODO

Data Inicial do período de apuração gerado para o livro, conforme calendário fiscal\.

Data Fim do Período

DAT\_FIM\_PERIODO

Data Final do período de apuração gerado para o livro, conforme calendário fiscal\.

Data/Hora Início da Geração

DAT\_INI\_GERACAO

Data e hora inicial da execução da geração do livro\.

Data/Hora Fim da Geração

DAT\_FIM\_GERACAO

Data e hora final da execução da geração do livro\.

Consolidado

IND\_CONSOLIDA\_P2

Indicador de livro consolidado pertencente a programação executada\.

Número do Processo

NUM\_PROCESSO

Número do processo da geração do livro\.

Status da Geração

STATUS

0 – Sucesso

1 – Aviso

\-1 \- Erro

Alteração da __MFS2131__: 

A geração batch do livro de apuração 108 passou a considerar o novo parâmetro “__*Apuração ICMS Dif\.Alíquota UF Orig/Dest \- EC 87/15*__” incluído na geração do livro\. Através deste novo parâmetro, será executado o novo processo especifico de Apuração do ICMS de Diferencial de Alíquota UF Origem/Destino, da mesma forma que será feito na geração do livro fiscal “108”, do menu “Datamart 🡪 Apuração do ICMS 🡪 Ajuste SINIEF”\.

O conteúdo do parâmetro a ser utilizado na chamada será o da parametrização do menu “*Parâmetros por UF*” \(parâmetro 91\), considerando a UF do Estabelecimento\.

= = = = = =

 


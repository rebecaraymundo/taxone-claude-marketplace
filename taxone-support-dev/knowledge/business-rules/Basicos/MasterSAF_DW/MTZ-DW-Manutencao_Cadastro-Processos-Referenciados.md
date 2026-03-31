# MTZ-DW-Manutencao_Cadastro-Processos-Referenciados

- **Fonte:** MTZ-DW-Manutencao_Cadastro-Processos-Referenciados.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Módulo DW – Manutenção do Cadastro de Processos Referenciados

__Localização__: Menu Básicos, Módulo DW, item Manutenção 🡪 Códigos 🡪 Cadastro de Processos Referenciados

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS5860

Aumento do tamanho do número do processo 

Aumento do tamanho do número do processo

29/12/2016

MFS14228

Julyana Perrucini

Esse documento tem como objetivo incluir a opção 9 no campo Natureza da Ação Judicial\.

01/11/2017 

MFS29841

Andréa Rocha

Esse documento tem como objetivo incluir novas opções no campo Natureza da Ação Judicial

Sumário

[1\.	Regras Gerais	3](#_Toc497317291)

[2\.	Layout da Tela	3](#_Toc497317292)

[3\.	Regras de Funcionamento dos Campos	3](#_Toc497317293)

# <a id="_Toc497317291"></a>Regras Gerais

Conforme consta no help deste item de menu, esta tabela foi criada para o cadastro dos processos referenciados que serão utilizados nas informações complementares a serem prestadas na EFD\-PIS/COFINS\.

# <a id="_Toc497317292"></a>Layout da Tela

# <a id="_Toc497317293"></a>Regras de Funcionamento dos Campos

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Número do Processo

Alfanumérico 

S

S

Alteração MFS5860: O tamanho deste campo foi aumentado de 15 posições para 20 posições p/atender ao layout da EFD\-Contribuições\.

MFS5860

Natureza da Ação Judicial

Alfanumérico

S

S

Formato: Combo Box

Default: Habilitado

Esse campo permite o usuário informar qual o indicador da natureza da Ação Judicial, obtida na Justiça Federal, em atendimento o Registro 1010 da EFD\-Contribuições\.

O campo só será disponibilizado quando o campo Tipo do Processo for igual à Ação Judicial\.

__\[ALTERADA – MFS14228\]__

__\[ALTERADA – MFS29841\]__

__Conteúdo:__

01 – Decisão judicial transitada em julgado, a favor da pessoa jurídica\.

02 – Decisão judicial não transitada em julgado, a favor da pessoa jurídica\.

03 – Decisão judicial oriunda de liminar em mandado de segurança\.

04 – Decisão judicial oriunda de liminar em medida cautelar\.

05 – Decisão judicial oriunda de antecipação de tutela\.

06 \- Decisão judicial vinculada a depósito administrativo ou judicial em montante integral\.

07 – Medida judicial em que a pessoa jurídica não é o autor\.

08 – Súmula vinculante aprovada pelo STF ou STJ\.

09 – Decisão judicial oriunda de liminar em mandado de segurança coletivo\.

12 – Decisão judicial não transitada em julgado, a favor da pessoa jurídica \- Exigibilidade suspensa de contribuição\.

13 – Decisão judicial oriunda de liminar em mandado de

segurança \- Exigibilidade suspensa de contribuição\.

14 – Decisão judicial oriunda de liminar em medida cautelar \- Exigibilidade suspensa de contribuição\.

15 – Decisão judicial oriunda de antecipação de tutela \-

Exigibilidade suspensa de contribuição\.

16 \- Decisão judicial vinculada a depósito administrativo ou judicial em montante integral \- Exigibilidade suspensa de contribuição\.

17 – Medida judicial em que a pessoa jurídica não é o autor \- Exigibilidade suspensa de contribuição\.

19 – Decisão judicial oriunda de liminar em mandado de

segurança coletivo \- Exigibilidade suspensa de contribuição\.

99 \- Outros\.

MFS14228

MFS29841

       = = = = = =


# MTZ-Tela_de_Perfil

- **Fonte:** MTZ-Tela_de_Perfil.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 43 KB

---

##### Tela de Cadastro do Perfil – ECD

Módulo: SPED >> ECD – Escrituração Contábil Digital

Menu: Parâmetros >> Perfil

###### DR

###### Nome

__Descrição__

OS3835\-C1

ECD – Tela de Perfil de Geração do Meio Magnético\.

Este documento tem por objetivo especificar as alterações para que o mastersaf possa contemplar o layout da ECD 2013\.

OS4123

ECD – Tela de Perfil de Geração do Meio Magnético\.

Habilitar para geração o Registro I020 – Campos Adicionais\.

OS4745

ECD – Tela de Perfil de Geração do Meio Magnético\.

Criação do Tipo de Livro “S – Escrituração SCP Mantida pelo Sócio Ostensivo” e inclusão dos registros “0035”, “I053” e “J935”\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

__Campo Tipo de Livro__

Campo do tipo lista com as opções:

- G \- Livro Diário \(Completa sem Escrituração Auxiliar\)
- R \- Livro Diário com Escrituração Resumida \(com Escrituração Auxiliar\)
- A \- Livro Diário Auxiliar ao Diário com Escrituração Resumida
- B \- Livro Balancetes Diários e Balanços \(Matriz\)
- Z \- Razão Auxiliar \(Livro Contábil conforme Leiaute definido nos Registros I500 e I555\)
- S \- Escrituração SCP Mantida pelo Sócio Ostensivo

OS3835\-C1

OS4745

__RN02__

__Campo Perfil__

Campo do tipo texto, com a possibilidade de indicação do código e descrição do Perfil\.

OS3835\-C1

__RN03__

__Quadro Definição dos Blocos__

Serão exibidas as opções:

0 Abertura, Identificação e Referências

I Lançamentos Contábeis

J Demonstrações Contábeis

9 Controle e Encerramento do Arquivo Digital

OS3835\-C1

__RN04__

__Quadro Definição dos Registros__

No quadro de definição dos registros serão demonstrados os registros conforme Tipo de Livro e Bloco de Registros indicado pelo usuário\.

__REGISTRO__

__DESCRIÇÃO DOS REGISTROS__

__G__

__R__

__A__

__B__

__Z__

__S__

0000

Abertura do Arquivo Digital e Identificação do empresário ou da sociedade empresária

O

O

O

O

O

O

0001

ABERTURA DO BLOCO 0

O

O

O

O

O

O

[0007](#REGISTRO0007)

Outras inscrições Cadastrais do Empresário ou Sociedade Empresária

O

O

O

O

O

O

[0020](#REGISTRO0020)

ESCRITURAÇÃO CONTÁBIL DESCENTRALIZADA

F

F

F

F

F

F

0035

IDENTIFICAÇÃO DAS SCP

F

F

N

F

N

N

[0150](#REGISTRO0150)

TABELA DE CADASTRO DO PARTICIPANTE

F

F

F

N

F

F

[0180](#REGISTRO0180)

IDENTIFICAÇÃO DO RELACIONAMENTO COM O PARTICIPANTE

F

F

F

N

F

F

[0990](#REGISTRO0990)

ENCERRAMENTO DO BLOCO 0

O

O

O

O

O

O

[I001](#REGISTROI001)

ABERTURA DO BLOCO I

O

O

O

O

O

O

[I010](#REGISTROI010)

IDENTIFICAÇÃO DA ESCRITURAÇÃO CONTÁBIL

O

O

O

O

O

O

[I012](#REGISTROI012)

LIVROS AUXILIARES AO DIÁRIO

N

O

O

F

O

N

[I015](#REGISTROI015)

IDENTIFICAÇÃO DAS CONTAS DA ESCRITURAÇÃO RESUMIDA A QUE SE REFERE A ESCRITURAÇÃO AUXILIAR

N

O

O

F

O

N

[I020](#REGISTROI020)

CAMPOS ADICIONAIS

F

F

N

F

N

F

[I030](#REGISTROI030)

TERMO DE ABERTURA

O

O

O

O

O

O

[I050](#REGISTROI050)

PLANO DE CONTAS

O

O

O

O

F

O

[I051](#REGISTROI051)

PLANO DE CONTAS  REFERENCIAL

F

F

F

F

F

F

[I052](#REGISTROI052)

INDICAÇÃO DOS CÓDIGOS DE AGLUTINAÇÃO

F

F

N

F

N

F

[I05](#REGISTROI052)3

SUBCONTAS CORRELATAS

F

F

N

F

N

F

[I075](#REGISTROI075)

TABELA DE HISTÓRICO PADRONIZADO

F

F

F

N

F

F

[I100](#REGISTROI100)

CENTRO DE CUSTOS

F

F

F

F

F

F

[I150](#REGISTROI050)

SALDOS PERIÓDICOS – IDENTIFICAÇÃO DO PERÍODO

O

O

F

O

F

O

[I151](#REGISTROI151)

ASSINTURA DIGITAL DOS ARQUIVOS QUE CONTÊM AS FICHAS DE LANÇAMENTO UTILIZADOS NO PERÍODO

N

N

N

F

N

N

[I155](#REGISTROI155)

DETALHE DOS SALDOS PERIÓDICOS

O

O

F

O

F

O

[I157](#REGISTROI157)

TRANSFERÊNCIA DE SALDOS DO PLANO DE CONTAS ANTERIOR

F

F

N

F

N

F

[I200](#REGISTROI200)

LANÇAMENTO CONTÁBIL

O

O

O

N

N

O

[I250](#REGISTROI250)

PARTIDAS DO LANÇAMENTO

O

O

O

N

N

O

[I300](#REGISTROI300)

BALANCETES DIÁRIOS – IDENTIFICAÇÃO DA DATA

N

N

N

O

N

N

[I310](#REGISTROI310)

DETALHES DO BALANCETE DIÁRIO

N

N

N

O

N

N

[I350](#REGISTROI350)

SALDOS DAS CONTAS DE RESULTADO ANTES DO ENCERRAMENTO – IDENTIFICAÇÃO DA DATA

F

F

N

F

N

F

[I355](#REGISTROI355)

DETALHES DOS SALDOS DAS CONTAS DE RESULTADO ANTES DO ENCERRAMENTO

F

F

N

F

N

F

[I500](#REGISTROI500)

PARÂMETROS DE IMPRESSÃO E VISUALIZAÇÃO DO LIVRO RAZÃO AUXILIAR COM LEIAUTE PARAMETRIZÁVEL

N

N

N

N

O

N

[I510](#REGISTROI510)

DEFINIÇÃO DE CAMPOS DO LIVRO RAZÃO AUXILIAR COM LEIAUTE PARAMETRIZÁVEL

N

N

N

N

O

N

[I550](#REGISTROI550)

DETALHES DO LIVRO AUXILIAR COM LEIAUTE PARAMETRIZÁVEL

N

N

N

N

O

N

[I555](#REGISTROI555)

TOTAIS NO LIVRO AUXILIAR COM LEIAUTE PARAMETRIZÁVEL

N

N

N

N

F

N

[I990](#REGISTROI990)

ENCERRAMENTO DO BLOCO I

O

O

O

O

O

O

[J001](#REGISTROJ001)

ABERTURA DO BLOCO J

O

O

O

O

O

O

[J005](#REGISTROJ005)

DEMONSTRAÇÕES CONTÁBEIS

F

F

N

F

N

F

[J100](#REGISTROJ100)

BALANÇO PATRIMONIAL

F

F

N

F

N

F

[J150](#REGISTROJ150)

DEMONSTRAÇÃO DO RESULTADO DO EXERCÍCIO

F

F

N

F

N

F

[J200](#REGISTROJ200)

TABELA DE HISTÓRICO DE FATOS CONTÁBEIS QUE MODIFICA A CONTA LUCROS ACUMULADOS OU A CONTA PREJUÍZOS ACUMULADOS OU TODO O PATRIMÔNIO LÍQUIDO

F

F

N

F

N

F

[J210](#REGISTROJ210)

DLPA – demonstração de  lucros ou prejuízos acumulados / DMPL – Demonstração DE mutações do patrimônio

F

F

N

F

N

F

[J215](#REGISTROJ215)

FATO CONTÁBIL QUE ALTERA A CONTA LUCROS ACUMULADOS OU A CONTA PREJUÍZOS ACUMULADOS OU TODO O PATRIMÔNIO

F

F

N

F

N

F

[J800](#REGISTROJ800)

outras informações

F

F

N

F

N

F

[J900](#REGISTROJ900)

TERMO DE ENCERRAMENTO

O

O

O

O

O

O

[J930](#REGISTROJ930)

IDENTIFICAÇÃO DOS signatários da escrituração

O

O

O

O

O

O

[J935](#REGISTROJ930)

IDENTIFICAÇÃO DOS AUDITORES INDEPENDENTES

F

F

F

F

F

F

[J990](#REGISTROJ990)

ENCERRAMENTO DO BLOCO J

O

O

O

O

O

O

[9001](#REGISTRO9001)

ABERTURA DO BLOCO 9

O

O

O

O

O

O

[9900](#REGISTRO9900)

REGISTROS DO ARQUIVO

O

O

O

O

O

O

[9990](#REGISTRO9990)

ENCERRAMENTO DO BLOCO 9

O

O

O

O

O

O

[9999](#REGISTRO9999)

ENCERRAMENTO DO ARQUIVO DIGITAL

O

O

O

O

O

O

Considerar as seguintes regras para seleção dos registros:

- Os registros Indicados como "O" para o Tipo de Livro indicado pelo usuário serão demonstrados já selecionados para geração e não será possível remover a sua seleção\.
- Os registros Indicados como "N" para o Tipo de Livro indicado pelo usuário não serão demonstrados para seleção\.
- Os registros Indicados como "F" para o Tipo de Livro indicado pelo usuário serão demonstrados não selecionados para geração e será possível a sua seleção por parte do usuário\.

OS3835\-C1

OS4123

OS4745


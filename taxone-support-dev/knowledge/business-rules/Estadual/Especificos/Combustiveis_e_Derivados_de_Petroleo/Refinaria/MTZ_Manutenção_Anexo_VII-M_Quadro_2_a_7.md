# MTZ_Manutenção_Anexo_VII-M_Quadro 2 a 7

- **Fonte:** MTZ_Manutenção_Anexo_VII-M_Quadro 2 a 7.docx
- **Modificado:** 2023-05-31
- **Tamanho:** 66 KB

---

THOMSON REUTERS

Manutenção Anexo VII\-M Quadros 2 a 7

Módulo Combustível e Derivados de Petróleo \(SCANC\)

Localização: Movimento de Refinaria 🡪 Manutenção Anexo VII\-M 🡪 Quadros 2 a 7

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS535202

Sumário

[1\.	Regras dos Campos	3](#_Toc494454507)

# <a id="_Toc350763252"></a><a id="_Toc494454507"></a>Regras dos Campos 

__Localização da tela:__ Específicos >> Combustível e Derivados de Petróleo

__                                   __Movimento de Refinaria 🡪 Manutenção Anexo VII\-M 🡪 Quadros 2 a 7

Tabela de Destino: CBT\_ANEXO7M\_QUADR2A7

Definição dos campos a serem apresentados na tela:

__Estabelecimento__:

Habilitado se o usuário entrou sem estabelecimento de login\.

Desabilitado se o estabelecimento foi informado no login do módulo\.

Campo Obrigatório

Gravar campo COD\_ESTAB CBT\_ANEXO7M\_QUADR2A7

__Mês/Ano Referência__:

Habilitado

Campo obrigatório\.

Gravar DAT\_APURACAO CBT\_ANEXO7M\_QUADR2A7 com o último dia do mês/ano informado\.

__UF Destinatária do Anexo VII\-M:__

Habilitado

Campo Obrigatório

Gravar IDENT\_ESTADO\_DESTINO CBT\_ANEXO7M\_QUADR2A7

__Tipo:__

Radium Botton com duas opções:

\( \) Repasse

\( \) Dedução

Default: Repasse

Campo Obrigatório\. Não é gravado na tabela CBT\_ANEXO7M\_QUADR2A7, serve apenas como filtro para a lista a ser apresentada no campo seguinte\.

__Quadro:__

Habilitado

Campo Obrigatório

Lista fixa composta pelos itens, que são apresentados de acordo com a seleção no campo anterior \(Repasse ou Dedução\):

2 \- REPASSE GLOSADO REFERENTE A OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRR

3 – REPASSE GLOSADO REFERENTE A OPERAÇÕES REALIZADAS POR IMPORTADORES

4 \- REPASSE GLOSADO REFERENTE A BIOCOMBUSTÍVEIS

5 – DEDUÇÃO GLOSADA REFERENTE A OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRR

6 \- DEDUÇÃO GLOSADA REFERENTE A OPERAÇÕES REALIZADAS POR IMPORTADORES

7 – DEDUÇÃO GLOSADA REFERENTE A BIOCOMBUSTÍVEIS

Gravar os campos COD\_TAG CBT\_ANEXO7M\_QUADR2A7 conforme regra abaixo:

__Item__

__COD\_TAG__

2

A7MQ2

3

A7MQ3

4

A7MQ4

5

A7MQ5

6

A7MQ6

7

A7MQ7

__Pessoa Fís/Jur:__

Habilitado

Campo Obrigatório

Gravar IDENT\_FIS\_JUR CBT\_ANEXO7M\_QUADR2A7

__UF do Quadro:__

Habilitado\.

Campo Obrigatório

Gravar IDENT\_ESTADO\_QUAD CBT\_ANEXO7M\_QUADR2A7

Os campos __Pessoa Fís/Jur__ e __UF do Quadro __variam de acordo com o item selecionado no campo Quadro:

__Item \- Quadro__

__Título Pessoa Fís/Jur__

__Título UF do Quadro__

__Regra do Campo UF do Quadro__

2

Distribuidora/TRR

UF Distribuidora/TRR

Habilitado e trazer como default a UF da Pessoa Fis/Jur \(Cadastro da X04\)

3

Importadora

UF Importadora

Habilitado e trazer como default a UF da Pessoa Fis/Jur \(Cadastro da X04\)

4

Distribuidora/TRR

UF Distribuidora/TRR

Habilitado e trazer como default a UF da Pessoa Fis/Jur \(Cadastro da X04\)

5

Distribuidora/TRR

UF Destinatária

Habilitar

6

Importadora

UF Destinatária

Habilitar

7

Distribuidora/TRR

UF Destinatária

Habilitar

__Vlr ICMS__

Habilitado

Gravar VLR\_ICMS\_ST CBT\_ANEXO7M\_QUADR2A7

__No Processo__

Desabilitado

Gravar NUM\_PROCESSO CBT\_ANEXO7M\_QUADR2A7

__Ind Dig Calc:__

Não apresentar na tela\. 

Gravar:

Gravar:

1 – inserido via tela de manutenção

2 – inserido via geração do Anexo VII\-M

3 \- inserido via geração do Anexo VII\-M e atualizado pela tela de manutenção

__Usuário __

Não apresentar na tela\. 

Gravar o usuário de login da aplicação\.

__Tela__

__PL usado pela tela__

__Manutenção Anexo VII\-M __

             Quadro 1      

	Quadros 2 a 7 

Saf\_atualiza\_anexo\_7M\_q1 da Pkg\_Cbt\_Anexo7\_fproc


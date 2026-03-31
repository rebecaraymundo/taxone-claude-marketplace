# MTZ_ECD_Versao_Leiaute_300

- **Fonte:** MTZ_ECD_Versao_Leiaute_300.docx
- **Modificado:** 2021-06-04
- **Tamanho:** 70 KB

---

THOMSON REUTERS

ECD

Atualização da Geração do Arquivo para atender ao Leiaute 3\.00

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4745

Marcos G\. de Paula

Atualização das Informações do arquivo da ECD para atender à versão 3\.00 do Leiaute da ECD\.

CH22230/2015

Marcos G\. de Paula

Atualização da regra de geração do campo 03 – COD\_CNT\_CORR do registro I053 para geração do cadastro correspondente\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral__

Este documento tem como objetivo demonstrar as alterações da versão 3\.00 do leiaute da ECD em relação à versão 2\.00\. Este novo leiaute será obrigatório a partir do ano\-calendário 2014\.

Todos os registros deverão ser mantidos conforme layout anterior, incluindo as alterações e criação dos novos registros que estarão definidos nas regras de negócios descritas neste documento, documento de requisito e documentos matriz relacionados na alteração da versão\.

OS4745

__Alterações Registro 0000__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN0000\-17

__Registro 0000 – Campo 17 – IND\_GRANDE\_PORTE__

Este campo já existia na versão 2\.00 e na versão 3\.00 o seu nome foi alterado\. Passou de IND\_EMP\_GRD\_PRT para IND\_GRANDE\_PORTE\.

Sua origem era o campo “Empresa de Grande Porte” na tela de Dados Iniciais \(Módulo ECD / Menu Parâmetros\)\. Esta origem permanece, mas o nome do campo em tela foi alterado para “Empresa Sujeita a Auditoria Independente”\. A regra de geração permanece a mesma: quando selecionado gera conteúdo “1” e quando desmarcado, gera conteúdo “0”\.

OS4745

RN0000\-18

__Registro 0000 – Campo 18 – TIP\_ECD__

Este campo existe a partir da versão 3\.00\. Será gerado com o conteúdo do campo “Tipo da ECD” da tela de Dados Iniciais \(Módulo ECD / Menu Parâmetros\)\.

OS4745

RN0000\-19

__Registro 0000 – Campo 19 – COD\_SCP__

Este campo existe a partir da versão 3\.00\. Será gerado com o conteúdo do campo “Código da SCP” da tabela SAFX2057 – Cadastro da SCP, do estabelecimento que está gerando o arquivo quando o Tipo da ECD da tela de Dados Iniciais for igual a “2 – ECD da SCP”\.

OS4745

__Novo Registro 0035 – Identificação das SCPs__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN0035\-00

__Registro 0035 – Regra Geral__

__Origem das informações__: SAFX2057 – Cadastro da SCP

__Regra de Seleção__: Serão considerados os registros da tabela SAFX2057 – Cadastro da SCP do estabelecimento centralizador e seus centralizados, quando no cadastro de Dados Iniciais \(Módulo ECD / Menu Parâmetros\) do estabelecimento o campo Tipo da ECD for igual a “1 – ECD da Empresa participante de SCP como Sócio Ostensivo” e que tenham a Data de Validade Inicial menor ou igual a data final parametrizada para geração do arquivo E a Data de Validade Final do Cadastro da SCP \(SAFX2057\) não preenchida ou maior ou igual a Data Inicial de geração\. Caso o Tipo da ECD seja diferente de “1 – ECD da Empresa participante de SCP como Sócio Ostensivo”, não será gerado\.

Caso exista para mais de um estabelecimento o mesmo Código de SCP válido \(sem data final preenchida\), será gerado apenas um registro 0035, evitando assim duplicidade de Código da SCP\.

__Campo\-chave__: COD\_SCP

__Registro pai / Nível hierárquico__: 0000 / Nível 2

__Ocorrência__: vários por arquivo

OS4745

RN0035\-01

__Registro 0035 – Campo 01 – REG__

Informação fixa “0035”\.

OS4745

RN0035\-02

__Registro 0035 – Campo 02 – COD\_SCP__

Será gerado com o Código da SCP parametrizado na aba Identificação da SCP\.

OS4745

RN0035\-03

__Registro 0035 – Campo 03 – NOME\_SCP__

Será gerado com o Nome da SCP parametrizado na aba Identificação da SCP\.

OS4745

__Alterações Registro I010__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI010\-02

__Registro I010 – Campo 02 – IND\_ESC__

Deve considerar também o novo Tipo de Livro \(S – Escrituração SCP Mantida pelo Sócio Ostensivo\) criado quando indicado na tela de geração do Meio Magnético\.

OS4745

RNI010\-03

__Registro I010 – Campo 03 – COD\_VER\_LC__

Para a versão 3\.00, será gerado com o código “3\.00”\.

OS4745

__Alterações Registro I030__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI030\-13

__Registro I030 – Campo 13 – NOME\_AUDITOR__

Este campo não será mais gerado a partir da versão 3\.00\.

OS4745

RNI030\-14

__Registro I010 – Campo 14 – COD\_CVM\_AUDITOR__

Este campo não será mais gerado a partir da versão 3\.00\.

OS4745

__Alterações Registro I051__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI051\-02

__Registro I051 – Campo 02 – COD\_PLAN\_REF__

O nome deste campo foi alterado de COD\_ENT\_REF para COD\_PLAN\_REF\. A partir da versão 3\.00 este registro será gerado apenas quando o Código da Entidade for igual a “1 \- PJ em Geral”, ”2 \- PJ em Geral \- Lucro Presumido”, “3 – Financeiras”, “4 – Seguradoras”, “5 \- Imunes e Isentas em Geral”, “6 \- Financeiras \- Imunes e Isentas”, “7 \- Seguradoras \- Imunes e Isentas”, “8 \- Entidades Fechadas de Previdência Complementar” ou “9 \- Partidos Políticos”\.

Caso o usuário não tenha realizado parametrização para uma destas entidades indicadas acima em Dados Iniciais e/ou Plano de Contas Referencial X Plano de Contas Empresa e esteja gerando a versão 3\.00 do Leiaute, será demonstrada uma mensagem no log: “A partir da versão 3\.00 do leiaute não serão válidas as Contas Referenciais de entidade 00\-SUSEP ou 10\-Secretaria da Receita Federal ou 20\- Banco Central do Brasil \(COSIF\)”\.

OS4745

__Novo Registro I053 – Subcontas Correlatas__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI053\-00

__Registro I053 – Regra Geral__

__Origem das informações__: Tela de Subcontas Correlatas \(Módulo ECD / Menu Manutenção\)

__Regra de Seleção__: Este registro será gerado sempre que, na tela de Subcontas Correlatas existir algum registro associando para a conta contábil informada no I050 as subcontas correlatas\.

__Campo\-chave__: COD\_CNT\_CORR

__Registro pai / Nível hierárquico__: I050 / Nível 4

__Ocorrência__: vários por plano de Contas

OS4745

RNI053\-01

__Registro I053 – Campo 01 – REG__

Informação fixa “I053”\.

OS4745

RNI053\-02

__Registro I053 – Campo 02 – COD\_IDT__

Será gerado com o conteúdo do campo Gr\. Conta\-Subconta da tela de Subconta Correlata\.

OS4745

RNI053\-03

__Registro I053 – Campo 03 – COD\_CNT\_CORR__

Será gerado com o conteúdo do campo Subconta Correlata da tela de Subconta Correlata\.

\[CH22230/2015\] Para o código de conta contábil informado neste campo também deve ser gerado o cadastro correspondente o registro I050\.

OS4745

22230/2015

RNI053\-04

__Registro I053 – Campo 04 – NAT\_SUB\_CNT__

Será gerado com o conteúdo do campo Natureza da Subconta da tela de Subconta Correlata\.

OS4745

__Alterações Registro J930__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNJ930\-08

__Registro J930 – Campo 08 – FONE__

O tamanho do campo foi alterado de 11 para 14 posições\. Ele deve ser gerado com base no cadastro do responsável indicado na aba Signatários da tela de Dados Iniciais \(Módulo ECD / Menu Parâmetros\) considerando a concatenação das 5 últimas posições do campo DDD \+ as 9 posições do campo Telefone\.

OS4745

__Novo Registro J935 – Identificação dos Auditores Independentes__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNJ935\-00

__Registro J935 – Regra Geral__

__Origem das informações__: Aba Auditores Independentes / Dados Iniciais

__Regra de Seleção__: Serão considerados os registros da aba de Auditores Independentes da tela de Dados Iniciais \(Módulo ECD / Menu Parâmetros / Aba Auditores Independentes\)\.

__Campo\-chave__: COD\_CVM\_AUDITOR

__Registro pai / Nível hierárquico__: J900 / Nível 3

__Ocorrência__: vários por arquivo

OS4745

RNJ935\-01

__Registro J935 – Campo 01 – REG__

Informação fixa “J935”\.

OS4745

RNJ935\-02

__Registro J935 – Campo 02 – NOME\_AUDITOR__

Será gerado com o conteúdo do campo Nome do Auditor da aba Auditores Independentes\.

OS4745

RNJ935\-03

__Registro J935 – Campo 03 – COD\_CVM\_AUDITOR__

Será gerado com o conteúdo do campo Registro do Auditor na CVM da aba Auditores Independentes\.

OS4745

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


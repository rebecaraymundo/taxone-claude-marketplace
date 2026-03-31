# Tela_Informacoes_ECF

- **Fonte:** Tela_Informacoes_ECF.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 61 KB

---

THOMSON REUTERS

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a><a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>Tela Informações ECF

ECF \- Escrituração Contábil Fiscal \(DW\)

##### DOCUMENTO DE REQUISITO

__Data__

__MFS__

__Descrição__

__Autor__

04/10/2017

MFS\-12691

Criação do Documento

Alessandra Cristina Navatta

28/11/2017

MFS\-14482

Ajustes em regras \(Teste de tela\)

Alessandra Cristina Navatta

23/03/2018

MFS\-17490

Inclusão da aba LALUR e LACS \(parâmetros referentes a Compensação de Prejuízos e de Base Negativa\)

Alessandra Cristina Navatta

23/05/2018

1. MFS\- [18703](http://ent.jira.int.thomsonreuters.com/browse/MFS-18703)

Inclusão na aba LALUR e LACS \(Lançamento da Parte B Automático para Incentivo PAT\)\.

Validação no botão excluir, quando existir cálculo do PAT \(realizado pelo processamento em lote\)\.

Inclusão de regra para edição do botão Versão\.

Alessandra Cristina Navatta

13/08/2018

MFS\-20274

Inclusão do parâmetro referente a DEREX na aba Parâmetros Complementares para a geração dos dados do bloco V a partir da versão 4\.00\.

Validação no campo Versão

Alessandra Cristina Navatta

Sumário

[1 INTRODUÇÃO	3](#_Toc524695747)

[2 DOCUMENTOS DE REFERÊNCIA	3](#_Toc524695748)

[3 TELA/MODAIS	3](#_Toc524695749)

[3\.1 Pesquisa de Registros	3](#_Toc524695750)

[3\.2	Regras dos Campos Tela Principal	4](#_Toc524695751)

# <a id="_Toc380499982"></a><a id="_Toc392000488"></a><a id="_Toc392076129"></a><a id="_Toc392083096"></a><a id="_Toc524695747"></a>1 INTRODUÇÃO

Objetivo desta especificação é criar a tela de Informações ECF\.

# <a id="_Toc380499983"></a><a id="_Toc392000489"></a><a id="_Toc392076130"></a><a id="_Toc392083097"></a><a id="_Toc524695748"></a>2 DOCUMENTOS DE REFERÊNCIA

Mensagens\_Sistema\_DWECF\.xlsx

Regras\_Gerais\_DWECF\.docx

# <a id="_Toc524695749"></a>3 TELA/MODAIS

## <a id="_Toc524695750"></a>3\.1 Pesquisa de Registros

__Localização da tela:__ 

ECF – Escrituração Contábil Fiscal >> Parâmetros >> Critérios de Apuração

__Título da tela: __Informações ECF

 

__Campo__

__Tipo__

__Regra__

Estabelecimento

LOV

\(Tipo – Código – Descrição\)

Permite que o usuário busque o registro pelo Código do Estabelecimento\.

Exercício

Texto

\(AAAA\)

O usuário poderá informar o exercício\. 

Data Inicial

Data

DD/MM/AAAA

O usuário poderá informar a data inicial da Informação ECF\.

Versão

Lista

Aplicar a RNG00004 \- Versão de Layout

## <a id="_Toc350763252"></a><a id="_Toc360443175"></a><a id="_Toc376978350"></a><a id="_Toc524695751"></a>Regras dos Campos Tela Principal

__Localização da tela:__ 

ECF – Escrituração Contábil Fiscal >> Parâmetros >> Critérios de Apuração

__Título da tela: __Informações ECF

__Considerações:__ Nesta tela é permitido consulta, inclusão, alteração e exclusão de registros\.

Aplicar RNG00010 – Campo Obrigatório	

As regras destacadas em amarelo \(e com fonte vermelha\), não serão implementadas neste momento\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS__

__Cabeçalho\(\*\)  
Título: \(\*\)__

__Dados Gerais __

__ __

Estabelecimento

LOV

S

N

Tipo – Código – Descrição

Permite que o usuário selecione o estabelecimento, que possui acesso e está licenciado para o módulo\.  
  
__Tratamentos:  
  
__Recuperar os Estabelecimentos Centralizador e Descentralizados de acordo com a Central de Escrituração de Obrigações Federais\.  
  
Campos de Pesquisa: Código e Descrição

MFS\-12691

Exercício

Texto

S

N

AAAA

Permite inserir o exercício da escrituração\.  
  
Tratamento:  
  
Permitir exercício a partir de 2014\.  
Caso o usuário informe um exercício anterior a 2014, exibir a mensagem para o usuário: DW00027

MFS\-12691

Data Inicial

Texto

S

N

DD/MM/AAAA

Permite que o usuário informe a data de inicial de vigência da parametrização\.  
  
__Tratamento: __  
  
  
Aplicar a <<RNG00008 \- Data Inicial x Estabelecimento >>  
Aplicar a <<RNG00009 \- Data Inicial x Exercício >>  
  
\- A data deve ser a partir de 01/01/2014\. Caso o usuário informe uma data inicial anterior a 01/01/ 2014, exibir a mensagem para o usuário: DW00028\.

MFS\-12691

Versão

Lista

S

N

Código – Descrição

Permite que o usuário selecione a Versão do Layout que será considerada para o processamento dos registros\.  
  
__Valores Válidos: __  
Conteúdo da RNG00004 \- Versão de Layout  
  
__Tratamentos:__  
Aplicar RNG00003 \- Versão da Escrituração  
  
__Validações Adicionais:__  
  
\- Recuperar as versões cuja Data Inicial e Final compreendam “DATA\_INICIAL” da Informação ECF\. Sabendo que a Data Final pode estar nula\.  
Se o resultado da recuperação trouxer mais de uma versão, apresentar a de Data Inicial mais atual\.  
Desabilitar o campo caso o resultado traga uma versão\.  
Habilitar o campo caso o resultado traga mais de uma versão\.  
  
Na edição do registro, este campo deve estar não editável:   
\- Se existir uma abertura de apuração criada para esta Informação ECF,   
\- Se existir informações dos blocos Q, X \(X280, X291, X292, X300 ou X310\),Y , W e V para esta escrituração \(estabelecimento, exercício, data inicial e versão\)\.  


MFS\-12691

MFS\-18703

MFS\-20274

Associação Tabela Referencial com o Plano Empresa

LOV

N

S

Código – Descrição

Permite que o usuário selecione uma associação de Tabela Referencial com o Plano Empresa \.  
  
Tratamento:  
Recuperar as associações da Tela de Associação de Tabela Referencial com o Plano Empresa, vigente na data inicial deste cadastro, cuja a versão do Plano Referencial usado na parametrização, seja igual a versão digitada na tela de Informações ECF\.  
  
Este campo só deve estar disponível se preenchida uma Versão\.  
  
Campos de Pesquisa: Código e Descrição  
  
Na edição do registro, este campo deve estar não editável:  
\- Se existir uma abertura de apuração criada para esta Informação ECF com status diferente de Apuração em Aberto\.

MFS\-12691

Associação Tabela Dinâmica com o Plano Empresa

LOV

N

S

Código – Descrição

Permite que o usuário selecione uma associação de Tabela Dinâmica com o Plano Empresa \.  
  
Tratamento:  
Recuperar as associações da Tela de Associação de Tabela Dinâmica com o Plano Empresa, vigente na data inicial deste cadastro,  cuja a versão da Tabela Dinâmica usada na parametrização, seja igual a versão digitada na tela de Informações ECF\.  
  
Este campo só deve estar disponível se preenchida uma Versão\.  
  
Campos de Pesquisa: Código e Descrição  
  
Na edição do registro, este campo deve estar não editável:  
\- Se existir uma abertura de apuração criada para esta Informação ECF com status diferente de Apuração em Aberto\.

MFS\-12691

 

Recuperação de Valores

LOV

N

S

Código – Descrição

Permite que o usuário selecione uma parametrização de recuperação de valores\.  
  
Tratamento:  
Recuperar as parametrizações vigentes na data inicial deste cadastro\.  
  
Este campo só deve estar disponível se preenchida a data inicial estiver preenchida\.  
  
Campos de Pesquisa: Código e Descrição  
  
Na edição do registro, este campo deve estar não editável:  
\- Se existir uma abertura de apuração criada para esta Informação ECF com status diferente de Apuração em Aberto\.

MFS\-14674

Perfil

LOV

N

S

Código – Descrição

Permite que o usuário selecione um perfil para geração do arquivo texto\.  
  
__Tratamento:__  
Recuperar Dados da Tela de Perfil de Geração de mesma Versão da Tela de Informações ECF\.  
  
Este campo só deve estar disponível se preenchida uma Versão\.  
  
Campos de Pesquisa: Código e Descrição

MFS\-12691

__Aba \(\*\)  
 Parâmetros Gerais__

__ __

__ __

__Título: \(\*\)__

__PARÂMETROS TRIBUTÁRIOS__

__ __

Tipo da ECF

Lista

S

S

Código – Descrição

Permite que o usuário informe o tipo da ECF cadastrada para o estabelecimento\.

Lista – Valores Válidos:

0 – ECF de empresa não participante de SCP como sócio ostensivo  
1 – ECF de empresa participante de SCP como sócio ostensivo  
2 – ECF da SCP

MFS\-12691

Natureza Jurídica

Lov

S

S

Código 

Permite que o usuário informe o código da natureza jurídica\.   
  
__Tratamentos:  
  
__Recuperar as informações da TACES49 e desconsiderar os códigos descritos na coluna de observação, deste documento, pois são códigos que caíram em desuso, originários da DIPJ\.

MFS\-12691

Descrição da Natureza Jurídica 

Texto

S

N

Descrição

Exibe a Descrição da Natureza Jurídica selecionada através da lov\.

MFS\-12691

Forma de Tributação

Lista

S

S

Descrição

Permite que o usuário informe a forma de tributação cadastrada para a empresa\.  
  
Aplicar a regra abaixo:  
  
Lista – Valores Válidos:   
  
Lucro Real, Lucro Presumido, Lucro Arbitrado\.  
Imune de IRPJ   
Isento do IRPJ   


__Tratamentos:__  
Na edição do registro, este campo deve estar não editável:  
\- Se existir uma abertura de apuração criada para esta Informação ECF   
Na edição, se o valor do campo for igual à:  
Imune de IRPJ ou Isento do IRPJ apresentar a mensagem DW00034\.  


MFS\-12691

Apuração

Lista

N

S

Default:  
Desabilitado

Permite que o usuário informe a forma de apuração cadastrada para a empresa\.  
  
Aplicar as regras abaixo:  
  
Lista – Valores Válidos:   
Anual;  
Trimestral;  
  
__Tratamentos:__  
\-Este campo só deve ficar habilitado e ser obrigatório se o campo Forma de tributação estiver preenchido com a opção igual a ‘Lucro Real, Lucro Presumido, Lucro Arbitrado’\.  
  
\-Se o campo Forma de tributação for igual a ‘ Lucro Real, Lucro Presumido, Lucro Arbitrado’, o valor Default para o campo é Anual\. Para os demais valores \(Imune de IRPJ ou Isento de IRPJ\), este campo não deve ficar habilitado\.  
  
Na edição do registro, este campo deve estar não editável:  
\- Se existir uma abertura de apuração criada para esta Informação ECF\.

MFS\-12691

Tipo de Entidade

Lista

N

S

Default:  
Desabilitado  
Formato: Descrição

Permite que o usuário informe o tipo de entidade cadastrado para a empresa\.  
  
Aplicar as regras abaixo:  
Lista – Valores Válidos:  
   
01 – Assistência Social   
02 – Educacional   
03 – Sindicato de Trabalhadores   
04 – Associação Civil   
05 – Cultural   
06 – Entidade Fechada de Previdência Complementar   
07 – Filantrópica   
08 – Sindicato   
09 – Recreativa   
10 – Científica   
11 – Associação de Poupança e Empréstimo   
12 – Entidade Aberta de Previdência Complementar \(Sem Fins Lucrativos\)   
13 – Fifa e Entidades Relacionadas  
14 – CIO e Entidades Relacionadas  
15 – Partidos Políticos  
99 – Outras\.  
  
Obs\. Os códigos devem ser exibidos somente na geração do arquivo ECF\. Na tela deve ser exibida somente a descrição do campo\.   
  
Esse campo só deve ficar habilitado se o campo “Forma de Tributação” estiver preenchido com as opções ‘Imune de IRPJ’ ou ‘Isento de IRPJ’, este campo é de preenchimento obrigatório\.  
Neste caso, aplicar a regra de negócio geral <<RNG00010 – Campo Obrigatório>>\.  
  
Se “Forma de Tributação” estiver preenchido com a opção ‘Lucro Real, Lucro Presumido, Lucro Arbitrado’, este campo não deve ser preenchido e não deve ficar habilitado na tela\.

MFS\-12691

Qualificação da Pessoa Jurídica

Lista

N

S

 

Permite que o usuário informe a qualificação da Pessoa Jurídica cadastrada para a empresa\.  
  
Aplicar a regra abaixo:  
  
Lista – Valores Válidos:   
  
PJ em Geral  
PJ Componente do Sistema Financeiro  
Sociedades Seguradoras, de Capitalização ou Entidade Aberta de  
Previdência Complementar  
  
\-Este campo só deve ficar habilitado e ser obrigatório se o campo Forma de tributação estiver preenchido  com a opção igual a ‘Lucro Real, Lucro Presumido, Lucro Arbitrado’\.  
  
Neste caso, aplicar a regra de negócio geral <<RNG00010 \- Campo Obrigatório >>\.  
  
Na edição do registro, este campo deve estar não editável:  
\- Se existir uma abertura de apuração criada para esta Informação ECF com status diferente de Apuração em Aberto\.  
  


MFS\-12691

Apuração do IRPJ 

Lista

N

S

Default:  
Desabilitado

Permite que o usuário informe a forma de apuração das empresas que estão Imune ou Isenta de IRPJ\.  
  
Lista – Valores Válidos:  
Anual  
Trimestral  
Desobrigada  
__  
Tratamentos:__  
  
Esse campo só deve ficar habilitado se o campo “Forma de Tributação” estiver preenchido com as opções ‘Imune de IRPJ’ ou ‘Isento de IRPJ’, este campo é de preenchimento obrigatório\.  
  
Se “Forma de Tributação” estiver preenchido com a opção ‘Lucro Real, Lucro Presumido, Lucro Arbitrado’ este campo não deve ser preenchido e não deve ficar habilitado na tela\.  
  
Se o campo “Apuração da CSLL” estiver preenchido com a opção “Anual”, não deve ser exibida a opção “Trimestral” nesse campo\.  
  
Se o campo “Apuração da CSLL” estiver preenchido com a opção “Trimestral”, não deve ser exibida a opção “Anual” nesse campo\.  
  
Se existir alguma abertura da apuração correspondente ao registro selecionado, com status = ‘Calculo Realizado‘, este campo deve estar não editável, caso contrário o campo deve ser editável\. Se este campo for alterado, exibir a mensagem DW00035\.

MFS\-12691

Apuração da CSLL

Lista

N

S

Default:  
Desabilitado

Permite que o usuário informe o tipo de Apuração da CSLL, quando a empresa for Imune ou Isenta de IRPJ\.  
  
Lista – Valores Válidos:  
Anual  
Trimestral  
Desobrigada  
  
Tratamentos:   
Esse campo só deve ficar habilitado se o campo “Forma de Tributação” estiver preenchido com as opções  ‘Imune de IRPJ’ ou ‘Isento de IRPJ’, este campo é de preenchimento obrigatório\.  
  
Se “Forma de Tributação” estiver preenchido com a opção ‘Lucro Real, Lucro Presumido, Lucro Arbitrado’ este campo não deve ser preenchido e não deve ficar habilitado na tela\.  
  
Se o campo “Apuração do IRPJ” estiver preenchido com a opção “Anual”, não deve ser exibida a opção “Trimestral” e “Desobrigada” nesse campo e preencher automaticamente com “Anual”\.  
  
Se o campo “Apuração do IRPJ” estiver preenchido com a opção “Trimestral”, não deve ser exibida a opção “Anual” e “Desobrigada” nesse campo e preencher automaticamente com “Trimestral”\.  
  
  
Se o campo “Apuração do IRPJ” estiver preenchido com a opção “Desobrigada”, deve ser exibida as opções “Anual“, “Trimestral” e “Desobrigada” nesse campo\.  
  
Se existir alguma abertura da apuração correspondente ao registro selecionado, com status = ‘Calculo Realizado’, este campo deve estar não editável , caso contrário o campo deve ser editável\. Se este campo for alterado, exibir a mensagem DW00032\.

MFS\-12691

Critério de Reconhecimento de Receitas 

Lista

S

S

__ __

Permite que o usuário informe o critério de reconhecimento de receitas para empresas tributadas pelo Lucro Presumido\.  
  
Lista – Valores Válidos:   
Não se aplica  
Regime de Caixa  
Regime de Competência   
  
  
Tratamento: Este campo só deve ser habilitado se o campo Forma de Tributação = Lucro Real, Lucro Presumido, Lucro Arbitrado\.  
  
Este campo só deve ser exibido a partir da Versão 3\.00

MFS\-12691

Escrituração

Lista

S

S

 

Permite que o usuário informe a escrituração cadastrada para a empresa\.  
  
Lista – Valores Válidos:   
\-Não se aplica  
\-Livro Caixa ou Sem Escrituração   
\-Contábil   
  
__Tratamentos:__  
  
Até a versão 2\.00:  
  
Se a forma de tributação for ‘Imune de IRPJ’ ou ‘Isento de IRPJ’, apenas as opções ‘Livro Caixa ou Sem Escrituração’ e ‘Contábil, devem ficar disponíveis’\.  
  
Se “Forma de Tributação” estiver preenchido com a opção ‘Lucro Real, Lucro Presumido, Lucro Arbitrado’ todas as opções devem ficar disponíveis\.  
Não será permitida alteração deste campo para a opção ‘Não se aplica’, quando existir uma abertura de apuração com Forma de Tributação igual a Lucro Presumido\. Neste caso, exibir a DW00033\.  
  
A partir da versão 3\.00:  
  
Se a forma de tributação for ‘Imune de IRPJ’ ou ‘Isento de IRPJ’, apenas as opções ‘Livro Caixa ou Sem Escrituração’ e ‘Contábil, devem ficar disponíveis’ para serem selecionadas\.  
Se “Forma de Tributação” estiver preenchida com a opção ‘Lucro Real, Lucro Presumido, Lucro Arbitrado’ e campo Critério de Reconhecimento de Receitas igual a ‘Regime de Competência’, apresentar já preenchida e sem permitir alteração a opção ‘Contábil’\. Caso o campo Critério de Reconhecimento de Receitas igual a ‘Não se aplica’, apresentar já preenchida a opção ‘Não se aplica’ sem permitir alteração da opção\.

MFS\-12691

__  
Título: \(\*\)__

__SIGNATÁRIOS __

__ __

Título : \(\*\)

SIGNATÁRIO CONTADOR

Signatário\(\*\)

LOV

S

S

 Código – CPF – Nome do Responsável

Permite que o usuário visualize o assinante do signatário \(Contador\) para a geração da ECF, selecionada através do LOV\.  


Tratamento:  
Recuperar dados da tabela de Responsável\.

Apresentar na lista o registro mais atual de cada CPF sem duplicidade   
  
Campos de Pesquisa: Código, Nome e CPF\.

MFS\-12691

Qualificação do Assinante

Lista

S

N

Desabilitado

Permite que o usuário visualize a qualificação do assinante do signatário \(Contador\) para a geração da ECF\.  
  
Valor Válido:  
\-Contador/Contabilista

MFS\-12691

Inscrição do Contabilista 

Texto

S

N

 

Permite que o usuário informe o número de inscrição do contabilista no Conselho Regional de Contabilidade\.

MFS\-12691

Título\(\*\)

SIGNATÁRIO OUTROS

Signatário\(\*\)

LOV

S

N

Código – CPF – Nome do Responsável 

Permite que o usuário visualize o assinante do signatário \(Outros\) para a geração da ECF, selecionada através do LOV\.  
  
Tratamento:  
Recuperar Dados da Tabela de Responsável\.  
  
Apresentar na lista o registro mais atual de cada CNPJ e CPF sem duplicidade   
  
  
Campos de Pesquisa: Código, Nome e CPF

MFS\-12691

Qualificação do Assinante

Lista

S

S

 

Permite que o usuário selecione a qualificação do assinante do signatário  \(outro\) para a geração da ECF\.  
  
Lista de Valores Válidos:  
  
• Diretor  
• Conselheiro de Administração  
• Administrador  
• Administrador do Grupo  
• Administrador de Sociedade Filiada  
• Administrador Judicial – Pessoa Física  
• Administrador Judicial – Pessoa Jurídica – Profissional Responsável  
• Administrador Judicial/Gestor  
• Gestor Judicial  
• Procurador  
• Inventariante  
• Liquidante  
• Interventor  
• Titular Pessoa Física  
• Empresário  
• Outros  
  
Obs\. As informações acima foram retiradas da tabela “SPEDECF\_LOCAL$SPEDECF\_QUALIF\_ASSINANTE$6$522” \(Documento Matriz\\SPED\\ECF – Escrituracao Contabil Fiscal\\Tabelas de Referencia\\Qualificacao\_Assinante\), disponibilizada pela Receita \(diretório do PVA\)

MFS\-12691

__  
Título: \(\*\)__

__ Lançamento de Encerramento__

__ __

Título\(\*\)

LANÇAMENTO DE ENCERRAMENTO – INFORMAÇÕES PARA A CRIAÇÃO DO LANÇAMENTO DE ENCERRAMENTO DO BLOCO K

Conta Contábil

LOV

\-

\-

Desabilitado

Código – Descrição – Data de Inicio

Permite que o usuário informe a conta contábil que será utilizada na criação do lançamento de encerramento  
  
Tratamentos:  
\-Recuperar as contas contábeis que estão indicadas na Associação \(campo Associação da Tabela Referencial com o Plano Empresa\)  
  
\-Esse campo só deve ficar habilitado, se os campos Estabelecimento, Exercício e Data Inicial estiverem preenchidos\.  
  
\-Recuperar as contas contábeis associadas às contas referenciais da tabela de associação do plano referencial com plano empresa, cuja natureza = ‘7’ \(Patrimônio Líquido\) e de mesma Versão da tela de Informações ECF\.  
  
Campos de Pesquisa: Código e Descrição\.

MFS\-12691

 Cód\. Do Centro de Custo

LOV

N

N

Desabilitado

Código – Descrição – Data de Inicio

Permite que o usuário informe o centro de custo que será utilizado na criação do lançamento de encerramento  
  
Tratamentos:  
\-Recuperar os centros de custo que estão associados na conta contábil selecionada\.  
  
\-Esse campo só deve ficar habilitado, se o campo Conta Contábil estiver preenchido\.  
Campos de Pesquisa: Código e Descrição\.

MFS\-12691

__Aba \(\*\) __

__LALUR e LACS__

__INFORMAÇÕES PARA A CRIAÇÃO DO LANÇAMENTO NO EXERCÍCIO – CONTAS DA PARTE B__

GRUPO

LOV

\-

\-

Código – Descrição

Permite que o usuário indique o grupo de contas que será usado\.

Tratamentos:

Recuperar os grupos de contas vigentes na data inicial da escrituração\.

Campos de Pesquisa: Código e Descrição\.

MFS\-17490

__Título\(\*\)__

__LANÇAMENTO DE PREJUÍZO__

__Título\(\*\)__

ATIVIDADE GERAL

Conta da Parte B

LOV

\-

\-

Código – Descrição

Permite que o usuário informe a conta da parte B que será utilizada na criação do lançamento de prejuízo do exercício\.

__Tratamentos:__

Recuperar as contas da parte B que estão cadastradas no grupo selecionado e que estão vigentes na data inicial da escrituração\.

Campos de Pesquisa: Código e Descrição\.

MFS\-17490

__Título\(\*\)__

ATIVIDADE RURAL

Conta da Parte B

LOV

\-

\-

Código – Descrição

Permite que o usuário informe a conta da parte B que será utilizada na criação do lançamento de prejuízo do exercício

__Tratamentos:__

Recuperar as contas da parte B que estão cadastradas no grupo selecionado e que estão vigentes na data inicial da escrituração\.

Campos de Pesquisa: Código e Descrição\.

MFS\-17490

__LANÇAMENTO DE BASE NEGATIVA __

__Título\(\*\)__

ATIVIDADE GERAL

Conta da Parte B

LOV

\-

\-

Código – Descrição

Permite que o usuário informe a conta da parte B que será utilizada na criação do lançamento de base negativa do exercício

__Tratamentos:__

Recuperar as contas da parte B que estão cadastradas no grupo selecionado e que estão vigentes na data inicial da escrituração\.

Campos de Pesquisa: Código e Descrição\.

MFS\-17490

__Título\(\*\)__

ATIVIDADE RURAL

Conta da Parte B

LOV

\-

\-

Código – Descrição

Permite que o usuário informe a conta da parte B que será utilizada na criação do lançamento de base negativa do exercício\.

__Tratamentos:__

Recuperar as contas da parte B que estão cadastradas no grupo selecionado e que estão vigentes na data inicial da escrituração\.

Campos de Pesquisa: Código e Descrição\.

MFS\-17490

Criar Ajustes Mensalmente de Compensação de Prejuízos e de Base Negativa de Períodos Anteriores

Checkbox

N

S

Desmarcado

Permite o usuário parametrizar que a compensação de prejuízos e de base negativa de períodos anteriores seja realizada de forma mensal\.

__Tratamento: __

\- Se a Apuração for Trimestral o campo deve ser exibido desabilitado\.

Assim, somente será habilitado quando a Apuração for Anual\. 

\- Ao ser selecionado, esse parâmetro deverá ser aplicado igualmente para os tributos IRPJ e CSLL tanto para Atividade Geral quanto para Atividade Rural\. 

MFS\-17490

__Título\(\*\)__

__LANÇAMENTO DA PARTE B AUTOMÁTICO PARA INCENTIVO PAT__

Conta da Parte B

LOV

\-

\-

Código – Descrição

Permite que o usuário informe a conta da parte B que será utilizada criação de lançamentos automáticos provenientes do incentivo PAT\.

Tratamentos:

Recuperar as contas da parte B que estão cadastradas no grupo selecionado e que estão vigentes na data inicial da escrituração\.

Campos de Pesquisa: Código e Descrição\.

1. MFS\- [18703](http://ent.jira.int.thomsonreuters.com/browse/MFS-18703)

Histórico Padrão do Lançamento da Parte A

Texto

S

S

“Lançamento de Ajuste da Parte A”

Permite que o usuário visualize e edite o texto referente ao histórico padrão a ser aplicado nos lançamentos da Parte A\.

Tratamento:

O sistema apresentará um valor padrão para o campo, mas que pode ser modificado pelo usuário\.

MFS\-17490

__Aba \(\*\)  
__

__Parâmetros Complementares__

__ __

__Título\(\*\)__

PARÂMETROS COMPLEMENTARES

PJ Sujeita à Alíquota da CSLL

Lista

S

S

Se a Versão for igual a 1\.00:  
• N \- 9%  
  
Se a Versão for igual ou maior a 2\.00:  
• 1 \- 9%

Permite que o usuário informe se a empresa está sujeita a alíquota da CSLL   
  
__Tratamentos:__  
  
O Campo só deve ser habilitado após o preenchimento de uma Data Inicial e Versão correspondente\.  
  
Se a Versão for igual a 1\.00:  
  
Conteúdos Válidos:  
Domínio \- Descrição  
• N \- 9%  
• S \- 15%  
  
Se a Versão for igual ou maior a 2\.00:  
O Campo só deve ser habilitado após o preenchimento de uma Data Inicial, Versão correspondente e Forma de Tributação igual Lucro Real, Lucro Presumido, Lucro Arbitrado, ou Imune de IRPJ com Apuração da CSLL diferente de Desobrigada ou Isento do IRPJ com Apuração da CSLL diferente de Desobrigada, caso contrário o campo deve ficar desabilitado e sem preenchimento\.  
  
Conteúdos Válidos:  
Domínio \- Descrição  
• 1 \- 9%  
• 2 \- 17%   
• 3 \- 20%  
  
Quando o campo for habilitado, ele deve ser obrigatório, aplicar  RNG00010 \- Campo Obrigatório

MFS\-12691

Atividade Rural

Check\-box

N

S

Desmarcado

Permite que o usuário informe se a empresa possui Atividade Rural\.  
  
Tratamentos:  
  
Se a Versão for igual a 1\.00:  
  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado\.  
  
Se a Versão for igual ou maior a 2\.00:  
  
O campo deve ficar sempre habilitado\.

MFS\-12691

Lucro da Exploração 

Check\-box

N

S

Desmarcado  
  


Permite que o usuário informe se a empresa possui o incentivo do Lucro da Exploração\.  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado\.

MFS\-12691

Administradora de Fundos e Clubes de Investimento

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa é administradora de fundos e clubes de investimento\.  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado\.  
Exceto se o campo “Tipo de Entidade” for igual a “Entidade Fechada de Previdência Complementar” ou “Associação de Poupança e Empréstimo” ou “Entidade Aberta de Previdência”\.

MFS\-12691

Participações em Consórcios de Empresas

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui participações em consórcios de empresa\.  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” e o campo “Tipo de Entidade” for igual a “Fifa e Entidades Relacionadas” ou “CIO e Entidades Relacionadas”, esse campo deverá ficar desabilitado\.

MFS\-12691

Operações com o Exterior

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui operações com o Exterior\.  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado\.

MFS\-12691

Rendimentos Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui rendimentos relativos a serviços, juros e dividendos recebidos do Brasil e do Exterior\.  
   
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” e o campo “Tipo de Entidade” for igual a “Fifa e Entidades Relacionadas” ou “CIO e Entidades Relacionadas”, esse campo deverá ficar desabilitado\.

MFS\-12691

Pagamentos ao Exterior ou a Não Residentes

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui pagamentos ao exterior ou a não residentes  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” e o campo “Tipo de Entidade” for igual a “Fifa e Entidades Relacionadas” ou “CIO e Entidades Relacionadas”, esse campo deverá ficar desabilitado\.

MFS\-12691

Ativos no Exterior

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui ativos no Exterior\.  
  
__Tratamentos:__  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” e o campo  “Tipo de Entidade” for igual a “Fifa e Entidades Relacionadas” ou “CIO e Entidades Relacionadas”, esse campo deverá ficar desabilitado\.

MFS\-12691

Royalties Recebidos do Brasil e do Exterior

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui royalties recebidos do Brasil e do Exterior  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” e o campo “Tipo de Entidade” for igual a “Fifa e Entidades Relacionadas” ou “CIO e Entidades Relacionadas”, esse campo deverá ficar desabilitado\.

MFS\-12691

Pagamentos ou Remessas a Titulo de Serviços, Juros e Dividendos a Beneficiários do Brasil e do Exterior

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui pagamentos ou remessas a titulo de serviços, juros e dividendos a beneficiários do Brasil e do Exterior\.  
   
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” e o campo “Tipo de Entidade” for igual a “Fifa e Entidades Relacionadas” ou “CIO e Entidades Relacionadas”, esse campo deverá ficar desabilitado\.

MFS\-12691

Rendimentos do Exterior ou de Não Residentes

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui rendimentos do exterior ou de não residentes\.  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” e o campo “Tipo de Entidade” for igual a “Fifa e Entidades Relacionadas” ou “CIO e Entidades Relacionadas”, esse campo deverá ficar desabilitado\.

MFS\-12691

Royalties Pagos a Beneficiários do Brasil e do Exterior

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui royalties pagos aos beneficiários do Brasil e do Exterior\.  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” e o campo “Tipo de Entidade” for igual a “FIFA e Entidades Relacionadas” ou “CIO e Entidades Relacionadas”, esse campo deverá ficar desabilitado\.

MFS\-12691

Participações no Exterior

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui participações no Exterior\.   
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado\.

MFS\-12691

Operações com Pessoa Vinculada/Interposta Pessoa / Pais com Tributação Favorecida

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui operações com pessoa vinculada/interposta pessoa / pais com tributação favorecida\.  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado\.

MFS\-12691

PJ Enquadrada nos artigos 48 ou 49 da IN RFB no 1\.312/2012

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui PJ Enquadrada nos artigos 48 ou 49 da IN RFB no 1\.312/2012\.  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado\.

MFS\-12691

Isenção e Redução do Imposto para Lucro Presumido

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui isenção e redução do imposto para lucro presumido\.   
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado\.

MFS\-12691

FINOR/FINAM/FUNRES

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui FINOR/FINAM/FUNRES\.  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado\. 

MFS\-12691

Doações a Campanhas Eleitorais

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui doações a campanhas eleitorais

MFS\-12691

Participação Permanente em Coligadas ou Controladas

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui participação permanente em coligadas ou controladas\.   
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” e o campo “Tipo de Entidade” for igual a “Fifa e Entidades Relacionadas” ou “CIO e Entidades Relacionadas”, esse campo deverá ficar desabilitado\.

MFS\-12691

PJ Efetuou Vendas a Empresa Comercial Exportadora com Fim Especifico de Exportação

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa efetuou vendas a empresa comercial exportadora com fim especifico de exportação   
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado\.

MFS\-12691

PJ Comercial Exportadora

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa é Comercial Exportadora\.  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado

MFS\-12691

Indicador de optante pelo PAES

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa é optante pelo PAES\.

MFS\-12691

Indicador de optante pelo REFIS

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa é optante pelo REFIS\.

MFS\-12691

Comércio Eletrônico e Tecnologia da Informação

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui comércio eletrônico e tecnologia da informação\.  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” e o campo “Tipo de Entidade” for igual a “Fifa e Entidades Relacionadas” ou “CIO e Entidades Relacionadas”, esse campo deverá ficar desabilitado\.

MFS\-12691

Inovação Tecnológica e Desenvolvimento Tecnológico

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui inovação tecnológica e desenvolvimento tecnológico\.   
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado\.

MFS\-12691

Capacitação de Informática e Inclusão Digital

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui capacitação de informática e inclusão digital\.  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado\.

MFS\-12691

PJ Habilitada no Repes, Recap, Padis, \.\.\. \(vide ícone “i”\)

   
Apresentar tooltip: PJ Habilitada no Repes, Recap, Padis,PATVD, Reidi, Repenec, Reicomp, Retaero, Recine, Resíduos Sólidos, Recopa, Copa do Mundo, Retid, REPNBL\-Redes, Reif e Olimpíadas

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa é habilitada no Repes, Recap, Padis, PATVD, Reidi, Repenec, Reicomp, Retaero, Recine, Resíduos Sólidos, Recopa, Copa do Mundo, Retid, REPNBL\-Redes, Reif e Olimpíadas\.  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado\.  
  
Tratamento a partir da versão 3\.00:  
  
Se este campo estiver selecionado, é obrigatório o preenchimento de pelo menos um campo da aba Parâmetros de Identificação dos Tipos de Programa\. Quando este campo estiver selecionado pelo menos um campo da aba Parâmetros dos Tipos de Programa deve estar selecionado\. Caso contrário, ao salvar, exibir a DW00031\.  
  
Se for removida a seleção desse campo e na aba Parâmetros dos Tipos de Programa houver campos selecionados, ao salvar, limpar a seleção desses campos\. 

MFS\-12691

Polo Industrial Manaus e Amazônia Ocidental 

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui Polo Industrial Manaus e Amazônia Ocidental\.  
  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado\. 

MFS\-12691

Zonas de Processamento de Exportação

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui Zonas de Processamento de Exportação\.  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado\.

MFS\-12691

Áreas de Livre Comércio

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa possui áreas de livre comércio\.  
  
Tratamentos:  
Se o campo Forma de Tributação na aba Parâmetros de Tributação, estiver com a opção “Imune de IRPJ” ou “Isento do IRPJ” esse campo deverá ficar desabilitado\.

MFS\-12691

Optante pela extinção do RTT no Ano\-Calendário 2014

Checkbox

N

S

Desmarcado

Permite que o usuário informe se a empresa é optante pela extinção do RTT no Ano\-Calendário 2014  
  
Tratamentos:  
  
Apresentar este campo para escriturações com versão anterior a 3\.00\. Para versão 3\.00 ou superior, este campo não deve ser exibido\.

MFS\-12691

Existe diferenças entre a Contabilidade Societária e Fcont

Checkbox

N

S

Desmarcado

Permite que o usuário informe se existem diferenças entre a Contabilidade Societária e Fcont\.  
  
Tratamentos:  
Apresentar este campo para escriturações com versão anterior a 3\.00\. Para versão 3\.00 ou superior, este campo não deve ser exibido\.

MFS\-12691

Entidade Integrante de Grupo Multinacional

Checkbox

N

S

Desmarcado

Quando selecionado indica que o estabelecimento possui relações com estabelecimento de outro País\.  A seleção desse campo está relacionada com a geração do Bloco W\.  
  
Tratamentos:  
Este campo deve ser exibido somente para escriturações a partir da versão 3\.00\.

MFS\-12691

Declaração sobre utilização dos recursos em moeda estrangeira decorrentes do recebimento de exportações \(DEREX\)

Checkbox

N

S

Desmarcado

Quando selecionado indica que o estabelecimento possui informações da DEREX\.  A seleção desse campo está relacionada com a geração do BlocoV\.  


Tratamentos:  
Este campo deve ser habilitado somente para escriturações a partir da versão 4\.00\.

MFS\-20274

__Aba \(\*\)  
Parâmetros de Identificação dos Tipos de Programa__

__ __

__ __

__ __

__ __

__ __

__ __

__Título\(\*\)__

PARÂMETROS DE IDENTIFICAÇÃO DOS TIPOS DE PROGRAMA

Regime Especial de Tributação para a Plataforma de Exportação de Serviços de Tecnologia da Informação \(Repes\)

 

Checkbox

N

S

Desmarcado

Tratamentos:  
  
Apresentar esta aba a apartir da versão 3\.00\. Quando selecionado, indica que o estabelecimento possui o programa na escrituração\. O conteúdo selecionado neste item,  será gerado no registro 0021 \(a partir da versão 3\.00\)\.  
  
Só será permitido marcar um dos parametros desta aba, se o parâmetro "PJ Habilitada no Repes, Recap, Padis, \.\.\. \(vide ícone “i”\)" da aba "Parâmetros Complementares" estiver marcado\. Caso contrário, exibir a mensagem DW00127

MFS\-12691

Regime Especial de  Aquisição  de  Bens   de  Capital  para  Empresas Exportadoras \(Recap\)

 

Checkbox

N

S

Desmarcado

MFS\-12691

Programa de Apoio ao Desenvolvimento Tecnológico da Indústria de Semicondutores \(Padis\)

 

Checkbox

N

S

Desmarcado

MFS\-12691

Programa de Apoio ao Des envolvimento Tecnológico da Indústria de Equipamentos para TV Digital \(PATVD\)

 

Checkbox

N

S

Desmarcado

MFS\-12691

Regime Especial de Incentivos para o Desenvolvimento da Infraestrutura \(Reidi\)

 

Checkbox

N

S

Desmarcado

MFS\-12691

Regime Especial de Incentivos para  o  Desenvolvimento da Infraestrutura  da  Indústria  Petrolífera  das  Regiões  Norte,  Nordeste e Centro\-Oeste \(Repenec\)

 

Checkbox

N

S

Desmarcado

MFS\-12691

Regime Especial de Incentivo a Computadores para Uso Educacional \(Reicomp\)

 

Checkbox

N

S

Desmarcado

MFS\-12691

Regime Especial para a Indústria Aeronáutica Brasileira \(Retaero\)

 

Checkbox

N

S

Desmarcado

MFS\-12691

Regime Especial de Tributação para Des envolvimento da Atividade de Exibição Cinematográfica \(Recine\)

 

Checkbox

N

S

Desmarcado

MFS\-12691

Estabelecimentos industriais que façam jus a crédito presumido do  IPI na aquisição de resíduos  sólidos, de que trata a Lei nº 12\.375, de  30 de dezembro de 2010

 

Checkbox

N

S

Desmarcado

MFS\-12691

Regime Especial de Tributação para construção, ampliação, reforma ou modernização de estádios de futebol \(Recopa\)

 

Checkbox

N

S

Desmarcado

MFS\-12691

Habilitada para fins de fruição dos benefícios fis cais, não abrangidos na alínea anterior,   relativos   à   realização,   no   Brasil,   da   Copa   das Confederações FIFA \.\.\. \(vide ícone “i”\)

Apresentar Tolltip: Habilitada para fins de fruição dos benefícios fiscais, não abrangidos na alínea   anterior,   relativos   à   realização,   no   Brasil,   da   Copa   das Confederações FIFA 2013 e da Copa do Mundo FIFA 2014, de que trata a Lei nº 12\.350, de 2010 regulamentada pelo Decreto nº 7\.578, e 11 de outubro de 2011

Checkbox

N

S

Desmarcado

MFS\-12691

Regime Especial Tributário para a Indústria de Defesa \(Retid\)

 

Checkbox

N

S

Desmarcado

MFS\-12691

Regime Especial de Tributação  do Programa Nacional de Banda Larga para Implantação de Redes de Telecomunicações \(REPNBL\-Redes \)

 

Checkbox

N

S

Desmarcado

MFS\-12691

Regime Especial de Incentivo ao Des envolvimento da Infraestrutura da Indústria de Fertilizantes \(REIF\)

 

Checkbox

N

S

Desmarcado

MFS\-12691

Habilitada para fins de fruição   dos  benefícios   fiscais,  relativos   à realização,   no  Brasil,  dos  Jogos   Olímpicos   de   2016  e  dos  Jogos Paraolímpicos de 2016, de que trata a Lei nº 12\.780, de 2013

 

Checkbox

N

S

Desmarcado

MFS\-12691

__Aba \(\*\) Replicar para os Estabelecimentos \(\*\)__

__ __

__ __

__ __

__ __

__ __

__ __

Replicar para os Estabelecimentos\(\*\)

check\-box

N

S

Desmarcado

Permite que o usuário informe  para quais estabelecimento será replicado a parametrização\.

MFS\-12691

Estabelecimentos\(\*\)

Texto

N

S

Tipo – Código \- Nome

Exibe os estabelecimento\.  
  
__Tratamentos:  
__  
Exibe todos os Estabelecimentos Centralizador e Descentralizados de acordo com a Central de Escrituração de Obrigações Federais no formato Tipo \- Código \- Descrição e em cada registro, que não possua uma Informação ECF de mesma data inicial, exercício e versão, do registro que está sendo inserido/alterado na tela\. Apresentar um check\-box na frente de cada registro\.

MFS\-12691

Selecionar Todos

Botão

\-

\-

Desabilitado

Permite selecionar todos os estabelecimentos\.  
  
__Tratamentos:__  
  
Só habilita o botão, se existir uma Informação ECF aberta na tela e se o check\-box na funcionalidade estiver marcado\.

MFS\-12691

Desmarcas Todos

Botão

\-

\-

Desabilitado

Permite desmarcar todos os estabelecimentos\.  
  
  
__Tratamentos:__  
  
Só habilita o botão, se existir uma Informação ECF aberta na tela e se o check\-box na funcionalidade estiver marcado\.

MFS\-12691

__Demais Botões \(\*\)__

__ __

__ __

__ __

__ __

__ __

__ __

Confirma

Botão

\-

\-

 

Permite que o usuário inclua/altera as informações\.  
  
__  
Tratamentos:  
  
__Quando o usuário estiver editando o registro, o campo Forma de Tributação deverá ficar desabilitado\.   
  
O sistema não deve permitir alteração no campo ‘Critério de Reconhecimento de Receitas’ para a opção ‘Não se aplica’, quando existir uma abertura de apuração com Forma de Tributação igual a Lucro Presumido\. Caso seja encontrado este cenário, exibir a DW00033\.  
  
Quando o usuário estiver editando o registro e alterar o parâmetro ‘Indicador de optante pelo REFIS’, se existir alguma abertura da apuração correspondente ao registro com Forma de Tributação = Lucro Presumido, não permitir a alteração e exibir a DW00039\. Caso contrário, permitir a alteração\.  
  
Se o valor do campo Forma de Tributação for igual à:  
Imune de IRPJ ou Isento do IRPJ, verificar a ocorrência de registro Y600 na tela de Informações Econômicas e Gerais, se houver: excluir a ocorrência do Y600 pertinente à Informação ECF que está sendo salva\.  
  
Aplicar RNG00012 \- Salvar, RNG00007 \- Associação da Tabela Dinâmica com o Plano Empresa x Informações ECF  
  
Se o campo  Se “Forma de Tributação” estiver preenchida com a opção ‘Lucro Real, Lucro Presumido, Lucro Arbitrado’ e o campo \_ Critério de Reconhecimento de Receitas igual a ‘Regime de Caixa’, o campo escrituração só pode ser preenchido com as opções ‘Livro Caixa ou Sem Escrituração’ e  ‘Contábil ‘, caso contrário, exibir a mensagem DW00065\.

MFS\-12691

Exclui

Botão

\-

\-

 

Permite que o usuário exclua um registro\.  
  
__Tratamentos:__  
  
Ao clicar no botão e o sistema encontrar uma Informação ECF sem criação de abertura da apuração, permitir a exclusão do registro, exibindo a mensagem de confirmação padrão do sistema e se o usuário confirmar, mostrar a mensagem do sistema de Registro Excluído com Sucesso\. Caso o usuário selecione ‘Não’, o registro não deve ser excluído\.  
  
Se existirem aberturas da apuração com status igual:  
“Apuração em Aberto” ou “Importação de Saldos Realizada” ou “Alteração Manual Realizada” ou “Aguardando Alteração Manual” ou “Reapurar”, permitir a exclusão do registro, se o usuário clicar em Sim para a mensagem DW00125 e depois mostrar a mensagem do sistema de Registro Excluído com Sucesso\. Caso o usuário selecione ‘Não’, o registro não deve ser excluído\.  
  
Se existir aberturas de apuração com status igual a “Cálculo Realizado” exibir a seguinte mensagem ao usuário: DW00044 e não excluir o registro\.

Se existir cálculo de PAT \(tela Programa de Alimentação do Trabalhador \- PAT\), desconsiderar todos os valores calculados para o PAT, linha 9 do registro N620 ou linha 8 do registro N630 \(conforme RNC018, RNC19 e RNC20, do documento MTZ\_Processamento\_em\_Lote\.docx\), inclusive o valor utilizado no período e de períodos anteriores\. Vale ressaltar que o PAT utilizado dos períodos anteriores \(calculado para cada período de apuração\) deve voltar para o período anterior\.

MFS\-12691  
MFS\-14482

MFS\-18703


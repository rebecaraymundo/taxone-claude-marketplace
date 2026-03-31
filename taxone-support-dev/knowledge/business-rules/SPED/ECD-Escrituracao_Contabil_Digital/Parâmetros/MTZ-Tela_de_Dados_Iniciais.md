# MTZ-Tela_de_Dados_Iniciais

- **Fonte:** MTZ-Tela_de_Dados_Iniciais.docx
- **Modificado:** 2023-04-28
- **Tamanho:** 49 KB

---

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3835

 Tela de Dados Iniciais

Este documento tem por objetivo especificar as alterações para que o mastersaf possa contemplar o layout da ECD 2012\.

OS3676

Tela de Dados Iniciais, aba Demonstrações Contábeis

Inclusão de opções nos campos Periodicidade e Referência

CH21456\_2013

Ajuste para Signatários

Ajuste na tabela de Signatários

OS3835\-C

Indicador de Porte da Empresa

Inclusão do campo para informar se a empresa é de grande porte\.

OS4711

Saldo Antes do Encerramento \(SAFX169\) 

Inclusão do campo Saldo Antes do Encerramento\.

OS4745

Atualização para atender versão 3\.00 do layout da ECD

Atualização da opção de entidade responsável pelo plano referencial, criação de um novo parâmetro de tipo de ECD e criação de uma nova aba\.

MFS\-2632

Atualização para atender versão 4\.00 do layout da ECD

Criação do novo parâmetro “ECD com Movimentação em Moeda Funcional”\.

MFS\-4878

Atualização para atender ao cenário de Moeda Funcional

Criação do novo parâmetro “Gerar Balanço Patrimonial e DRE com base nos valores de Moeda Funcional”

MFS\-8216

Atualização para atender versão 5\.00 do layout da ECD

Inclusão do código 910 no campo Cod\. Qualificação SPED e inclusão campo dados iniciais\. \(RN04 e RN14\) 

MFS\-8620

Atualização para atender versão 5\.00 do layout da ECD

Inclusão do código 920 no campo Cod\. Qualificação SPED e inclusão de nova entidade no campo Entidade Responsável pelo Plano Referencial e novos campos J800 e J801\. \(RN04, RN07, RN15, RN16, RN17 e RN18\) 

MFS\-10358

Atualização para atender versão 5\.00 do layout da ECD

Criação do novo parâmetro “Escriturações Contábeis Consolidadas”\.

MFS\-10684

Atualização para atender versão 5\.00 do layout da ECD

Inclusão do código 001 e ajuste no código 910 no campo Cod\. Qualificação SPED \(RN04\) 

MFS\-13062

Alteração da aba Dados Iniciais para incluir parametrização em atendimento ao Registro I015

Este documento tem como objetivo criar parametrização na tela de Dados Iniciais para que o usuário possa informar como deseja gerar o Registro, se pela conta parametrizada em Livros Auxiliares ao Diário ou se pela associação da conta analítica com a conta sintética\.

CH19329\_2017

\(MFS\-14108\)

Tela de Dados Iniciais:

No campo “ECD com Movimentação em Moeda Funcional”\.

Este documento tem por objetivo especificar a obrigatoriedade do preenchimento da moeda funcional no registro ‘0000’\.

MFS\-11946

Tela de Dados Iniciais:

Inclusão de Parâmetro

Esse documento tem por objetivo especificar a criação do parâmetro “Gerar Código do Participante \(SAFX39\) onde o usuário poderá indicar que deseja gerar o Participante com relacionamento \(registro na SAFX39\), independente da movimentação \(registro na SAFX01\)\.

MFS\-20244

Tela de Signatários:

Inclusão de Parâmetro

Esse documento tem por objetivo a inclusão de um novo valor válido para o campo “Cód\. Qualificação SPED”\.

MFS\-22414

Inclusão do Parâmetro na aba “Auditores Independentes” e nova validação para o campo “Registro do Auditor no CVM”\.

Esse documento tem por objetivo a inclusão do campo __“CPF/CNPJ do Auditor “ __na aba de Auditores Independentes e incluir nova validação para o campo Registro do Auditor no CVM\.

MFS27094

Alteração do parâmetro “Gerar Plano de Contas”

Esse documento tem por objetivo a inclusão de novas opções para o campo __“Gerar Plano de Contas”__

MFS58039

Inclusão de Código de Qualificação \(Aba Signatários\)

Disponibilizar no menu Parâmetros >> Dados Gerais >> Aba Signatários o novo Cod\. Qualificação SPED: 940\. Ajuste RN04\.

MFS62417

Alteração descrição parâmetro Gerar Plano de Contas \(Aba Dados Iniciais\)

Alteração da descrição da opção: “Somente contas movimentadas no ano da geração \(até a data da geração\)” e “Somente contas \+ centro de custo movimentados no ano da geração \(até a data da geração\)” do campo __“Gerar Plano de Contas”\. \(RN24\)__

MFS\-68575

Inclusão do Parâmetro “Registro I050 – Ordenar p/ Indicador de Natureza” na aba “Dados Adicionais” 

Esse documento tem por objetivo de incluir o parâmetro __“__Ordenar Plano de Contas p/ Indicador de Natureza__” __na aba de Dados Iniciais passando a ordenar os Registros I050 e filhos pelo Campo 07 – Indicador da Natureza\. __\(RN25\)__

MFS\-532288

Inclusão do Parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis \+ Contas Contábeis/Centro de Custo p/ mesma Conta Contábil” na aba “Dados Adicionais”  

Esse documento tem por objetivo de incluir o parâmetro “Gerar Lançamentos/Saldos de Contas Contábeis \+ Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”  na aba de Dados Iniciais passando a gerar os Registros I155/I250/J100/J150\. __\(RN26\)__

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Alteração da tela ‘Dados Iniciais’, no Módulo: SPED/ECD – Escrituração Contábil Digital, Menu: Parâmetros:

Incluir novo campo ‘Dia e Mês do Encerramento do Exercício Social’

Tamanho: 04 posições

Tipo: Numérico

Campo: Não Obrigatório

Validação: Consistir os dados informados no campo ‘Dia e Mês do Encerramento do Exercício Social’, conforme o período do calendário \(aceitar dias de 01 a 31 e os meses de 1 a 12\), caso o cliente informe algo diferente, exibir a seguinte msg de erro: Período do Encerramento do Exercício Social inválido\.

OS3835

__RN01__

Na aba Demonstrações Contábeis, incluir a Periodicidade Trimestral

OS3676

__RN02__

Inclusão das opções:  1º Trimestre, 2º Trimestre, 3º Trimestre e 4º Trimestre, no campo Referência\.

OS3676

__RN03__

Quando a Periodicidade Trimestral for selecionada pelo usuário, mostrar no campo Referência, as opções: 1ºTrimestre, 2º Trimestre, 3º Trimestre e 4º Trimestre\. 

OS3676

__RN04__

Módulo: SPED\\ ECD\-Escrituração Contábil Digital

Menu: Parâmetros\\ Dados Iniciais\\ Aba Signatários

Alterar o campo Cod\. Qualificação SPED\.

__Valores Válidos:__

__\[Alterada \- CH21456\_2013/MFS8216/MFS8620/MFS10684\]__

Código

Descrição

001

Pessoa Jurídica \(e\-CNPJ ou e\-PJ\)

203

Diretor

204

Conselheiro de Administração

205

Administrador

206

Administrador do Grupo

207

Administrador de Sociedade Filiada

220

Administrador Judicial – Pessoa Física

222

Administrador Judicial – Pessoa Jurídica \- Profissional Responsável

223

Administrador Judicial/Gestor

226

Gestor Judicial

309

Procurador

312

Inventariante

313

Liquidante

315

Interventor

401

Titular – Pessoa Física \- EIRELI

801

Empresário

900

Contador/Contabilista

901

Contabilista

910

Contador/Contabilista Responsável Pelo Termo de Verificação para Fins de Substituição da ECD Laudo de Substituição

920

Auditor Independente Responsável pelo Termo de Verificação para Fins de Substituição da ECD

940

Auditor Independente

999

Outros

CH21456\_2013

MFS8216

MFS8620

MFS10684

MFS20244

MFS58039

__RN05__

Módulo: SPED\\ ECD\-Escrituração Contábil Digital

Menu: Parâmetros\\ Dados Iniciais \\ aba Dados Iniciais

Incluir o campo “Empresa de Grande Porte sujeita à Auditoria Independente” do tipo checkbox, mantendo a informação como selecionada por default\.

OS3835\-C

OS4745

__RN06__

__Campo Saldo Antes do Encerramento \(SAFX169\)__

Checkbox

Default não selecionado 

Não obrigatório

Quando selecionado no caminho: 

Módulo: Sped à ECD Escrituração Contábil Digital

Menu: Parâmetros à Dados Iniciais

Indica que as informações serão recuperadas a partir da “SAFX169 – Saldo Antes do Encerramento” importada\. Caso não selecionado, seguir com a regra de cálculo hoje existente no sistema\.

Obs: deverá absorver a regra existente referente para o checkbox “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos”\.

OS4711

__RN07__

__Aba Dados Iniciais – Entidade Responsável pelo Plano Referencial__

A lista de entidades responsáveis deve ser atualizada com as novas opções:

1 \- PJ em Geral

2 \- PJ em Geral \- Lucro Presumido

3 \- Financeiras

4 \- Seguradoras

5 \- Imunes e Isentas em Geral

6 \- Financeiras \- Imunes e Isentas

7 \- Seguradoras \- Imunes e Isentas

8 \- Entidades Fechadas de Previdência Complementar

9 \- Partidos Políticos

10 \- Financeiras – Lucro Presumido/Secretaria da Receita Federal

Excluir a opção 10 \- Secretaria da Receita Federal da lista, pois a mesma será atendida juntamente com a opção 10 \- Financeiras – Lucro Presumido/Secretaria da Receita Federal\.

OS4745

MFS8620

__RN07__

__Aba Dados Iniciais – Entidade Responsável pelo Plano Referencial__

A lista de entidades responsáveis deve ser atualizada com as novas opções:

1 \- PJ em Geral

2 \- PJ em Geral \- Lucro Presumido

3 \- Financeiras

4 \- Seguradoras

5 \- Imunes e Isentas em Geral

6 \- Financeiras \- Imunes e Isentas

7 \- Seguradoras \- Imunes e Isentas

8 \- Entidades Fechadas de Previdência Complementar

9 \- Partidos Políticos

OS4745

__RN08__

__Aba Dados Iniciais – Campo Tipo da ECD__

O campo tipo da ECD foi criado na versão de layout 3\.00 do SPED Contábil\. Será um campo do tipo alfanumérico e deve gravar um caractere\. Será na tela um dropdounlist com as opções:

0 – ECD de empresa não participante de SCP como Sócio Ostensivo;

1 – ECD de empresa participante de SCP como Sócio Ostensivo;

2 – ECD da SCP\.

Por default, será demonstrada a opção “0 – ECD de empresa não participante de SCP como Sócio Ostensivo”, sendo permitida a alteração por parte do usuário\.

OS4745

__RN09__

__Aba Auditores Independentes – Funcionamento da Aba__

Na aba Auditores Independentes o usuário deverá informar o Nome e o Código CVM do profissional que realiza auditoria interna\. Poderá ser apenas um ou “N” profissionais, considerando a distinção por código CVM\.

OS4745

__RN10__

__Aba Auditores Independentes – Campo Nome do Auditor__

O campo Nome do Auditor será um campo do tipo texto e que permitirá no máximo 250 caracteres\.

OS4745

__RN11__

__Aba Auditores Independentes – Campo Registro do Auditor na CVM__

O campo Registro do Auditor na CVM será um campo do tipo texto e que permitirá no máximo 250 caracteres\.

__Regras:__

- Se o campo __“CPF/CNPJ do Auditor” __estiver preenchido com__ __11 posições__ ‘CPF’__ e o usuário não preencher o campo __“Registro do Auditor no CVM”__, uma mensagem de alerta é exibida na tela: *“O campo Registro do Auditor no CVM é obrigatório de preenchimento para pessoa física”\.*

*Sem Default*

OS4745

MFS22414

__RN12__

__Aba Dados Iniciais – Campo ECD com Movimentação em Moeda Funcional__

Criar o campo “ECD com Movimentação em Moeda Funcional”\. Será um checkbox, cujo padrão deve ser “não selecionado”, mas que permita seleção pelo usuário\.

Não é campo obrigatório\.

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>Quando marcado – Na geração do arquivo magnético será preenchido com “S”

Quando desmarcado – Na geração do arquivo magnético será preenchido com “N”

Campo Obrigatório \(na geração do arquivo\)

Tipo: Caractere 

Tamanho: 1 posição

MFS\-2632

CH19329\_2017

\(MFS\-14108\)

__RN13__

__Aba Dados Iniciais – Campo Gerar Balanço Patrimonial e DRE com base nos valores de Moeda Funcional__

Criar o campo “Gerar Balanço Patrimonial e DRE com base nos valores de Moeda Funcional”\. Será um checkbox, cujo padrão deve ser “desabilitado” e “não selecionado”\. Ele deve ser habilitado para seleção quando a opção “ECD com Movimentação em Moeda Funcional” for selecionada\.

Não é campo obrigatório\.

MFS\-4878

__RN14__

__Aba Signatários – Campo Indicação do Representante Legal Junto às Bases da RFB__

Criar o campo “Indicação do Representante Legal Junto às Bases da RFB” ao lado do campo Cod\. Qualificação SPED\. Será um checkbox criado de acordo com cada Responsável, cujo padrão deve ser “desabilitado” e “não selecionado”\. Ele deve ser habilitado para seleção quando a opção “Indicação do Representante Legal Junto às Bases da RFB” for selecionada\.

MFS\-8216

__RN15__

__Aba Demonstrações Contábeis: __

__Quadro ‘Outras Informações das Demonstrações Contábeis \(Balanço Patrimonial e Demonstração de Resultado\)’ – Campo Tipo do Documento__

Criar o campo “Tipo do Documento”\. Será um ComboBox\.

A lista de Tipo do Documento a ser apresentada:

001: Demonstração do Resultado Abrangente do Período 

002: Demonstração dos Fluxos de Caixa 

003: Demonstração do Valor Adicionado 

010: Notas Explicativas 

011: Relatório da Administração 

012: Parecer dos Auditores 

099: Outros

Deverá ser demostrado ao usuário apenas as descrições acima\.

Campo obrigatório\.

Default não selecionado\. Como se trata de um campo obrigatório se não selecionado nenhuma opção deverá ser apresentada a mensagem:

*‘Tipo de Documento deve ser informado’*

MFS\-8620

__RN16__

__Aba Demonstrações Contábeis: __

__Quadro ‘Outras Informações das Demonstrações Contábeis \(Balanço Patrimonial e Demonstração de Resultado\)’ – Campo Descrição \(\.rtf\)__

Criar o campo “Descrição \(\.rtf\)”\. Será um campo do tipo texto e que permitirá no máximo 255 caracteres\.

MFS\-8620

__RN17__

__Aba Demonstrações Contábeis: __

__Quadro ‘Termo de Verificação para Fins de Substituição da ECD \(Balanço Patrimonial e Demonstração de Resultado\)’ – Campo Tipo do Documento__

Criar o campo “Tipo do Documento”\. Será um ComboBox com a opção fixa:

001: Termo de Substituição da ECD

Sem possibilidade de alteração e devendo ser demostrado ao usuário apenas a descrição acima\.

MFS\-8620

__RN18__

__Aba Demonstrações Contábeis: __

__Quadro ‘Termo de Verificação para Fins de Substituição da ECD \(Balanço Patrimonial e Demonstração de Resultado\)’ – Campo Descrição \(\.rtf\)__

Criar o campo “Descrição \(\.rtf\)”\. Será um campo do tipo texto e que permitirá no máximo 250 caracteres\.

MFS\-8620

__RN19__

__Aba Dados Iniciais – Campo Escriturações Contábeis Consolidadas__

Criar o campo “Escriturações Contábeis Consolidadas”\. Será um checkbox, cujo padrão deve ser “não selecionado”, mas que permita seleção pelo usuário\.

Não é campo obrigatório\.

MFS\-10358

__RN20__

__Aba Dados Iniciais – Campo Gerar Conta Resumida parametrizada em Livros Auxiliares ao Diário__

Criar o campo “Gerar Conta Resumida parametrizada em Livros Auxiliares ao Diário”\. Será um checkbox, cujo padrão deve ser “não selecionado”, mas que permita seleção pelo usuário\.

Não é campo obrigatório\.

MFS\-13062

__RN21__

__Aba Dados Iniciais – Gerar Código do Participante \(SAFX39\)__

Criar o campo “Gerar Código do Participante \(SAFX39\)”\. Será um checkbox, cujo padrão deve ser “não selecionado”, mas que permita seleção\. Ao marcar esse campo o usuário indicará que deseja gerar o Código do Participante com relacionamento \(registro na SAFX39\), independente da movimentação dos lançamentos contábeis \(registro na SAFX01\)\.

Não é campo obrigatório\.

MFS\-11946

__RN22__

__Aba Auditores Independentes – Campo CPF/CNPJ do Auditor__

Criar o campo __“CPF/CNPJ do Auditor”\. __Este campo possui 14 posições, sendo:

14 posições para pessoa jurídica \- CNPJ

11 posições para pessoa física \- CPF

Campo de preenchimento obrigatório

__Regras:__

- Se o usuário não preencher a informação do documento do auditor e tentar salvar o cadastro, o sistema deve emitir uma mensagem de alerta: *“O campo CPF/CNPJ do Auditor é obrigatório”\.* 

*Sem Default*

MFS22414

__RN23__

__Aba Demonstrações Contábeis – Campo Código Motivo da Substituição__

O campo Código do Motivo da Substituição será um DropDownList que permite a seleção das seguintes opções:

001 – Mudanças de saldos das contas que não podem ser realizadas por meio de lançamentos extemporâneos; 

002 – Alteração de assinatura; 

003 – Alteração de demonstrações contábeis; 

004 – Alteração da forma de escrituração contábil; 

005 – Alteração do número do livro;

099 – Outros; 

__Regras:__

- O label do campo será apresentado como: “Motivo da Substituição” sem default, exibindo a descrição do código na tela\.
- Ao carregar o arquivo RTF na parte de “Termo de Verificação para Fins de Substituição da ECD \(Balanço Patrimonial e Demonstração de Resultado\) e tentar salvar sem o campo __“Motivo da Substituição” não __preenchido, o sistema emite uma mensagem de alerta na tela: *“O campo Motivo da Substituição é obrigatório de preenchimento”\.*

MFS22414

__RN24__

__Aba Dados Iniciais – Gerar Plano de Contas__

__\[MFS62417\] Alteração de descrição das opções referente aos movimentos no ano__

O campo Gerar Plano de Contas será uma lista que permite a seleção das seguintes opções:

\- Completo;

\- Somente contas movimentadas no período da geração;

\- Somente contas \+ centro de custo movimentados no período da geração;

\- Somente contas movimentadas no ano da geração \(até a data da geração\);

\- Somente contas \+ centro de custo movimentados no ano da geração \(até a data da geração\)\.

\- Completo;

\- Somente contas movimentadas no período da geração;

\- Somente contas \+ centro de custo movimentados no período da geração;

\- Somente contas movimentadas no ano da geração;

\- Somente contas \+ centro de custo movimentados no ano da geração\.

MFS27094

MFS62417

__RN25__

__Aba Dados Iniciais – Ordenar Plano de Contas p/ Indicador de Natureza__

Criar o campo “Ordenar Plano de Contas p/ Indicador de Natureza”\. Será um checkbox, cujo padrão deve ser “não selecionado”, mas que permita seleção pelo usuário\.

Quando Desmarcado – Na geração do arquivo magnético os Registros I050 e filhos serão ordenados conforme regra atual do sistema\.

Quando Marcado – Na geração do arquivo magnético os Registros I050 e filhos serão ordenados considerando o Campo 07 \- Indicador de Natureza e Campo 01 – Código da Conta da tabela SAFX2002\.

Não é campo obrigatório\.

Default: Desmarcado

__Obs\.: Incluir abaixo do parâmetro “Gerar Plano de Contas”__

MFS\-68575

__RN26__

__Campo “Gerar Lançamentos/Saldos de Contas Contábeis \+ Contas Contábeis/Centro de Custo p/ mesma Conta Contábil”\.__

Checkbox

Default: Desmarcado

Não obrigatório

Quando selecionado no caminho: 

Módulo: SPED à ECD Escrituração Contábil Digital

Menu: Parâmetros à Dados Iniciais

Indica que as informações dos Lançamentos Contábeis/Saldos Contábeis deverão ser recuperadas a partir da SAFX02/SAFX80 e SAFX226/SAFX227, para lançamentos com ou sem Centro de Custos, \(mesma conta contábil

Obs\.: Caso o parâmetro “Omitir informação Centro de Custo em Lançamentos Contábeis e Saldos” estiver selecionado, esse parâmetro deverá estar desabilitado\.

MFS\-532288


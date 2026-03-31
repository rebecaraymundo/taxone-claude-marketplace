# MTZ_OTF_Gerar_DIRF_com_Filtro_por_Empresa

- **Fonte:** MTZ_OTF_Gerar_DIRF_com_Filtro_por_Empresa.docx
- **Modificado:** 2022-05-05
- **Tamanho:** 37 KB

---

# OTF – Gerar DIRF com Filtro por Empresa

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS2607

OTF \- Gerar DIRF com Filtro por Empresa

O objetivo deste documento de requisito é permitir que na geração da DIRF o usuário possa selecionar através de um filtro a empresa desejada e seus respectivos estabelecimentos\.

OS3960

Resumo das informações DIRF

Conforme Chamado nº 2607/2013, o cliente solicitou que na Aba Resumo das Informações DIRF seja exibida a soma das Deduções \(Previdência Oficial, Previdência Privada, Pensão Alimentícia e Dependentes\)\.

OS3961

OTF – Gerar DIRF

Inclusão de informações referente a Beneficiários Residentes no Exterior

MFS81694

Resumo das informações DIRF

Retirar regra para listar os Beneficiários Não\-Informados, somente, quando o campo “VLR\_DED\_INSS\_TERC” estiver preenchido com valor > que ‘0’ \.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Será criada na tela de Geração da DIRF \(módulo __Federal – Obrigações de Tributos Federais__ menu __DIRF – Geração DIRF__\) um filtro intitulado “Empresa”\.

OS2607

__RN02__

Esse filtro irá permitir que o usuário selecione as empresas cadastradas no sistema\. As informações serão recuperadas da tabela EMPRESA\.

OS2607

__RN03__

Ao selecionar a empresa através do filtro, o sistema irá atualizar a relação de estabelecimentos\. Os estabelecimentos exibidos são os que pertencem à empresa selecionada\.

OS2607

__RN04__

Só serão exibidos os estabelecimentos que atenderem às seguintes premissas:

- Estabelecimentos licenciados através do Controle de Licenciamentos do Manager ;
- Estabelecimentos que o usuário possua direito de acesso através da ferramenta PowerLock\.

OS2607

__RN05__

Além das empresas listadas o filtro exibe uma opção chamada “\*\*\* Todas as Empresas \*\*\*”\.

OS2607

__RN06__

Caso o usuário selecione a opção “\*\*\* Todas as Empresas \*\*\*”, o sistema não exibe nenhum estabelecimento\. A geração será realizada para \*\*\* Todas as Empresas \*\*\* as empresas e seus respectivos estabelecimentos\.

OS2607

__RN07__

Por padrão, a empresa exibida no filtro logo ao entrar na tela é a empresa selecionada no Manager\. 

OS2607

__RN08__

No campo “Empresa” será exibido o código da empresa \(campo COD\_EMPRESA da tabela EMPRESA\) concatenado com a descrição da empresa \(campo RAZAO\_SOCIAL da tabela EMPRESA\)\.

Exemplo: 076 – TEXAS INSTRUMENTOS ELETRONICOS DO BRASIL LTDA\.

OS2607

__RN09__

Caso na geração do meio magnético seja informada no filtro a opção \*\*\* Todas as Empresas \*\*\*, o sistema deve associar números de processos diferentes para cada uma das empresas selecionadas na geração\. Essa regra afeta diretamente o processo Formatação das Mídias do Meio Magnético, pois o mesmo é responsável por realizar a geração do arquivo com as informações da DIRF\.

OS2607

__RN10__

Incluir a opção “2010” no campo “Ano Calendário” no menu DIRF >> Geração do módulo Obrigações de Tributos Federais\. Essa opção só será visível caso o flag “Extinção” seja selecionado\.

OS2965

__RN11__

Incluir a opção “2009” no campo “Ano Calendário” no menu DIRF >> Geração do módulo Obrigações de Tributos Federais\.

OS2965

__RN12__

Alterar o campo “Ano Referência\-DIRF” para que seja exibida a opção “2010”\. 

OS2965

__RN13__

Gravar no campo “Ano\-calendário” do registro tipo 1 \(posição 28 a 31\) a informação que estiver contida no campo “Ano\-Calendário” da tela de geração contida no menu DIRF >> Geração do módulo Obrigações de Tributos Federais\.

OS2965

__RN14__

Gravar no campo “Ano de referência” do registro tipo 1 \(posição 37 a 40\) a informação que estiver contida no campo “Ano Referência\-DIRF” no menu DIRF >> Geração do módulo Obrigações de Tributos Federais\. Nesse caso será sempre gravado “2010”\.

OS2965

__RN15__

Gravar no campo “Indicador de sócio ostensivo responsável por Sociedade em Conta de Participação – SCP” do registro tipo 1 \(posição 42 a 42\), “0” ou “1” para os anos\-calendário 2007 a 2010 situação especial\. Gravar “ “ \(branco\) para anos\-calendário 2004 a 2007 situação especial\.

OS2965

__RN16__

Gravar no campo Data do evento do registro tipo 1 \(posição 114 a 121\) a Data do Evento preenchida na tela de geração no menu DIRF >> Geração do módulo Obrigações de Tributos Federais\. A partir do ano\-calendário 2004, deve estar sempre preenchido com a data do evento, nos casos de situação especial \(extinção/saída definitiva do país/encerramento de espólio\)\.

OS2965

__RN17__

Gravar no campo Tipo de Evento do registro tipo 1 \(posição 122 a 1220\) o Tipo de Evento informado na tela de geração no menu DIRF >> Geração do módulo Obrigações de Tributos Federais\. A partir do ano\-calendário 2004, deve estar sempre preenchido nos casos de situação especial \(saída definitiva do país/encerramento de espólio\)\. Se declarante pessoa jurídica, deixar em “ “ \(branco\)\.

OS2965

__RN18__

Gravar no campo Informações mensais dos beneficiários pessoas físicas ou jurídicas do registro tipo 2 \(posição 103 a 687\) as informações referente aos valores mês a mês\. Caso o Ano\-calendário informado seja 2004 a 2006 e 2007 situação especial, a coluna dedução deverá estar totalizada \(soma mês a mês de todas as deduções\) e a posição 689 \(ver RN19\), deixar em “ “ \(branco\)\. Caso o Anos\-calendário 2007 a 2010 situação especial a coluna dedução deverá estar com “0” \(zeros\) e posição 689 \(ver RN19\) deverá ser preenchida com “0” \(zero\)\.

OS2965

__RN19__

Gravar no campo Identificação da especialização das deduções do registro tipo 2 \(posição 689 a 689\) “0” \(zero\) para os anos\-calendário 2007 a 2009 e 2010 situação especial\. Gravar “ “ \(branco\) para os anos\-calendário de 2004 a 2006 e 2007 situação especial\.

OS2965

__RN20__

__Aba Resumo das Informações Dirf__

Módulo: Federal à Obrigações de Tributos Federais

Menu: DIRFà Geração DIRF

__Deduções:__ deverá ser informado o valor do campo \(VLR\_VERBA\) da SAFX21, conforme parametrização referente a deduções na tela Parâmetros/Verba \(Módulo >> Federal >> Obrigações de Tributos Federais –Menu >> Parâmetros\)\. 

__OS3960__

__RN21__

__Aba Resumo das Informações Dirf__

Na aba “Resumo das informações da DIRF“ na tela de “Geração DIRF” Caminho: Módulo Federal à Obrigações de Tributos Federais Menu: DIRF à Geração Dirf

Inclusão das Informações referente a Quantidade e valores de “Rendimentos”, “Deduções” e “Retido” para Beneficiários Residentes no Exterior PF/PJ\.

o sistema deverá gerar as colunas “Rendimentos”, “Deduções” e “Imposto Retido” considerando a seguinte regra:

- __Rendimentos:__ deverá ser informado o somatório de todo o valor do campo Valor Bruto da tela de Controle de Tributos \(campo 14 – VLR\_BRUTO da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\) para o mês em questão\.
- __Deduções:__ deverá ser informado o somatório de todo o valor dos campos Valor INSS Retido – Terceiros, Valor Dependentes – Terceiros, Valor Previdência Privada e Valor Pensão Alimentícia da tela de Controle de Tributos \(campos 29 – VLR\_PREV\_PRIVADA, 30 – VLR\_PENS\_ALIMENT, 41 – VLR\_DED\_INSS\_TERC e 42 – VLR\_DED\_DEP\_TERC da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\) para o mês em questão\. Só será gerado está informação para beneficiário PF residente no Brasil\.
- __Imposto Retido:__ deverá ser informado o somatório de todo o valor do campo Valor Tributo da tela de Controle de Tributos \(campo 15 – VLR\_IR\_RETIDO da SAFX53 ou X530\_RETIFICACAO\_IRRF mais recente\) para o mês em questão\.

Residentes no exterior pessoa Física e Jurídica \(UF=EX\)

O campo CPF/CNPJ\(SAFX04\) não deverá ser preenchido, para estes casos utiliza\-se a informação do ID Fiscal que quando preenchido considera\-se o beneficiário como pessoa física, quando não preenchido pessoa jurídica\.

OS3961

__RN22__

__Aba Resumo das Informações Dirf__

Na aba “Resumo das informações da DIRF“ na tela de “Geração DIRF” Caminho: Módulo Federal à Obrigações de Tributos Federais Menu: DIRF à Geração Dirf

__\[MFS81694\] __Retirar regra para listar os Beneficiários Não\-Informados, somente, quando o campo “VLR\_DED\_INSS\_TERC” estiver preenchido com valor > que ‘0’ \.

__Lista do Beneficiários Não Informados: __Apresentar a lista de “Beneficiários Não\-Informados”, sempre que o Campo ‘VLR\_IR\_RETIDO’ for igual à ‘0’, __E__ o Campo “VLR\_DED\_INSS\_TERC” estiver preenchido com valor > que ‘0’\.

__CPF/CNPJ:  __Recuperar informação do Campo “CPF\_CGC” da tabela X04\_PESSOA\_FIS\_JUR;

__Nome/Razão Social: __Recuperar informação do Campo “RAZAO\_SOCIAL” da tabela X04\_PESSOA\_FIS\_JUR;

__Cod\. Retenção: __Recuperar informação do Campo “COD\_DARF” da tabela X53\_RETENCAO\_IRRF;

__ReNdimentos: __Recuperar informação do Campo “VLR\_BRUTO” da tabela X53\_RETENCAO\_IRRF;

__MFS81694__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


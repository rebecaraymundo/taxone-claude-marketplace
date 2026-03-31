# MTZ_EFD_Geracao_Apuracao_Estoque_Rest_Compl_ST_MG

- **Fonte:** MTZ_EFD_Geracao_Apuracao_Estoque_Rest_Compl_ST_MG.docx
- **Modificado:** 2024-07-03
- **Tamanho:** 82 KB

---

THOMSON REUTERS

Módulo Sped Fiscal 

Geração do arquivo digital – Portaria 165 – 27/11/2018

__Geração da Apuração de Estoque, Restituição e Complementação ST \- MG__

 

__Localização__: Menu Sped, Módulo EFD \- Escrituração Fiscal Digital, item Pré\-Geração à Ressarcimento ICMS\-ST – \(Específico MG\) à Geração do Arquivo Digital \(Portaria 165/2018\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS422889

Andréa Rocha

Criação da geração do arquivo digital da Apuração de Estoque, Restituição e Complementação ST \- MG, conforme definições da  Portaria 165 – 27/11/2018\.

27/02/2023 \(criação do documento\)

MFS570956

Andréa Rocha

Inclusão de um parâmetro para definir se será gerado um arquivo único para os estabelecimentos selecionados para a geração\.

03/10/2023

MFS570966

Graciela Soares

Inclusão de um parâmetro para gerar um arquivo particionado de Restituição ST, quando a opção sleecionada for igual a “4”, ativar o check\-box para gerar arquivos separados considerando a parametrização de Operações\.

20/05/2024

Sumário

[1\.	Parâmetros da Tela	3](#_Toc128588343)

[2\.	Recuperação dos Dados do arquivo 4 – Restituição ST	4](#_Toc128588344)

[3\.	Geração do arquivo 4 – Restituição ST	4](#_Toc128588345)

[4\.	Recuperação dos Dados do arquivo 5 – Complementação e/ou Restituição ST	7](#_Toc128588346)

[5\.	Geração do arquivo 5 – Complementação e/ou Restituição ST	7](#_Toc128588347)

# <a id="_Toc128588343"></a>Parâmetros da Tela 

Esta geração foi criada com o objetivo de gerar o arquivo digital da Apuração de Estoque, Restituição e Complementação ST – MG, conforme definições da Portaria SRE n° 165, de 27 de novembro de 2018\. Conforme alinhado com o PM \(Marcos de Paula\), será criada a funcionalidade para a geração dessas informações em excel, mas somente serão geradas as finalidades 4 \(“4 – Restituição ST \(ART\. 23 – ANEXO XV\)”\) e 5 \(“5 – Complementação e/ou Restituição ST \(ARTS\. 31\-A a 31\-I DO ANEXO XV\)”\)\.

A geração do arquivo digital tem como pré\-requisito a carga da SAFX296, que pode ser feita através da pré\-geração do ressarcimento ICMS\-ST/MG ou através da importação ou manutenção da SAFX296\.

Serão gerados dois arquivos no formato excel, um arquivo para a finalidade 4 – Restituição ST e outro arquivo para a finalidade 5 – Complementação e/ou Restituição ST\.

Parâmetros da geração:

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Período

Data

S

S

Neste campo o usuário informará o mês/ano do período da geração

MFS422889

Finalidade

Radiobutton

S

S

Opção = Todos

Este campo é do tipo Radiobutton, com as seguintes opções:

\- Todos;

\- 4 – Restituição ST;

\- 5 – Complementação e/ou Restituição ST

MFS422889

Gerar arquivo particionado por operações 

Radiobutton

S

N

Este campo é do tipo Checkbox\.

Default = desmarcado

Habilitar campo apenas quando a opção do campo Finalidade for igual a “4”

MFS570966

Gerar Arquivo Único por Finalidade

Radiobutton

S

N

Este campo é do tipo Checkbox\.

Default = desmarcado

MFS570956

Estabelecimentos

Alfanumérico

S

S

Neste campo será exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário e que seja da UF = MG\.

Deverá ter a opção de selecionar todos os estabelecimentos\.

MFS422889

# <a id="_Toc475630413"></a><a id="_Toc128588344"></a>Recuperação dos Dados do arquivo 4 – Restituição ST

Este processo irá recuperar as informações da tabela de Informações Complementares das Operações Sujeitas ao ST \(SAFX296\) e da tabela de cadastro do produto \(SAFX2013\), que atendam aos seguintes critérios:

- Empresa igual a empresa selecionada na geração;
- Estabelecimento igual ao estabelecimento selecionado na geração;
- A data fiscal da nota deve ser referente ao período \(mês/ano\) informado em tela;
- O Código Motivo \(Saídas\) deve ser igual “MG200”;

       Os registros recuperados serão agrupados por empresa, estabelecimento e produto, sendo assim as suas quantidades e valores serão totalizados\.

# <a id="_Toc128588345"></a>Geração do arquivo 4 – Restituição ST

\[MFS570956\] Inclusão da geração do arquivo único por finalidade

\[MFS570966\] Inclusão da geração do arquivo particionados por operações

Regra de criação do nome do arquivo em excel:

Se o parâmetro “Gerar Arquivo Único por Finalidade” estiver desmarcado

Se o parâmetro “Gerar arquivo particionado por operações” estiver marcardo o arquivo deve ser gerado particionado por Operações\. 

As operações estão parametrizadas no Menu: Parâmetros >> Ressarcimento ICMS\-ST >> Operações >> CFOP / Natureza de Operação\.

Identificar as operações parametrizadas no parâmetro acima e gerar os aquivos por tipo de operação\.

     Num\_processo\_Estab\_MMAAAA\_Fin4, onde:

            Num\_processo: representa o número do processo da geração\.

            Estab: representa o código do estabelecimento da geração\.

            MMAAAA: representa o período da geração\.

	       Fin4: representa o tipo de arquivo que está sendo gerado, 4 – Restituição ST\.

Ex:00000001\_001MG\_012023\_Fin4\.XLS   


Quando a geração do arquivo ocorrer particionado por tipo de operação, necessário acrescentar o código de operação na  nomenclatura do arquivo gerado\. EX:  00000001\_001MG\_012023\_Fin4\_767\.XLS

Se o parâmetro “Gerar Arquivo Único por Finalidade” estiver marcado

Se o parâmetro “Gerar arquivo particionado por operações” estiver marcardo o arquivo deve ser gerado particionado por Operações\. 

As operações estão parametrizadas no Menu: Parâmetros >> Ressarcimento ICMS\-ST >> Operações >> CFOP / Natureza de Operação\.

Identificar as operações parametrizadas no parâmetro acima e gerar os aquivos por tipo de operação\.

     Num\_processo\_MMAAAA\_Fin4, onde:

            Num\_processo: representa o número do processo da geração\.

            MMAAAA: representa o período da geração\.

	       Fin4: representa o tipo de arquivo que está sendo gerado, 4 – Restituição ST\.

Ex: 00000001\_012023\_Fin4\.XLS

Quando a geração do arquivo ocorrer particionado por tipo de operação, necessário acrescentar o código de operação na nomenclatura do arquivo gerado\. EX:  00000001\_012023\_Fin4\_767\.XLS

Layout do arquivo em excel:

CD\_SPED

Código SPED/Sintegra

Campo alfanumérico de 60 posições\.

Preencher com o campo 13\-Código do Produto da SAFX296\.

CD\_NCM

Código NCM

Campo alfanumérico de 8 posições\.

Preencher com o campo 05\-Código NBM da SAFX2013\.

CD\_EAN13

Código EAN\-13

Campo alfanumérico de 13 posições\.

Preencher com o campo 40\-Código de Barras da SAFX2013\.

DS\_PRODMERC

Descrição do produto/mercadoria NCM

Campo alfanumérico de 80 posições\.

Preencher com o campo 04\-Descrição do Produto da SAFX2013\.

TP\_UNIDADE

Tipo de Unidade

Campo alfanumérico de 30 posições\.

Preencher com o campo 20\-Unidade de Medida Padrão da SAFX2013\.

QT\_PROD\_FGP

Quantidade

Campo numérico de 15 posições, sendo 4 casas decimais\.

Preencher com o campo 16\-Quantidade Convertida da SAFX296\.

VR\_ICMS\_FGP\_OPC

Valor ICMS OP\. Próprias

Campo numérico de 15 posições, sendo 2 casas decimais \.

Preencher com o campo 26\-Valor Unitário ICMS Estoque Conv\. \(Saídas\) \* campo 16\-Quantidade Convertida da SAFX296\.

Obs\.: O resultado do cálculo deve ser arredondado em 2 casas decimais\.

VR\_ICMS\_FGP\_STR

Valor ICMS\-ST

Campo numérico de 15 posições, sendo 2 casas decimais\.

Preencher com o campo 29\-Valor Unitário ICMS\-ST Conv\. Rest\. \(Saídas\) da SAFX296 \* campo 16\-Quantidade Convertida da SAFX296\.

Obs\.: O resultado do cálculo deve ser arredondado em 2 casas decimais\.

VR\_FEM\_FGP\_REST

Valor FEM

Campo numérico de 15 posições, sendo 2 casas decimais\.

Preencher com o campo 30\-Valor Unitário FCP\-ST Conv\. Rest\. \(Saídas\) da SAFX296 \* campo 16\-Quantidade Convertida da SAFX296\.

Obs\.: O resultado do cálculo deve ser arredondado em 2 casas decimais\.

# <a id="_Toc128588346"></a>Recuperação dos Dados do arquivo 5 – Complementação e/ou Restituição ST

Este processo irá recuperar as informações da tabela de Informações Complementares das Operações Sujeitas ao ST \(SAFX296\) e da tabela de cadastro do produto \(SAFX2013\), que atendam aos seguintes critérios:

- Empresa igual a empresa selecionada na geração;
- Estabelecimento igual ao estabelecimento selecionado na geração;
- A data fiscal da nota deve ser referente ao período \(mês/ano\) informado em tela;
- O Código Motivo \(Saídas\) deve ser igual “MG100” ou “MG300”;

Os registros recuperados serão agrupados por empresa, estabelecimento e produto, sendo assim as suas quantidades e valores serão totalizados\.

# <a id="_Toc128588347"></a>Geração do arquivo 5 – Complementação e/ou Restituição ST

\[MFS570956\] Inclusão da geração do arquivo único por finalidade

Regra de criação do nome do arquivo em excel:

Se o parâmetro “Gerar Arquivo Único por Finalidade” estiver desmarcado

 Num\_processo\_Estab\_MMAAAA\_Fin5, onde:

            Num\_processo: representa o número do processo da geração\.

            Estab: representa o código do estabelecimento da geração\.

            MMAAAA: representa o período da geração\.

	       Fin5: representa o tipo de arquivo que está sendo gerado, 5 – Complementação e/ou Restituição ST\.

Se o parâmetro “Gerar Arquivo Único por Finalidade” estiver marcado

 Num\_processo\_MMAAAA\_Fin5, onde:

            Num\_processo: representa o número do processo da geração\.

            MMAAAA: representa o período da geração\.

	       Fin5: representa o tipo de arquivo que está sendo gerado, 5 – Complementação e/ou Restituição ST\.

Ex: 00000001\_012023\_Fin5\.XLS

Layout do arquivo em excel:

CD\_SPED

Código SPED/Sintegra

Campo alfanumérico de 60 posições\.

Preencher com o campo 13\-Código do Produto da SAFX296\.

CD\_NCM

Código NCM

Campo alfanumérico de 8 posições\.

Preencher com o campo 05\-Código NBM da SAFX2013\.

CD\_EAN13

Código EAN\-13

Campo alfanumérico de 13 posições\.  O contéudo deve ser truncado em 13 posições\.

Preencher com o campo 40\-Código de Barras da SAFX2013\.

DS\_PRODMERC

Descrição do produto/mercadoria NCM

Campo alfanumérico de 80 posições\.

Preencher com o campo 04\-Descrição do Produto da SAFX2013\.

TP\_UNIDADE

Tipo de Unidade

Campo alfanumérico de 30 posições\.

Preencher com o campo 20\-Unidade de Medida Padrão da SAFX2013\.

QT\_PROD\_ST\_COMP

Quantidade \- Complementação

Campo numérico de 15 posições, sendo 4 casas decimais\.

Se campo 31\-Valor Unitário ICMS\-ST Conv\. Compl\. \(Saídas\) da SAFX296  for maior que zero

     Preencher com o campo 16\-Quantidade Convertida da SAFX296\.

VR\_ICMS\_ST\_COMP

Valor ICMS\-ST \- Complementação

Campo numérico de 15 posições, sendo 2 casas decimais\.

Preencher com o campo 31\-Valor Unitário ICMS\-ST Conv\. Compl\. \(Saídas\) da SAFX296  \* campo 16\-Quantidade Convertida da SAFX296\.

Obs\.: O resultado do cálculo deve ser arredondado em 2 casas decimais\.

VR\_FEM\_ST\_COMP

Valor do FEM \- Complementação

Campo numérico de 15 posições, sendo 2 casas decimais\.

Preencher com o campo 32\-Valor Unitário FCP\-ST Conv\. Compl\. \(Saídas\) da SAFX296  \* campo 16\-Quantidade Convertida da SAFX296\.

Obs\.: O resultado do cálculo deve ser arredondado em 2 casas decimais\.

QT\_PROD\_ST\_REST

Quantidade \- Restituição

Campo numérico de 15 posições, sendo 2 casas decimais\.

Se o campo 29\-Valor Unitário ICMS\-ST Conv\. Rest\. \(Saídas\) da SAFX296 for maior que zero

      Preencher com o campo 16\-Quantidade Convertida da SAFX296\.

VR\_ICMS\_ST\_RET

Valor do ICMS\-ST \- Restituição

Campo numérico de 15 posições, sendo 2 casas decimais\.

Preencher com o campo 29\-Valor Unitário ICMS\-ST Conv\. Rest\. \(Saídas\) da SAFX296 \* campo 16\-Quantidade Convertida da SAFX296\.

Obs\.: O resultado do cálculo deve ser arredondado em 2 casas decimais\.

VR\_FEM\_ST\_REST

Valor do FEM \- Restituição

Campo numérico de 15 posições, sendo 2 casas decimais\.

Preencher com o campo 30\-Valor Unitário FCP\-ST Conv\. Rest\. \(Saídas\) da SAFX296 \* campo 16\-Quantidade Convertida da SAFX296\.

Obs\.: O resultado do cálculo deve ser arredondado em 2 casas decimais\.


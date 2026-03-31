# MTZ_ICMS_Convenio_115_Quantidade_Documentos_Fiscais_por_Volume

- **Fonte:** MTZ_ICMS_Convenio_115_Quantidade_Documentos_Fiscais_por_Volume.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 66 KB

---

THOMSON REUTERS

ICMS

Geração do Arquivo Magnético Convênio ICMS 115

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4281

Julyana Perrucini

Criação de parâmetro para quantidade de documento fiscal por volume \(quebra de arquivo\)

MFS17746

Vânia Mattos

Alteração do Convênio 29/2018 \(ver __RN02__\)

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

__RN01__

__Cálculo da quantidade de documentos fiscais por volume \(arquivo\):__

a\-\) Contar o total de notas existentes na x42 para empresa, estabelecimento e período \(filtrando pela data fiscal\) informados na tela de geração, em que o \[modelo da NF for diferente de ‘06’\] OU \[o modelo for igual a ‘06’ E a UF do estabelecimento for diferente de ‘SP’\];

b\-\) Contar o total de notas existentes na x42 para empresa, estabelecimento e período \(filtrando pela data de vencimento\) informados na tela de geração, em que o \[modelo da NF for igual a ‘06’ E o código do estado do estabelecimento for igual a ‘SP’\]\.

O total de NF’s do período \(t\) será = \(a\+b\):

__1ª ETAPA:__

Se o parâmetro “Arquivo com qtde de cem mil” estiver marcado na tela de geração, o sistema deve quebrar em volumes de até cem mil notas caso o total de NF’s \(t\) seja de até 1 milhão de registros\.

__OU__

__2ª ETAPA:__

Se o parâmetro “Arquivo com qtde específica” estiver marcado na tela de geração, verificar a quantidade informada no campo “Qtde Específica”, o sistema deve quebrar em volumes de até <<quantidade específica informada>> caso o total de NF’s \(t\) seja de até 1 milhão de registros\.

__OU__

__3ª ETAPA:__

Será quebrado em volumes de até 1 milhão de notas caso o total de NF’s \(t\) seja maior que 1 milhão de registros\.

Ou seja, quando a quantidade de NFs do período for menor que um milhão, quebra\-se em arquivos de cem mil se estiver com o parâmetro da 1ª ETAPA ou quebra\-se em arquivos de acordo com o que o usuário informar na Qtde Específica se estiver com o parâmetro da 2ª ETAPA\. Quando for maior que um milhão, serão realizadas quebras de um em um milhão, sendo que se houver um saldo de NFs menores que um milhão, este saldo será gerado em um único arquivo\.

__Exemplos: __

Da 1ª ETAPA:

Parâmetro __“Arquivo com qtde de cem mil”__ marcado na tela de geração\.

- Existe uma quantidade de 733\.000 NFs processadas, então serão gerados 8 arquivos:
	- 7 arquivos contendo 100\.000 NFs
	- 1 arquivo contendo 33\.000 Nfs

Da 2ª ETAPA:

Parâmetro __“Arquivo com qtde específica”__ marcado na tela de geração e o campo __“Qtde Específica”__ informado com 500\.000

- Existe uma quantidade de 733\.000 NFs processadas, então serão gerados 2 arquivos:
	- 1 arquivo contendo 500\.000 NFs
	- 1 arquivo contendo 233\.000 Nfs

Da 3ª ETAPA:

- Se atingir uma quantidade de 5\.344\.000 NFs, então serão gerados 6 arquivos:
- 5 arquivos contendo um milhão de NFs
- 1 arquivo contendo 344\.000 mil notas

__Atenção: __Quando o usuário optar pela geração única, ou seja, escolhendo um ou mais estabelecimentos o processo de geração, o cálculo não será afetado\. A rotina deve continuar com as regras atuais\.

__Atenção \(MFS17746\): __Esta regra de geração dos volumes pode ser alterada a partir do mês de Junho/2018, sempre que a numeração das notas for reiniciada no meio do período\. Ver detalhes na RN02\. 

__OS4281__

__RN02__

__Alteração do Convênio 29/2018 \(MFS17746\):__ Conforme alteração feita no item 2\.1\.2, sempre que a sequência de numeração das notas for reiniciada, em qualquer dia do período, haverá a “quebra” do volume\.

A partir do mês __Junho/2018 __\(conforme a cláusula quinta do Convênio 29/2018\), a geração dos arquivos do Convênio passa a efetuar o procedimento descrito a seguir *\(para períodos anteriores a este, o procedimento não se aplica, e a geração continua a gerar os volumes apenas com base na RN01\):*

Sempre que a sequência de numeração das notas for reiniciada \(independente disso ocorrer no início, no meio ou no final de um período\), será feita a “quebra” do arquivo em um novo volume\. 

Ou seja, sempre que surgir um documento fiscal de número 1, será finalizado o volume em curso, e iniciado um novo volume\.

Exemplo:  


__Data de Emissão__

__Número do Documento__

01/04/2018

   999\.999\.996

05/04/2018

   999\.999\.997

06/04/2018

   999\.999\.998

10/04/2018

   999\.999\.999

15/04/2018

   000\.000\.001

20/04/2018

   000\.000\.002

25/04/2018

   000\.000\.003

27/04/2018

   000\.000\.004

Neste exemplo simples, na quinta nota emitida no mês a numeração foi reiniciada\. Assim, esta nota de número 1 deve “abrir” um novo volume de arquivo, mesmo que o volume anterior contenha poucas notas\.

Então teríamos:

Volume 1 – Notas 999\.999\.996 a nota 999\.999\.999

Volume 2 – Notas 000\.000\.001 a nota 000\.000\.004

__Para efetuar este procedimento, é importante que a recuperação das notas de cada Modelo / Série seja feita em ordem de data de emissão e número de documento__\.

*\(Lembrando que a geração do Conv\. 115 já é feita separadamente por Modelo e Série, e assim, cada arquivo, com seus respectivos volumes, só contém documentos de uma único Modelo e Série\)*

__IMPORTANTE: __Observar que as regras básicas sobre a quebra dos volumes, conforme descrito na __RN01__, se mantêm\. No entanto, sempre que ocorrer o reinicio da numeração, a regra __RN02__ se sobrepõe as demais regras\. Ou seja, o procedimento de partir para um novo volume sempre que a numeração for reiniciada, será realizado independente das outras regras, e assim, o documento de número 1 iniciará um novo volume de arquivo\. 

__MFS17746__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


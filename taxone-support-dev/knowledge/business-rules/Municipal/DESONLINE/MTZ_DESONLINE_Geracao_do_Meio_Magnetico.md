# MTZ_DESONLINE_Geracao_do_Meio_Magnetico

- **Fonte:** MTZ_DESONLINE_Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2025-11-25
- **Tamanho:** 94 KB

---

THOMSON REUTERS

Municipal 

 Serviços Tomados e Prestados

__Geração do Meio Magnético – DES ONLINE__

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS16077

João Henrique

Criação do município de Cachoeirinha \-RS no validador DES ONLINE\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN01

__Regra p/ inclusão do novo módulo no Manager:__

O novo módulo Cachoeirinha deve ficar localizado no grupo “Municipal”\.

Descrição do módulo Cachoeirinha: *“Consiste na entrega das informações sobre os serviços tomados e prestados do município de Cachoeirinha”*\.

MFS16077

RN02

__Regra p/ abertura do novo módulo no Manager:__

Caso esteja selecionado no Manager um estabelecimento que não pertença à UF “RS” e ao código de município do IBGE igual a “3103” \(Cachoeirinha\), o sistema abre o módulo, porém exibe a seguinte mensagem de alerta:

“Este estabelecimento não pertence ao município de Cachoeirinha, Rio Grande do Sul\. Alguns dados não estarão disponíveis\. Deseja continuar?”

Na mensagem são exibidos os botões “Sim” e “Não”\. Caso o usuário clique no botão “Sim” o módulo é aberto normalmente\. Caso o usuário clique no botão “Não” o módulo não é aberto\.

O botão “Não” é default\.

MFS16077

RN03

__Estrutura de menus do módulo DES ONLINE:__

Deverão ser criados os seguintes itens de menu no módulo DES ONLINE:

- Arquivo
- Obrigações
	- __Geração do Meio Magnético__
	- __Arquivo de Entradas de Serviços \(Const\. Civil/ Utilities/ Telecom\)__
- Janela
- Ajuda

MFS16077

RN04

__Regra de criação do nome do arquivo:__

__Serviços Tomados:__

__ST\_DESONLINE\_DDMMAAAA\.XML__, onde:

__ST\_ DESONLINE__: representa a obrigação que está sendo gerada, apenas para registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial informada na geração do arquivo\.

__\.XML__: extensão do arquivo\.

Ex: ST\_DESONLINE\_01012013\.XML

Caso o parâmetro “__Quebrar Arquivo por Data de Emissão” __estiver marcado deverá ser realizada a seguinte verificação:

Se dentro do período de geração, houver notas fiscais com data de emissão fora do período gerado, deverá haver quebra por arquivo de acordo com a competência referente à data de emissão da nota fiscal\. Esse arquivo deve conter todas as notas fiscais que tenham a mesma competência \(mesmo mês referente à data de emissão\)\.

Portanto poderão ser gravados N arquivo de acordo com as competências geradas, e nesse caso o arquivo normal também deverá ser gerado, além dos arquivos indicando competências distintas\. 

A nomenclatura desses arquivos deverá ser:

__ST\_DESONLINE\_DDMMAAAA\_MMAAAA\.XML__, onde:

__ST\_DESONLINE__: representa a obrigação que está sendo gerada, apenas para registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial informada na geração do arquivo\.

__MMAAAA:__ representa o mês da competência referente à nota fiscal gerada\.

__\.XML__: extensão do arquivo\.

Ex: ST\_ DESONLINE\_01012013\_122012\.XML

__Serviços Prestados:__

__ST\_ DESONLINE\_DDMMAAAA\.XML__, onde:

__ST\_DESONLINE__: representa a obrigação que está sendo gerada, apenas para registros de serviços tomados\.

__DDMMAAAA__: representa a data inicial informada na geração do arquivo\.

__\.XML__: extensão do arquivo\.

Ex: ST\_ DESONLINE\_01012013\.XML

__*Observação:* Este parâmetro \(Quebrar Arquivo por Data de Emissão\) será válido apenas para Notas de Serviços Tomados\.__

MFS16077

RN05

__Regra p/ tela da Geração do Meio Magnético:__

A tela de geração do meio magnético deve exibir os seguintes campos:

__Data Inicial:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o primeiro dia do mês corrente\. \(SYSDATE\)\.

__Data Final:__ deve ser exibido através de um TextBox, com a máscara DD/MM/AAAA\. O sistema deve exibir o último dia do mês corrente\. \(SYSDATE\)\.

__Gerar Serviços Prestados:__ deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Gerar Serviços Tomados:__ deve ser exibido através de um checkbox\. Deve ser exibido marcado como default\. \(Opções S = Marcado e N = Desmarcado\)

__Quebrar arquivo por Data de Emissão:__ deve ser exibido através de um checkbox\. Deve ser exibido desmarcado como default\. \(Opções S = Marcado e N = Desmarcado\)\.

__Base de Cálculo: __deve ser exibido através de um TextBox, com a máscara de valor 0,00 contendo tamanho de 15 posições\. Habilitar esse campo somente quando a opção Gerar Serviços Prestados for selecionado\.

__Estabelecimento:__ o sistema deve exibir os estabelecimentos ao município escolhido no Manager, que estejam licenciados e que o usuário possua acesso no PowerLock\.

MFS16077

RN06

__Regra p/ Geração do Arquivo Magnético__

- Todos os campos devem estar entre aspas, conforme os exemplos que serão apresentados a seguir; 
- Os campos de valores NÃO devem conter pontos ou vírgulas e têm as últimas 2\(duas\) casas para decimais; Ex: 1000\(representa o número 10,00\); 
- Deverá ser respeitado o tamanho máximo dos campos; 
- Campos de data DEVEM conter o separador "/"\. Ex: 15/02/1998 
- O CPF/CNPJ não deve conter separadores, como pontos, traços, etc\.;
- O Número da Nota não deve conter separadores, como pontos, traços, etc\. 

MFS16077

RN07

__Regra p/ Recuperar Notas Fiscais de Serviços Tomados:__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de entrada \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL <> 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência
- Não deve recuperar notas canceladas \(campo SITUACAO da tabela DWT\_DOCTO\_FISCAL <> S\)

*Observação: *Quando a nota fiscal não tiver itens não deve ser considerada\.

MFS16077

RN08

__Estrutura do Arquivo:__

<declaracao>

  <retencao cpfcnpj="88148945000104">

    <info\_retencao data\_informacao="29/06/2005" exercicio="2005"

    mes="06" observacao="observacao da entrega"

 aplicacao="N">

      <nota\_retencao data\_emissao="08/06/2005" 

      numero="1" serie="A" cpfcnpf\_prestador="40726258091"

      atividade\_desenvolvida="1516"

      descricao\_atividade="Armazenamento" numero\_servico="11"

      valor\_bruto="0500000" valor\_deducao="0200000"

      valor\_tributavel="000000300000" aliquota="300"

      valor\_retido="0009000"  

      ></nota\_retencao>

      <nota\_retencao data\_emissao="07/06/2005"

      numero="2" serie="A" cpfcnpf\_prestador="00125392000115"

      descricao\_atividade="Armazenamento" numero\_servico="11"

      atividade\_desenvolvida="1516" valor\_bruto="0500000"

      valor\_deducao="0200000" valor\_tributavel="000000300000"

      aliquota="200" valor\_retido="0006000"></nota\_retencao>

    </info\_retencao>

    <info\_retencao data\_informacao="29/03/2005" exercicio="2005"

    mes="02" observacao="observacao da entrega" aplicacao="N">

      <nota\_retencao data\_emissao="07/03/2005" numero="1" serie="A" cpfcnpf\_prestador="00125392000115"

      descricao\_atividade="Armazenamento" numero\_servico="11"

      atividade\_desenvolvida="1516" valor\_bruto="0800000"

      valor\_deducao="0200000" valor\_tributavel="000000600000"

      aliquota="3" valor\_retido="000180" </nota\_retencao>

    </info\_retencao>

  </retencao>

</declaracao>

MFS16077

RN09

__Regra para tag <declaracao> __

Tag __<declaracao__ Indica o início da Declaração\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TAG e informação obrigatória\.

MFS16077

RN10

__Regra para tag <retencao cpfcnpj="">__

Tag __<retencao__ Indica o início da Declaração para determinado contribuinte\.

__*Informação que irá compor a Tag:*__

__cpfcnpj__

Formato: 99999999999999

Tipo: Numérico

Tamanho: 14

Preencher com o conteúdo do campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento que está sendo gerado o arquivo magnético\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TAG e informação obrigatória\.

MFS16077

RN11

__Regra para tag <info\_retencao data\_informacao="" exercicio=""__

__    mes="" observacao="" aplicacao="">__

Tag __<info\_retencao __Indica o início das informações da retenção, indica a competência, pode\-se ter mais de uma por declaração\.

__*Informações que irão compor a Tag:*__

__data\_informacao__

Formato: DD/MM/AAAA

Tipo: Data

Tamanho: \-

Preencher com o conteúdo do campo DATA\_FISCAL da tabela DWT\_DOCTO\_FISCAL \(campo 20 da SAX07\)\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__exercicio__

Formato: 9999

Tipo: Numérico

Tamanho: 04

Preencher com o ANO do conteúdo do campo “Data Inicial” da tela de geração do meio magnético\. *Exemplo:* 01/01/__2005__\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__mes__

Formato: 99

Tipo: Numérico

Tamanho: 02

Preencher com o MÊS do conteúdo do campo “Data Inicial” da tela de geração do meio magnético\.* Exemplo:* 01/__01__/2005\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__observacao__

Formato: XXXXXXXXX\.\.\.

Tipo: Alfanumérico

Tamanho: 300

Esse campo deverá ser gerado em branco, pois não é obrigatório\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__aplicacao__

Formato: X

Tipo: Alfanumérico

Tamanho: 01

Preencher fixo com “N”\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TAG e informações obrigatórias, exceto a informação observacao\.

MFS16077

RN12

__Regra para tag <nota\_retencao data\_emissao=""__

__      numero="" serie="" cpfcnpf\_prestador=""__

__      atividade\_desenvolvida=""__

__      descricao\_atividade="" numero\_servico=""__

__      valor\_bruto="" valor\_deducao=""__

__      valor\_tributavel="" aliquota=""__

__      valor\_retido="" codigo\_obra="" numero\_projeto= ""__

__      ></nota\_retencao>__

Tag __ <nota\_retencao __Indica o início de informações sobre as notas fiscais retidas nas competências\.

__*Informações que irão compor a Tag:*__

__data\_emissao__

Formato: DD/MM/AAAA

Tipo: Data

Tamanho: \-

Preencher com o conteúdo do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAX07\)\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__numero__

Formato: 9999999999

Tipo: Numérico

Tamanho: 10

Preencher com o conteúdo do campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\)\.

__Tratamento:__

- Considerar as 10 primeiras posições;
- Se o campo ultrapassar 10 posições, emitir a mensagem de log: “O campo número do documento <<Nº documento>> ultrapassou o tamanho máximo permitido \(10 posições\)”\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__serie__

Formato: XX

Tipo: Alfanumérico

Tamanho: 02

Preencher com o conteúdo do campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__Tratamento:__

- Considerar as 2 primeiras posições;
- Se o campo ultrapassar 2 posições, emitir a mensagem de log: “O campo série do documento <<Nº documento>> ultrapassou o tamanho máximo permitido \(2 posições\)”\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__cpfcnpf\_prestador__

Formato: 99999999999 ou 99999999999999

Tipo: Numérico

Tamanho: até 14

Preencher com o conteúdo do campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR \(campo 06 da SAFX04\) referente o prestador cadastrado na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido \(em caso de prestador com situação especial\), preencher com zeros com 14 posições\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__atividade\_desenvolvida__

Formato: 999999

Tipo: Alfanumérico

Tamanho: 06

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\. Não é necessário preencher o restante do campo com espaços em branco\.

__Tratamento:__

- Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 0 \(zero\) e emitida a mensagem de log: *“Erro: Favor preencher o código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal <<NF>>, <<Série>>, <<Data Fiscal>>”*\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__descricao\_atividade__

Formato: XXXXXXXX\.\.\.

Tipo: Alfanumérico

Tamanho: 200

Preencher com o conteúdo do campo DSC\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\. Não é necessário preencher o restando do campo com espaços em branco\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__numero\_servico__

Formato: 99

Tipo: Numérico

Tamanho: 02

Preencher com:

__“33” – Imposto devido em Cachoeirinha, com obrigação de retenção na fonte\.__

- Se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) e o campo UF da tabela X04\_PESSOA\_FIS\_JUR \(campo 19 da SAFX04\) referente à PFJ cadastrada na nota fiscal for igual a “EX”\.

__“32” – Imposto devido em Cachoeirinha, sem obrigação de retenção na fonte\.__

- Se o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) e o campo UF da tabela X04\_PESSOA\_FIS\_JUR \(campo 19 da SAFX04\) referente à PFJ cadastrada na nota fiscal for igual a “EX”\.

__“28” – Não Tributável\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “10” e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for diferente do município do estabelecimento; __OU__
- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “11” e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for diferente do município do estabelecimento\.

__“24” – Imposto devido em Cachoeirinha, sem obrigação de retenção na fonte\.__

- Se o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) e o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV \(campo 58 da SAFX09\) estiver preenchido e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for diferente do município do estabelecimento e o campo\.

__“23” – Imposto devido em Cachoeirinha, com obrigação de retenção na fonte\.__

- Se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) e o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV \(campo 58 da SAFX09\) estiver preenchido e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for diferente do município do estabelecimento e o campo\.

__“22” – Imposto devido fora de Cachoeirinha, sem obrigação de retenção na fonte\.__

- Se o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for diferente do município do estabelecimento e o campo\.

__“21” – Imposto devido fora de Cachoeirinha, com obrigação de retenção na fonte\.__

- Se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for diferente do município do estabelecimento e o campo\.

__“18” – Não Tributável \(Casos de Isenção, ou Suspensão de Exigibilidade\)\.__

- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “10” e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for igual ao município do estabelecimento; __OU__
- Se o campo IND\_CLASSE\_PFJ da tabela X04\_PESSOA\_FIS\_JUR \(campo 26 da SAFX04\) = “11” e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for igual ao município do estabelecimento\.

__“12” – Imposto devido em Cachoeirinha, sem obrigação de retenção na fonte\.__

- Se o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for igual ao município do estabelecimento\.

__“11” – Imposto devido em Cachoeirinha, com obrigação de retenção na fonte\.__

- Se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for igual ao município do estabelecimento\. 

__Tratamento:__

- Se nenhuma das situações acima for atendida, emitir uma mensagem de log: *“Erro: Favor verificar as operações de acordo com a LISTAGEM DE OPERAÇÕES ISSQN MUNICÍPIO DE CACHOEIRINHA com orientação no manual operacional do módulo <<NF>>, <<Série>>, <<Data Fiscal>>”\.*

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__valor\_bruto__

Formato: 999999999999999

Tipo: Valor

Tamanho: 15

Preencher com o conteúdo do campo VLR\_TOT da tabela DWT\_ITENS\_SERV \(campo 15 da SAFX09\)\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 3 para ser preenchido de acordo com o tamanho exigido no layout\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__valor\_deducao__

Formato: 999999999999999

Tipo: Valor

Tamanho: 15

Preencher com o conteúdo do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV \(campo 59 da SAFX09\)\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 3 para ser preenchido de acordo com o tamanho exigido no layout\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__valor\_tributavel__

Formato: 999999999999999

Tipo: Valor

Tamanho: 15

Preencher com o conteúdo do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV \(campo 33 da SAFX09\)\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 3 para ser preenchido de acordo com o tamanho exigido no layout\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__aliquota__

Formato: 9999999999

Tipo: Valor

Tamanho: 10

Preencher com o conteúdo do campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV \(campo 32 da SAFX09\)\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__valor\_retido__

Formato: 9999999999

Tipo: Valor

Tamanho: 10

Preencher com o conteúdo do campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV \(campo 58 da SAFX09\)\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 7 para ser preenchido de acordo com o tamanho exigido no layout\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TAG e informações obrigatórias, exceto as informações serie, valor\_deducao, valor\_tributavel, valor\_retido, aliquota\.

MFS16077

RN13

__Regra para tag ></nota\_retencao>__ Tag relacionada ao encerramento da formatação do arquivo e que deve receber as informações das notas tomadas declaradas com o texto fixo: __></nota\_retencao>__\.

MFS16077

RN14

__Regra para tag </info\_retencao> __Tag relacionada ao encerramento da formatação do arquivo e que deve receber as informações das notas tomadas declaradas com o texto fixo: __</info\_retencao>__\.

MFS16077

RN15

__Regra para tag </retencao> __Tag relacionada ao encerramento da formatação do arquivo e que deve receber as informações das notas tomadas declaradas com o texto fixo: __</retencao>__\.

MFS16077

RN16

__Regra para tag </declaracao> __Tag relacionada ao encerramento da formatação do arquivo e que deve receber as informações das notas tomadas declaradas com o texto fixo: __</declaracao>__\.

MFS16077

RN17

__Regra p/ Recuperar Notas Fiscais de Serviços Prestados:__

Considerar todas as notas fiscais de serviço com as seguintes características:

- Notas fiscais de saída \(campo MOVTO\_E\_S da tabela DWT\_DOCTO\_FISCAL = 9\)
- Classificação da nota fiscal = 2 ou 3
- Empresa e estabelecimento escolhidos na tela de geração
- Data fiscal da nota dentro do período de referência

Para cada TAG <informacao poderá ter várias notas fiscais agrupando\-as por alíquota \(Ver RN23\)\.

*Observação: *Quando a nota fiscal não tiver itens não deve ser considerada\.

MFS16077

RN18

__Estrutura do Arquivo:__

<declaracao>

  <empresa nome="Nome da empresa 2" inscricao="3"

  cpfcnpj="00000000000000">

    <informacao exercicio="2009" mes="04"

    atividade\_desenvolvida="3872" aliquota="2000" basecalculo=""

    observacao="OPCIONAL>

      <nota data\_emissao="20/04/2009" numero="3" serie="A"

      valor\_tributavel="10000" situacao="A" valor\_bruto="0"

      valor\_deducao="0" modelo="01" cpfcnpj\_tomador="00000000000"

      numero\_servico="52" />

      <nota data\_emissao="30/04/2009" numero="4" serie="A"

      valor\_tributavel="20000" situacao="N" valor\_bruto="0"

      valor\_deducao="0" modelo="01" cpfcnpj\_tomador="00000000000"

      numero\_servico="52" />

    </informacao>

    <informacao exercicio="2009" mes="04" aliquota="0500"

    basecalculo="" quantidade\_issfixo="200" observacao="OPCIONAL">

      <nota data\_emissao="20/04/2009" numero="3" serie=""

      valor\_tributavel="15000" situacao="N" valor\_bruto="0"

      valor\_deducao="0" modelo="01" cpfcnpj\_tomador="00000000000"

      numero\_servico="52" />

      <nota data\_emissao="30/04/2009" numero="4" serie=""

      valor\_tributavel="12000" situacao="R" valor\_bruto="0"

      valor\_deducao="0" modelo="01" cpfcnpj\_tomador="00000000000"

      numero\_servico="51/>

    </informacao>

  </empresa>

</declaracao>

__*Quando não houver movimentação para o período gerado, deve ser gerado o arquivo com a seguinte estrutura:*__

<?xml version="1\.0" encoding="iso\-8859\-1"?>

<declaracao>

<empresa nome="TESTE" inscricao="100" cpfcnpj="12345678000123">

<informacao exercicio="2014" mes="02" atividade\_desenvolvida="416" aliquota="200" basecalculo="0" observacao=""></informacao>

</empresa>

</declaracao>

__Atenção: __Os campos atividade\_desenvolvida, aliquota deveram ser gerados sem informação para o arquivo sem movimentação\. 

MFS16077

RN19

__Regra para tag <declaracao> __

Tag __<declaracao__ Indica o início da Declaração\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TAG e informação obrigatória\.

MFS16077

RN20

__Regra para tag <empresa nome="" inscricao=""__

__  cpfcnpj="">__

Tag __<empresa __Indica a abertura da guia por empresa\.

__*Informações que irão compor a Tag:*__

__nome__

Formato: XXXXXXXXXX\.\.\.

Tipo: Alfanumérico

Tamanho: 100

Preencher com o conteúdo do campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO referente ao estabelecimento que está sendo gerado o arquivo magnético\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__inscricao__

Formato: 9999999999

Tipo: Numérico

Tamanho: 10

Preencher com o conteúdo do campo INSC\_MUNICIPAL da tabela ESTABELECIMENTO referente ao estabelecimento que está sendo gerado o arquivo magnético\.

__Tratamento:__

- Considerar as 10 primeiras posições da inscrição cadastrada;
- Se o campo não estiver preenchido, emitir uma mensagem padrão de log\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__cpfcnpj__

Formato: 99999999999999

Tipo: Numérico

Tamanho: 14

Preencher com o conteúdo do campo CGC da tabela ESTABELECIMENTO referente ao estabelecimento que está sendo gerado o arquivo magnético\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TAG e informações obrigatórias\.

MFS16077

RN21

__Regra para tag <informacao exercicio="" mes=""__

__    atividade\_desenvolvida="3872" aliquota="2000" basecalculo=""__

__    observacao="">__

Tag __<informacao __Indica a abertura do movimento informado\.

__*Informações que irão compor a Tag:*__

__exercicio__

Formato: 9999

Tipo: Numérico

Tamanho: 04

Preencher com o ANO do conteúdo do campo “Data Inicial” da tela de geração do meio magnético\. *Exemplo:* 01/01/__2005__\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__mes__

Formato: 99

Tipo: Numérico

Tamanho: 02

Preencher com o MÊS do conteúdo do campo “Data Inicial” da tela de geração do meio magnético\.* Exemplo:* 01/__01__/2005\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__atividade\_desenvolvida__

Formato: 999999

Tipo: Alfanumérico

Tamanho: 06

Preencher com o conteúdo do campo COD\_SERV\_LEI\_116 da tabela DWT\_SERVICO\_LEI\_116 referente ao serviço cadastrado na SAFX2018 e vinculado ao item da nota fiscal\. Não é necessário preencher o restante do campo com espaços em branco\.

__Tratamento:__

- Se o código de serviço da lei 116 não estiver cadastrado na SAFX2018, deverá ser gravado com 0 \(zero\) e emitida a mensagem de log: *“Erro: Favor preencher o código da Lei 116 no cadastro do serviço para o serviço informado na nota fiscal <<NF>>, <<Série>>, <<Data Fiscal>>”*\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__aliquota__

Formato: 9999

Tipo: Valor

Tamanho: 04

Preencher com o conteúdo do campo ALIQ\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV \(campo 32 da SAFX09\)\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 7 antes da casa decimal e ignorar as 2 últimas posições após a casa decimal para ser preenchido de acordo com o tamanho exigido no layout\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__basecalculo__

Formato: 999999999999999

Tipo: Valor

Tamanho: 15

Preencher com o conteúdo informado no campo Base de Cálculo da tela de parametrização\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__observacao__

Formato: XXXXXXXXX\.\.\.

Tipo: Alfanumérico

Tamanho: 200

Esse campo deverá ser gerado em branco, pois não é obrigatório

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TAG e informações obrigatórias, exceto as informações aliquota, basecalculo, observação\.

MFS16077

RN22

__Regra para tag <nota data\_emissao="" numero="" serie=""__

__      valor\_tributavel="10000" situacao="A" valor\_bruto="0"__

__      valor\_deducao="0" modelo="01" cpfcnpj\_tomador="00000000000"__

__      numero\_servico="52"/>__

__      <nota data\_emissao="30/04/2009" numero="4" serie="A"__

__      valor\_tributavel="20000" situacao="N" valor\_bruto="0"__

__      valor\_deducao="0" modelo="01" cpfcnpj\_tomador="00000000000"__

__      numero\_servico="52" />__

Tag __<informacao __Indica a abertura do movimento informado\.

__*Informações que irão compor a Tag:*__

__data\_emissao__

Formato: DD/MM/AAAA

Tipo: Data

Tamanho: \-

Preencher com o conteúdo do campo DATA\_EMISSAO da tabela DWT\_DOCTO\_FISCAL \(campo 11 da SAX07\)\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__numero__

Formato: 9999999999

Tipo: Numérico

Tamanho: 10

Preencher com o conteúdo do campo NUM\_DOCFIS da tabela DWT\_DOCTO\_FISCAL \(campo 08 da SAFX07\)\.

__Tratamento:__

- Considerar as 10 primeiras posições;
- Se o campo ultrapassar 10 posições, emitir a mensagem de log: “O campo número do documento <<Nº documento>> ultrapassou o tamanho máximo permitido \(10 posições\)”\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__serie__

Formato: XX

Tipo: Alfanumérico

Tamanho: 02

Preencher com o conteúdo do campo SERIE\_DOCFIS da tabela DWT\_DOCTO\_FISCAL\.

__Tratamento:__

- Considerar as 2 primeiras posições;
- Se o campo ultrapassar 2 posições, emitir a mensagem de log: “O campo série do documento <<Nº documento>> ultrapassou o tamanho máximo permitido \(2 posições\)”\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__valor\_tributavel__

Formato: 999999999999999

Tipo: Valor

Tamanho: 15

Preencher com o conteúdo do campo VLR\_TRIBUTO\_ISS da tabela DWT\_ITENS\_SERV \(campo 33 da SAFX09\)\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 3 para ser preenchido de acordo com o tamanho exigido no layout\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__situacao__

Formato: 9

Tipo: Numérico

Tamanho: 01

Preencher com:

__“N” – Nula ou cancelada\.__

- Se o campo SITUACAO da tabela DWT\_DOCTO\_FISCAL \(campo 30 da SAFX07\) for igual a “S”\.

__“E” – Extraviada\.__

- Se o campo IND\_NOTA\_SERVICO da tabela DWT\_DOCTO\_FISCAL \(campo 137 da SAFX07\) for igual a “E”\.

__“R” – Retida\.__

- Se o campo IND\_TP\_RET da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) estiver preenchido com “2" e se o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL \(campo 73 da SAFX07\) for igual do estabelecimento selecionado; __OU__ 
- Se o campo IND\_SUBSTITUIDO\_ISS da tabela X2098\_ALIQ\_SERVICO \(campo 06 da SAFX2098\) for igual a “N” \(para o serviço cadastrado na nota e utilizando o campo COD\_MUNIC\_ISS da tabela ESTABELECIMENTO\) e se o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL \(campo 73 da SAFX07\) for igual do estabelecimento selecionado; __OU__
- Se o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV \(campo 58 da SAFX09\) estiver preenchido e se o campo COD\_MUNICIPIO da tabela DWT\_DOCTO\_FISCAL \(campo 73 da SAFX07\) for igual do estabelecimento selecionado\.

__“A” – Ativa\.__

- Se nenhuma das situações acima for verdadeira\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__valor\_bruto__

Formato: 999999999999999

Tipo: Valor

Tamanho: 15

Preencher com o conteúdo do campo VLR\_TOT da tabela DWT\_ITENS\_SERV \(campo 15 da SAFX09\)\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 3 para ser preenchido de acordo com o tamanho exigido no layout\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__valor\_deducao__

Formato: 999999999999999

Tipo: Valor

Tamanho: 15

Preencher com o conteúdo do campo VLR\_DEDUCAO\_ISS da tabela DWT\_ITENS\_SERV \(campo 59 da SAFX09\)\.

__Tratamento:__

- Considerar contagem do campo a esquerda a partir da posição 3 para ser preenchido de acordo com o tamanho exigido no layout\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__modelo__

Formato: XX

Tipo: Alfanumérico

Tamanho: 02

Preencher com o conteúdo do campo COD\_MODELO da tabela DWT\_DOCTO\_FISCAL \(campo 13 da SAX07\)\.

__Tratamento:__

- Se o campo não estiver preenchido, preencher com brancos\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__cpfcnpf\_tomador__

Formato: 99999999999 ou 99999999999999

Tipo: Numérico

Tamanho: até 14

Preencher com o conteúdo do campo CPF\_CGC da tabela X04\_PESSOA\_FIS\_JUR \(campo 06 da SAFX04\) referente o prestador cadastrado na nota fiscal\.

__Tratamento:__

- Se o campo não estiver preenchido \(em caso de prestador com situação especial\), preencher com zeros com 14 posições\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

__numero\_servico__

Formato: 99

Tipo: Numérico

Tamanho: 02

Preencher com:

__“79” – Imposto recolhido pelo regime único de arrecadação\.__

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “07” e o campo UF da tabela X04\_PESSOA\_FIS\_JUR \(campo 19 da SAFX04\) referente à PFJ cadastrada na nota fiscal for igual a “EX”\.

__“78” – Não Tributável\.__

- Se o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) e o campo UF da tabela X04\_PESSOA\_FIS\_JUR \(campo 19 da SAFX04\) referente à PFJ cadastrada na nota fiscal for igual a “EX”\.

__“69” – Imposto recolhido pelo regime único de arrecadação\.__

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “07” e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for diferente do município do estabelecimento\.

__“68” – Não Tributável\.__

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “04” e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for diferente do município do estabelecimento\.

__“64” – Imposto devido em Cachoeirinha, sem obrigação de retenção na fonte\.__

- Se o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) e o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV \(campo 58 da SAFX09\) estiver preenchido e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for diferente do município do estabelecimento e o campo\.

__“63” – Imposto devido em Cachoeirinha, com obrigação de retenção na fonte\.__

- Se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) e o campo VLR\_ISS\_RETIDO da tabela DWT\_ITENS\_SERV \(campo 58 da SAFX09\) estiver preenchido e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for diferente do município do estabelecimento e o campo\.

__“62” – Imposto devido fora de Cachoeirinha, sem obrigação de retenção na fonte\.__

- Se o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for diferente do município do estabelecimento e o campo\.

__“61” – Imposto devido fora de Cachoeirinha, com obrigação de retenção na fonte\.__

- Se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for diferente do município do estabelecimento e o campo\.

__“59” – Imposto recolhido pelo regime único de arrecadação\.__

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “07” e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for igual ao município do estabelecimento\.

__“58” – Não Tributável \(Casos de Isenção, ou Suspensão de Exigibilidade\)\.__

- Se o campo IND\_ISS da tabela ESTABELECIMENTO = “04” e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for igual ao município do estabelecimento\.

__“57” – Imposto recolhido pelo regime único de arrecadação – ISSQN fixo\.__

- Se o serviço cadastrado na nota e o município cadastrado no estabelecimento estiverem parametrizados na tela Parâmetros – Classificação de Serviços com o COD\_PARAM = “495”\.

__“52” – Imposto devido em Cachoeirinha, sem obrigação de retenção na fonte\.__

- Se o campo IND\_TP\_RET for igual a “2” da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for igual ao município do estabelecimento\.

__“51” – Imposto devido em Cachoeirinha, com obrigação de retenção na fonte\.__

- Se o campo IND\_TP\_RET for igual a “1” da tabela DWT\_DOCTO\_FISCAL \(campo 141 da SAFX07\) e o campo COD\_MUNICIPIO da tabela X04\_PESSOA\_FIS\_JUR \(campo 25 da SAFX04\) referente à PFJ cadastrada na nota fiscal for igual ao município do estabelecimento\.

__Tratamento:__

- Se nenhuma das situações acima for atendida, emitir uma mensagem de log: *“Erro: Favor verificar as operações de acordo com a LISTAGEM DE OPERAÇÕES ISSQN MUNICÍPIO DE CACHOEIRINHA com orientação no manual operacional do módulo <<NF>>, <<Série>>, <<Data Fiscal>>”*\.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TAG e informações obrigatórias, exceto as informações serie, valor\_tributavel, valor\_deducao, modelo\.

MFS16077

RN23

__Regra para tag />__ Tag relacionada ao encerramento da formatação do arquivo e que deve receber as informações das notas prestadas declaradas com o texto fixo: /__>__\. 

*Observação: *Para cada TAG <informação pode haver mais de uma TAG <nota\.

Exemplo:

__<informacao__ exercicio="2009" mes="04"

    atividade\_desenvolvida="3872" __aliquota="2000"__ basecalculo=""

    observacao="OPCIONAL">

__      <nota__ data\_emissao="20/04/2009" numero="3" serie="A"

      valor\_tributavel="10000" situacao="A" valor\_bruto="0"

      valor\_deducao="0" modelo="01" cpfcnpj\_tomador="00000000000"

      numero\_servico="52"__/>__

      __<nota__ data\_emissao="30/04/2009" numero="4" serie="A"

      valor\_tributavel="20000" situacao="N" valor\_bruto="0"

      valor\_deducao="0" modelo="01" cpfcnpj\_tomador="00000000000"

      numero\_servico="52"__ />__

MFS16077

RN24

__Regra para tag </informacao> __Tag relacionada ao encerramento da formatação do arquivo e que deve receber as informações do movimento declarado com o texto fixo: __</informacao >__\.

MFS16077

RN25

__Regra para tag </empresa> __Tag relacionada ao encerramento da formatação do arquivo e que deve receber as informações da declaração da empresa com o texto fixo: __</empresa>__\.

MFS16077

RN26

__Regra para tag </declaracao> __Tag relacionada ao encerramento da formatação do arquivo e que deve receber as informações das notas prestadas declaradas com o texto fixo: __</declaracao>__\.

MFS16077

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


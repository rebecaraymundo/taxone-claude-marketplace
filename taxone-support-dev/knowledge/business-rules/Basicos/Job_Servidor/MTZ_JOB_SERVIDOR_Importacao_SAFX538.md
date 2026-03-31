# MTZ_JOB_SERVIDOR_Importacao_SAFX538

- **Fonte:** MTZ_JOB_SERVIDOR_Importacao_SAFX538.docx
- **Modificado:** 2024-08-20
- **Tamanho:** 73 KB

---

THOMSON REUTERS

TAXONE >> FEDERAL >> CREDPIS >> Manutenção >> Controle de Parcelas

##### DOCUMENTO DE REQUISITO

__MFS__

__Nome__

__Descrição__

MFS\-651783

Alessandra Cristina Navatta

Definição das regras de Carga, importação \(Online e Batch\) e Exportação da SAFX538\.

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__MFS__

RN00

As rotinas de Carga, Importação \(Online e Batch\) e Exportação do módulo Job Servidor deverão ser alteradas para contemplar os campos listados abaixo na tabela SAFX538:

__Campo__

__Tipo__

__Tam\.__

__Obrig\.__

__Chave__

Código da Empresa

A

003

SIM

SIM

Código do Estabelecimento

A

006

SIM

SIM

Código do Bem

A

060

SIM

SIM

Código do Incorporador do Bem

A

006

SIM

SIM

Número da parcela do CREDPIS

N

003

SIM

NÃO

Data do Início do Crédito

N

008

SIM

NÃO

Data do Fim do Crédito

N

008

SIM

NÃO

Indicador Baixa

A

001

NÃO

NÃO

Data da Baixa

N

008

NÃO

NÃO

Indicador do Motivo da Baixa

A

001

NÃO

NÃO

 

MFS\-651783

RN00\.1

__Verificação de existência do registro __

O registro não será criado na importação, apenas será atualizado na tabela CREDPIS\_CONTROLE, por isso, se não for encontrado um registro na tabela, a importação não será realizada e a mensagem <<913257>> será exibida: “Não foi encontrado registro na CREDPIS\_CONTROLE para este bem”\. Este cenário será considerado na importação como erro \(para o usuário conseguir identificar o próprio registro\)\.

Tela de Manutenção:  TAXONE >> FEDERAL >> CREDPIS >> Manutenção >> Controle de Parcelas

MFS\-651783

RN00\.2

__Campos Obrigatório não preenchido__

Se algum campo de preenchimento obrigatório não estiver preenchido, exibir a mensagem “Campo <<Nome do campo>> deve ser preenchido”

MFS\-651783

__RN01__

__Campo 01 \- Código da empresa__

 

__Tabela: __SAFX538

__Item: __01

__Nome do Campo: __COD\_EMPRESA

__Descrição: __Código da empresa

__Tipo:__ A

__Tamanho: __003

__Campo Obrigatório__

__Comentário: __Campo destinado ao código da Empresa\.

__Chave Primária__

MFS\-651783

__RN02__

__Campo 02 \- Código do estabelecimento__

__Tabela: __SAFX538

__Item: __02

__Nome do Campo: __COD\_ESTAB

__Descrição: __Código do estabelecimento

__Tipo:__ A

__Tamanho: __006__ __

__Campo Obrigatório__

__Comentário: __Campo destinado ao código do Estabelecimento\.

__Chave Primária__

MFS\-651783

__RN03__

__Campo 03 – Código do Bem__

__Tabela: __SAFX538

__Item: __03

__Nome do Campo:__ COD\_BEM

__Descrição: __Código do Bem

__Tipo:__ A

__Tamanho: __060

__Campo Obrigatório__

__Comentário:__ Informar o Código do Bem\. O código do bem deverá ter sido previamente cadastrado na tabela SAFX13\.

__Chave Primária__

__Validação:__

Se o bem não estiver cadastrado na SAFX13, exibir a mensagem <<913252>>: “Campo ‘Código do Bem’ deve estar previamente cadastrado na tabela de Arquivo de Cadastro de Bem\. Localização: Módulo: BÁSICOS > DATAWAREHOUSE > Manutenção > Cadastros > Bem Patrimonial”

MFS\-651783

__RN04__

__Campo 04 – Código do Incorporador do Bem__

__Tabela: __SAFX538

__Item: __04

__Nome do Campo:__ COD\_INC

__Descrição: __Código do Incorporador do Bem 

__Tipo:__ A

__Tamanho: __006

__Campo Obrigatório__

__Comentário: __Informar o Código do Incorporador do Bem\. O código incorporador do bem deverá ter sido previamente cadastrado na tabela SAFX13\. 

__Chave Primária__

__Comportamento:__

Caso o campo não esteja preenchido, gravar um espaço\. \(esse comportamento já existe na tela\)

MFS\-651783

__RN05__

__Campo 05 – Número da Parcela do CREDPIS__

__Tabela: __SAFX538

__Item: __05

__Nome do Campo:__ IND\_PARCELA

__Descrição: __Número da Parcela do CREDPIS 

__Tipo:__ N

__Tamanho: __003

__Campo Obrigatório__

__Comentário: __Informar o número da parcela de apropriação do crédito do CREDPIS\. 

MFS\-651783

__RN06__

__Campo Data do Início do Crédito__

__Tabela: __SAFX538

__Item: __06

__Nome do Campo: __Data do Início do Crédito

__Nome da tabela: __DATA\_INI\_CRED

__Tipo:__ N

__Tamanho:__ 08

__Campo Obrigatório__

__Comentário:__ Informar a Data de Início do Crédito do PIS/COFINS sobre o Bem Patrimonial\. CREDPIS\.

Validação:

Se a data não estiver com formato válido \(DDMMAAAA\), exibir a mensagem<<93651>>: “Data do Início do Crédito com formato inválido\.”

MFS\-651783

__RN07__

__Campo Data do Fim do Crédito__

__Tabela: __SAFX538

__Item: __07

__Nome do Campo: __Data do Fim do Crédito

__Nome da tabela: __DATA\_FIM\_CRED

__Tipo:__ N

__Tamanho:__ 08

__Campo Obrigatório__

__Comentário:__ Informar a Data de Fim do Crédito do PIS/COFINS sobre o Bem Patrimonial\. CREDPIS\.

Validações:

Se a data não estiver com formato válido \(DDMMAAAA\), exibir a mensagem<<93652>>: “Data do Fim do Crédito com formato inválido\.”

A data do fim do crédito deve ser maior ou igual que a data do início do crédito, caso não esteja, exibir a mensagem <<913254>> : “Data do Fim do Crédito deve ser maior ou igual que a Data do Início do Crédito”

MFS\-651783

__RN08__

__Campo Indicador da Baixa__

__Tabela: __SAFX538

__Item: __08

__Nome do Campo:__ Indicador da Baixa

__Nome da tabela: __IND\_BAIXA

__Tipo: __A

__Tamanho:__ 01

__Campo Não Obrigatório__

__Comentário:__ Informar se o bem está baixado ou não\.

Opções Válidas:

S = Sim

N ou Nulo = Não

__Validações: __

Se for informado um valor que não está na lista de opções válidas, exibir a mensagem <<93653>>: “O Indicador da Baixa deve ser igual a:  <S> , <N> ou <Nulo>\.”

MFS\-651783

__RN09__

__Campo Data da Baixa__

__Tabela:__ SAFX538

__Item:__ 09

__Nome do Campo:__ Data da Baixa

__Nome da tabela: __DATA\_BAIXA

__Tipo: __N

__Tamanho: __08

__Campo Não Obrigatório__

__Comentário:__ Data da Baixa do bem, referente aos tributos PIS/PASEP e COFINS\.

__Validação:__ A data da baixa deve estar no formato correto, caso contrário, exibir a mensagem <<913250>> “Campo 'Data da Baixa' com formato inválido\.”

O campo ‘Data da Baixa’ só deve ser preenchido, quando o campo ‘Indicador da Baixa’ for informado com ‘S’\. Se o campo ‘Indicador do Motivo da Baixa’ for preenchido com “S” e o campo ‘Data da Baixa’ sem preenchimento, exibir a mensagem: <<913255>> “Campo ‘Data da Baixa’ deve ser preenchido quando o campo ‘Indicador da Baixa’ estiver preenchido com ‘S’”\.

O campo ‘Data da Baixa’ deve ser preenchido, quando o campo ‘Indicador da Baixa’ for informado com ‘S’\. Se o campo ‘Indicador do Motivo da Baixa’ for preenchido com “N” ou estiver nulo e o campo ‘Data da Baixa’ estiver preenchido, exibir a mensagem <<913256>>: “Campo ‘Data da Baixa’ só deve ser preenchido quando o campo ‘Indicador da Baixa’ estiver preenchido com ‘S’”

MFS\-651783

__RN10__

__Campo Indicador do Motivo da Baixa__

__Tabela:__ SAFX538

__Item:__ 10

__Nome do Campo:__ Indicador do Motivo da Baixa

__Nome da tabela: __IND\_MOTIVO\_BAIXA

__Tipo:__ A

__Tamanho: __01

__Campo Não Obrigatório__

__Comentário:__ Indicador do Motivo da Baixa do bem, referente aos tributos PIS/PASEP e COFINS\. 

Opções válidas: 

1 \- Venda

2 \- Obsolescência ou sucateamento

3 \- Sinistros;

4 \- Doação;

6 \- Outros;

7 – Automática

__Validações: __

Se for informado um valor que não está na lista de opções válidas, exibir a mensagem <<913247>>: “O conteúdo informado deve ser igual a:  <1> ou <2> ou <3> ou <4> ou <6> ou <7>\.”

O campo ‘Indicador do Motivo da Baixa’ só deve ser preenchido, quando o campo ‘Data da Baixa’ for informado\. Se o campo ‘Indicador do Motivo da Baixa’ for preenchido e o campo ‘Data da Baixa’ sem preenchimento, exibir a mensagem <<913248>>: “Campo ‘Data da Baixa’ deve ser preenchido quando o campo ‘Indicador do Motivo da Baixa’ estiver preenchido”\.

Se o campo ‘Data da Baixa’ estiver preenchido e não for indicado o campo ‘Indicador do Motivo da Baixa’, exibir a mensagem  <<913249>>: “Campo ‘Indicador do Motivo da Baixa’ é de preenchimento obrigatório, quando o campo ‘Data da Baixa’ estiver preenchido\.”

MFS\-651783

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


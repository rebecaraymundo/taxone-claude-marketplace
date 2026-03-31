# MTZ-OTF-GPS

- **Fonte:** MTZ-OTF-GPS.docx
- **Modificado:** 2020-08-29
- **Tamanho:** 27 KB

---

# Obrigações de Tributos Federais – GPS

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS2494

GPS – Cooperativa de Trabalho de Transporte 

Durante a geração das retenções do INSS os dados deverão ser gravados considerando o campo 26 da SAFX04, onde o sistema deverá verificar se a informação é referente à Cooperativa de transporte, caso seja, a nota gerada referente a essa Pessoa Fis/Jur deve ser levada para a tela de manutenção com a data do fato gerador preenchida conforme a data fiscal\.

Durante a geração da Guia a data de competência apresentada na GPS deve ser a mesma da data fiscal\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

No campo 26 da SAFX04 “Classe de Pessoa Fís/Jur” deverá ser incluída a opção “05\-Cooperativa de transporte”\.

OS2494

__RN01__

O nome desse campo será somente “Data do Fato gerador”

OS2494

__RN02__

Quando da geração da retenção de INSS, se identificado que no campo 26 da SAFX 04 a informação colocada é “Cooperativa de transporte”, o campo “Data do fato gerador” dessa tela \(Manutenção de Dados de Retenção\) será igual a informação colocada no campo “Data Fiscal”\.

OS2494

__RN03__

__Regra para retirada do campo Mês/Ano Competência:__

O campo Mês/Ano Competência deve ser retirado da tela de emissão de GPS\.

OS2858

__RN04__

__Regra para inclusão dos novos campos de filtro:__

Devem ser incluídos os seguintes campos:

Competência: Quando selecionada, as notas deverão ser recuperadas através da data de emissão\.

Data Fiscal: Quando selecionada, as notas deverão ser recuperadas através da data fiscal\.

Período: Informará o período para a emissão da GPS

Somente Extemporâneo: Quando selecionado, deverão recuperar as notas que estão fora do período informado e que tenham a data maior do que o dia limite informado na tela Parâmetros – Parâmetros DARF/GPS\.

 

OS2858

__RN05__

Se o usuário clicar no filtro “Competência” e o campo “Somente Extemporâneo” estiver desmarcado:

O sistema deverá recuperar as informações que:

    \- Possuírem mês e ano competência dentro do período informado

OS2858

__RN06__

Se o usuário clicar no filtro “Competência” e o campo “Somente Extemporâneo” estiver marcado:

O sistema deverá recuperar as informações que:

   \- Possuírem mês e ano competência dentro do período informado

   \- Possuírem data de lançamento \(data fiscal\) fora do período informado

   \- A data de lançamento \(data fiscal\) ultrapasse o dia limite para recebimento cadastrado na tela Parâmetros – Parâmetros DARF/GPS\.

OS2858

__RN07__

Se o usuário clicar no filtro “Data Fiscal” e o campo “Somente Extemporâneo” estiver desmarcado:

O sistema deverá recuperar as informações que:

   \- Possuírem data de lançamento \(data fiscal\) dentro do período informado

OS2858

### RN08

Se o usuário clicar no filtro “Data Fiscal” e o campo “Somente Extemporâneo” estiver marcado:

O sistema deverá recuperar as informações que:

   \- Possuírem data de lançamento \(data fiscal\) dentro do período informado

   \- Possuírem mês e ano competência fora do período informado

   \- A data de lançamento \(data fiscal\) ultrapasse o dia limite para recebimento cadastrado na tela Parâmetros – Parâmetros DARF/GPS\.

OS2858

### RN09

Alterar as telas de emissão dos demonstrativos de INSS para que as mesmas passem a considerar a nova ordem dos campos\. O campo Cedente deve ser transferido para baixo do groupbox Filtros\.

OS2858


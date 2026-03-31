# MTZ_EFD_Parametros_Apuracao_Assistida_RS

> Fonte: MTZ_EFD_Parametros_Apuracao_Assistida_RS.docx






THOMSON REUTERS

Módulo EFD – Escrituração Fiscal Digital


Parametrização dos Ajustes da Apuração Assistida do RS


Localização: Menu SPED, módulo EFD – Escrituração Fiscal Digital , menu Parâmetros  Apuração Assistida - RS



DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	2
3.	Regras de Funcionamento dos Campos	4

























## Regras Gerais


Parametrização criada na MFS34777 para atendimento ao regime especial do cliente Zaffari, concedido através do Ato Declaratório 010/2020.

A Zaffari é cliente piloto do projeto “Apuração Assistida” do Rio Grande do Sul. O projeto prevê que todos os documentos eletrônicos sejam escriturados na EFD de forma consolidada, através de ajustes. O projeto será iniciado pelos documentos NFC-e (nota fiscal consumidor eletrônica, modelo = 65).
Esta parametrização foi criada para o usuário informar os parâmetros necessários para a geração automática dos ajustes (E111) e valores declaratórios (E115), de acordo com o Ato Declatório 010/2020, que concedeu o regime especial ao cliente.
MFS40151 – Atualização legal do projeto “Apuração Assistida”. O registro E115, que demonstrava o total do valor contábil das notas de Modelo 65, não será mais exigido. Com esta alteração, os campos da parametrização referentes ao E115 foram retirados da tela.

## Layout da Tela




MFS40151: Os campos da parametrização referentes ao E115 foram retirados da tela.

Botões da barra de menu:





## Regras de Funcionamento dos Campos


Segue detalhamento do funcionamento dos campos:

Chave da Tabela: UF

Esta tabela tem como chave a identificação da UF, mas este campo não aparece na tela.

A tabela foi criada para um regime especial do RS, sobre a escrituração das notas eletrônicas no Sped Fiscal. A ideia de incluir a UF na chave, tem como objetivo atender a outras UF’s, caso no futuro alguma outra UF venha a adotar regime semelhante ao do RS.




= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS34777 | Criação da parametrização do Regime Especial do RS | Criação da parametrização para geração dos ajustes do projeto “Apuração Assistida” do estado do Rio Grande do Sul. | 28/04/2020 |
| MFS40151 | Atualização Legal | Atualização legal dos procedimento do projeto “Apuração Assistida” do estado do Rio Grande do Sul. | 07/07/2020 |


| Apuração Assistida – RS |
| --- |
| Ajuste à Débito do ICMS das NFC-e (E111):     Código de Ajuste:  XXXXXXXX - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     Descrição Complementar: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  Valor Declaratório do Total das NFC-e (E115):     Código Informação Adicional: XXXXXXXX - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     Descrição Complementar: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  Código de Ajuste utilizado na  Sub-Apuração p/as NFC-e (1921): XXXXXXXX - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |


| CONFIRMA | Opção para salvar os dados alterados ou incluídos. |
| --- | --- |
| EXCLUI | Permite a exclusão dos dados parametrizados. |
| RELATÓRIO | Esta opção permite imprimir os dados da parametrização. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/ Default | Regra |
| --- | --- | --- | --- | --- | --- |
| Código de Ajuste | Alfanumérico      A(08) | S | S |  | Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste de Sped Fiscal (Módulo ICMS, menu “Apuração > Apuração do ICMS > Lançamentos Complementares  Código de Ajuste Sped Fiscal”).  Serão disponibilizados para seleção apenas os seguintes códigos:  - Códigos do RS (os dois primeiros caracteres devem ser = “RS”); - O terceiro caracter deve ser = “0” (=Apuração Própria); - O quarto caracter deve ser = “0” (=Outros Débitos);  Após a seleção do código desejado, será exibido o seu código e sua descrição.   Quando o código for digitado, será verificada a sua existência na tabela, e também, se esta de acordo com as cadacterísticas acima. Caso não, será considerado um código inválido. |
| Descrição Complementar | Alfanumérico     A(150) | N | S |  | Neste campo será informada, opcionalmente, uma descrição complementar para o ajuste. |
| Código Informação Adicional  Campo retirado da tela na (MFS40151) | Alfanumérico      A(08) | S | S |  | Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Informação Adicional do Sped Fiscal (Módulo SPED Fiscal, menu “Parâmetros > Registros E115/1925 > Informações Adicionais da Apuração”).  Serão disponibilizados para seleção apenas os seguintes códigos:  - Códigos do RS (os dois primeiros caracteres devem ser = “RS”);  Após a seleção do código desejado, será exibido o seu código e sua descrição.   Quando o código for digitado, será verificada a sua existência na tabela, e também, se esta de acordo com as cadacterísticas acima. Caso não, será considerado um código inválido. |
| Descrição Complementar  Campo retirado da tela na (MFS40151) | Alfanumérico     A(150) | N | S |  | Neste campo será informada, opcionalmente, uma descrição complementar para o valor declaratório. |
| Código de Ajuste utilizado na Sub-Apuração p/as NFC-e (1921) | Alfanumérico      A(08) | S | S |  | Este campo trabalha com janela de seleção dos dados da Tabela dos Códigos de Ajuste de Sped Fiscal (Módulo ICMS, menu “Apuração > Apuração do ICMS > Lançamentos Complementares  Código de Ajuste Sped Fiscal”).  Serão disponibilizados para seleção apenas os seguintes códigos:  - Códigos do RS (os dois primeiros caracteres devem ser = “RS”); - O terceiro caracter deve ser = “0” (=Apuração Própria); - O quarto caracter deve ser = “0” (=Outros Débitos);  Após a seleção do código desejado, será exibido o seu código e sua descrição.   Quando o código for digitado, será verificada a sua existência na tabela, e também, se esta de acordo com as cadacterísticas acima. Caso não, será considerado um código inválido. |

# MTZ-Canoas-Manutencao-Dados_Iniciais

- **Fonte:** MTZ-Canoas-Manutencao-Dados_Iniciais.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 36 KB

---

# Canoas \- Manutenção \- Dados Iniciais

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3651

Geração do Meio Magnético Canoas

Este documento tem como objetivo criar o novo módulo que permita a geração do meio magnético de Canoas que irá conter as informações de serviços prestados e tomados\.

OS3926\-O

Elaboração da regra para os segmentos de Construção Civil, Utilities e Telecom para o município atendido pelo validador de Canoas

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regra da tela Manutenção – Dados Iniciais:__

Abertura da janela:

Ao abrir a tela, fazer a seguinte verificação:

Se login no Manager foi feito __sem__ estabelecimento:

Abrir a tela de manutenção\.

Se login no Manager foi feito __com__ estabelecimento, verificar:

Se a UF/Município do estabelecimento  for igual ao município em questão, então 

	Abrir a tela de manutenção\.

Senão 

 Se a UF/Município do estabelecimento for diferente do município em questão, porém possui inscrição municipal válida para esse município cadastrada na tela Básicos – MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais

          Abrir a tela de manutenção\.

       Senão 

Não abrir a tela\. E dar a seguinte mensagem: “Este estabelecimento não pertence ao município de “XXXXX/YY e não possui inscrição municipal válida para esse município cadastrada na tela Básicos – MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais\.”

XXXXX: Descrição do município passado pelo Manager na abertura do módulo\.

YY: Código da UF passada pelo Manager na abertura do módulo\.

__OS3926\-O__

__RN01__

__Regra do campo Estabelecimento da tela Manutenção – Dados Iniciais:__

Quando o estabelecimento estiver selecionado no Manager esse campo deve exibir o estabelecimento solicitado, desde que o mesmo seja do município em questão\. 

Quando o estabelecimento não estiver selecionado no manager, o campo deve exibir os estabelecimentos do município em questão\.

Quando o estabelecimento selecionado não for do município em questão, deve\-se exibir uma mensagem e não abrir a tela de manutenção\. 

Deverá exibir o estabelecimento selecionado no Manager desde que o mesmo seja do município em questão do validador CANOAS\. O campo deverá ficar desabilitado não permitindo que o mesmo seja alterado\.

Caso não esteja selecionado nenhum estabelecimento, o sistema deve permitir que o usuário selecione no campo o estabelecimento desejado, através de um listbox\.

Deverá exibir o estabelecimento selecionado no Manager desde que o mesmo seja de Canoas\. O campo deverá ficar desabilitado não permitindo que o mesmo seja alterado\.

Caso não esteja selecionado nenhum estabelecimento, o sistema deve permitir que o usuário selecione no campo o estabelecimento desejado, através de um listbox\.

Devem ser exibidos os estabelecimentos que atenderem as seguintes premissas:

- Que estejam licenciados\.
- Que o usuário possua direito de acesso na ferramenta PowerLock\.
- Que pertença a Canoas\.

                                                   OU

- Que não pertença ao município em questão, porém possui inscrição municipal válida para esse município cadastrada na tela Básicos – MasterSAF DW – Manutenção – Cadastros – Inscrições Municipais\.

OS3651 / OS3926\-O

__RN02__

__Regra do campo Perfil do Declarante – Prestador de serv\./ISSQN próprio pela Empresa da tela Manutenção – Dados Iniciais:__

Deve ser exibido através de um checkbox com as seguintes opções: ‘S’ quando estiver marcado e ‘N’ quando estiver desmarcado\.

OS3651

__RN03__

__Regra do campo Perfil do Declarante – Prestador de serv\./ISSQN próprio – Instituição financeira pela Empresa da tela Manutenção – Dados Iniciais:__

Deve ser exibido através de um checkbox com as seguintes opções: ‘S’ quando estiver marcado e ‘N’ quando estiver desmarcado\.

OS3651

__RN04__

__Regra do campo Perfil do Declarante – Prestador de serv\./ Simples Nacional pela Empresa da tela Manutenção – Dados Iniciais:__

Deve ser exibido através de um checkbox com as seguintes opções: ‘S’ quando estiver marcado e ‘N’ quando estiver desmarcado\.

OS3651

__RN05__

__Regra do campo Perfil do Declarante – Data Inclusão Simples pela Empresa da tela Manutenção – Dados Iniciais:__

Deve ser exibido através de um textbox\. Apenas deve ser habilitado quando o campo Perfil do Declarante – Prestador de serv\./ Simples Nacional estiver marcado\. Formato: DD/MM/AAAA\.

OS3651

__RN06__

__Regra do campo Perfil do Declarante – Tomador de serviço pela Empresa da tela Manutenção – Dados Iniciais:__

Deve ser exibido através de um checkbox com as seguintes opções: ‘S’ quando estiver marcado e ‘N’ quando estiver desmarcado\.

OS3651

__RN07__

__Regra do campo Responsável pelas Informações da tela Manutenção – Dados Iniciais:__

Deve ser composto pelo código do responsável \+ pastinha amarela \+ nome do responsável desabilitado\. As informações podem ser recuperadas através da pastinha amarela ou pela digitação do código do responsável\. 

Quando a pastinha amarela for acionada, sistema deve exibir a tela de critério de seleção contendo os campos da tabela RESP\_INFORMACAO\. 

OS3651


# MTZ-Canal_Distri_Obras_x_Sequencial

- **Fonte:** MTZ-Canal_Distri_Obras_x_Sequencial.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 35 KB

---

# Parâmetros \- Canal Distrib\./Obras x Sequencial ISSQNDec

##### DOCUMENTO DE REQUISITO

###### MFS/CH

###### Nome

__Descrição__

MFS8420

DW \- MUNICIPAL \- ISS – Reestruturação do módulo Colombo

Este documento tem como objetivo alterar a geração do Meio Magnético do município de Colombo para que o mesmo passe a considerar as alterações da versão 8\.49\.00\. Além disso, a geração será reestruturada para que a mesma fique de acordo com a nova estrutura do grupo Municipal\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### MFS/CH

__RN01__

__Regra do campo Canal Distribuição/Obra da tela Parâmetros – Canal Distrib\./Obras x Sequencial:__

Deverá recuperar o COD\_CANAL\_DISTRIB campo da tabela DWT\_CANAIS\_DISTRIB\. A recuperação deve ser realizada através da pastinha amarela\. Quando a pastinha amarela for acionada devem ser exibidos os campos da tabela DWT\_CANAIS\_DISTRIB\.

__MFS8420__

__RN02__

__Regra do campo Seqüencial ISSQNDec da tela Parâmetros – Canal Distrib\./Obras x Sequencial:__

Esse campo deve ser um texbox\. Numérico com 9 posições\.

__MFS8420__

__RN03__

__Regra do campo Validade da tela Parâmetros – Canal Distrib\./Obras x Sequencial:__

Irá permitir que diferentes canais de distribuição/obras cadastrados no MasterSAF possam ser relacionados com o mesmo sequencial para diferentes períodos\. A data de validade é do tipo “a partir de”\. Deve conter a máscara DD/MM/AAAA\. 

__MFS8420__

__RN04__

__Regra da tela Parâmetros – Canal Distrib\./Obras x Seqüencial:__

A tela deve conter as seguintes funcionalidades: 

Novo: o sistema criará um novo registro\.

Abrir: o sistema abrirá todos os registros existentes\.

Excluir: o sistema excluirá um registro existente\.

Confirmar: o sistema salvará as informações cadastradas\.

Ordenar: o sistema irá ordenar as informações de acordo com o escolhido\. Deve ser possível realizar a ordenação por todos os campos da tela\.

Relatório: o sistema chamará o relatório de conferência da tela\.

Sair: o sistema fechará a tela\.

__MFS8420__

__RN05__

__Regra do relatório da tela Parâmetros – Canal Distrib\./Obras x Seqüencial:__

Deve existir um relatório de conferência que informe os relacionamentos existentes entres os canais de distribuição/obras cadastrados no MasterSAF e o seqüencial fornecido pelo programa da ISSQNDec

__MFS8420__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


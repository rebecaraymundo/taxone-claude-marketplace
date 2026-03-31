# MTZ-OTF-Gerar_Relatorio_de_DARF_com_Pagos_e_Nao_Pagos

- **Fonte:** MTZ-OTF-Gerar_Relatorio_de_DARF_com_Pagos_e_Nao_Pagos.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 33 KB

---

# Obrigações de Tributos Federais \- Gerar Relatório de DARF com Pagos e Não Pagos

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS2797

Obrigações de Tributos Federais \- Gerar Relatório de DARF com Pagos e Não Pagos

__Módulo: MasterSAF DW__

Alterar opção “Gerado” para “Gerado/Não Pago” no campo “Situação DARF” da tela de Controle de Tributos – SAFX53 

__Módulo: Obrigações de Tributos Federais__

Alterar opção “Gerado” para “Gerado/Não Pago” no campo “Situação DARF” na emissão do relatório por Empresa e por Estabelecimento\.

CH86451

Considerar geração por Parâmetro de Operação

Quando a geração for feita com os parâmetros de operação, gravar o status na safx53 da mesma forma como é feito na geração normal

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Alterar o flag “Gerado” do campo “Situação DARF” para “Gerado/Não Pago” na tela de Emissão de Tributos – Estabelecimento\.

__OS2797__

__RN01__

A sistemática de geração caso a opção “Gerado/Não Pago” será mantida, ou seja, os DARF’s que tenham sido gerados a partir das retenções mas que ainda não foram pagos serão gerados\.

__OS2797__

__RN02__

Alterar a opção “Gerado” para “Gerado/Não Pago”  do campo “Situação DARF” da tela de Controle de Tributos do módulo MasterSAF DW – menu: Manutenção >> Controle de Tributos\.

__OS2797__

__RN03__

Caso a DARF esteja sendo gerado em quotas, o sistema só irá considerar que a DARF está totalmente paga quando todas as referências da mesma na tabela X75\_DCTF estiverem com o campo STATUS = P\. Caso contrário, a DARF será considerada “Gerada/Não Pago”\.

__OS2797__

__RN04__

Ao gerar o relatorio \(tanto por Estabelecimento quanto por Empresa\) o label “Situação DARF” deverá seguir os mesmos status do campo “Situação DARF” da tela de seleção de parâmetros\.

__OS2797__

__RN05__

Quando na tela:

Obrigações de Tributos Federais → Outras Obrigações → DARF’s → Geração a partir das Retenções

O parâmetro “__Utilizar parâmetros p/ Operação__” estiver marcado:

__\. __Efetuar a geração dos DARF’s considerando o código de operação\.

Da mesma forma como é feita a geração do DARF normalmente, alterar a “situação do DARF” no Controle de Tributos \(safx53\)

__\. __Apresentar o DARF gerado na tela de manutenção:

Obrigações de Tributos Federais → Outras Obrigações → DARF’s → Manutenção

O parâmetro “__Utilizar parâmetros p/ Operação__” NÃO estiver marcado:

Não haverá alteração, a funcionalidade continuará da mesma forma\.

__CH86451__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


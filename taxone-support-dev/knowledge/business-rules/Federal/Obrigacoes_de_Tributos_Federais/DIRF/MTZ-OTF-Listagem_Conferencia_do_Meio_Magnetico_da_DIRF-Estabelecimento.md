# MTZ-OTF-Listagem_Conferencia_do_Meio_Magnetico_da_DIRF-Estabelecimento

- **Fonte:** MTZ-OTF-Listagem_Conferencia_do_Meio_Magnetico_da_DIRF-Estabelecimento.docx
- **Modificado:** 2022-03-02
- **Tamanho:** 34 KB

---

# Módulo: Obrigações de Tributos Federais 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

CH2574\_2014

Obrigações de Tributos Federais – Considerar apenas uma pessoa física/jurídica caso exista mais de uma no mesmo ano calendário com datas de validade distintas

O objetivo deste documento de requisito é permitir a correta geração do fornecedor no registro BPFDEC ou BPJDEC quando existem para o mesmo ano calendário\. No caso será gerado apenas o fornecedor mais recente nesses registros, conforme testes realizados\.

CH459\_2014

Obrigações de Tributos Federais – Alteração da descrição da coluna “IRRF Retido”

O objetivo deste documento de requisito é alterar a nomenclatura da coluna “IRRF Retido” para “Retenções” nos relatórios de Conferência da DIRF por Estabelecimento e por Estabelecimento Central\. Essa mudança é necessária, visto que códigos de retenção como o 5952 do grupo ‘CSRF’ não se trata de IRRF – Imposto de Renda Retido na Fonte\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Caso no mesmo ano calendário, a pessoa física ou jurídica possua retenções ou retificações distintas para a mesma pessoa física ou jurídica, porém as mesmas tenham datas de validade distintas, deverá ser gerado no relatório a pessoa física ou jurídica com a descrição no campo “Beneficiário” cuja data de validade seja a mais recente no ano calendário\.

__CH2574\_2014__

__RN02__

Na exibição do relatório após ser solicitada a geração do mesmo, a coluna “IRRF Retido” deverá ter sua coluna alterada para “Retenções”\.

__CH459\_2014__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


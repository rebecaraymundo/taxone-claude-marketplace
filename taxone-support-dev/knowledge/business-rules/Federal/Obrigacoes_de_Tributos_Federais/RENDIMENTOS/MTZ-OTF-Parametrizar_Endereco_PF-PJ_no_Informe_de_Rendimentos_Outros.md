# MTZ-OTF-Parametrizar_Endereco_PF-PJ_no_Informe_de_Rendimentos_Outros

- **Fonte:** MTZ-OTF-Parametrizar_Endereco_PF-PJ_no_Informe_de_Rendimentos_Outros.docx
- **Modificado:** 2020-08-31
- **Tamanho:** 27 KB

---

# OTF \- Parametrizar Endereço PF\-PJ no Informe de Rendimentos Outros

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS2624

OTF \- Parametrizar Endereço PF\-PJ no Informe de Rendimentos Outros

O objetivo do documento de requisito é criar um parâmetro nas telas de geração por CPF e por Nome que permite que o usuário escolha se essa informação deverá ser gerada ou não, conforme hoje já é utilizado na geração por CNPJ e Nome\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Será criado na tela “Emissão de Declaração de Rendimentos – por CPF” um flag chamado “Imprime Endereço Fis/Jur”\.

__OS2624__

__RN01__

Por padrão esse flag ficará desmarcado\.

__OS2624__

__RN02__

Caso a Declaração de Rendimentos por CPF for gerada com essa opção marcada, o sistema gera a Declaração de Rendimentos exibindo o Endereço, Cidade, UF e CEP do CPF informado nos respectivos campos do relatório \(seção 2 – PESSOA FÍSICA BENEFICIÁRIA DOS RENDIMENTOS\)\.

__OS2624__

__RN03__

Caso a Declaração de Rendimentos por CPF for gerada com essa opção desmarcada, o sistema gera a Declaração de Rendimentos sem as informações de Endereço, Cidade, UF e CEP do CPF nos respectivos campos do relatório \(seção 2 – PESSOA FÍSICA BENEFICIÁRIA DOS RENDIMENTOS\)\. Os campos virão vazios\.

__OS2624__

__RN04__

Será criado na tela “Emissão de Declaração de Rendimentos – por Nome” um flag chamado “Imprime Endereço Fis/Jur”\.

__OS2624__

__RN05__

Caso a Declaração de Rendimentos por Nome for gerada com essa opção marcada, o sistema gera a Declaração de Rendimentos exibindo o Endereço, Cidade, UF e CEP do Nome informado nos respectivos campos do relatório \(seção 2 – PESSOA FÍSICA BENEFICIÁRIA DOS RENDIMENTOS\)\.

__OS2624__

__RN06__

Caso a Declaração de Rendimentos por Nome for gerada com essa opção desmarcada, o sistema gera a Declaração de Rendimentos sem as informações de Endereço, Cidade, UF e CEP do Nome informado nos respectivos campos do relatório \(seção 2 – PESSOA FÍSICA BENEFICIÁRIA DOS RENDIMENTOS\)\. Os campos virão vazios\.

__OS2624__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN


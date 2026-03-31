# MTZ-Manutencao_do_registro_65_da_DAC_AL

- **Fonte:** MTZ-Manutencao_do_registro_65_da_DAC_AL.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 28 KB

---

__DAC\-AL – Manutenção Registro 65 – Estoque e Balanço__

__Módulo:__ Estadual → DAC\-AL

__Menu: __Manutenção → Registros 65, 66, 67 e 68

__DOCUMENTO DE REQUISITO__

__DR__

__Nome__

__Descrição__

OS3480

Inclusão do Registro 65 – Estoque e Balanço na DAC\-AL Anual

Inclusão do Registro 65 – Estoque e Balanço na DAC\-AL Anual

__REGRAS DE NEGÓCIO__

__Cód\.__

__Descrição__

__DR__

__RN00__

__Regras Gerais__

Todos os campos de valor terão tamanho de 17, sendo 15 inteiros e 2 decimais\. Somente uma linha que é apresentada deste registro por período e deve ser gravado na nova tabela\.  

Deverá emitir o Relatório de Conferência dos campos do registro\.

OS3480

__RN01__

__Campo Estabelecimento:__

Utilizar para o critério de busca o estabelecimento que o usuário escolheu\.  Trará o estabelecimento que o usuário está logado\. Se o usuário não estiver logado em nenhum, trará a lista de estabelecimentos de Alagoas\.

Campo obrigatório\.

Campo chave\.

Este campo não deverá estar bloqueado\.

OS3480

__RN02__

__Campo Ano:__

Utilizar para o critério de busca a data inicial e final que o usuário preencheu\. Trazer no formato AAAA\.

Campo obrigatório\.

Campo chave\.

Este campo não deverá estar bloqueado\.

OS3480

__RN03__

__Campo Data do balanço__

Trazer fixo o conteúdo gerado através da RN27 do documento matriz “MTZ \- DAC\_AL\_ANUAL\.doc”\.

Este campo deverá estar habilitado para digitação\. Se for digitada alguma data, considerar esta data na geração do arquivo\.

Campo obrigatório\.

OS3480

__RN04__

__Indicador Lucro Bruto:__

Trazer fixo o conteúdo gerado através da RN36 do documento matriz “MTZ \- DAC\_AL\_ANUAL\.doc”\.

Este campo deverá estar habilitado para o usuário escolher do tipo de apuração: “Presumido” ou “Real” 

Deverá ser default a opção “Presumido”\.

OS3480

__RN05__

__Indicador Sistema de Inventário:__

Trazer fixo o conteúdo gerado através da RN37 do documento matriz “MTZ \- DAC\_AL\_ANUAL\.doc”\.

Este campo deverá estar habilitado para o usuário escolher do tipo de sistema de inventário: “Anual” ou “Periódico”

Deverá ser default a opção “Anual”\.

OS3480

__RN06__

__Indicador Cálculo do Estoque:__

Trazer fixo o conteúdo gerado através da RN38 do documento matriz “MTZ \- DAC\_AL\_ANUAL\.doc”\.

Este campo deverá estar habilitado para o usuário escolher do tipo de cálculo de estoque: “Custo Médio“ ou “PEPS”

Deverá ser default a opção “Custo Médio”\.

OS3480

__RN07__

__Campo Número de Empregados:__

Trazer fixo o conteúdo gerado através da RN39 do documento matriz “MTZ \- DAC\_AL\_ANUAL\.doc”\.

Este campo deverá estar habilitado para o usuário digitar do Número de empregados na empresa\. 

Se não for digitado nada, considerar zeros\. Se for digitado algum valor, considerar este valor na geração do arquivo\.

OS3480

__RN08__

__Campo Outras Receitas__

Trazer fixo o valor gerado através da RN40 do documento matriz “MTZ \- DAC\_AL\_ANUAL\.doc”\.

Este campo deverá estar habilitado para o usuário digitar do Valor de Outras Receitas obtidas\. Se não for digitado nada, considerar zeros\. Se for digitado algum valor, considerar este valor na geração do arquivo\.

OS3480

  



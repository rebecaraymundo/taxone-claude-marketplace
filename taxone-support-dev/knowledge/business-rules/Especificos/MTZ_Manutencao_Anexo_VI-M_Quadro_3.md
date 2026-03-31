# MTZ_Manutenção_Anexo_VI-M_Quadro 3

> Fonte: MTZ_Manutenção_Anexo_VI-M_Quadro 3.docx






THOMSON REUTERS

Manutenção Anexo VI-M Quadro 3
Módulo Combustível e Derivados de Petróleo (SCANC)

Localização: Movimento de Refinaria  Manutenção Anexo VI-M  Quadro 3


DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3

## Regras dos Campos


Localização da tela: Específicos >> Combustível e Derivados de Petróleo
Movimento de Refinaria  Manutenção Anexo VI-M  Quadro 3

Tabela de Destino: CBT_ANEXO6M_QUADR3

Nomeclatura dos campos:

- Estabelecimento:
- Mês/Ano Referência:  gravar o último dia do mês/ano
- UF Destinatária do Anexo VI-M
- Grupo Combustível
- Quantidade (Base de Cálculo)
- Vlr ICMS Cobrado
- Vlr ICMS Retido
- Vlr ICMS Total: (ICMS Cobrado + Retido) desabilitado
- No Processo



Ao salvar se o Grupo de Combustível não estiver parametrizado com o check-box (Anexo VI-M) marcado, exibir a mensagem abaixo e não gravar o registro:
“Grupo de Combustível não relacionado ao Anexo VI-M. Favor associá-lo ao referido anexo através da parametrização disponível no menu Parâmetros  Grupos de Combustíveis e Derivados”




| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS535202 |  |  |


| Tela | PL usado pela tela |
| --- | --- |
| Manutenção Anexo VI-M |  |
| Quadro 1 e 2 |  |
| Quadro 3 | Saf_atualiza_anexo_6M_q1_2 da Pkg_Cbt_Anexo_6 |
| Quadros 4 a 15 | Saf_atualiza_anexo_6M_q1_2 da Pkg_Cbt_Anexo_6 |
| Manutenção Anexo VII-M |  |
| Quadro 1 |  |
| Quadros 2 a 7 | Saf_atualiza_anexo_7M_q1 da Pkg_Cbt_Anexo7_fproc |

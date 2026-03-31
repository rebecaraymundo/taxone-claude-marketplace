# MTZ_Manutenção_Anexo_VI-M_Quadro 3

- **Fonte:** MTZ_Manutenção_Anexo_VI-M_Quadro 3.docx
- **Modificado:** 2023-05-29
- **Tamanho:** 63 KB

---

THOMSON REUTERS

Manutenção Anexo VI\-M Quadro 3

Módulo Combustível e Derivados de Petróleo \(SCANC\)

Localização: Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadro 3

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS535202

Sumário

[1\.	Regras dos Campos	3](#_Toc494454507)

# <a id="_Toc350763252"></a><a id="_Toc494454507"></a>Regras dos Campos 

__Localização da tela:__ Específicos >> Combustível e Derivados de Petróleo

__                                   __Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadro 3

Tabela de Destino: CBT\_ANEXO6M\_QUADR3

Nomeclatura dos campos:

- Estabelecimento:
- Mês/Ano Referência:  gravar o último dia do mês/ano
- UF Destinatária do Anexo VI\-M
- Grupo Combustível
- Quantidade \(Base de Cálculo\)
- Vlr ICMS Cobrado
- Vlr ICMS Retido
- Vlr ICMS Total: \(ICMS Cobrado \+ Retido\) desabilitado
- No Processo

__Tela__

__PL usado pela tela__

__Manutenção Anexo VI\-M__

	Quadro 1 e 2  

	Quadro 3        

Saf\_atualiza\_anexo\_6M\_q1\_2 da Pkg\_Cbt\_Anexo\_6

	Quadros 4 a 15 

Saf\_atualiza\_anexo\_6M\_q1\_2 da Pkg\_Cbt\_Anexo\_6

__Manutenção Anexo VII\-M __

             Quadro 1      

	Quadros 2 a 7 

Saf\_atualiza\_anexo\_7M\_q1 da Pkg\_Cbt\_Anexo7\_fproc

Ao salvar se o Grupo de Combustível não estiver parametrizado com o check\-box \(Anexo VI\-M\) marcado, exibir a mensagem abaixo e não gravar o registro:

“*Grupo de Combustível não relacionado ao Anexo VI\-M\. Favor associá\-lo ao referido anexo através da parametrização disponível no menu Parâmetros 🡪 Grupos de Combustíveis e Derivados*”


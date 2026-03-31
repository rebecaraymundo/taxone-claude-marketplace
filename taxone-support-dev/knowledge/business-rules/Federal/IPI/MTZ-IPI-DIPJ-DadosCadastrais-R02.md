# MTZ-IPI-DIPJ-DadosCadastrais-R02

- **Fonte:** MTZ-IPI-DIPJ-DadosCadastrais-R02.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 63 KB

---

THOMSON REUTERS

                                                                                             __Módulo IPI__

__  __

__                                      DIPJ – Manutenção dos Dados Cadastrais – R02__

__Localização__: Menu Federal, Módulo IPI, item Apuração DIPI/DIPJ 🡪DIPJ2014 🡪 Informações Complementares 🡪 Dados Cadastrais – R02

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

OS3655

Novos Campos Cadastro dos Estabelecimentos

Alteração nos dados cadastrais da DIPJ para utilizar os novos campos “Razão Social” e “Bairro” incluídos no cadastro dos Estabelecimentos\.

17/07/2014

\(criação do docto\)

REGRAS DE NEGÓCIO

__RN00__

__                                                         Regras Gerais__

Os dados desta manutenção são pré\-requisito para geração da DIPJ, e nela constam as informações de identificação do estabelecimento\.

Na abertura da tela, alguns campos são preenchidos com as informações de cadastro do estabelecimento matriz \(estabelecimento mostrado no campo “Estabelecimento Matriz”\)\. As informações exibidas são recuperadas do cadastro do Estabelecimento\.

__Alteração da OS3655:__

O preenchimento dos campos “Nome Empresarial”  e “Bairro/Distrito” foi alterado para considerar os novos campos de razão social e bairro criados no cadastro dos estabelecimentos \(quadro “*Informações para geração das obrigações fiscais*”\. Como a DIPJ tem o tamanho destes campos superior ao tamanho dos campos originais do Mastersaf, a DIPJ passou a utilizar os novos campos, caso eles estejam preenchidos\.

__Se__ campo “Informações para geração das obrigações fiscais – Razão Social” preenchido

     No campo “Nome Empresarial” será exibido o conteúdo do novo campo Razão Social;

__Senão__

     No campo “Nome Empresarial” será exibido o conteúdo do campo Razão Social original, conforme o funcionamento original da tela;

__Se__ campo “Informações para geração das obrigações fiscais – Bairro” preenchido

     No campo “Bairro/Distrito” será exibido o conteúdo do novo campo Bairro, *mas*, considerando apenas as 50 primeiras posições\.

__Senão__

     No campo “Bairro/Distrito” será exibido o conteúdo do campo Bairro original, conforme o funcionamento original da tela\.

__RN__


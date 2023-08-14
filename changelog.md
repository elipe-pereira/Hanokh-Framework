### Hanokh-framework
### Framework para desenvolvimento de software para web

#### [Released]
#### [0.7.0]
##### Added
- Adicionado suporte a verificação de versão do python através de um script helper.

#### [release]
#### [0.6.0]
##### Changed
- Alterado cor do título do framework para branco

#### [release]
#### [0.5.1]
##### Added
- Adicionado método para caso haja falha no carregamento do template
##### Changed
- Agora será chamado o método de falha ao carregar template em vez de um retorno
 direto com o html de erro.

#### [release]
#### [0.5.0]
##### Changed
- Estrutura do projeto foi modificada pra ficar mais enxuta.
- Alterado função application.
- Alterado formato de criação de rotas.

#### [release]
#### [0.4.3]
##### Changed
- Arrumado a estrutura de páginas.
##### Removed
- Removido a class page dando lugar a classes para cada página

#### [release]
#### [0.4.2]
##### Changed
- Removido método create_user da classe Page do módulo model.core.
- Ajustado métodos da classe page para haver alternativas caso
 não exista template para as requisições efetuadas.

#### [release]
#### [0.4.1]
##### Changed
- Criado modulo templates e adicionado movido classes de leitura de templates
 para novo local
- Movido leitura de assets para dentro de model.

#### [release]
#### [0.4.0] - 2022-01-25
##### Added
- Aplicado logs nas várias partes do framework

#### [release]
#### [0.3.2] - 2021-12-16
##### Fixed
- Resolvido problema ao criar rotas para downloads privados.

#### [release]
#### [0.3.1] - 2021-12-14
##### Fixed
- Resolvido problemas de autenticação
- Aplicado algumas melhorias no código
- Deixado o debug opcional ao desenvolvedor

#### [released]
#### [0.3.0] - 2021-12-13
##### Added
- Adicionado estrutura de pastas system, para suporte arquivos de usuário
- Adicionado suporte a downloads de arquivos públicos e privados
- Adicionado suporte para geração de logs para debug.
##### Fixed
- Resolvido falha na autenticação por cookies

#### [released]
#### [0.2.5] - 2021-12-10
##### Changed
- Dividido a class RouteAssets em duas classes, Assets() e ReadAssets(),
 melhorando a legibilidade e deixando cada uma com uma só responsabilidade.
- Adicionado as classes AssetsController e ReadAssetsController para futuras
 extensões.

#### [released]
#### [0.2.4] - 2021-12-09
##### Changed
- Alterado classe Auth para ficar mais legível e menor
- Acrescentado classes hash, request e cookie para dar suporte à classe Auth.

#### [released]
#### [0.2.3] - 2021-12-08
##### changed
- Alterado estrutura na pasta model

#### [released]
#### [0.2.2] - 2021-12-07
##### Changed
- Removido varíavel comenta self.is_auth da classe Route e adicionado comentada
 na classe RouteController, para que o Developer decida ou não ativar a página
 de autenticação.

#### [released]
#### [0.2.1] - 2021-12-04
##### Changed
- Adicionado variável TEMPLATE_NAME no hanokh.conf.sample para ser usado
 na configuração e não mais no proj_config.
- Alterado para que o page_header e page_status fiquem no construtor da classe
 route.

#### [released]
#### [0.2.0] - 2021-12-03
##### Added
- Framework javascript vue.js
- Framework javascript react.js
- Framework javascript angularJS
- Framework javascript dojo
- Framework javascript jquery/UI/Mobile
- Framework javascript marionettejs
- Framework css Semantic UI
- Framework css Pure
- Framework css Milligram
- Framework css uikit
- Framework css skeleton
- Framework css tacit
- Framework css vuetify
- Framework css onsenui
- Framework css groundwork
- Framework css materialize
- Framework css material
- Framework css groundwork
- Framework css foundation
- Framework css bulma
- Framework css bonsai
- Framework css 960gridsystem
- Framework css w3css
- Framework css zimit
- Framework css kickstart
- Framework css ink
- Framework css flexboxgrid
- Frameowrk css cardinal
- Framework css cirrus
- Framework css metro
- Framework css bootflat

##### changed
- update bootstrap to 5.1.3

#### [Released]
#### [0.1.0-0]  - 2021-12-01
##### Added
- Arquivo gunicorn.py com as configurações default
- Arquivo hanokh.conf.sample com os itens de configuração modelo
- Estrutura MVC
- Base padrão para rotas e carregamento de páginas
- Suporte a templates.
- Banco de dados inicial, para conta de usuário
- Suporte a autenticação
- Arquivos para configuração de serviço
- Arquivos modelo para configuração do apache e proxy reverso
- Suporte a templates
- Ativos do framework bootstrap

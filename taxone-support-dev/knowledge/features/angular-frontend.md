# Angular Frontend - TAX ONE

## Monorepo: taxsami_taxone_frontend

Repositorio Angular 11 que contem todas as aplicacoes frontend do TAX ONE.

**Caminho local:** `$TAXONE_FRONTEND_REPO` (env var, default em `.env`)

---

## Aplicacoes

| App      | Diretorio                  | Porta Dev | Descricao                   |
|----------|----------------------------|-----------|-----------------------------|
| `taxone` | `projects/taxone/`         | 4200      | Aplicacao principal TAX ONE |
| `t1dw`   | `projects/t1dw/`           | 4350      | TAX ONE Data Warehouse      |
| `cat83`  | `projects/cat83/`          | 4300      | Catalogo 83                 |

## Bibliotecas Compartilhadas

| Lib                       | Diretorio                              | Descricao                                     |
|---------------------------|----------------------------------------|-----------------------------------------------|
| `@libs/tr-core`           | `projects/libs/tr-core/`               | Core TR: HttpProxyService, auth, interceptors |
| `@libs/bento-components`  | `projects/libs/bento-components/`      | Design System Bento (UI padrao TR)            |
| `@libs/mbl-*`             | `projects/libs/mbl-*/`                 | Mobilize (migracao PowerBuilder->Angular)     |
| `@libs/shared-components` | `projects/libs/shared-components/`     | Componentes compartilhados entre apps         |

---

## Dependencias Principais

| Pacote            | Versao   | Uso                           |
|-------------------|----------|-------------------------------|
| `@angular/core`   | 11.2.14  | Framework principal           |
| `@angular/material`| 11.2.9  | UI components Material Design |
| `rxjs`            | 6.6.7    | Programacao reativa           |
| `typescript`      | 4.1.5    | Linguagem                     |
| `@grapecity/wijmo`| *        | FlexGrid para tabelas         |

---

## Patterns de Codigo

### 1. HttpProxyService (chamadas API)

Todas as chamadas HTTP devem usar `HttpProxyService` de `@libs/tr-core`:

```typescript
import { HttpProxyService } from '@libs/tr-core';

constructor(private httpProxy: HttpProxyService) {}

getData(): Observable<Model[]> {
  return this.httpProxy.get<Model[]>('/ws/api/endpoint', { params });
}

saveData(body: Model): Observable<Model> {
  return this.httpProxy.post<Model>('/ws/api/endpoint', body);
}
```

### 2. State Management (BehaviorSubject)

Nao usa NgRx. Estado local via BehaviorSubject em services:

```typescript
@Injectable({ providedIn: 'root' })
export class FeatureService {
  private _items$ = new BehaviorSubject<Item[]>([]);
  public items$ = this._items$.asObservable();

  loadItems(): void {
    this.httpProxy.get<Item[]>('/ws/api/items').subscribe(
      items => this._items$.next(items)
    );
  }
}
```

### 3. Mobilize (PB->Angular)

Libs `@libs/mbl-*` contem telas migradas de PowerBuilder via framework Mobilize. Essas libs possuem patterns proprios e nao devem ser refatoradas para Angular puro sem justificativa.

### 4. Lazy Loading

Cada feature e um modulo lazy-loaded:

```typescript
const routes: Routes = [
  {
    path: 'feature',
    loadChildren: () => import('./feature/feature.module').then(m => m.FeatureModule)
  }
];
```

### 5. Proxy Config (desenvolvimento)

```
/ws     -> http://localhost:8087  (backend Java TAX ONE)
/t1dw   -> http://localhost:9595  (backend Java T1DW)
/cat83  -> http://localhost:8090  (backend Java CAT83)
```

---

## Convencoes de Nomenclatura

| Artefato         | Pattern                              | Exemplo                       |
|------------------|--------------------------------------|-------------------------------|
| Componente       | `nome-feature.component.ts`          | `doc-fiscal-list.component.ts`|
| Service          | `nome-feature.service.ts`            | `doc-fiscal.service.ts`       |
| Module           | `nome-feature.module.ts`             | `doc-fiscal.module.ts`        |
| Routing Module   | `nome-feature-routing.module.ts`     | `doc-fiscal-routing.module.ts`|
| Model/Interface  | `nome-feature.model.ts`              | `doc-fiscal.model.ts`         |
| Spec (teste)     | `nome-feature.component.spec.ts`     | `doc-fiscal-list.component.spec.ts` |
| Selector         | `app-nome-componente`                | `app-doc-fiscal-list`         |

## Estrutura de Feature Module

```
src/app/features/nome-feature/
├── nome-feature.module.ts
├── nome-feature-routing.module.ts
├── components/
│   ├── nome-feature-list/
│   │   ├── nome-feature-list.component.ts
│   │   ├── nome-feature-list.component.html
│   │   ├── nome-feature-list.component.scss
│   │   └── nome-feature-list.component.spec.ts
│   └── nome-feature-detail/
│       └── ...
├── services/
│   └── nome-feature.service.ts
└── models/
    └── nome-feature.model.ts
```

---

## Cenarios Frequentes

### Adicionar nova tela
1. Criar feature module com lazy loading
2. Criar componente(s) com OnPush change detection
3. Criar service com HttpProxyService + BehaviorSubject
4. Registrar rota no routing module pai
5. Importar modulos Bento/Material necessarios

### Corrigir bug em tela existente
1. Identificar o componente/service afetado
2. Verificar se e componente Mobilize (@libs/mbl-*) ou Angular nativo
3. Para Mobilize: seguir patterns do framework Mobilize
4. Para Angular nativo: seguir patterns padrao do projeto

### Adicionar coluna/filtro em grid
1. Localizar o FlexGrid (Wijmo) no template
2. Adicionar `<wj-flex-grid-column>` no template
3. Atualizar model/interface com novo campo
4. Atualizar service se necessario (novo parametro de API)

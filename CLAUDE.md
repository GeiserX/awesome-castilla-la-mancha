# CLAUDE.md — awesome-castilla-la-mancha

## Propósito

Selección de software open source que da **soporte específico a Castilla-La Mancha** — su gobierno autonómico (JCCM), ayuntamientos, universidades, empresas, infraestructuras y patrimonio. Todo el contenido en español. El foco es Castilla-La Mancha: el software debe dirigirse específicamente a esta comunidad autónoma o a sus municipios.

## Ámbito

- **5 provincias**: Albacete, Ciudad Real, Cuenca, Guadalajara, Toledo.
- Principales ciudades: Toledo (capital), Albacete, Ciudad Real, Guadalajara, Cuenca, Talavera de la Reina, Puertollano, Tomelloso, Alcázar de San Juan, Hellín, Valdepeñas, Manzanares, Daimiel, Almansa, La Solana, Socuéllamos, Villarrobledo, Illescas, Seseña, Azuqueca de Henares, La Roda, Madridejos, Consuegra, Campo de Criptana, Sigüenza.
- **Universidad**: UCLM (Universidad de Castilla-La Mancha — campuses en Albacete, Ciudad Real, Cuenca, Toledo y Talavera de la Reina).
- **Instituciones**: JCCM (Junta de Comunidades de Castilla-La Mancha), SESCAM (Servicio de Salud de Castilla-La Mancha), Instituto de Estadística de CLM, Confederación Hidrográfica del Guadiana, Confederación Hidrográfica del Tajo.

## Criterios de inclusión

### Incluir

- Software que interactúa con la **JCCM** o sus organismos (Sede Electrónica, Portal de Transparencia, datos abiertos, DOCM).
- Herramientas para **ayuntamientos** de Castilla-La Mancha.
- Software de la **UCLM** cuando sea específico de la región o la universidad.
- Herramientas de **datos abiertos** de Castilla-La Mancha.
- Software relacionado con el **medio ambiente** de CLM (Tablas de Daimiel, Lagunas de Ruidera, Parque Nacional de Cabañeros, ríos Tajo, Guadiana, Júcar, Segura).
- Herramientas de **agricultura** de CLM (viñedos, azafrán, aceite de oliva, queso manchego).
- Software de **transporte** castellanomanchego (autobuses urbanos, interurbanos).
- Herramientas de **cartografía y SIG** específicas de CLM.
- Software sobre **turismo y patrimonio** de la región (Ruta de Don Quijote, molinos de viento, castillos, casco histórico de Toledo/Cuenca).
- Herramientas de **energía** regional (hidrógeno verde Puertollano, energía solar, eólica).
- Software sobre **deportes** de CLM (Albacete Balompié, CF Talavera, equipos locales).
- Proyectos del **sistema sanitario** de CLM (SESCAM, hospitales).
- Software **educativo** específico de la región.
- Herramientas de **meteorología** regional.
- Proyectos de **industria y empresa** castellanomanchega.

### No incluir

- Software **genérico** que funciona en toda España sin funcionalidad específica de CLM — eso pertenece a awesome-spain.
- Software de **ámbito europeo** — eso pertenece a awesome-europe.
- Software de **otras comunidades autónomas** españolas.
- Software creado por castellanomanchegos que **no tiene funcionalidad específica** de la región.
- Repositorios **archivados o de solo lectura** — van a `DELETED.md`.
- Repos donde el autor indica que el proyecto está **roto, sin mantenimiento o deprecado**.
- Repos **sin README significativo** o que son claramente repos de test/experimento.
- Ejercicios de clase o trabajos académicos sin utilidad real.

### Zona gris — usar criterio

- Proyectos de la UCLM que podrían ser genéricos — incluir si tienen datos o configuración específica de CLM.
- Software que cubre CLM junto con otras regiones — incluir si CLM es un foco principal.

## Estándares de calidad

**Mismo listón que [awesome-spain](https://github.com/GeiserX/awesome-spain):**

- **No repos archivados**: si se descubre archivado tras la inclusión, mover a `DELETED.md` inmediatamente.
- **No repos extremadamente sin mantenimiento**: al menos un commit en los últimos 3 años, salvo que sea un proyecto claramente estable/completo.
- **No repos rotos**: si el README dice «deprecated», «no longer maintained», «use X instead» o similar — no incluir. Mover a `DELETED.md` si ya está listado.
- **Estrellas mínimas**: preferir repos con al menos unas pocas estrellas, pero herramientas nicho excepcionales con 0-1 estrellas pueden incluirse si cubren un hueco importante.
- **Verificar cada repo** antes de añadir: comprobar `archived`, `pushed_at`, `stargazers_count` vía `gh api repos/owner/name`.

## Formato de entrada

```markdown
- [Nombre](https://github.com/owner/repo) [![Stars](...)](stargazers) [![Last Commit](...)](commits) [![Language](...)](repo) [![License](...)](LICENSE) [![Tag](...)](url) - Descripción que empieza en mayúscula y termina con punto.
```

Las insignias se generan automáticamente con `scripts/transform-readme.py`. Para contribuir, basta con añadir la entrada en formato simple:

```markdown
- [Nombre](https://github.com/owner/repo) - Descripción que empieza en mayúscula y termina con punto.
```

- La descripción **no debe empezar con el nombre** del proyecto.
- Máximo una línea por entrada.
- Validar con awesome-lint-extra: `python3 lint.py` o mediante el workflow de CI.
- Entradas en **orden alfabético** dentro de cada categoría.
- Categorías en **orden alfabético** en el índice y en el cuerpo del documento.
- Entradas en `DELETED.md` también en **orden alfabético** dentro de cada sección.

## Verificación antes de añadir

Antes de incluir un repositorio, comprobar:

- **Existe y es público**: el enlace de GitHub funciona y el repo no es privado.
- **No está archivado o de solo lectura**: si archivado, va a `DELETED.md` (sección «Archivados»).
- **No está deprecado**: comprobar si el README dice «deprecated», «unmaintained», «broken», «use X instead».
- **Actividad razonable**: al menos un commit en los últimos 3 años, salvo que sea un proyecto estable/completo.
- **No es un duplicado**: cruzar con `README.md` y `DELETED.md`.
- **Calidad mínima**: tiene documentación (README) y no es un repositorio vacío o de test.

## Pull requests y contribuciones

- Las PRs deben usar la plantilla en `.github/PULL_REQUEST_TEMPLATE.md`.
- **Obligatorio**: incluir en la PR la **URL del servicio, API o institución castellanomanchega** a la que el software da soporte.
- Plantillas de issues disponibles para sugerir proyectos (`anadir-proyecto.md`) y solicitar retirada (`retirar-proyecto.md`).

## Estructura

- Secciones con `##`, subsecciones con `###`.
- Índice de contenido al principio entre comentarios `<!--lint disable/enable awesome-list-item-->`.
- Al final: sección Contribuir, Nota y Descargo de responsabilidad (como párrafos en negrita, no encabezados ##).

## Temas prohibidos

No se aceptan proyectos relacionados con: pornografía, contenido NSFW, loterías o apuestas, religión, política partidista.

## Difusión

- Notificar a los propietarios de repos abriendo un issue titulado «Listado en awesome-castilla-la-mancha» con un breve mensaje en español (tuteo) ofreciendo retirar si lo prefieren. Solo 1 issue por organización/usuario — no spamear repos del mismo propietario.
- Publicar en comunidades de CLM (Reddit, foros de la UCLM, Telegram de devs, GDG Toledo, TomellosoTech) tras alcanzar masa crítica.
- Enviar PR a [sindresorhus/awesome](https://github.com/sindresorhus/awesome) tras 30 días desde la creación del repo.

## Aprendizajes

- Las búsquedas en GitHub con `"castilla la mancha"` dan resultados limitados. Es más efectivo buscar por instituciones (JCCM, UCLM, SESCAM), ciudades (Toledo, Albacete, Ciudad Real, Talavera) y comunidades (GDG Toledo, TomellosoTech).
- Muchos repos de la UCLM son ejercicios de clase sin utilidad real — filtrar con criterio.
- La UCLM tiene organización `UCLM-ESI` con repos útiles (plantillas TFG, materiales de sistemas distribuidos).
- `UCLM-eiia-to` es la Escuela de Ingeniería Industrial y Aeroespacial de Toledo con plantilla TFG.
- `gdgtoledo` (GDG Toledo) tiene el ecosistema Katangapp (app de autobuses de Toledo) y Talabus (autobuses de Talavera).
- `TomellosoTech` es una comunidad tech de Tomelloso (Ciudad Real) con repos de open data y herramientas locales.
- `IsidroHidalgo` tiene herramientas de análisis de empleo y desempleo específicas de CLM.
- `carmenbelenm` tiene repos de sostenibilidad y Agenda 2030 de Albacete (UCLM + Ayuntamiento).
- `civio` tiene el visor de presupuestos de la JCCM (presupuesto-castillalamancha).
- `sao-albacete` es la Sociedad Albacetense de Ornitología con el anuario ornitológico online.
- La JCCM no tiene organización propia en GitHub.
- El SESCAM no tiene presencia significativa en GitHub — solo ejercicios de clase de gestión sanitaria.
- **Toledo**: la mayoría de resultados de búsqueda confunden con Toledo, Ohio (EE.UU.). Filtrar siempre.
- **Guadalajara**: la mayoría de resultados de búsqueda confunden con Guadalajara, México. Filtrar siempre.
- **Cuenca**: también confunde con Cuenca, Ecuador. Filtrar siempre.
- No hay co-lengua oficial — todo en español.

*Generated by [LynxPrompt](https://lynxprompt.com) CLI*

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:6cd5cc61 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

## Agent Context Profiles

The managed Beads block is task-tracking guidance, not permission to override repository, user, or orchestrator instructions.

- **Conservative (default)**: Use `bd` for task tracking. Do not run git commits, git pushes, or Dolt remote sync unless explicitly asked. At handoff, report changed files, validation, and suggested next commands.
- **Minimal**: Keep tool instruction files as pointers to `bd prime`; use the same conservative git policy unless active instructions say otherwise.
- **Team-maintainer**: Only when the repository explicitly opts in, agents may close beads, run quality gates, commit, and push as part of session close. A current "do not commit" or "do not push" instruction still wins.

## Session Completion

This protocol applies when ending a Beads implementation workflow. It is subordinate to explicit user, repository, and orchestrator instructions.

1. **File issues for remaining work** - Create beads for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **Handle git/sync by active profile**:
   ```bash
   # Conservative/minimal/default: report status and proposed commands; wait for approval.
   git status

   # Team-maintainer opt-in only, unless current instructions forbid it:
   git pull --rebase
   git push
   git status
   ```
5. **Hand off** - Summarize changes, validation, issue status, and any blocked sync/commit/push step

**Critical rules:**
- Explicit user or orchestrator instructions override this Beads block.
- Do not commit or push without clear authority from the active profile or the current user request.
- If a required sync or push is blocked, stop and report the exact command and error.
<!-- END BEADS INTEGRATION -->

## Where the tracker syncs

This repo is public, so its tracker syncs only to the private remote named by `sync.remote` in `.beads/config.yaml`. The block above says sync uses "your git remote". Here that never means this GitHub repo. Don't add it as a Dolt remote and don't push `refs/dolt/*` to it.

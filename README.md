# GSES3
Тестове завдання для Genesis Software Engineering School 3.0
Реалізоване на мові Python з використанням фреймворку FastAPI.

> На жаль, не маю можливості доробити, бо в батьків вітчима 
> під час артилерійського обстрілу розвалило хату, і я трошки 
> мушу їм допомогти. В деяких місцях залишив коментарі з 
> розрахунку того, як це має бути.

## Хід думок:

Маю гарну звичку користуватися conventional commits, через що 
відслідковувати хід думок під час написання проєкту стає дуже 
просто:

```
ci(project): introduce requirements.txt to build project
feat(structure): sketch required endpoints 
fix(endpoints): make endpoints closer match api specs
fix(subscribe): introduce email validation for /subscribe endpoint
feat(rate): make /rate endpoint work with real data
style(subscribe): sketch API levels for subscribe.py
test(subscribe): create some tests cases that do fail yet
feat(subscribe): implement actual functionality so module does something actually useful now
style(subscribe): add comment that elaborates usage of broad Exception usage instead of a specific one
test(subscribe): amend tests to make them more reliable
style(test): adjust codestyle in fixtures
feat(subscribe): make exception show which e-mail failed to add to enhance UX
feat(app): introduce db setup function to create db for current project, if needed
feat(app): introduce exception handler for app that creates response based on exception
feat(subscribe): make endpoint actually useful
style(structure): separate core to another package, so project is more flexible and all its handlers are reusable
feat(mailing): sketch mailing module structure
refactor(db): separate db and make it more flexible via adjusting db backend
fix(mailing): make mailing.py use some useful existing functions
feat(mailing): introduce stubs for future enhancements of project
fix(db): fix db.csv default file paths
ci(docker): create Dockerfile for project
```

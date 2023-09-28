TITLE = 'Adivinando personajes de Marvel'

DESCRIPTION = '''
Implemente un "clon" de [Akinator](https://es.akinator.com/) que permita adivinar el personaje de [Marvel](https://marvel.fandom.com/es/wiki/Categor%C3%ADa:Personajes) en base a las tres preguntas siguientes:
1. ¿Puede volar? → Se representa por la variable de entrada: **can_fly**
2. ¿Es humano? → Se representa por la variable de entrada: **is_human**
3. ¿Tiene máscara? → Se representa por la variable de entrada: **has_mask**
```
                                                ✔
                                            ┌──────► Ironman
                              ✔             │
                            ┌───► Has mask? │
                            │               │
                            │               └──────► Captain Marvel
                            │                   ˟
             ✔              │
         ┌──────► Is human? │
         │                  │                   ✔
         │                  │               ┌──────► Ronan Accuser
         │                  │               │
         │                  └───► Has mask? │
         │                    ˟             │
         │                                  └──────► Vision
         │                                      ˟
         │
Can fly? │
         │                                      ✔
         │                                  ┌──────► Spiderman
         │                    ✔             │
         │                  ┌───► Has mask? │
         │                  │               │
         │                  │               └──────► Hulk
         │                  │                   ˟
         │                  │
         └──────► Is human? │
             ˟              │                   ✔
                            │               ┌──────► Black Bolt
                            │               │
                            └───► Has mask? │
                              ˟             │
                                            └──────► Thanos
                                                ˟
```
'''

ENTRYPOINT = {
    'PARAMS': [
        ['can_fly', bool],
        ['is_human', bool],
        ['has_mask', bool],
    ],
    'RETURN': [
        ['character', str],
    ],
}

CHECK_CASES = [
    [[True, True, True], ['Ironman']],
    [[True, True, False], ['Captain Marvel']],
    [[True, False, True], ['Ronan Accuser']],
    [[True, False, False], ['Vision']],
    [[False, True, True], ['Spiderman']],
    [[False, True, False], ['Hulk']],
    [[False, False, True], ['Black Bolt']],
    [[False, False, False], ['Thanos']],
]

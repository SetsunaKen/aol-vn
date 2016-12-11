## The Anthem of Love - Prima Sonata
## by Setsuna Ken
## https://setsuna-ken.online

define so = Character('Sora Kurosaki')
define em = Character('Emi Kanagi')
define yu = Character('Yuzuki Sasagawa')
define ara = Character('Arata Ishida')
define to = Character('Touka Kisoki')
define ri = Character('Rina Hashibara')
define sh = Character('Shiori Tachibana')

label splashscreen:
    scene black with fade
    show text "The Anthem of Love\nAlpha Demo" with fade
    $renpy.pause(3.0)
    return

label start:
    stop music fadeout 1.0
    jump prologue

label end:
    return

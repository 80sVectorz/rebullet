from bullets import BulletCli
from bullets import colors

cli = BulletCli(
        choices = ["apple", "banana", "orange", "watermelon", "strawberry"], 
        indent = 0,
        align = 5, 
        margin = 2,
        bullet = "★",
        bullet_color=colors.bright(colors.foreground["cyan"]),
        word_color=colors.bright(colors.foreground["yellow"]),
        word_on_switch=colors.bright(colors.foreground["yellow"]),
        background_color=colors.background["black"],
        background_on_switch=colors.background["black"],
        pad_right = 5
    )

result = cli.launch("\nPlease choose a fruit: ")
print("You chose:", result)

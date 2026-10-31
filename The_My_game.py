# ================================================
# ИГРА «ПОДЗЕМЕЛЬЕ: КРИСТАЛЬНАЯ ПЕЩЕРА»
# Автор: Алёна Архипова
# Дата начала написания кода: сентябрь 2026
# ================================================

 # --- Заголовок ------------------------------------ #
import random

title = "ПОДЗЕМЕЛЬЕ: КРИСТАЛЬНАЯ ПЕЩЕРА"
frame = "=" * 40

print(frame)
print("    " + title + "    ")
print(frame)

print()

# --- Знакомство с героем -------------------------- #
print("Как зовут героя?") 

hero_name = input()
frame = "=" * 85

print(frame)

print(f"Добро пожаловать, {hero_name}!") 
text = "Перед тобой подземелье. Здесь светло, свет дают кристаллы разного размера и цвета, растущие из стен, тихо, пахнет сыростью, но зато красиво)"

print("    " + text + "    ")
print(frame)

print("Нажмите ENTER для продолжения") 
input()

# --- Характеристики героя -----------------------------------

frame = "=" * 83

print(frame)

text = "Характеристика героя:"

health = 100
strength = 17
reverse_of_strength = 15
stamina = 60
crit_health = 10
damage = 10

print("    " + text + "    ")
print(frame)

# ----- Расчет урона ------------------------------

base_attack = 2
damage = base_attack + strength * 1.2
crit_damage = damage * 2

print(f"Здоровье: {health}")
print(f"Сила: {strength}")
print(f"Выносливость: {stamina}")
print(f"Урон героя: {damage:.1f}")
print(f"Критический уровень здоровья: {crit_health}")
print(f"Запас сил: {reverse_of_strength}")
print(f"Критический урон: {crit_damage:.1f}")

print()

def hero_hit(strike_n):
    if strike_n % 3 == 0:
        return 
crit_damage, True 
damage, False

# --- Выбор перед героем -----------------------------------

running = True 
actions = 0

enemies = ["призрак", "скелет", "паук", "летучая мышь"]
useful_phrases = ["Что сделаешь первым делом?","Что будешь делать теперь?"]
log = []
enemy_hp = 45 
round_n = 0 
enemy_damage = 10
menu_last = 9

frame = "=" * 83
print(frame)

while running:
    text1 = "1 - осмотрюсь, ведь такой пещеры я еще не видел"
    text2 = "2 - пойду вперед, разведую обстановку"
    text3 = "3 - прислушаюсь и убежусь, настолько ли в этой пещере тихо"
    text4 = "4 - полюбуюсь кристаллами, они красивые)"
    text5 = "5 - возьму для себя кристалл в качестве сувенира, что бы друзья точно поверили, что я тут был!"
    text6 = "6 - потренируюсь, в пещере могут быть враги, надо быть готовым к наподению!"
    text7 = "7 - пройду глубже в пещеру, интересно, что там в глубине"
    text8 = "8 - Дайте посмотреть таблицу лидеров!"
    print()
    if actions == 0:
        print(useful_phrases.pop(0))
    else:
        print(useful_phrases[0])
        #print(useful_phrases[(actions - 1) % len(useful_phrases)])
    print("    " + text1 + "    ")
    print("    " + text2 + "    ")
    print("    " + text3 + "    ")
    print("    " + text4 + "    ")
    print("    " + text5 + "    ")
    print("    " + text6 + "    ")
    print("    " + text7 + "    ")
    print("    " + text8 + "    ")
    if actions > 3:
            text0 = "0 - покинуть подземелье"
            print("    " + text0 + "    ")
    print(frame)

# --- Выбор героя ----------------------------------

    while True:
        choice = input()         
        try:
            menu_number = int(choice)         
        except ValueError:
            print("Такого пункта нет. Введи номер пункта из меню")
            continue         
        if 0 <= menu_number <= menu_last:
            break
        print("Такого пункта нет. Введи номер пункта из меню")

    choice = str(menu_number)

    match choice:
        
        case "0":
           frame = "=" * 83
           print("    " + text + "    ")
           print(frame)
           if actions > 2:
               print(frame)
               text = "Ты поднимаешься обратно к свету. Подземелье остаётся позади, а ты на свободе"     
               running = False
           else:
               print("Тебе еще рано выходть, ты не исследовал пещеру!")

        case "1":
            frame = "=" * 83
            print(frame)
            text = "Ты осматриваешься. Вокруг лишь свет, кристаллы и тишина"
            print("    " + text + "    ")
            print(frame)

        case "2":
            reverse_of_strength = reverse_of_strength - 2
            cost = 2         
            if reverse_of_strength >= cost:             
                reverse_of_strength -= cost
            else:
                health -= cost - reverse_of_strength
                reverse_of_strength = 0
                print("Силы кончились — тобой движет лишь упорство")
            frame = "=" * 83
            print(frame)
            text = "Ты идешь вперед. Пол усыпан осколками светящихся кристаллов, создавая красивую подсветку на каменном полу пещеры"
            print("    " + text + "    ")
            print(frame)

        case "3":
            frame = "=" * 83
            print(frame)
            text ="Ты прислушиваешься к звукам пещеры - тишина, слышно только твое дыхание, рядом ни души..."
            print("    " + text + "    ")
            print(frame)

        case "4":
            reverse_of_strength = reverse_of_strength + 2
            frame = "=" * 83
            print(frame)
            text = "Ты подходишь к ближайшему кристаллу и рассматриваешь его, подмечая детали: форму, размер, свет, что он излучает... Красиво, не правда ли?"
            print("    " + text + "    ")
            print(frame)

        case "5":
            reverse_of_strength = reverse_of_strength -2
            cost = 2         
            if reverse_of_strength >= cost:             
                reverse_of_strength -= cost
            else:
                health -= cost - reverse_of_strength
                reverse_of_strength = 0
                print("Силы кончились — тобой движет лишь упорство")
            frame = "=" * 83
            print(frame)
            text = "Ты подходишь к ближайшему кристаллу, достаешь из за спины свою кирку и осторожно откалываешь себе кусочек светящегося кристалла, размером с..."
            print("    " + text + "    ")
            print(frame)

        case "6":
            reverse_of_strength = reverse_of_strength -3
            cost = 2         
            if reverse_of_strength >= cost:             
                reverse_of_strength -= cost
            else:
                health -= cost - reverse_of_strength
                reverse_of_strength = 0
                print("Силы кончились — тобой движет лишь упорство")
            strikes = 7
            total_damage = 0
            crit_count = 0

            frame = "=" * 83
            print(frame)
            text = "Ты подходишь к тренировочному чучелу, что видишь неподалеку от входа пещеру. Оно стоит здесь стех пор, как сюда приходил последний искатель. Видимо ему оно не помогло... Давай узнаем, поможет ли оно в будущем тебе?"
            print("    " + text + "    ")
            print(frame)

            print(f"Ты наносишь {strikes} ударов")
            
            for i in range(1, strikes, + 1):
                if i % 3 == 0:
                    hit_damage = crit_damage
                    crit_count += 1
                    print(f"Критический удар {i}: {hit_damage: .1f} урона")
                else:
                    hit_damage = damage
                    print(f"Удар {i}: {damage: .1f} урона")
                total_damage += hit_damage

        case "7":
            frame = "=" * 83
            print(frame)
            text = "Ты проходишь в глубь пещеры, говорят, оттуда никто не возвращался, но тебя это не пугает"
            enemy = random.choice(enemies)
            print("    " + text + "    ")
            print(f"И тут на тебя наподает {enemy}! Ты берешь свою дубинку и начинаешь отбиваться")
            print("Раунд 1")

            while enemy_hp > 0 and health > 0:
                round_n += 1
                crit_enemy = round_n % 3 == 0
                hit = crit_damage if crit_enemy else damage
                enemy_hp -= hit
                line = f"Раунд {round_n} завершен! Ты нанес {hit} урона!"

                if enemy_hp <= 0:           
                    line = "Враг повержен... пока"                             
                    log.append([round_n, hit, 0])                         
                else:                             
                    blow = random.randint(2, 6)
                    health -= blow
                    line = f"Здоровье {enemy}'а: {enemy_hp:.1f} \n{enemy.capitalize()} нанес-(ла) тебе {blow} единиц-(ы) урона"
                    log.append([round_n, hit, blow])
                    print(line)
            if enemy_hp <= 0:
                enemies.remove(enemy)
                print(f"{enemy} побежден! Осталось {len(enemies)} врага")
            print(f"Было {round_n} раунда-(ов)")
            print(frame)

        case 8:
            frame = "=" * 83
            print(frame)
            if not log:
                print(f"Рано тебе еще таблицу глядеть, {hero_name}! \nТы еще не сражался")                 
            else:
                top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
                worst = max(log, key=lambda r: r[2])                     
                print(f"Наибольший урон врага: {worst[2]} (round {worst[0]})")
                print(f"Таблица лидеров (урон {hero_name}):")                     
            for i in range(len(top)):                         
                print(f"{i + 1}. Round {top[i][0]}: {top[i][1]:.1f}")
            print(frame)

        case _:
            print("Такого действия нет")

# ---- Строка состояния героя -------------------------
    if running:
        actions += 1
    print(f"Здоровье: {health}")
    print(f"Запас сил: {reverse_of_strength}")

    if health <= 0:
        print(f"{hero_name} падает без сил. Подземелье забирает ещё одного искателя приключений. А ведь все так хорошо начиналось...")         
        running = False























# ================================================
# ИГРА «ПОДЗЕМЕЛЬЕ: КРИСТАЛЬНАЯ ПЕЩЕРА»
# Автор: Алёна Архипова
# Дата начала написания кода: сентябрь 2026
# ================================================

        # --- Прощание ------------------------------------ #
title = "ПОДЗЕМЕЛЬЕ: КРИСТАЛЬНАЯ ПЕЩЕРА"
frame = "=" * 40

print(frame)
print("    " + title + "    ")
print(frame)
print(f"Забег окончен! Это пока всё. \nДо скорых встреч, {hero_name}! \nДействий совершено: {actions}") 
print(frame)

print()

print(frame) 
if health <= 0:     
    print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}") 
else:
    print(f"Забег окончен, {hero_name}. Действий совершено: {actions}") 

print(frame)
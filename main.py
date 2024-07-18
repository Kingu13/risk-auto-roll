"""import random

def attack_and_defend():
    try:
        num_troops_attack = int(input("Enter attacking troops: "))
    except ValueError:
        print("Enter a number. ")
        return
    
    try:
        num_troops_defend = int(input("Enter defending troops: "))
    except ValueError:
        print("Enter a number. ")
        return
    
    if num_troops_attack >= 3:
        dice_attacking = 3
    elif num_troops_attack == 2:
        dice_attacking = 2
    else:
        dice_attacking = 1

    if num_troops_defend >= 2:
        dice_defending = 2
    else:
        dice_defending = 1
        
    rolls_attacking = roll_dice(dice_attacking)
    rolls_attacking.sort(reverse=True)
    print(f"Attacker rolls: {rolls_attacking}")
    
    rolls_defending = roll_dice(dice_defending)
    rolls_defending.sort(reverse=True)
    print(f"Defending rolls: {rolls_defending}")
    
    compare_dice(rolls_attacking, rolls_defending, num_troops_attack, num_troops_defend)

    
    
def roll_dice(num_dice):
    rolls = [random.randint(1, 6) for i in range(num_dice)]
    return rolls

def compare_dice(rolls_attacking, rolls_defending, num_troops_attack, num_troops_defend):
    # Compare the highest rolls
    attacker_losses = 0
    defender_losses = 0
    
    for i in range(min(len(rolls_attacking), len(rolls_defending))):
        if rolls_attacking[i] > rolls_defending[i]:
            defender_losses += 1
        else:
            attacker_losses += 1
    
    print(f"Attacker loses {attacker_losses} troops.")
    print(f"Defender loses {defender_losses} troops.")
    
    num_troops_attack -= attacker_losses
    num_troops_defend -= defender_losses
    
    print(f"Remaining attacking troops: {num_troops_attack}")
    print(f"Remaining defending troops: {num_troops_defend}")
        
     
attack_and_defend()
    """
    
import random

def attack_and_defend():
    try:
        num_troops_attack = int(input("Enter attacking troops: "))
    except ValueError:
        print("Enter a valid number.")
        return
    
    try:
        num_troops_defend = int(input("Enter defending troops: "))
    except ValueError:
        print("Enter a valid number.")
        return

    while num_troops_attack > 0 and num_troops_defend > 0:
        if num_troops_attack >= 3:
            dice_attacking = 3
        elif num_troops_attack == 2:
            dice_attacking = 2
        else:
            dice_attacking = 1

        if num_troops_defend >= 2:
            dice_defending = 2
        else:
            dice_defending = 1
            
        rolls_attacking = roll_dice(dice_attacking)
        rolls_attacking.sort(reverse=True)
        print(f"Attacker rolls: {rolls_attacking}")
        
        rolls_defending = roll_dice(dice_defending)
        rolls_defending.sort(reverse=True)
        print(f"Defender rolls: {rolls_defending}")
        
        num_troops_attack, num_troops_defend = compare_dice(rolls_attacking, rolls_defending, num_troops_attack, num_troops_defend)

        if num_troops_attack <= 0:
            print("Attacker has no troops left. Defender wins!")
            break
        if num_troops_defend <= 0:
            print("Defender has no troops left. Attacker wins!")
            break
        
        user_input = input("Press Enter to continue the battle or type retreat to stop the attack: ")
        if user_input.lower() == "retreat":
            break


def roll_dice(num_dice):
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    return rolls

def compare_dice(rolls_attacking, rolls_defending, num_troops_attack, num_troops_defend):
    attacker_losses = 0
    defender_losses = 0
    
    for i in range(min(len(rolls_attacking), len(rolls_defending))):
        if rolls_attacking[i] > rolls_defending[i]:
            defender_losses += 1
        else:
            attacker_losses += 1
    
    print(f"Attacker loses {attacker_losses} troops.")
    print(f"Defender loses {defender_losses} troops.")
    
    num_troops_attack -= attacker_losses
    num_troops_defend -= defender_losses
    
    print(f"Remaining attacking troops: {num_troops_attack}")
    print(f"Remaining defending troops: {num_troops_defend}")
    
    return num_troops_attack, num_troops_defend

attack_and_defend()

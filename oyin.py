import time
import random
import sys

def oyin_boshlash():
    print("="*40)
    print("   KULGILI O'PISHISH O'YINI (Termux Edition) ")
    print("="*40)
    print("Vazifa: Sezdirmasdan marraga yetib o'pishish!")
    print("Akasi kelib qolganda 'w' tugmasini bosib yashirining!")
    print("Yaqinlashish uchun har safar 'Enter' bosasiz.\n")
    
    masofa = 10  # Qolgan qadamlar
    
    while masofa > 0:
        # Har qadamda akasi kelish xavfi (30% imkoniyat)
        xavf = random.random() < 0.3
        
        if xavf:
            print("\n⚠️  DIQQAT! Qizning akasi uzoqdan ko'rinib qoldi!!!")
            print("Tezda yashirinish uchun 'w' deb yozing va Enter bosing!")
            
            start_time = time.time()
            harakat = input("Sizning harakatingiz: ").strip().lower()
            end_time = time.time()
            
            # Agar 3 soniyadan kechiksa yoki 'w' bosmasa
            if end_time - start_time > 3.0:
                print("\n❌ GAME OVER! Juda sekin harakat qildingiz, akasi ushlab oldi! 👊")
                return
            elif harakat != 'w':
                print("\n❌ GAME OVER! Yashirinishga ulgurmadingiz! 🏃‍♂️💨")
                return
            else:
                print("✅ Ofarin! Yashirinishga ulgurdingiz. Akasi ketdi. Davom etamiz...")
                time.sleep(1)
                continue
        
        # Oddiy holatda yaqinlashish
        input(f"\n[Marragacha {masofa} qadam]. Yaqinlashish uchun Enter bosing...")
        masofa -= 1
        print("👩 " + " " * (masofa * 2) + "👨") # Xarakterlar yaqinlashmoqda

    print("\n" + "="*40)
    print("🎉 G'ALABA! Hech kimga sezdirmasdan marraga yetdingiz! 👩‍❤️‍👨💋")
    print("="*40)

oyin_boshlash()

print("""Wifi Görüntüleyici

                        --
""")

import time

while True:

    import subprocess

    print("Sistem analiz ediliyor")
    import time

    time.sleep(1)

    print("Bulunan Wifiler: ")

    veri = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    sistemler = [i.split(":")[1][1:-1] for i in veri if "All User Profile" in i]
    for i in sistemler:
        sonuç = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split(
            '\n')
        sonuç = [b.split(":")[1][1:-1] for b in sonuç if "Key Content" in b]
        try:
            print(" \\{:<30}| Şifre:  {:<}".format(i, sonuç[0]))
        except IndexError:
            print(" \\{:<30}| Şifre:  {:<}".format(i, ""))

    exe = int(input("\n \n \n1'e basarak yeniden sistemi analiz edebilirsiniz \n2'ye basarak çıkış yapabilirsiniz "))
    if (exe == 1):
        print("")
        import time

        time.sleep(1)


    elif (exe == 2):
        print("")
        import time

        time.sleep(1)
        break
        quit()

    else:
        print("Bir hata yaptınız lütfen tekrar deneyin")
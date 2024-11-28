if True:
    print("hello_world!")
print("maraba")


if not True:
    print("hello_world!")
print("maraba")



yas=input("yaşınızı girin")








yas=int(input("yaşınızı girin:"))
if (yas>=18):
    print("ehliyet alabilirsiniz")

if (yas<18):
    print("ehliyet alamazsınız")






instagram_db={
"username":"ellap",
"password":"12345"
}
username=input("kullanıcı adınızı girin:")
password=input("Lütfen şifrenizi girin:")

if (instagram_db["username"]==username and instagram_db["password"]==password):
    print("Hesaba başarılı bi şekilde girdiniz")

if (instagram_db["username"]!=username and instagram_db["password"]==password):
    print("Yanlış kullanıcı adı")

if (instagram_db["username"]==username and instagram_db["password"]!=password):
    print("Yanlış şifre")

if (instagram_db["username"]!=username and instagram_db["password"]!=password):
    print("Şifre ya da kullanıcı adı yanlış")








a=int(input("yaşınızı girin:"))

if(65>a>=18):
    print("motorsiklet ve araba ehliyeti alabilirisiniz")
elif(18>a>=15):
    print("motorsiklet ehliyeti alabilirsin")
else:
    print("ehliyet alamazsın")






al_vb={"kart_no":"123456","cvv":"110","skl":"10/26"}

kn=input("kredi kartı girin:")
cv=input("cvv girin:")
sk=input("son kullanma tarihi girin:")

if((kn==al_vb["kart_no"])and(cv==al_vb["cvv"])and(sk==al_vb["skl"])):
    print("bilgiler doğrulandı")
else:
    print("yanlış bilgi girildi")




a=int(input("sayı gir"))
b=int(input("sayı gir"))
c=int(input("sayı gir"))

if(a>b>c):
    print(a)
elif(a>c>b):
    print(a)
elif(b>a>c):
    print(b)
elif(b>c>a):
    print(b)
elif(c>a>b):
    print(c)
elif(c>b>a):
    print(c)
else:
    print("sayılar arasında eşitlik var")


if(85<=do<=100):
    print("takdir belgesi aldınız")
elif(70<=do<85):
    print("teşekkür belgesi aldınız")
else:
    print("hiçbir belge alamadınız")




a=float(input("metre cinsinden boyunuzu girin:"))
b=float(input("kilogram cinsinden kilonuzu girin:"))

f=b/a**2

print(f)

if(f<=18.4):
    print("Çok zayıfsınız")
elif(18.5<=f<=24.9):
    print("sağlıksınız")
elif(25<=f<=29.9):
    print("şişmansınız")
elif(30<=f<=40):
    print("obezsiniz")
else:
    print("marbid obezsiniz")







a=input("c mi f mi:")




if(a=="c"):
    b=float(input("celcius gir:"))
    f1=(b-32)/1.8
    print("{} celcius {}fahrenayta eşit".format(b,f1))
elif(a=="f"):
    b=float(input("fahrenayt gir:"))
    f1=(b*1.8)+32
    print("{} fahrenayt {}celcius eşit".format(b,f1))

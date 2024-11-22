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

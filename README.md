Bu belge deneme yapmak amacıyla oluşturuldu!

# Keci

## Kullanım Talimatları

Kendi bilgisayarınızda lokal olarak siteyi çalıştırabilmek için sırasıyla,

1-Python 3.8.5 indirmeniz

2-git sistemini kurmanız

3-bir klasöre bu repository-i klonlamanız

4-Klonladığınız dosyada veya -virtualenvwrapper ile- system-wide bir virtuelenv kurmanız

5-requiriments.txt'de belirtilen package'ları indirmeniz

6-migration'ları yapmanız

gerekiyor. Ardından klasörde açacağınız terminal/cmd ile kodları çalıştırabilirsiniz.

7-python manage.py runserver komutu ile sitenin çalıştırılması.

2.0 Linux ve Windows İçin Git Verisyon Kontrol Sisteminin İndirilmesi

Linux için https://git-scm.com/download/linux sitesinden kullandığınız distribution'a uygun şekilde git kurabilirsiniz.
Debian-Ubuntu için terminali açıp 'apt-get install git' komutunu çalıştırmanıoz yeterli olacaktır.

Windows için ise https://git-scm.com/download/win üzerinden doğrudan indirebilirsiniz.

2.1 Git Konfigürasyonunun Yapılması

Linux için terminalde, Windows için cmd'de sırasıyla kullanıcı adınızı ve e-posta adresinizi girmeniz gerekiyor.

    git config --global user.name "kullanıcı_adın"

    git config --global user.email "email_adresin@kimbilir.com"

3 keci Repository'sini Klonlanması 

Repo'yu klonlamak istediğiniz klasörde terminal veya cmd açarak aşağıdaki komutu çalıştırabilirsiniz (Repodaki belge ve klasörler keci/ klasörü içinde klonlanacak!),

    git clone https://github.com/dakyol/keci.git

daha sonra cd keci ile manage.py belgesinin bulunduğu konuma gidelim. İçinde bulunduğunuz klasörde manage.py belgesinin olduğundan emin olun.

4.0 virtualenv kurulması

Şimdi site yazılırken kullanılan framework'ü kurmamız gerekiyor. İndirilen packageler diğer projeleriniz için problem yaratabileceğinden virtalenv kullanmayı unutmayın.

...

5.0 Packagelerin indirilmesi

pip install -r requirements.txt ile belgede bulunan bütün packageleri tek seferde kurabilirsiniz. -r flag'ine dikkat edin.

6.0 migtrationların yapılması

Bulunduğunuz klasörde manage.py belgesinin bulunduğundan emin olduktan sonra sıraıylsa şu komutları çalıştırın,

    python manage.py makemigrations
    python manage.py migrate

Bu komutlar keci/model.py da yazan modellerde belirtilene uygun şekilde database oluşturacaktır. Bunu .dbsqlite uzantılı belgede görebilirsiniz.

7.0 Sitenin çalıştırılması

Aşağıdaki komut ilr django sitenizi çalıştırabilirsiniz

    python manage.py runserver

Not: karşınıza çıkan url'in sonuna /keci eklemeniz gerekiyor.

Tehcnologies used:

* Frontend: HTML5, CSS (Bootstrap5 and Custom CSS), JS
* Backend: Django, PostgreSQL
* Deployment: DigitalOcean

## Detailed Explanation of Frontend Technologies



## Detailed Explanation of Backend Technologies

Pagination

Download



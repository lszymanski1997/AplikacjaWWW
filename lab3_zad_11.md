from sample.models import Osoba
from sample.models import Druzyna
Osoba.objects.all()
Osoba.objects.get(id=3)
Osoba.objects.filter(imie__startswith="T") 
Druzyna.objects.exclude(osoba__isnull=True)
Druzyna.objects.order_by("nazwa")
o = Osoba(imie="Krzysztof",nazwisko="Krawczyk",miesiac_urodzenia="4")
o.save()


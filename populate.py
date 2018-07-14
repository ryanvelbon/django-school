import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bilbla.settings')
from django.conf import settings

import django
django.setup()
#
# from datetime import date
# from dateutil.relativedelta import relativedelta
#
# import random
from users.models import Locality
# from faker import Faker
#
# fakegen = Faker()

def populate_locality():
    """populates users.models.Locality"""

    Locality.objects.all().delete()
    LOCALITIES = ['Attard','Bahar ic-Caghaq','Bahrija','Balzan','Bidnija','Birguma','Birkirkara','Birzebbugia','Blata l-Bajda','Bugibba','Burmarrad','Buskett','Cirkewwa','Cospicua','Dingli','Dwejra','Fgura','Fleur-de-Lys','Floriana','Ghajn Tuffieha','Gharghur','Ghaxaq','Gnejna','Gudja','Gwardamangia','Gzira','Hal Farrug','Hal-Far','Hamrun','Ibrag','Ibrag, High Ridge','Ibrag, Victoria Gardens','Iklin','Kalafrana','Kalkara',
        'Kalkara, Smart City','Kappara','Kirkop','Lija','Luqa','Madliena','Madliena, Madliena Village','Maghtab','Manikata','Marsa','Marsascala','Marsascala, Ta&#39; Monita Residence','Marsaxlokk','Mdina','Mellieha','Mellieha, Ghadira','Mellieha, Santa Maria Estate','Mellieha, Tas-Sellum','Mgarr','Mosta','Mqabba','Mriehel','Msida','Mtahleb','Mtarfa','Naxxar','Paola','Pembroke','Pieta','Pwales','Qajjenza','Qawra','Qormi','Qrendi','Rabat','Rabat, Tal-Virtu','Ricasoli','Safi','Salina','San Gwann','San Gwann, Mensija','San Pawl tat-Targa','Santa Lucia','Santa Venera','Selmun','Senglea','Siggiewi','Sliema','Sliema, Fort Cambridge','Sliema, Tigne','Sliema, Tigne Point','St Julians','St Julians, Pender Gardens','St Julians, St George&#39;s Park','St Julians, The Gardens','St Pauls Bay','St. Julians, Paceville','St. Julians, Portomaso','St. Julians, Ta&#39; Giorni','St. Julians, The Village','Swatar','Swieqi','Swieqi, St Andrews','Ta&#39; Qali','Ta&#39; Xbiex','Tarxien','Valletta','Vittoriosa','Vittoriosa, St Angelo Mansions','Wardija','Xemxija','Xghajra','Zabbar','Zebbiegh','Zebbug','Zejtun','Zurrieq',]

    print("populating model Locality...")
    for locality in LOCALITIES:
        p = Locality.objects.get_or_create(
            name = locality,
        )[0]
    print("complete")

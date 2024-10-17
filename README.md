Spustenie:
 - dve rozdelené terminály
    pre backend:
        cieľom aby bolo toto Simple_Transport_Management_System> ale nie dva krát rovnaké po sebe 
        python manage.py runserver
    pre client: 
        cd client 
        cd django-vue-client
        npm run serve
Scenár:
    -po spustení sa na Local: ctrl+click sa zobrazí app. Skladá sa z troch klikateľných rôzdielnych sekcií, z tlačidla  
     ktoré zákazníkovi(používateľovi) umožnuje vykonať objednávku. Nachádza sa tu aj tabuľka, ktorá zobrazuje aktualné údaje s možnosťami pre
     edit alebo delete. 
     - Tlačidlo Order Transport zobrazí formulár, ktorý vykoná objednávku po vyplení príslušných hodnôt. Po úložení sa môžme vrátiť na sekciu
        Customers, ktorá zobrazí údaje z vytvorenej objednávky.
     - Tlačidlo Delete umožnuje vymazať alebo zrušiť objednávku a tlačidlo Edit upraviť a aktualizovať objednávku. 
     - V časti sekcie Departments je oddelenie pre zamestnancov. Nachádza sa tu tabuľka, ktorá zobrazuje údaje z objednávky nie z department, a takto môžu      
       sledovať a zabezpečiť jednotlivé objednávky. 
     - Sekcia Home je úvodná stránka.

     - Všetká funkčnosť medzi frontend a backend funguje, všetky jednotlivé api metody. V prípade formulára sa po uložení, 
       jednotlivé hodnoty nedokážu vypísať do tabuľky. Ale táto fukčnosť sa dá otestovať cez postman 
       a to zadaním príslušnej url http://127.0.0.1:8000/customer a zvolením methody(POST). 
       A po vložení údajov, je potrebné zvoliť metodu GET a tak získať výpis všetkých(pridaných) údajov. 
       - Pre tlačidlo edit je princíp podobne rovnaký ale z dôvodu nevpisania údajov z formulára je táto funkčnosť otestovaná
         cez postman a to takto:
                        http://127.0.0.1:8000/customer/1/edit
                                    cez put a vložením existujúcich dát s úpravou a po tlačidle Send sa záznam 
                                    úspešne editoval a aktualizoval čoho výsledkom je aj zmena na časti client, ktorá 
                                    už zobrazuje túto zmenu.
   



1.	Ako code editor som použil vscode(visual studio code), ktorý som už mal nainštalovaný, 
    takže jeho inštalácia nebola  potrebná. Pgadmin, budem potrebovať na použitie pre connect to postgresql a vytvorenie databázových objektov.
2.	Ďalej prebiehala inštalácia django to je:::: pip install django
	a ďalej pre vytvorenie rest api je potrebné nainštalovať:::: pip3 install djangorestframework
	Inak defaultne django project prichádza s bezpečnosťou, ktorá blokuje requests prichádzajúce z rôznych domains 
	preto pre vypnutie sa inštaluje:::: install django-cors-headers 

3.  Vytvorenie django projectu:
	1. Vstup priamo do prienčinka a do path som zadal cmd a to sa otvorí cmd s danou path a zadal som príkaz code .
	2. Potom na spustenie projectu a na pozretie ako to vyzerá v prehliadavači: v cmd napíš(samozrejme pri path ceste projektu ktorá končí nazvom projektu): python manage.py runserver 
	    - takto aplikácia je teraz spustená v porte 8000 a túto url z cmd stačí vložiť to do prehliadavača.
	    - to čo vidím je predvolená šablóna, ktorá je súčasťou každého projektu django
    3. Teraz idem vytvoriť app v django projecte:
        - Vytvára sa jedna aplikácia na implementáciu  metód api.
		- Na vytvorenie appky potrebujem zadať tento príkaz: python manage.py startapp TransportOrderApp
		- Ďalej zaregistrujem aplikáciu a požadované moduly a settings.py: v sekcie INSTALLED_APP = ....  'rest_framework',
        'corsheaders',
		
		 a ešte v sekci MIDDLEWARE = 
    				toto: 'corsheaders.middleware.CorsMiddleware',
 
		 a daľej pridám tiež inštrukciu, ktorá umožní všetkým doménam prístup k apis takto: CORS_ORIGIN_ALLOW_ALL = True

        - Vytvoriť modely potrebné pre aplikáciu, potrebujem dva modely: jeden, ktorý ukladá údaje pre oddelenie
            ďalší, ktorý ukladá údaje o zakazníkoch. Tieto modely majú svoje jednotlivé polia.
		- Nachádza sa to v TransportOrderApp vo file models.py
        - Použijem postgresql ako databázu na vytvorenie tabuliek z tých modelov.
		  Ale na spojenie connect do postgresql z django appky je potrebné nainštalovať database adapter:::: pip install psycopg2
        - Po vytvorení databázy a pri rozbalení vidím, že nemá žiadne tables.
        - Teraz pridám databázové detaily do settings.py súboru v časti DATABASES 

5. Vytvorenie tabuliek z tých spomínaných modelov:
	- Najprv do cmd napíšem command pre vytvorenie migrations file(súboru) pre alebo do modelov.
		príkazom: python manage.py makemigrations TransportOrderApp
	- Potomto môžem vidieť migračný súbor 0001_initial.py ktorý hovorí, aké zmeny v databáze sa vykonajú
		- Keď sa to spraví tak potom sa zadá príkaz, ktorý posunie tieto zmeny do databázy: python manage.py migrate TransportOrderApp
		- Takto sa nám v databaze vytvoria tabuľky.
		- Ak kliknem na Tables a hore na prvú ikonku query tool tak spustím toto: select * from public."TransportOrderApp_customers"
		- Potom možme vložiť aj nejaké údaje a to: insert into public."TransportOrderApp_departments" values(1,'Delivery','Thomas','2024-09-27'); to je pre otestovanie

6. Teraz idem vytvoriť serializers pre modely:
		- Serializátory sú v podstate alebo pomáhajú konvertovať komplexné typy alebo inštancie modelov na natívne dátové typy jazyka Python,ktoré sa potom dajú ľahko vykresliť do json alebo xml alebo iných typov obsahu. Pomáhajú aj pri deserializácii, čo nie je nič iné ako prevod minulých údajov späť na komplexné typy.
		- Vytvorím si serializers.py file do folderu TransportOrderApp
		
7. Teraz idem písať API metody:
	- Preto vo views.py file a tam import na csrf decorator, aby bolo možné povoliť iným doménam prístup k api 
      metódam. A aj potrebujem json parser na rozbor prichádzajúcich údajov do dátového modelu. 
    - Potom nastáva import na modely, ktoré som si vytvoril a tiež zodpovedajúce serializátory.


    - Teraz idem napísať  api metody pre departments table:
        GET:
		- metóda dostane voliteľné id, ktoré budem musieť použiť v metóde delete
		- v metóde get vrátim všetky záznamy vo formáte json
		- využívam triedu serializer na konverziu do formátu json. Parameter safe rovný false a to sa v podstate používa na informovanie djanga, že sa snažím konvertovať do json 

        POST:
        - Teraz metóda post, ktorá sa použije na vloženie nového záznamu do tabuľky oddelení
		- Toto sa deje v POST: analyzujem požiadavku a pomocou serializéra ju konvertujem na model
		- Toto dep...is_valid() ak model je platný tak ho uložím do databázy		
		- A vrátim uspešnú správu.

        PUT:
        - Teraz metóda put, ktorá sa použije na aktualizáciu daného záznamu
		- najprv zachytím existujúci záznam pomocou id oddelenia
		- ďalej ho mapujem novými hodnotami pomocou triedy serializer
		- a zase Toto dep...is_valid() ak model je platný tak ho uložíme do databazy		
		- A vrátim uspešnú správu.

        DELETE:
        - a na záver delete method: tam odovzdávam id, ktoré sa má vymazať z url

8. Teraz určenie url pre naše metódy api:

	- Najprv pridaj new file urls.py do folderu TransportOrderApp.
		- toto: .../[0-9]+    - metóda delete dostane id v url

    urlpatterns=[
        re_path(r'^department$',views.departmentApi),
        re_path(r'^department/([0-9]+)$',views.departmentApi),

        re_path(r'^customer$',views.customerApi),
        re_path(r'^customer/([0-9]+)$',views.customerApi)
    ]
    - teraz potrebujem zahrnúť tieto urls do main urls.py file to je vo folderi Simple_Transport...
        from django.conf.urls import re_path,include
			re_path(r'^',include('TransportOrderApp.urls'))


    - A teraz idem otestovať api metody:
			1. najprv spustenie projectu cez príkaz:::: python manage.py runserver
			2. copy adresa url z cmd túto: http://127.0.0.1:8000/
			3. najprv testujem metódu get, ktorá vráti všetky údaje z tabuľky
			4. v postman vlož url pri slove GET: http://127.0.0.1:8000/department  a stlač Send takto nám vrati údaje a funguje to.
			5. teraz idem vyskušať POST methodu na vloženie nových údajov: klik a zmeň z GET na POST potom klikni na Body a zmen na raw a skopíruj data z GET, ktoré prišli a vlož do toho pola na písanie.
				- a prepni z Text na JSON a vymaž ten riadok s id číslom a zmen hodnotu Thomas na inú hodnotu  
                - a odošli cez Send tak ak dam znova GET tak  to funguje
							lebo sa to pridalo      
            6. teraz test na put metodu a to tak, že si skopírujem data z get a upravím hodnotu ako keby aktualizácia.
                - to znamená, že funguje lebo ak si dám get tak dostanem naspäť všetky svoje data a tam je aj tá zmena 
            7. a posledne otestovanie delete methody a to tak, že z put prepni na delete a v url pridaj /a číslo, ktoré znamená id pre dané data napr.2 a daj v body none a potom send. A ak dám get tak vidim, že sa odstranilo a funguje to.

9. Teraz implementovať metódy api pre tabuľku zakaznikov:
		1. Najprv skopírujem to vo views.py file čo mám pre departments a vložím to dole pod tými už vytvorenými api metodami.
				- A tam sa budú meniť. Z department na customers
		2. Teraz v urls.py pridať url pre tieto api metody alebo pridanie na určenie url pre metódy api
			
			    re_path(r'^customer$',views.customerApi),
    			re_path(r'^customer/([0-9]+)$',views.customerApi)

		3. A teraz znova otestovať api v postman samozrejme mať zapnutý projekt v cmd a teraz v postman vložiť url túto http://127.0.0.1:8000/customer

			funguje lebo výpisalo [] lebo som tam nič nevkládal ako dáta.
		4. Teraz testovanie POST metody tu sa id nepíše lebo ide o post to už dá samo a potom Send a keď dám get tak nám už výpíše vložený údaj to znamená že to funguje. Potom put metoda otestovanie a po get methode vidím, že aj tá funguje.

        5. Otestovanie delete tu nezabudni na none nie raw a v url zadaj /a číslo id ktorý udaj chceš vymazať a po get methode vidím, že to funguje.

Všetko tu funguje.

11. Teraz Frontend(client) lebo sa  vytvorí vue.js project: 
    - Vytvorenie new folder client.
    - Príkaz:::: cd client a potom vue create django-vue-client
    - Potom nastáva úprava App.vue file.
    - A zároveň úprava main.ts pre import bootstrap.
    - Vytvorím nový súbor s názvom router.ts v priečinku client/src.
        A to na smerovača so štyrmi trasami, pričom toto napr.: component: Customer odkazuje na import daného file,ktoré medzitým vytvárame zatiaľ ako prázdne v priečinku views.
    - Naspäť do main.ts pre zahrnutie router.ts.


12. Vytvorenie Custormer.vue:
    - vytvorenie template a v ňom table
    - script lebo na zacyklenie údajov potrebujem získať údaje
    - po načítaní stránky musím zavolať dáta z api:
		- na to potrebujem axios http call a do get volám url
    - a funkciu getData() do mounted(){} funkcie: pri načítaní stránky toto montované volanie voá funkciu getData() a to volá údaje
    
    - Teraz loop na tie údaje do našej tabulky:
        - Najprv do getData() pridať toto:
             this.customers = res.data
             console.log(this.customers)
        - a teraz loop this data do html tabuľky
			preto idem naspäť do tr kde sa napíše fro loop to v-for
			spolu s edit a delete button
        - takto sa uspešne podarilo fetched the data s použitím api v tomto file
    
    - inak z toho dôvodu, že mi nedokázalo najsť: Cannot find module 'vue-property-decorator' or its corresponding type declarations.ts-plugin(2307) aj ked som to mal nainstalovaný tento package tak som pre funkčnosť a dokončenie to nepoužil.


13. Teraz idem to, že ako vložiť udaje do tabuľky(databazy) s pomocou API
    1. v router.ts je potrebné napísať toto:
        import CustomerCreate from './views/CustomersCreate.vue'
				                        {
                path: '/customer/create',
                component: CustomerCreate,
                },	- to je cesta k file CustomersCreate.vue


    2. Teraz vytvorenie formulára vo file CustomersCreate.vue.
    3. Vložíť a uložíť záznam do  db ktorá používa API.
        - pri script je potrebné získať všetky podrobnosti o vstupných poliach 
        - na manažovanie vstupných údajov je potrebné definovať model.
        - čokoľvek zadám vo svojom vstupe, tak to príde a uloží sa to do daných premenných
        - preto potrebujem pridať v hypen model do input tagov
        - takéto niečo do html:
				v-model="model.customer.CustomerName"
            - takto sú input boxy manažované a všetky detaily budu uložené do tých customer premenných
        - ak si to chcem skontrolovať tak takto: pridam Vue devtools rožšíreneie do prehliadača a potom klik na CustomerCreate componennt a po klik vidím, že customer je objekt ale nie sú tam data a tak stačí, že tam len niečo napíšem a ono sa to bude zobrazovať priamo v tom objekte

		- a takto sme uspešne naplnili všetky input detaily vo forme

14. Vytvorenie Departments.vue:
    - postupujem rovnako ako pri Customers.vue s tým, že tam je zmena pre zobrazenie určitých dát 


15. Vytvorenie save button lebo ak vyplním tak aby sa to uložilo.
    - pridanie button element v html časti.
    - a teraz funkcie v časti methods dole v scripte.
	- musím zavolať prístup, aby som mohol spravovať ukladanie údajov 
							a to je axios

16. Vymazanie záznamu z tabuľky.
    1. vo Customers.vue: pridanie button elementu s definovaním funkcie
    2. v script vytvorenie funkcie:
        - a v stránke v console po kliknutí sa zobrazí hláška s danou vetou ak dam ok v console bude číslo id záznamu ak dam nie tak nič.
    3. Teraz vykonať volanie axios, vymazať záznam z údajov api
        - to je to axios.delete(...)...

    4. a keď sa tam niečo vymaže ako údaj tak chcem akutalizovať alebo  
        refreshnuť data a na to sa použije názov funkcie, ktorá na get ktorú používam v mountedtoto: this.getData(); keď je stránka načítaná tak volám this.getData(); a ked sa vymaže keď prejde úspešné vymazanie tak voláme this.getData(); record znova

			a ak sa customerId nenájde tak 
				nastáva toto:
			.catch(function (error){})

    5. Pre otestovanie tak stačí ísť na stránku a kliknuť na delete a  vymaže daný  údaj.


17. Možnosť upravenia a aktualizácie údajov pomocou API.
    1. Preto potrebujem edit form a to cez copy CustomerCreate.vue a vložením tohto súboru do priečinka views a jeho zmenou na Edit.vue, kedže v podstate je princíp podobný s tím, že tu už údaje sú a chceme ich opraviť alebo aktualizovať a to tak že sa zobrazia cez form po kliknutí na tlačidlo edit, preto aj to copy daného .vue súboru.
	- ísť do Customers.vue vyhladať edit button a zadať toto:
		to="/customer/id/edit"
	- ako to spojiť: je tú jeden spôsob:
			:to="{path: '/customer/'+customer.CustomerId+'/edit'}"
	- na otestovanie stačí ísť do frontendu(client) a po kliknutí na edit button sa zobrazí hore presne tá url s daním id.
	- potrebujem vytvoriť route pre tú path a to v router.ts takto:
            {
            path: '/customer/:id/edit',
            component: CustomerEdit,
            },
    - v CustomersEdit.vue zmeň toto name:'customerCreate', na toto name:'customerEdit',
					- to je form name to customerEdit
		- data input fields ostanú rovnaké lebo ideme vložiť alebo edit tieto data
		- keď sa klikne na edit tlačidlo a zobrazí sa form tak musíme volať http call a to je axious
			to sa spraví pri mounted() a chcem aby dostal id, console.log(this.$route.params.id) - to id je z from route.ts a akékoľvek name tam dam tak sa volá tu v tomto .vue file
			- ak volám to id tak to znamená že má byť aktuálne a na otestovanie takto:
				priamo cez console a refresh a tam sa zobrazí id číslo
		- teraz použijem id a získam data:
				 this.getCustomerData(this.$route.params.id);
        - a skopíruj function name a vytvor ju v methods:
                 getCustomerData() - do parametru sa dá studentId 
			a vo vnútri potrebujem http volanie s axious ziskať data z API
        - ale do urls.py pridám toto: re_path(r'^customer/([0-9]+)/edit$',views.customerApi)
        - potom pre otestovanie stačí isť do frontend page a dať refresh a v console je data zaznam a po napísaní tohto console.log(res.data) dostaneme len customer data
        - potom napíš toto: priradiť všetky záznamy o zákazníkoch do tejto premennej customer:
                this.model.customer = res.data
            ale malo by to vložiť data automaticky do form ale táto funkčnosť sa nezobrazuje.
            - ak napr. teraz nenajde id take ktore mam v db tak takto:
				tak tam vlož ten catch
		- toto všetko bolo o fetch the data ale mne to nejde tak ako som hore spomínal

        2. teraz zmena tlačidla zo save na update takisto aj function updateCustomer
				a do script prebehla zmena a to na updateCustomer
				- zmen z post na put a vlož update url
                -a akekoľvek údaje dostanem tak ich ukladám do tohoto this.model.customer

        - používam customerId, takže ho musím deklarovať niekde inde a to v data function: data() zozačiatku je null
		- a potom do mounted() takto: this.customerId = this.$route.params.id 
			- customerId sa rovná hodnote, ktorú získam z parametra URL, a to sa vloží do customerId a to this.customerId použijem do update function

		- ak sa vrátim do otestovania tak už by tam mali byť údaje a pri zmene a uložení sa aj aktualizujú a vložia do tabuľky ale táto funkčnosť sa nezobrazuje.
			v tomto prípade bolo otestovanie funkcionality cez postman a to takto:
                        http://127.0.0.1:8000/customer/1/edit
                                    cez put a vložením existujúcich dát s úpravou a po tlačidle Send sa záznam úspešne editoval a aktualizoval čoho
                                    výsledkom je aj zmena na časti client, ktorá zobrazuje túto 
                                    zmenu.




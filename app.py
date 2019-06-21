from flask import Flask, render_template, request, redirect, url_for, session
import smtplib, time
import sqlite3 as sql
app = Flask(__name__)

conn = sql.connect('database.db')
conn.execute('DROP TABLE users')
conn.execute('DROP TABLE products')
conn.execute('DROP TABLE joiner')
conn.execute('CREATE TABLE users (username TEXT PRIMARY KEY, email TEXT, password TEXT)')
conn.execute('CREATE TABLE products (prodotto TEXT, descrizione TEXT, proprietario TEXT, prenotazioni INTEGER, quantita INTEGER, prezzo TEXT, img TEXT, categoria TEXT, primary key(prodotto,proprietario), foreign key(proprietario) references users(username))')
conn.execute('CREATE TABLE joiner (prodotto TEXT, joiner TEXT, primary key(prodotto,joiner), foreign key(prodotto) references products(prodotto), foreign key(joiner) references users(username)) ')
####### POPOLAMENTO INIZIALE #########    

#UTENTI
conn.execute("INSERT INTO users VALUES ('pippo42','pippo42@gmail.com','pippo42');")
conn.execute("INSERT INTO users VALUES ('sasybello','sasybello@gmail.com','sasybello');")
conn.execute("INSERT INTO users VALUES ('belgatto','belgatto@gmail.com','belgatto');")
conn.execute("INSERT INTO users VALUES ('utente1','utente1@gmail.com','utente1');")
conn.execute("INSERT INTO users VALUES ('utente2','utente2@gmail.com','utente2');")
conn.execute("INSERT INTO users VALUES ('utente3','utente3@gmail.com','utente3');")
conn.execute("INSERT INTO users VALUES ('utente4','utente4@gmail.com','utente4');")
conn.execute("INSERT INTO users VALUES ('utente5','utente5@gmail.com','utente5');")
conn.execute("INSERT INTO users VALUES ('utente6','utente6@gmail.com','utente6');")

#PRODOTTI
conn.execute("INSERT INTO products VALUES ('IphoneXS 64GB','Originale iphone nella versione 64GB di memoria','sasybello',4,20,'700 euro','https://www.manor.ch/productimages/P2-27044401_01_556939_jpg_zoom1000.jpg','tecnologia');")
conn.execute("INSERT INTO products VALUES ('Surface Pro 6','La versione 6 del super laptop di microsoft, in versione 128 Gb di memoria','utente1',4,5,'1500 euro','https://www.bhphotovideo.com/images/images1000x1000/microsoft_ljm_00029_surface_pro_6_i5_1467981.jpg','tecnologia');")
conn.execute("INSERT INTO products VALUES ('IphoneXS Max 64GB','Originale iphone nella versione 64GB di memoria','sasybello',0,30,'900 euro','https://www.manor.ch/productimages/P2-27044401_01_556939_jpg_zoom1000.jpg','tecnologia');")
conn.execute("INSERT INTO products VALUES ('Samsung Galaxy S10 64GB','Originale Samsung Galaxy s10 Plus nella versione 64GB di memoria','sasybello',0,30,'700 euro','https://www.wondamobile.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/s/u/sumsung10__1.jpg','tecnologia');")
conn.execute("INSERT INTO products VALUES ('Kant Divano 4 posti','Divano originale Kant 4 posti in velluto color senape','utente4',0,30,'700 euro','https://medias.maisonsdumonde.com/image/upload/q_auto,f_auto/w_1000/img/divano-4-posti-in-velluto-color-senape-1000-1-39-166499_2.jpg','casa');")
conn.execute("INSERT INTO products VALUES ('CZZ Scrivania Pieghevole','Scrivania Pieghevole Computer a Staffa a Forma di U - Semplice Economica per Casa','utente3',4,50,'20 euro','https://images-na.ssl-images-amazon.com/images/I/5175RPLcwrL._SL1000_.jpg','casa');")
conn.execute("INSERT INTO products VALUES ('Adidas Felpa Originals','Felpa con cappuccio trifoglio iconica con un logo trefoil davanti e al centro','utente3',2,30,'24 euro','https://images.eprice.it/nobrand/0/hres/713/207364713/137037260.jpg','abbigliamento');")
conn.execute("INSERT INTO products VALUES ('Scarpe Adidas VC 1000 Nere','Scarpe Adidas Sneaker Uomo nere, eleganti, sportive e comode','pippo42',0,30,'30 euro','https://images-na.ssl-images-amazon.com/images/I/51VFj0LwnxL._UL1000_.jpg','abbigliamento');")
conn.execute("INSERT INTO products VALUES ('Nike Air Zoom nere','Scarpe Nike air zoom Uomo nere, eleganti, sportive e comode','pippo42',0,40,'30 euro','https://www.sportway.it/shop/wp-content/uploads/2018/10/AH7857-001-PHCFH001-1000.jpeg','abbigliamento');")
conn.execute("INSERT INTO products VALUES ('Panca Piana','Panca piana di dimensioni ridotte per un petto pronunciato','pippo42',2,25,'200 euro','https://i2.wp.com/www.spartacosport.it/wp-content/uploads/2016/05/panca-piana-ipf.jpg?fit=1000%2C1000&ssl=1','fitness');")
conn.execute("INSERT INTO products VALUES ('Fiat Panda','La leggenda italiana su quattro ruote a buon prezzo','utente3',3,25,'750 euro','https://www.vehicletrackingtech.co.uk/media/catalog/product/cache/2/image/1200x/040ec09b1e35df139433887a97daa66f/t/e/temp_1_11.jpg','auto');")
conn.execute("INSERT INTO products VALUES ('Pegeout 208','La berlina francese amata da tutti, in versione grigio','utente1',3,25,'5750 euro','http://www.canm8.com/media/catalog/product/cache/4/image/1000x1000/9df78eab33525d08d6e5fb8d27136e95/p/e/peugeot_208_1.png','auto');")
conn.execute("INSERT INTO products VALUES ('Fiat Punto','Fiat Punto Evo bianca, diesel, km zero, full optional','utente5',3,25,'7550 euro','https://www.simoniracing.com/ProductsResources/1555/GPUNTO-INT_0_ori.jpeg','auto');")
conn.execute("INSERT INTO products VALUES ('Freeweight Leg Extension','Leg Extension multifunzione, adatta a qualsiasi utilizzo, comoda e motivante!','utente3',0,25,'550 euro','http://www.powerfit.shop/WebRoot/ce_it/Shops/990807526/59CB/DA68/3551/8AA8/AEDC/C0A8/1911/A133/leg_extension1_ml.jpg','fitness');")
conn.execute("INSERT INTO products VALUES ('Multipower','Attrezzo multiuso ideale per per eseguire innumerevoli esercizi assistiti.','utente2',0,25,'450 euro','http://img.medicalexpo.it/images_me/photo-g/70274-10271946.jpg','fitness');")
conn.execute("INSERT INTO products VALUES ('Dell Notebook XPS 13 9370','Notebook XPS 13 9370 con Processore di ultima generazione!.','utente2',0,25,'999 euro','https://images.eprice.it/nobrand/0/hres/163/205160163/6E4CF8EE-9675-4848-9C10-AB0A8671518F.jpg','tecnologia');")

#JOINERS
conn.execute("INSERT INTO joiner VALUES ('Surface Pro 6','sasybello');")
conn.execute("INSERT INTO joiner VALUES ('Surface Pro 6','belgatto');")
conn.execute("INSERT INTO joiner VALUES ('Surface Pro 6','utente3');")
conn.execute("INSERT INTO joiner VALUES ('Surface Pro 6','utente4');")
conn.execute("INSERT INTO joiner VALUES ('CZZ Scrivania Pieghevole','utente4');")
conn.execute("INSERT INTO joiner VALUES ('CZZ Scrivania Pieghevole','utente1');")
conn.execute("INSERT INTO joiner VALUES ('CZZ Scrivania Pieghevole','utente3');")
conn.execute("INSERT INTO joiner VALUES ('CZZ Scrivania Pieghevole','sasybello');")
conn.execute("INSERT INTO joiner VALUES ('IphoneXS 64GB','belgatto');")
conn.execute("INSERT INTO joiner VALUES ('IphoneXS 64GB','utente3');")
conn.execute("INSERT INTO joiner VALUES ('IphoneXS 64GB','utente4');")
conn.execute("INSERT INTO joiner VALUES ('IphoneXS 64GB','utente1');")
conn.execute("INSERT INTO joiner VALUES ('Adidas Felpa Originals','belgatto');")
conn.execute("INSERT INTO joiner VALUES ('Adidas Felpa Originals','utente3');")
conn.execute("INSERT INTO joiner VALUES ('Panca Piana','utente3');")
conn.execute("INSERT INTO joiner VALUES ('Panca Piana','utente1');")
conn.execute("INSERT INTO joiner VALUES ('Fiat Panda','pippo42');")
conn.execute("INSERT INTO joiner VALUES ('Fiat Panda','utente1');")
conn.execute("INSERT INTO joiner VALUES ('Fiat Panda','utente2');")
conn.execute("INSERT INTO joiner VALUES ('Pegeout 208','utente4');")
conn.execute("INSERT INTO joiner VALUES ('Pegeout 208','utente6');")
conn.execute("INSERT INTO joiner VALUES ('Pegeout 208','utente5');")
conn.execute("INSERT INTO joiner VALUES ('Fiat Punto','belgatto');")
conn.execute("INSERT INTO joiner VALUES ('Fiat Punto','utente3');")
conn.execute("INSERT INTO joiner VALUES ('Fiat Punto','utente2');")





conn.commit() 
conn.close()
app.secret_key='chiavesegretaIHVIHVIbshwvihsiwbs'

@app.route('/')
def init():
    if session.get('username') == None:
        return redirect(url_for('index'))
    return redirect(url_for('home'))

####### Go to page login ######
@app.route('/login')
def index():
    return render_template('Login.html')

####### Sign up #######
@app.route('/signup')
def signup():
    return render_template('signup.html')

####### Logout ########
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('init'))    

####### Esegui Registrazione #######
@app.route('/signupexec', methods = ['POST', 'GET'])
def signupexec():
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']

            with sql.connect("database.db") as con:
                cur = con.cursor()
            
                cur.execute("INSERT INTO users (username,email,password) VALUES (?,?,?)",(username,email,password) )
                con.commit()
                session['username'] = username
                session['email'] = email
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
            return redirect(url_for('init'))
        finally:
            return redirect(url_for('init'))
            con.close()

############ Esegui Login #############
@app.route('/loginexec', methods = ['POST', 'GET'])
def loginexec():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        con = sql.connect("database.db")
        cursor = con.cursor()
        cursor.execute("select * from users where username = (?)",[username])
        for row in cursor:
            if row[0] == username and row[2] == password:
                session['username'] = row[0]
                session['email'] = row[1]
                con.close()
                return redirect(url_for('home'))
            return redirect(url_for('init'))
    return redirect(url_for('init'))
        

############ Elenco Iscritti #############
@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from users")
   
   rows = cur.fetchall()
   return render_template("list.html",rows = rows)

########### Mostra Home ###########
@app.route('/home')
def home():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from products")

    rows = cur.fetchall()
    return render_template("home.html", username = session['username'], rows = rows)

########### Users Pages ##########
@app.route('/users/<user>',methods = ['GET'])
def users(user):
    if user == session.get('username'):
        return redirect(url_for('myaccount'))
    con = sql.connect("database.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from products where proprietario = (?)",[user])
    rows = cur.fetchall() #prodotti che sto vendendo

    cur2 = con.cursor()
    cur2.execute("select * from products natural join joiner where joiner = (?)",[user])
    rowsjoin = cur2.fetchall() #prodotti per cui ho fatto join


    return render_template("users.html", username = user, rows = rows, rowsjoin = rowsjoin)


##### MY ACCOUNT ############# 
@app.route('/myaccount')
def myaccount():
    username = session.get('username')
    con = sql.connect("database.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from products where proprietario = (?)",[username])
    rows = cur.fetchall() # Oggetti di cui sono il proprietario (che sto vendendo)

    cur2 = con.cursor()
    cur2.execute("select * from products natural join joiner where joiner = (?)",[username])
    rowsjoin = cur2.fetchall() #prodotti per cui ho fatto join 

    return render_template("myaccount.html", username = username, rows = rows, rowsjoin = rowsjoin)

####### CATEGORIE ##########
@app.route('/categoria/<cat>')
def categoria(cat):
    categoria = cat
    con = sql.connect("database.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from products where categoria = (?)",[cat])
    rows = cur.fetchall()

    return render_template("home.html",username = session['username'], rows = rows)

####### Join di un prodotto #############
@app.route('/join/<prod>')
def join(prod):
    username = session.get('username')
    prodotto = prod
    numero = 0
    proprietario = 0
    limite = 0

    con = sql.connect("database.db")
    cursor = con.cursor()
    cursor.execute("select * from products natural join joiner where prodotto = ?",(prodotto,))

    for row in cursor:
        # Cerco prodotto
        if row[0] == prodotto:
            # se gia ho joinato
            if row[8] == username:
                return "<h1>Hai gia joinato</h1>"
                return redirect(url_for('home'))
            # altrimenti prendi nome articolo e numero per incrementarlo    
            nome = row[0]
            proprietario = row[2]
            numero = row[3]
            limite = row[4]
    #inserisci nella tabella join
    con.execute("INSERT INTO joiner VALUES (?,?)",(prodotto,username,))
    numero = numero + 1
    # aumenta il contatore dei prenotati
    con.execute("UPDATE products set prenotazioni = (?) where prodotto = (?)",(numero,prodotto,))
    con.commit()
    con.close()


    #se contatore pieno manda email
    def mandamail(prodotto):
        con = sql.connect("database.db")
        cursor = con.cursor()
        cursor.execute("select * from joiner join users on joiner = username where prodotto = ?",(prodotto,))
        for row in cursor:
            destinatario = row[3]
            soggetto = "Subject: Vendita Prodotto Partita\n\n"
            contenuto = "Vendita del prodotto: " + prodotto + " partita, numero di joiners raggiunto! Congratulazioni!"
            messaggio = soggetto + contenuto
            email = smtplib.SMTP("smtp.gmail.com",587)
            email.starttls()
            email.login("jointheoffer@gmail.com","ProgettoTecWeb6")
            email.sendmail("jointheoffer@gmail.com",destinatario,messaggio)
    # Se numero raggiunge limite manda le mail
    if numero == limite:
        nome = mandamail(prodotto)
    return redirect(url_for('home'))

############ Rimuovi Join Prodotto ##################  NON FUNZIONANTE
@app.route('/remove/<prod>')
def remove(prod):
    username = session.get('username')
    prodotto = prod
    numero:int = 0

    con = sql.connect("database.db")
    cursor = con.cursor()
    cursor.execute("select * from products natural join joiner where prodotto = ?",(prodotto,))
    for row in cursor:
        # Cerco prodotto
        if row[0] == prodotto:
            # se gia ho joinato
            if row[8] == username:
                numero = row[3]
                con.execute("DELETE FROM joiner where joiner = ? and prodotto = ?",(username,prodotto))
                numero = numero - 1
                con.execute("UPDATE products set prenotazioni = (?) where prodotto = (?)",(numero,prodotto))
                con.commit()
                return redirect(url_for('home'))
    return redirect(url_for('home'))

########### listajoin #############
@app.route('/listajoin')
def listajoin():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from joiner")
   
   rows = cur.fetchall()
   return render_template("list.html",rows = rows)

########### Inserisci vendita #########
@app.route('/inserisci',methods = ['POST','GET'])
def inserisci():
    if request.method == 'POST':
        nome = request.form['nome']
        desc = request.form['descrizione']
        cate = request.form['categoria']
        quan = request.form['quantita']
        prez = request.form['prezzo']
        imag = request.form['img']
        user = session.get('username')
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("INSERT INTO products VALUES(?,?,?,?,?,?,?,?)",(nome,desc,user,0,quan,prez,imag,cate))
    con.commit()
    return redirect(url_for('home'))

######### Cerca ###########
@app.route('/ricerca',methods = ['POST','GET'])
def ricerca():
    parola = request.form['testo']
    stringa = "%" + parola + "%"
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from products where prodotto LIKE ? OR descrizione LIKE ?",(stringa,stringa,))

    rows = cur.fetchall()
    return render_template("home.html", username = session['username'], rows = rows)


########## Rimuovi Item ########
@app.route('/removeitem/<prodotto>')
def removeitem(prodotto):
    prod = prodotto
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()

    cur.execute("DELETE from products where prodotto = ?",(prod,))
    cur.execute("DELETE from joiner where prodotto = ?",(prod,))

    con.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug = True)

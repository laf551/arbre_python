
import requests, json
from tkinter import *
from  tkinter import ttk
import webbrowser
import folium
import pandas 
from bokeh.io import show
from bokeh.plotting import gmap
from bokeh.models import GMapOptions
 
latitude = (
        48.84622398855583,
        48.86795447258032,
        48.838298382880026 , 
        48.85062741001953,
        48.83105777775475,
        48.875118361545255,
        48.875118361545255,
        48.88325411495259, 
        48.83929680810438
) 
longitude = (2.255833638246479
		, 2.273538262995422
		, 2.360409677131808
		, 2.260194763051017
		, 2.301569697016761
		, 2.352241383581353
		, 2.367697186062777
		, 2.392029077680569
		, 2.285994733736869
		)


coordonner= []
localisation= {
    'PARIS 20E ARRDT': [48.8625565,2.3791177],
    'PARIS 19E ARRDT':[48.8871247,2.3702572],
    'PARIS 18E ARRDT': [48.8919626,2.331184],
    'PARIS 17E ARRDT': [48.8874353,2.2875386],
    'PARIS 16E ARRDT': [48.8572065,2.2279586] , 
    'PARIS 15E ARRDT': [48.8417055,2.2586112],
    'PARIS 14E ARRDT': [48.829721,2.3054438],
    'PARIS 13E ARRDT': [48.8302919,2.3480624] ,
    'PARIS 12E ARRDT': [48.8351159,2.3821336] ,
    'PARIS 11E ARRDT': [48.8601,2.36405] ,
    'PARIS 10E ARRDT':[48.8759882,2.3448933] ,
    'PARIS 9E ARRDT':[48.877097,2.3291154] ,
    'PARIS 8E ARRDT':[48.8732641,2.2935887] ,
    'PARIS 7E ARRDT': [48.8548603,2.2939732],
    'PARIS 6E ARRDT':[48.8495301,2.3131637] ,
    'PARIS 5E ARRDT': [48.8454734,2.3338198], 
    'PARIS 4E ARRDT': [48.8541126,2.3393264],
    'PARIS 3E ARRDT': [48.8625682,2.3505515],
    'PARIS 2E ARRDT': [ 48.8677006,2.3323497], 
    'PARIS 1ER ARRDT':[48.8620317,2.3183917],
    'CENTRE DE PARIS' : [48.8589465,2.2768229], 
    'HAUTS-DE-SEINE':[48.828508,2.2188068]
     
}
api_key = "AIzaSyAgeWLaNWCpA42a7LBytovrZbHVLPZNYz8"
for i in latitude: 
    for j in longitude : 
        coordonner.append((i,j)) 
        

print("les coordonner",coordonner)
'''
for i in coordonner : 
    localisation [i] = val

'''
new_df = pandas.read_csv("new_arbres.csv" , sep = "," , header= 0)

#ressort la latitude sous forme de liste
def getLatitude (arr, hau, lib) : 

    latitude_df = new_df[(new_df['ARRONDISSEMENT']==arr) & (new_df['HAUTEUR (m)']==hau) & (new_df['LIBELLE FRANCAIS']==lib)]["LATITUDE"]
    #latitude_df = new_df[(new_df['ARRONDISSEMENT']==arr) & (new_df['HAUTEUR (m)']==hau) & (new_df['LIBELLE FRANCAIS']==lib)]["LATITUDE"]
    #print(latitude_df.tolist())
    print("LATITUDE:",latitude_df.to_list())
    return latitude_df

#ressort la longitude sous forme de liste
def getLongitude (arr , hau, lib): 
    longitude_df = new_df[(new_df['ARRONDISSEMENT']==arr) & (new_df['HAUTEUR (m)']==hau) & (new_df['LIBELLE FRANCAIS']==lib)]["LONGITUDE"]
    print("LONGITUDE: ",longitude_df.to_list())
    return longitude_df

data = ["TOUS", "TOUS", "Quantite"]
def question1():
    if data[0]== "TOUS" and data[1]== "TOUS" and data[2]== "Quantite":
        reponse =[] 
        #Nbre d'arbre dans l'arrondissement qui en compte le plus
        #plus_arbres = new_df["ARRONDISSEMENT"].value_counts().max()
        #moins_arbres = new_df["ARRONDISSEMENT"].value_counts().min()
        nom_arrond_max = new_df["ARRONDISSEMENT"].value_counts().idxmax(axis=0)
        nom_arrond_min = new_df["ARRONDISSEMENT"].value_counts().idxmin(axis=0)
        if nom_arrond_max in localisation: 
        
            reponse.append(localisation[nom_arrond_max])
        

        if nom_arrond_min in localisation: 
            reponse.append(localisation[nom_arrond_min])
        
        strg = ""
        tmp = ""
        print("response ::::******",reponse)
        for i in reponse: 
            
            strg=tmp+str(i[0])+","+str(i[1])+"%7C"
            tmp = strg
        
        map(strg)
    else:
        print("autre Question")

    #print("******",strg)

def question2(): 
    # Arbre le plus haut par arrondissement
    if data[0]== "TOUS" and data[1]== "TOUS" and data[2]== "Quantite":
        reponse =[] 
        #liste_arrond = new_df.groupby(['ARRONDISSEMENT'], sort=True)['HAUTEUR (m)'].max()
        #print(liste_arrond)

        #hauteur arrondissement max 
        hautNom_arrMax = new_df.groupby(['ARRONDISSEMENT'])['HAUTEUR (m)'].mean().sort_values(ascending=False).idxmax(axis=0)

        #hauteur nombre max 
        hautNbr_Max = new_df.groupby(['ARRONDISSEMENT'])['HAUTEUR (m)'].mean().sort_values(ascending=False).max()

        #hauteur arrondissement max 
        hautNom_arrMin = new_df.groupby(['ARRONDISSEMENT'])['HAUTEUR (m)'].mean().sort_values(ascending=False).idxmin(axis=0)
        
        #hauteur nombre max 
        hautNbr_Min = new_df.groupby(['ARRONDISSEMENT'])['HAUTEUR (m)'].mean().sort_values(ascending=False).min()

        if hautNom_arrMax in localisation: 
        
            reponse.append(localisation[hautNom_arrMax])
        
        
        print(hautNom_arrMin)
        if hautNom_arrMin in localisation: 
            reponse.append(localisation[hautNom_arrMin])
        
        #print("l'arrondissement avec la moyenne d'arbre les plus hauts est", hautNom_arrMax, "démontrant une moyenne de", hautNbr_Max, "mètre.\ncelui avec la moyenne la moins haute est", hautNom_arrMin, "avec un total de", hautNbr_Min, "mètre.")
        
        strg = ""
        tmp = ""
        for i in reponse: 
            strg=tmp+str(i[0])+","+str(i[1])+"%7C"
            tmp = strg
        
        map(strg)
    else:
        print("autre Question")

def question3(): 
    print("wwww")
    #m = folium.Map(location=[45.5236, -122.6750])
    macarte = folium.Map(location=[50.7517,5.9106], zoom_start=13)
    macarte.create_map(path='macarte.html')

def question4(): 
    pass
def question5(): 
    pass
def one_one_qte():
    if data[0]== 1 and data[1]== 1 and data[2]== "Quantite":
        pass 
    else: 
    
        print("autre Question")

def one_one_hauteur(): 
    if data[0]== 1 and data[1] != "TOUS" and data[2]== "Hauteur":
        pass 
    else: 
    
        print("autre Question") 
def one_one_type(): 
    if data[0]== 1 and data[1] != "TOUS" and data[2]== "Type":
        pass 
    else: 
        print("autre Question") 

def one_all_qte(): 
    if data[0]== 1 and data[1]== "TOUS" and data[2]== "Quantite":
        pass 
    else: 
        print("autre Question") 
def one_all_hauteur(): 
    if data[0]== 1 and data[1]== "TOUS" and data[2]== "Hauteur":
        pass 
    else: 
        print("autre Question") 
def one_all_type(): 
    if data[0]== 1 and data[1]== "TOUS" and data[2]== "Type":
        pass 
    else: 
    
        print("autre Question") 
def all_one_qte(): 
    if data[0] != "TOUS" and data[1] != "TOUS" and data[2]== "Quantite":
        pass 
    else: 
    
        print("autre Question")  
def all_one_hauteur(): 
    if data[0]== "TOUS" and data[1] != "TOUS" and data[2]== "Hauteur":
        pass 
    else: 
    
        print("autre Question")  
def all_one_type(): 
    if data[0]== "TOUS" and data[1] != "TOUS" and data[2]== "Type":
        pass 
    else: 
    
        print("autre Question")  
def all_all_qte(): 
    if data[0]== "ALL" and data[1]== "ALL" and data[2]== "Quantite":
        pass 
    else: 
    
        print("autre Question")  
def all_all_hauteur(): 
    if data[0]== "TOUS" and data[1]== "TOUS" and data[2]== "Hauteur":
        pass 
    else: 
        print("autre Question")  
def all_all_type(): 
    if data[0]== "TOUS" and data[1]== "TOUS" and data[2]== "Type":
        pass 
    else: 
        print("autre Question")  

def map(strg):
    '''global latitude, longitude  '''
    
  
    '''strg = ""
    tmp = ""
    for i in range(len(latitude)): 
        strg= str(latitude[i])+","+str(longitude[i])+"%7C"+tmp
        tmp = strg
    '''
    print("GSTRs:::",strg)
    urls="https://maps.googleapis.com/maps/api/staticmap?center=Paris,&size=900x900&markers=color:red%7Clabel:P%7C"+strg+"&maptype=roadmap&style=feature:poi%7Cvisibility:off&style=feature:road.local%7Celement:labels%7Cvisibility:off&style=feature:road.highway%7Celement:labels%7Cvisibility:off&key="+api_key
    
    r=requests.get(urls)
    print(urls)
    webbrowser.open(urls)#permet d'acceder à un lien web directement, dans ce cas dès qu'on appuit sur le bouton
    



lat=getLatitude('PARIS 15E ARRDT', 10,'Cerisier à fleurs')
long=getLongitude('PARIS 15E ARRDT', 10,'Cerisier à fleurs')

#print("******",lat) ; print("######",long)
fenetre = Tk()

frame_principale = Frame(fenetre, background="blue")
#boutonU=Button(frame_principale,text="url", command=map).pack()
frame_principale.pack()
q1 = Button(frame_principale,text="Question1",command=lambda: question1()).pack()
q2 = Button(frame_principale,text="Question2",command=lambda: question2()).pack()
q3 = Button(frame_principale,text="Question3",command=lambda: question3()).pack()

#Label(fenetre, img = )

fenetre.title("Arbre de Paris")
fenetre.geometry("800x600") 
fenetre.minsize(480,360)

fenetre.mainloop()


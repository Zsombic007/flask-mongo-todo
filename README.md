MondoDB és Flask használata egy kis HTML UI al

Egyszerű todo lista

Funckiók: 
- Új elem felvétele
- Elem kipipélés
- Elem törlése

Az adatatokat egy ingyenes MONGODB Clusterben tároltam el.

Használt programok:
- PYTHON
- HTML/CSS
- FLASK
- MONGODB



Futtatás:

1. Klónozd a repót, hozz létre virtuális környezetet, telepítsd a függőségeket:
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\Activate.ps1
   pip install -r requirements.txt
2. Hozz létre egy .env fájlt a saját MongoDB kapcsolati stringeddel:
   MONGO_URI=mongodb+srv://<user>:<pass>@<cluster>.mongodb.net/tododb
3. Indítsd el:
   python app.py
4. Nyisd meg: http://127.0.0.1:5000


FONTOS KIEMELNI HOGY AZ AI STEP BY STEP GUIDEJÁVAL KÉSZÜLT EL A PROGRAM ALAPJA!
Későbbi kisebb updateknél szeretném hanyagolni az AI használatát. De majd beszámolok mindig róluk hogy mennyire kellett használnom.
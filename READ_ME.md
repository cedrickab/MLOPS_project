Pour le moment il est obligatoire de mettre les changements de path absolu dans les fichiers suivants : 

- fichier backend.data.model.ML.py
ligne 29, variable dataframe df (préciser où se trouve Anime_data.csv )

- fichier frontend.app.py 
ligne 7, variable str path_call (préciser où se trouve les callbacks)

- fichier frontend.front_app.py
ligne 8, var my_path_opt (préciser où se trouve treat_to_options.py)
ligne 15, var dataframe df (préciser où se trouve Anime_data.csv )

non obligatoire si model.pkl est naturellement généré dans le bon répertoire
-fichier predict.py
ligne 33, var rf (préciser où se trouve le modl.pkl)

POUR RUN LE PROJET DASH : il suffit de lancer le file app.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from app.getMeta import *
from app.obtenerMetadata import *
import joblib

def analisis_modelo(url):
    resultado = analizar_data(url)
    print(resultado)
    if len(resultado) == 2:
        return resultado
    df= pd.read_csv("app/metadataset.csv")
    data = df.dropna()
    X = data.drop(labels=['result'],axis=1)
    y = data['result'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=0)
    #model = RandomForestClassifier(n_estimators = 29,
    #                                  random_state = 2016,
    #                                  min_samples_leaf = 1,)
    #model.fit(X_train, y_train)
    #joblib.dump(model, 'modelo_entrenadoRF.pkl')
    model = joblib.load("app/modelo_entrenadoRF.pkl")

    try:
        prediction = model.predict(resultado)
        respuesta = {}
        respuesta['id'] = prediction.item()
        respuesta["metodo"] = 'metadata'
        # Imprimir el resultado de la predicción
        if respuesta['id'] == 1:
            respuesta['mensaje'] = "Alta probabilidad de phishing"
        else:
            respuesta['mensaje'] = "Baja probabilidad de phishing"
        return respuesta
    except requests.exceptions.RequestException as e:
        respuesta['id'] = 506
        respuesta['mensaje'] = "Excepción en algoritmo: ",e
        print("Excepción en algoritmo")
        return respuesta

#accuracy = model.score(X_test, y_test)
    #print("Precisión del análisis :", accuracy*100,"%")

    # Preprocesar el enlace ingresado por el usuario
    #url_transformed = vectorizer.transform([url])

    # Realizar la predicción
    #print(type(url_transformed))

#feature_list = list(X.columns)
        #feature_imp = pd.Series(model.feature_importances_,index=feature_list).sort_values(ascending=False)
        #print(feature_imp)

#X = vectorizer.fit_transform(data['URL'])
#vectorizer = CountVectorizer()
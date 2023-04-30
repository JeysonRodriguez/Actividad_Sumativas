app = Flask(_name_)


df = pd.read_excel('api.xls')

datos = df.to_dict(orient='records')

@app.route('/datos', methods=['GET'])
def get_datos():
    pais = 'Panama'
    indicador = 'Indicator'


    datos_filtrados = [dato for dato in datos if dato['Country Name'] == pais and dato['Indicator'] == indicador]


    return jsonify(datos_filtrados)

if _name_ == '_main_':
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de conexión a MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/libreria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class editoriales(db.Model):

    pub_id = db.Column(db.String(100), primary_key=True)
    pub_name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)

class titulos(db.Model):

    title_id = db.Column(db.String(100), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    pub_id = db.Column(db.Integer, db.ForeignKey('editoriales.pub_id'), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    anticipo = db.Column(db.String(100), nullable=False)
    renta = db.Column(db.String(100), nullable=False)
    vendidos = db.Column(db.String(100), nullable=False)
    observaciones = db.Column(db.String(100), nullable=False)
    fecha_alta = db.Column(db.String(100), nullable=False)

class ventas(db.Model):

    stor_id = db.Column(db.Integer, primary_key=True)
    ord_num = db.Column(db.String(100), nullable=False)
    ord_date = db.Column(db.String(100), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    payterms = db.Column(db.String(100), nullable=False)
    title_id = db.Column(db.String(100), db.ForeignKey('titulos.title_id'), nullable=False)


with app.app_context():
    db.create_all()

# La modificación que hice en el codigo fue en la forma de introducir el parametro en la URL y a su vez incluirlo en la función y variable. Cree la consulta por fecha para poder verificar la consulta a fechas modeladas como strings.
#No es obligatorio colocar <tipo_dato: parametro> en la URL, pero es una buena práctica para que Flask sepa qué tipo de dato esperar. En caso de no colocarlo, Flask asumirá que el parámetro es una cadena de texto (string) por defecto.

@app.route('/ventas/<int:stor_id>', methods=['GET'])
def ventas_por_id(stor_id):
    venta = ventas.query.filter_by(stor_id=stor_id).all()
    return jsonify([
        {
            'id': v.stor_id,
            'numero de orden': v.ord_num,
            'fecha de la orden': v.ord_date,
            'cantidad': v.qty,
            'payterms': v.payterms,
            'id del titulo': v.title_id
        } for v in venta
    ]), 200

@app.route('/ventas/años/<string:fecha>', methods=['GET'])
def ventas_por_fecha(fecha):
    ventas_filtradas = ventas.query.filter(ventas.ord_date.ilike(f"{fecha}%")).all()
    return jsonify([
        {
            'id': v.stor_id,
            'numero de orden': v.ord_num,
            'fecha de la orden': v.ord_date,
            'cantidad': v.qty,
            'payterms': v.payterms,
            'id del titulo': v.title_id
        } for v in ventas_filtradas
    ]), 200

@app.route('/titulos/tipo/<string:tipo>', methods=['GET'])
def titulos_por_tipo(tipo):
    titulo = titulos.query.filter_by(type=tipo).all()
    return jsonify([
        {
            'id': t.title_id,
            'titulo': t.title,
            'tipo': t.type,
            'id de la editorial': t.pub_id,
            'precio': t.price,
            'anticipo': t.anticipo,
            'renta': t.renta,
            'vendidos': t.vendidos,
            'observaciones': t.observaciones,
            'fecha de alta': t.fecha_alta
        } for t in titulo
    ]), 200


@app.route('/editoriales', methods=['POST'])
def editoriales_negocio():
    data = request.json
    nueva_editorial = editoriales(
        pub_id=data.get('pub_id'),
        pub_name=data.get('pub_name'),
        city=data.get('city'),
        state=data.get('state'),
        country=data.get('country')
    )
    db.session.add(nueva_editorial)
    db.session.commit()
    return jsonify({'mensaje': 'editorial cargada correctamente'}), 201

@app.route('/editoriales/pais/<string:pais>', methods=['GET'])
def editoriales_por_pais(pais):
    editorial = editoriales.query.filter_by(country=pais).all()
    return jsonify([
        {
            'id': e.pub_id,
            'nombre': e.pub_name,
            'ciudad': e.city,
            'estado': e.state,
            'pais': e.country
        } for e in editorial
    ]), 200

if __name__ == '__main__':
    app.run(debug=True)

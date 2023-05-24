from flask import Flask, render_template, request

app = Flask(__name__)

class Pharmacy:
    def __init__(self):
        self.medicines = []

    def add_medicine(self, medicine):
        self.medicines.append(medicine)

    def search_medicine(self, name):
        for medicine in self.medicines:
            if medicine.name == name:
                return medicine
        return None

    def buy_medicine(self, name):
        medicine = self.search_medicine(name)
        if medicine is None:
            return None
        else:
            return medicine

class Medicine:
    def __init__(self, name, price):
        self.name = name
        self.price = price

pharmacy = Pharmacy()

# Додати ліки в аптеку
pharmacy.add_medicine(Medicine("Аспірин", 10))
pharmacy.add_medicine(Medicine("Парацетамол", 15))
pharmacy.add_medicine(Medicine("Нурофен", 20))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    medicine_name = request.form['medicine_name']
    medicine = pharmacy.search_medicine(medicine_name)
    if medicine:
        return render_template('search.html', medicine=medicine)
    else:
        return render_template('search.html', medicine=None)

@app.route('/buy', methods=['POST'])
def buy():
    medicine_name = request.form['medicine_name']
    medicine = pharmacy.buy_medicine(medicine_name)
    if medicine:
        return render_template('buy.html', medicine=medicine)
    else:
        return render_template('buy.html', medicine=None)

if __name__ == '__main__':
    app.run()

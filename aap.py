
from flask import Flask, flash, redirect, render_template,request,session, url_for
from model import Model

app = Flask(__name__) 
app.secret_key = "1234567890"
db = Model()

@app.route('/detail/<int:id>')
def detail(id):
    data = db.readById(id)
    session['detail'] = id
    return render_template('detail.html', data=data)

    # Read data
@app.route('/')
def index():
    data=db.read()
    return render_template('index.html', data=data)

@app.route('/formsiswa')
def tambah():
    return render_template('tambah.html')

    # Tambah data
@app.route('/tambahdata', methods=['POST','GET'])
def tambahdata():
    if request.method=='POST' and request.form['submit']:
        student_id = request.form['student_id']
        student_name = request.form['student_name']
        student_class = request.form['student_class']
        student_gender = request.form['student_gender']
        favorite_course = request.form['favorite_course']
        reason = request.form['reason']

        if db.create(student_id, student_name, student_class, student_gender, favorite_course, reason):
            flash('Data Berhasil Ditambahkan!')

        else:
            flash('Data Tidak Berhasil Ditambahkan!') 
    
        return redirect(url_for('index'))
    
    else:
        return redirect('index')

    # Update data
@app.route('/update/<int:id>')
def update(id,):
    data = db.readById(id)
    session['update'] = id
    return render_template('update.html', data=data)

@app.route('/updatedata', methods = ['GET', 'POST'])
def updatedata():
    if request.method == 'POST' and request.form['update']:
        student_id = request.form['student_id']
        student_name = request.form['student_name']
        student_class = request.form['student_class']
        student_gender = request.form['student_gender']
        favorite_course = request.form['favorite_course']
        reason = request.form['reason']

        if db.update(student_id, student_name, student_class, student_gender, favorite_course, reason, session['update']):
            flash('Data Berhasil Diperbarui!')
        else:
            flash('Data Tidak Berhasil Diperbarui!')
        return redirect (url_for('index'))

    # Hapus Data
@app.route('/hapus/<int:id>', methods = ['GET', 'POST'])
def hapus(id):
    if request.method == 'GET':
        if db.delete(id):
            flash('Data Berhasil Dihapus!')
        else:
            flash('Data Tidak Berhasil Dihapus!')
        return redirect (url_for('index'))
     
if __name__=='__main__':
    app.run(debug=True)
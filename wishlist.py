from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)
items = []

def list_append(item):
    global items
    items.append(item)
    
def list_delete(item):
    global wishlist
    wishlist.remove(item)
    
@app.route("/", method = ['GET','POST'])
def wishlist():
    if request.method == 'POST':
        item_added = request.form['wishlist_item']
        if item_added != '':
            list_append(item_added)
            
    return render_template('wish.html',wishlist = wishlist)

@app.route('/delete/<item>')
def delete(item):
    list_delete(item)
    return redirect(url_for('wishlist'))

# app.run(debug = True) 
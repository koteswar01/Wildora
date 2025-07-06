from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'replace-this-with-a-secure-random-key'  # Needed for flash messages

@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/visit')
def visit():
    return render_template('visit.html', title="Visit")

@app.route('/species')
def species():
    return render_template('species.html', title="Species")

@app.route('/conservation')
def conservation():
    return render_template('conservation.html', title="Conservation")

@app.route('/support')
def support():
    return render_template('support.html', title="Support")

@app.route('/events')
def events():
    return render_template('events.html', title="Events")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")
    
@app.route('/discover')
def discover():
    reptiles = [
        {
            'name': 'Mugger Crocodile',
            'image': 'hero.jpg',
            'description': 'Native to the Indian subcontinent, prefers freshwater habitats, and is known for its broad snout.'
        },
        {
            'name': 'Gharial',
            'image': 'slide2.jpg',
            'description': 'Has a long, narrow snout and feeds mainly on fish. Found in Indian rivers and is critically endangered.'
        },
        {
            'name': 'Saltwater Crocodile',
            'image': 'slide3.jpg',
            'description': 'The largest living reptile, found in estuaries and mangrove swamps across South and Southeast Asia.'
        }
    ]
    return render_template('discover.html', reptiles=reptiles)

@app.route('/learn')
def learn():
    facts = [
        {
            'title': 'Crocodiles Can Live Over 70 Years',
            'content': 'Some crocodile species can live for more than 70 years in the wild, making them one of the longest-living reptiles.'
        },
        {
            'title': 'Gharials Are Fish-Eating Specialists',
            'content': 'With their narrow snouts, gharials are built to catch fish quickly and efficiently in river systems.'
        },
        {
            'title': 'Reptiles are Cold-Blooded',
            'content': 'They rely on external sources of heat to regulate body temperature, often basking in the sun.'
        }
    ]
    return render_template('learn.html', facts=facts)



@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        amount = request.form.get('amount')
        currency = request.form.get('currency')
        cause = request.form.get('cause')
        flash(f"Thank you for your generous donation of {currency} {amount} towards '{cause}'!", 'success')
        return redirect(url_for('donate'))
    return render_template('donate.html', title="Donate")

if __name__ == '__main__':
    app.run(debug=True)

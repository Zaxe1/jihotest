from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock data for products
PRODUCTS = [
    {"id": 1, "name": "Classic White Tee", "price": 29.99, "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"},
    {"id": 2, "name": "Denim Jacket", "price": 89.99, "image": "https://images.unsplash.com/photo-1523205771623-e0faa4d2813d?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"},
    {"id": 3, "name": "Slim Fit Jeans", "price": 59.99, "image": "https://images.unsplash.com/photo-1542272454315-4c01d7abdf4a?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"},
    {"id": 4, "name": "Summer Dress", "price": 49.99, "image": "https://images.unsplash.com/photo-1496747611176-843222e1e57c?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"},
    {"id": 5, "name": "Leather Boots", "price": 120.00, "image": "https://images.unsplash.com/photo-1608256246200-53e635b5b65f?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"},
    {"id": 6, "name": "Casual Hoodie", "price": 45.00, "image": "https://images.unsplash.com/photo-1556905055-8f358a7a47b2?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"},
]

@app.route('/')
def home():
    return render_template('index.html', products=PRODUCTS)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # In a real app, you would handle authentication here
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # In a real app, you would handle user creation here
        return redirect(url_for('login'))
    return render_template('login.html', mode='signup')

if __name__ == '__main__':
    app.run(debug=True)
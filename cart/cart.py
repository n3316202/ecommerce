class Cart():
    def __init__(self, request):
        self.session = request.session
        
        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # If the session key does not exist, create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        print(cart)

        #Make sure cart is available on all pages of site    
        self.cart = cart

    def add(self,product):

        product_id  = str(product.id)

        #>>> a[3] = [1, 2, 3]
        #>>> a
        #{1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        
        # Set session as modified to force data updates/cookie to be saved.
        self.session.modified = True
    
    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        
        # Get ids from cart
        product_ids = self.cart.keys()

        # use ids to lookup products in database model
        products =  Product.objects.filter(id__in=product_ids)
        print("프로덕트", products)
        #Return those looked up products
        return products
    

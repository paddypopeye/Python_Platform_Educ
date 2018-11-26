from decimal import Decimal
from django.conf import settings
from shop.models import Product
from coupons.models import Coupon


class Cart(object):
	
	def __init__(self, request):
		"""
		Initialize the cart
		"""
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			#save empty cart to session
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.coupon_id = self.session.get('coupon_id')
		self.cart = cart


	def add(self, product, quantity=1, update_quantity=False):
		"""
		Add to or update cart
		"""
		product_id = str(product.id)
		if product_id not in self.cart:
			self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

		if update_quantity:
			self.cart[product_id]['quantity'] = quantity
		else:
			self.cart[product_id]['quantity'] += quantity
		self.save()

	def save(self):
		#update the cart
		self.session[settings.CART_SESSION_ID] = self.cart
		#save the session 
		self.session.modified = True

	def remove(self, product):
		#remove all items from the cart session
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()
	

	def __iter__(self):
		#iterate over the  items in the cart and get from the db
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids)
		for product in products:
			self.cart[str(product.id)]['product'] = product

		for item in self.cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price']*item['quantity']
			yield item

	def __len__(self):
		#Count items in cart
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())

	def clear(self):
		#remove cart from the session

		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True	

	@property
	def coupon(self):
		if self.coupon_id:
			return Coupon.objects.get(id=self.coupon_id)
		return None

	def get_discount(self):
		if self.coupon:
			return (self.coupon.discount / Decimal('100'))*self.get_total_price()
		return Decimal('0')

	def get_total_price_after_discount(self):
		return self.get_total_price() - self.get_discount()
	
###########################
CONVENIENCE STORE CHALLENGE
###########################

A local convenience store requires an update for their payment registry system. As a developer you were asked to help with this.

******************
Carts and Products
******************

Implement two classes: Product adn ShoppingCart.

Product
=======

#.  Each Product class instance should implement properties:

    - ``name`` - a product's name of string type (e.g. "apple", "juice" etc.)
    - ``price`` - a price for a single product unit (e.g. 10.59)

#.  Product class should implement get_total method that implements the behavior of calculating the total price for a specified amount of goods

**Test cases**

.. code-block:: python

    obj = Product()
    obj.name = "apple"
    obj.price = 10.59
    assert obj.get_total(0.7) == 7.41

ShoppingCart
============

#.  ShoppingCart instance are containers for Products.
#.  Implement add_product method to add products instances of specified quantity to the cart instance.
#.  Cart instances should implement get_total method to calculate the total price for all products inside of the cart.

**Test cases**

.. code-block:: python

    apple = Product()
    apple.name = "apple"
    apple.price = 10.59
    juice = Product()
    juice.name = "juice"
    juice.price = 36.55

    obj = ShoppingCart()
    obj.add_product(apple, 0.35)
    obj.add_product(juice, 4)
    obj.add_product(apple, 0.35)

    assert obj.get_total() == 153.61

*********************************
Products to Carts, Carts to Carts
*********************************

Constructors
============

#.  Implement both Product and ShoppingCart initializers to provide required data while creating instances. It's ok to initialize empty carts.
#.  Implement a human readable string representations for these classes.

Apple (Fruit) equals to Apple (MacBook)?
========================================

#.  Implement equality comparison for the Product instances. Consider the products are equal in case both objects have the same name and price.

Casting
=======

#.  Implement type-casting for Product and ShoppingCart.

    - Product cast to float type should be equal to its price
    - Product cast to string type should be equal to its name
    - ShoppingCart cast to float type should be equal to its total price

Refactor products
=================

#.  Refactor add_product method in a way to avoid product instances duplication in the cart - adjust appropriate quantities only.

Addition
========

#.  Implement addition behavior for ShoppingCart class:

    - if a Product is added to the cart, the behavior is the same as for add_product method with quantity = 1.
    - if another ShoppingCart instance is added the result is an instance of the same type containing products and their quantities from both carts

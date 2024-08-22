# GAIN Supply

GAIN Supply is a fitness supplies store. It supplies a range of products from supplements and healthy food to fitness equipment. It will be beneficial to customers as it aims to provide a convenient place to find all of the supplies they need, rather than shop through multiple different sites. Users will be able to create profiles, storing their shipping information if they choose to and view their order history. Admin users can add, edit and delete products. Admins can also add to customer testimonials or remove them from the testimonials page.

## Table of Contents

**[1. User Experience](#user-experience)**
* [1.1 User Information](#user-information)
* [1.2 Design](#design)
* [1.3 User Stories](#user-stories)

**[2. Features](#features)**
* [2.1 Existing Features](#existing-features)
* [2.2 Features Left to Implement](#features-left-to-implement)

**[3. Testing](#testing)**

**[4. Technologies](#technologies)**
* [4.1 Languages](#languages)
* [4.2 Libraries & Programs Used](#libraries--programs-used)

**[5. Deployment](#deployment)**  
* [5.1 Deploying this repository](#deploying-this-repository)
* [5.2 Cloning this repository](#cloning-this-repository)
* [5.3 Forking this repository](#forking-this-repository)

**[6. Credits](#credits)**
* [6.1 Media](#media)
* [6.2 Code](#code)

## User Experience

### User Information

#### Typical Users

The main users of the site will be:
* Shoppers
* General
* Admin

#### User Stories

##### Shoppers

The main demographic for the site is shoppers looking to make a purchase.

1. As a shopper, I would like to be able to view products so I can make a purchase.
2. As a shopper, I would like to be able to view product details so I can feel secure in making a purchase.
3. As a shopper, I would like to be able to quickly find special offers so I can easily make a saving on a purchase.
4. As a shopper, I would like to be able to view my basket price at all times so I can avoid over-purchasing.
5. As a shopper, I would like to be able to sort products so I can easily find the ones I'm looking for.
6. As a shopper, I would like to be able to sort by category so I can find the best of a certain type of product.
7. As a shopper, I would like to be able to sort products by price so I can shop to a budget.
8. As a shopper, I would like to be able to search products by name so I can find what I need quickly.
9. As a shopper, I would like to be able to see how many products my search finds so I can tell if the site has what I need.
10. As a shopper, I would like to be able to easily select the quantity and size of products to ensure my order is correct.
11. As a shopper, I would like to be able to view my basket so I can remember what I have selected to purchase.
12. As a shopper, I would like to be able to be able to adjust quantity from the basket so I can easily correct any problems with my order.
13. As a shopper, I would like to be able to easily add my payment information so the process is fast.
14. As a shopper, I would like to know my payment information is secure to make safe purchases.
15. As a shopper, I would like to be able to view my order confirmation so I can confirm what I have ordered and that it was successful.
16. As a shopper, I would like to be able to receive my order confirmation by email so I have a copy for my own records.

##### General

1. As a general user, I would like to be able to easily register so that I can have my own account and profile.
2. As a general user, I would like to be able to log in and out so I can check my account information and keep it safe.
3. As a general user, I would like to be able to recover my password so I don't get locked out of my account if I forget it.
4. As a general user, I would like to receive a email confirmation when I register for an account so I know it has been created successfully.
5. As a general user, I would like to have a personalised account so I can see my order history, address and payment information.

##### Admin

1. As a admin user, I would like to be able to add products so I can add future products to sell.
2. As a admin user, I would like to be able to edit existing products so I can fix any errors or adjust price if necessary.
3. As a admin user, I would like to be able to delete products so I can remove any products the store no longer stocks.

### Design

#### Typography

There are 2 main fonts used across the whole of the site, they have been selected from [Google-Fonts](https://fonts.google.com/). These are Oswald and Open Sans. 

Oswald was selected for the company logo as it has a nice clean look that suits bold text and headings well. To keep things consistent and improve user experience the headings for each page also use the Oswald font. This helps make the site look professional.

Open Sans was chosen for the body because it is easy to read and fairly simplistic. It matches quite well with the Oswald font used for the logo and headings. The difference between the two fonts helps people search through the site faster and find what they are looking for easier.

#### Icons

All icons for the site have been taken from [Fontawesome](https://fontawesome.com/).

In the navbar you can find the first 3 icons.

![Navbar-icons](media/readme/icons/Navbar-icons.png)
1. Shopping bag (fas fa-shopping-bag): This icon was selected for the shopping bag element of the site because it's purpose is easily recognisable and familiar to users already. When there are products in the bag the icon changes colour, this makes it easier for customers to see if they have got any products selected yet.
2. User icon (fas fa-user): This icon was selected for the user profile element of the site because similarly to the shopping bag it's purpose is easily recognisable and familiar to users already.
3. Search icon (fas fa-search): This icon was selected for the user search feature of the site because similarly to the shopping bag and user icon it's purpose is easily recognisable and familiar to users already. The icon looks slightly different on mobile as it looks better matching the other icons due to lack of space.

The next two icons can be found on the product cards when browsing products on the site.

![Prouduct-card-icons](media/readme/icons/Product-card-icons.png)
1. Item tag (fas fa-tag): The tag icon was selected for the price tag icon as similarly to most icons on the site it's purpose is easily recognisable and familiar to users already. Unlike some of the icons it is also recognisable from shopping in person. 
2. Rating star (fas fa-star): The star icon was chosen for the rating section because it is very common to hear things rated out of 5 or 10 stars. This helps users instantly recognise that the number represents a star-rating.

The next three icons can be found on the product details page.

![Product-detail-icons](media/readme/icons/Product-detail-icons.png)
1. Minus icon (fas fa-minus): The minus symbol was selected for the site because it is globally recognised and looks good in the quantity selector.
2. Plus icon (fas fa-plus): The plus symbol was selected for the site because it is globally recognised and looks good in the quantity selector alongside the minus icon.
3. Back icon (fas fa-chevron-left): The chevron left icon was chosen to represent all links that direct the user backwards through the process of navigating the site. Here it can be seen in the Keep Shopping button. This helps give the buttons context and makes them more obvious to the user so they can easily find them.

The next icon is only found on error pages.

![Back-to-products-icon](media/readme/icons/back-to-products-icon.png)
1. Shopping basket (fa-solid fa-basket-shopping): This icon is found on error pages and helps give the user an alternative option to going back to the home page. The meaning of the basket is quite clear and it was selected because it is noticeably different to the bag icon and that will help prevent users from getting confused between the two. 

The next three icons are part of the checkout process.

![Checkout-icons](media/readme/icons/Checkout-icons.png)
1. Lock (fas fa-lock): The lock icon was selected for the Secure Checkout button because it hopes to make the user feel confident that their payment information is safe and secure. 
2. Exclamation circle (fas fa-exclamation-circle): The exclamation circle was chosen for the payment warning as it is a small but very noticeable icon, especially when paired with the bright red colour. This is useful as it provides the user with one last warning before they pay of how much their order will cost.
3. Spinning processing wheel (fas fa-3x fa-sync-alt fa-spin): This icon was selected for the order processing spinning wheel as it provides a clean way to communicate to the user that the order is being finalised. See below.

![Loading-spinner](media/readme/icons/Loading-spinner-icon.png)

#### Colours

The following colours have been used for the colour scheme of the site:
1. #87cefa - Light Sky Blue: This was selected as the company colour scheme, featuring in the logo and on many of the buttons across the site. Typically where the colour is used you while have white text instead of black as it is more visually appealing.
2. #ffffff - White: White was chosen to be used as the text colour for all blue buttons as it pairs much better with the light sky blue than black does.
3. #000000 - Black: Black is used for all headings or text against a plain white background, which makes up the majority of pages. This is to make sure that the user doesn't find it hard to see any of the content.

Additional colours:
#dc3545 - Red: Red is found only on warning messages and delete functions. This is to alert the user that they should be careful to avoid making a mistake and try reduce accidents.

#### Wireframes

## Features

### Existing Features

#### UX Features

1. Consistent Experience Across Different Pages and Devices
2. Home Page
3. View Products
4. Filtering, Searching and Sorting Products
5. View Testimonials
6. Pop Up Messages 

#### E-Commerce Features

1. Shopping Bag
2. Checkout 
3. Order Confirmation
4. Quantity and Size Selectors

#### Profile Features

1. User Registration
2. Log In
3. Log Out
4. Profile Page
5. Order History 

#### Admin Features

1. Accounts
2. Add Product
3. Edit Product
4. Delete Product 

### Possible Future Features

1. Ability for admin to add, edit and delete testimonials outside of the admin panel. Unfortunately due to time constraints the testimonials cannot be changed like the products can. If there was to be a future update to the site it would be a high priority feature so that admins can update them as new testimonials came in.
2. To extend the Testimonial functionality further it would be good to provide a form for users to send in their own Testimonials, which Admin could pick from to display.
3. Finally, building on Testimonials more there could be a 'Most Recent' section which automatically displays the 10 most recently submitted Testimonials for Users to look at. 

## Testing

### User Stories

#### Shoppers 

#### General

#### Admin

### Validator Testing

* **HTML**: 

* **CSS**: 

* **JS**:

* **Python**: 

### Responsivity and Browser Compatibility 

## Technologies

### Languages

HTML, CSS, JavaScript, Python

### Libraries & Programs Used

- Balsamiq - Used to create wireframes.
- Git - Used for version control.
- Github - Used to save site files.
- Google Fonts - Used to import fonts.
- Font Awesome - Used to import icons.
- Chrome Developer Tools - Used to test site responsiveness and design features.
- Materialize CSS - Used to speed up the design of the site.
- Django - Used to streamline the process of creating the site.
- Stripe - Used for handling payments.

## Deployment 

### Deploying this repository

### Cloning this repository

### Forking this repository

## Credits

### Content

- All clothing products for this site have been gathered from: https://www.adidas.co.uk/.
- All supplements and healthy snacks for this site have been gathered from: https://uk.esn.com/. 

### Media

- All clothing product images for this site have been gathered from: https://www.adidas.co.uk/.
- All supplements and healthy snacks images for this site have been gathered from: https://uk.esn.com/. 

### Code

- The core functionality for this site is largely based on CodeInstitute's Boutique Ado project.
- Special thanks to my mentor Brian Macharia for all his help with building and troubleshooting aspects of my project.

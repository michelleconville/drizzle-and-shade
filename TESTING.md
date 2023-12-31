# Testing and Validation

I took a multi-stage approach to testing the site.

The first stage was continuous testing as the site was being developed. This was important to do during development of the django apps to ensure that the different models, views and forms contained or returned the correct data type or values. During the styling of the site, I checked the visual appearance within a live server window to preview the changes before they were committed to reduce the number of bugs.

For the second stage of testing, I used a more structured approach, I created both manual and automated test cases, using the user stories to ensure all the features worked as expected, I executed the tests individually making a note of any errors or changes to the designed behaviour. Any errors were corrected and then the tests repeated.

I then validated all the different types of code and ran performance and accessibility test across different browsers and device types.

Finally, I asked friends to look at the site on their devices and report any issues they came found. All issues reported have been resolved. 


## Table of Contents 
 - [Automated testing](#automated-testing)
 - [Manual Testing](#manual-testing)
 - [Validator Testing](#validator-testing)
 - [Testing Browser Compatibility](#testing-browser-compatibility)
 - [Bugs](#bugs)



## Automated testing

### Unit Testing

Unit tests were created to test the functionality of the apps. These can be found in the tests.py files in the respective apps.

Running the test suite
The tests are run in the terminal window by entering 

        python3 manage.py test 

This will automatically run all test. If running tests in quick succession, it's recommended to add --keepdb at the end, so the database doesn't have to be rebuild for every test cycle. All tests passed, but if one failed, it would be displayed with a clear error message, so errors can be resolved.


<details><summary>Home tests</summary>

![home](docs/testing/unit-test-results/coverage-home.jpg) 

</details>

<details><summary>Profiles tests</summary>

![Profiles](docs/testing/unit-test-results/coverage-profiles.jpg) 

</details>


<details><summary>Products tests</summary>

![Products](docs/testing/unit-test-results/coverage-products.jpg) 

</details>

<details><summary>Checkout tests</summary>

![Checkout](docs/testing/unit-test-results/coverage-checkout.jpg) 

</details>

<details><summary>Contact tests</summary>

![Contact](docs/testing/unit-test-results/coverage-contact.jpg) 

</details>

<details><summary>FAQs tests</summary>

![Contact](docs/testing/unit-test-results/coverage-faqs.jpg) 

</details>

<details><summary>Bag tests</summary>

![Bag](docs/testing/unit-test-results/coverage-bag.jpg) 

</details>

### Site Coverage Report

                coverage run --source=drizzle_and_shade manage.py test

Through my testing, I was able to get a total of 72% coverage across the site. The remaining 28% will be covered through the manual testing below.

View the site wide coverage report [coverage-report](coverage.txt)

##### Back to [top](#table-of-contents)

## Manual Testing

### Navigation bar and homepage

        As a shopper I can easily navigate through the site so that I can view desired content

**Expected**

* All links should work
* Homepage should display image
* Call to action should link to the all products page

**Outcome**

* All links working as expected
* Landing page displays as expected

### Footer

#### Footer

        As a shopper I can easily find a navigation bar and footer so that I can see what content there is on the website
        As a shopper I can connect to the social media sites so that I can follow them and keep up to date with their products and promotions
        As a shopper I can sign up for the website's newsletter so that I can keep up to date with new products and promotions
        As a shopper I can contact the store so that I can find out information that I require

**Expected**

* The subscribe form for the newsletter should accept an email address, if the user enters their email for a seccond time a message should display.
* All product links open on the correct product category page
* All help links open on the correct pages
* Facebook link opens in a new tab

**Outcome**

* All links open as expected

* Subscribe form working as expected

![Subscribe form](docs/testing/manual-testing/subscribe-message.jpg)

### Product Search

        As a shopper I can search for products using the search form so that I can find the products I'm specifically looking for

**Expected**

* A search result page should open
* Empty search gives a error message

**Outcome**

* Search result page works as expected

![Subscribe form](docs/testing/manual-testing/search-result.jpg)

* Empty search gives a error message

![Subscribe form](docs/testing/manual-testing/search-error.jpg)


### All Products page

                As a shopper I can easily see the products list so that I can see what the site has to offer
                As a shopper I can search products by category so that I can easily find what I'm looking for
                As a shopper I can sort products by rating, price and name so that I can easily find what I'm looking for

**Expected**

* All products display
* Sorting works
* Product cards are showing the expected information
* Product links to product detail page
* Low or no stock badge diplaying
* Pagination functionality 
* Back to top button displaying
* Edit and delete functionality for the site owners/staff only 


**Outcome**

* All products displaying as expected
* All the links working as expected
* Sorting working as expected

![Product sorting](docs/testing/manual-testing/product-filter.jpg)

* Low or no stock badges diplaying as expected

![Product sorting](docs/testing/manual-testing/no-or-low-stock.jpg)

* Pagination working as expected 
* Back to top button working as expected
* Edit and delete button working as expected

![Product sorting](docs/testing/manual-testing/product-features.jpg)

### Product Detail

                As a shopper I can see the products details page so that I can see the rating, price, short and description
                As a shopper I can select the quantity of a product so that I can buy more 
                As a shopper I can add an umbrella to the shopping bag so that I can keep track of what I am spending
                As a logged-in shopper I can save selected products to my wishlist for later purchase
                As a shopper I can see ratings and reviews so that I can read the opinions of other shoppers
                As a logged-in shopper I can leave a rating and reviews so that I can share my experience with others


**Expected**

* The name of the product, the price, the catagory the product is in, the rating of product, a description and the product image displays
* A badge appears under the price to advise the user if the product is low in stock or out of stock
* A quanity selector so the user can change the quanity
* An add to cart button display and is disabled if the product is out of stock
* An add to wishlist icon displays, users need to be logged in for this functionality to work, a modal will display if the user selects the button and is not logged in.
* Toast messages display advising the user of any actions completed on this page either if they have added an item to the cart or added or removed an item from the wishlist. The success toast message 

**Outcome**

* Product information displays as expected
* Quanity selector works as expected
* Low or no stock badges diplaying as expected

![Product sorting](docs/testing/manual-testing/product-detail-page-test.jpg)

* The add to cart button works as expected
* The wishlist works as expected

![Product sorting](docs/testing/manual-testing/out-of-stock.jpg)

* Toast messages display as expected

![Product sorting](docs/testing/manual-testing/toast-message-success.jpg)

### Product detail - reviews

                As a shopper I can see ratings and reviews so that I can read the opinions of other shoppers
                As a logged-in shopper I can leave a rating and reviews so that I can share my experience with others

**Expected**

* Review section displays a list of reviews for a product if available 
* Registered users can rate and review a product
* Registered users can edit and delete their review
* When a producted is rated, the rating will update with the average rating across all reviews

**Outcome**

All review fucntionality working as expected

##### Unregistered user

![Product detail reivew page for Unregistered user](docs/features/product-detail-page-reivew-logged-out.jpg)

##### Registered user 

![Product detail reivew page for registered user](docs/features/product-detail-page-reivew-logged-in.jpg)


### Shopping cart

                As a shopper I can see the shopping bag summary and total cost so that I can see how much I will spend
                As a shopper I can select the quantity of a product so that I can buy more 
                As a shopper I can remove items from shopping bag so that I don't buy what I don't want


**Expected**

* Information and images display correctly
* Have the ability to change quantity in the bag of a product
* Have the ability to remove a product
* Calculations are correct
* Buttons link to the correct pages

**Outcome**

* Everything renders as it should
* Calculations are working as expected
* Delivery charge is being applied correctly
* Buttons working as expected
* Remove and Update woeking as expected

![Bag page](docs/features/shopping-bag.jpg)

### Checkout

                As a shopper I can put in my card details so that I can pay for my umbrella
                As a shopper I receive order confirmations so that I can be sure my order has been processed
                As a logged-in shopper I can save my details so that I don't have to retype my address every time

**Expected**

* Show the correct order summary
* Display all form fields
* Required fields are marked with an asterisk
* The payment field from Stripe works and gives error messages when card details are not correct
* After a successful order, a toast message confirms order and user recieves an email

**Outcome**

* Order summary displays correctly
* All form fields working as expected

![Checkout page](docs/features/checkout.jpg)

* Payment field working as expected 
* Toast message working as expected

![Checkout page](docs/testing/manual-testing/toast-message-checkout.jpg)

* Email confirmation working as expected

![Checkout page](docs/testing/manual-testing/email-confirmation-checkout.jpg)

### Contact us

                As a shopper I can contact the store so that I can find out information that I require
                As a shopper I can receive a contact confirmation email to let me know that my email has been sent

**Expected**

* Display all form fields
* Required fields are marked with an asterisk
* Buttons link to the correct pages
* After successfully submitting a query, a toast message confirms and user recieves an email

**Outcome**

* All form fields working as expected
* Toast message working as expected
* Buttons working as expected
* Email confirmation working as expected

![Contact page](docs/testing/manual-testing/contact-form.jpg)


![Contact - toast message](docs/testing/manual-testing/toast-message-contact.jpg)


![Contact - email confirmation](docs/testing/manual-testing/email-confirmation-contact.jpg)


### Toasts

                As a shopper I am notified about any actions I have made so that I have a clear understanding of what has been completed/updated


**Expected**

Displays four different types of toast messages
Toast meesages display the text from the respective view
Toast message has a close button 
Each message will display be 3 second before disappearing.

**Outcome**

Toast messages display as expected

**Selection of toat messages**

![Contact - toast message](docs/testing/manual-testing/toast-message-contact.jpg)

![Checkout - toast message](docs/testing/manual-testing/toast-message-checkout.jpg)

![Success - toast message](docs/testing/manual-testing/toast-message-success.jpg)

![error - toast message](docs/testing/manual-testing/toast-non-admin-access.jpg)

![alert - toast message](docs/testing/manual-testing/toast-message-alert.jpg)



### Account overview 
                As a shopper I can register for an account so that I can use features for logged-in users

**Expected**

* Buttons link to the correct pages

**Outcome**

* Buttons working as expected

![Account overview](docs/features/account-overview.jpg)


### My Profile
                As a logged-in shopper I can save my details so that I don't have to retype my address every time

**Expected**

* Display the order history
* Links to the order work
* Display all form fields
* Update information works
* Delete button deletes the users account

**Outcome**

* All form fields working as expected
* Information updating as expected
* Delete button working as expected
* Order history display and works as expected

![My profile](docs/features/my-profile.jpg)

### My Wishlist

                As a logged-in shopper I can save selected products to my wishlist for later purchase


**Expected**

* On the product detail page only allows registered users to add to the wishlist, you are redirected to a model if you are not logged in
* Displays a small product image, product name and price.
* The Remove button, removes the item

**Outcome**
* Adding item to wishlist is working as expected
* Page displaying as expected
* Remove button working as expected

![wishlist](docs/testing/gif/wishlist.gif)

### Admin Panel

                As a site owner I can log in/out to an admin panel so that I have full access to staff area

**Expected**

* Buttons link to the correct pages

**Outcome**

* Buttons working as expected

![Admin panel](docs/features/admin-panel.jpg)

### Category and product management

**Expected**

* Buttons link to the correct pages

**Outcome**

* Buttons working as expected

![Category and product management](docs/features/product-management.jpg)

#### Category management
                As a site owner I can add new categories to the shop so that I can make sure the website is up to date
                As a site owner I can edit/delete categories so that I can make sure the website is up to date

**Expected**

* A category can be added
* A category can be edited 
* A category can be deleted
* Toast message is displaying

**Outcome**

* All Functionality working as expected

![Category management](docs/testing/gif/category-management.gif)

### Add Products

                As a site owner I can add new product to the shop so that I can make sure the website is up to date
                As a site owner I can edit/delete products so that I can make sure the website is up to date

The Adding/Editing/Deleting of Products is only available to staff. 

**Expected**

* Here the staff member can select a products category and add the products details.
* New product can be viewed and edited and deleted

**Outcome**

* All Functionality working as expected

![Product management](docs/testing/gif/product-management.gif)


### Stock Management

**Expected**

* Displays a list of all products and the number of that product that is are available.
* An admin user can add or remove stock

**Outcome**

* All Functionality working as expected

![Product management](docs/testing/gif/stock-management.gif)

#### Managing shipping

**Expected**
* Displays a list of all orders, with the customers order number, full name and total and if the order has been shipped. 
* Edit button to allow order to me maked as shipped
* Email confirmation test to user to advise order has been shipped

**Outcome**

* All Functionality working as expected

##### Order list page

![Managing shipping page](docs/features/orders-list.jpg)

##### Confirm shipping page

![Confirm shipping page](docs/features/edit-shipping.jpg)

##### Confirmation email

![Confirm shipping page](docs/testing/manual-testing/email-confirmation-shipping.jpg)


#### Manage FAQs

                As a site owner I can add FAQs to the site so that I can make sure that the shopper can find answer
                As a shopper I can read the FAQ's so that I can find the answer to my question or concern before contacting the site

**Expected**

* Admin user can add a question and its answer, and it will be displayed on the website straight away.
* Admin users can edit, update and delete a faqs.

**Outcome**

* All Functionality working as expected

##### FAQ page

![FAQ page](docs/features/manage-faqs.jpg)

##### Add an FAQ 

![Add an FAQ](docs/features/add-faqs.jpg)

##### Edit an FAQ 

![Edit an FAQ](docs/features/edit-faqs.jpg)

##### Delete an FAQ 

![Delete an FAQ](docs/features/delete-faq.jpg)


#### AllAuth

                As a shopper I can easily see if I'm logged-in or logged-out so that I can be sure what my status is
                As a shopper I can log in/out of my account if I wish so that I can connect or disconnect from the website

**Expected**

* A user can register for an account
* A user can login
* A user can log out
* A user can change their password

**Outcome**

* All Functionality working as expected

##### Login page

![Login page](docs/features/signin.jpg)

##### Register page

![Register page](docs/features/register.jpg)

##### Logout page

![Logout page](docs/features/logout.jpg)

##### Forgot password page 

![forgot password page](docs/features/password-reset.jpg)

##### Change password page 

![Change password](docs/features/changepassword.jpg)


##### Back to [top](#table-of-contents)

## Validator Testing

### HTML

All HTML pages were run though the [html-checker](https://validator.w3.org/nu/). 

Due to the django templating language code used in the HTML files and pages with login required, these pages could not be copy and pasted into the validator. To test the validation on the files, open the page to validate, right click and view page source. Paste the raw html code into the validator as this will be only the HTML rendered code.

#### CSS

CSS was validated using the W3C Markup Validation Service. This was done using the 'Validate by Direct Input' option.

<details><summary>CSS results - base</summary>

![CSS validation results base](docs/testing/validation/css-base-page.jpg) 

</details>

<details><summary>CSS results - checkout</summary>

![CSS validation results checkout](docs/testing/validation/css-checkout-page.jpg) 

</details>

<details><summary>CSS results - products</summary>

![CSS validation results products](docs/testing/validation/css-products-page.jpg) 

</details>

<details><summary>CSS results - profiles</summary>

![CSS validation results profiles](docs/testing/validation/css-profiles-page.jpg) 

</details>

##### Back to [top](#table-of-contents)

### JavaScript

[JSHint Static Code Analysis Tool](https://jshint.com/) for JavaScript was used to validate the Javascript files. No significant issues were found.

One item to note:

When testing the button validation script in products, I did get a number of warnings but this was due to the templating variables included with the js, when I used the source code from the rendered page I no longer got these errors 

<details><summary>button validation script - warnings</summary>

![button validation script - warnings](docs/testing/validation/js-button-warning.jpg) 

</details>

<details><summary>button validation script</summary>

![button validation script - clean](docs/testing/validation/js-button-noerrors.png) 

</details>

### pep8 

[pep8ci](https://pep8ci.herokuapp.com/) was used for validating all python files. All python files were checked with no errors reported.

<details><summary>Example of pep8ci results</summary>

![Example of pep8ci results](docs/testing/validation/pep8-validation.jpg) 

</details>

### Accessibility

The WAVE WebAIM web accessibility evaluation tool was used throughout development and for final testing of the deployed website to ensure the website met high accessibility standard. I have included an image of the homepage result only, however, all pages passed with 0 errors. I tested the website through a [Colour Contrast Accessibility Validator](https://color.a11y.com/Contrast/) to further test the contrast and no issues were detected.


<details><summary>WAVE Homepage results</summary>

![WAVE Homepage results](docs/testing/validation/wave-home.jpg) 

</details>

<details><summary>Colour Contrast Accessibility Validator results</summary>

![Color Contrast Accessibility Validator results](docs/testing/validation/colour-contrast.jpg) 

</details>

## Performance

Google Lighthouse in Google Chrome Developer Tools was used to test the performance of the website.

<details>
<summary>Homepage</summary>

![homepage page](docs/testing/validation/lighthouse-home.jpg)

</details>

<details>
<summary>Products page</summary>

![Products page](docs/testing/validation/lighthouse-products.jpg)

</details>

<details>
<summary>Product detail page</summary>

![Product detail page](docs/testing/validation/lighthouse-product-detail.jpg)

</details>

<details>
<summary>Bag page</summary>

![Bag page](docs/testing/validation/lighthouse-bag.jpg)

</details>

<details>
<summary>Checkout page</summary>

![Checkout page](docs/testing/validation/lighthouse-checkout.jpg)

</details>

<details>
<summary>Contact page</summary>

![Contact page](docs/testing/validation/lighthouse-contact.jpg)

</details>

<details>
<summary>Profile page</summary>

![Profile page](docs/testing/validation/lighthouse-profiles.jpg)

</details>

<details>
<summary>Wishlist page</summary>

![Wishlist page](docs/testing/validation/lighthouse-wishlist.jpg)

</details>

<details>
<summary>Admin panel page</summary>

![Admin panel page](docs/testing/validation/lighthouse-admin-panel.jpg)

</details>

<details>
<summary>Category and Product Management page</summary>

![Category and Product Management page](docs/testing/validation/lighthouse-product-management.jpg)

</details>

<details>
<summary>Category Management page</summary>

![Category Management page](docs/testing/validation/lighthouse-category.jpg)

</details>

<details>
<summary>Product Management page</summary>

![Category Management page](docs/testing/validation/lighthouse-add-product.jpg)

</details>

<details>
<summary>Stock page</summary>

![Stock page](docs/testing/validation/lighthouse-stock.jpg)

</details>

<details>
<summary>Edit Stock page</summary>

![Edit Stock page](docs/testing/validation/lighthouse-stock-update.jpg)

</details>

<details>
<summary>Shipping page</summary>

![Shipping page](docs/testing/validation/lighthouse-order-list.jpg)

</details>

<details>
<summary>Confirm Shipping page</summary>

![Confirm Shipping page](docs/testing/validation/lighthouse-order-list-edit.jpg)

</details>

<details>
<summary>Privacy page</summary>

![Privacy page](docs/testing/validation/lighthouse-privacy.jpg)

</details>

<details>
<summary>Terms and Conditions page</summary>

![Terms and Conditions page](docs/testing/validation/lighthouse-terms.jpg)

</details>

## Testing Browser Compatibility

The website was successfully opened and rendered correctly in Chrome (both desktop and mobile versions), Edge, Firefox and Safari.

### Responsiveness
All pages were tested to ensure responsiveness on screen sizes from 320px and upwards on the following browsers and devices


### Devices
*   iPhone SE
*   OnePlus Nord
*   Dell laptop

In addition to the above listed devices, the Google Chrome Developer Tools device toggling option for all available devices was used.

##### Back to [top](#table-of-contents)

## Bugs

1. Products changing order on stock level page after clicking update stock

        Updates the stock_level view to include .order_by('-name') to prevent this from happening

2. Low or no stock badges were added to the product pages and the add to cart button was disabled for no stock but on the product page user could more items then were available in stock

        Added some js and a model to advise the user if they tried to add more products than available to the shopping cart

##### Back to [top](#table-of-contents)

## Unfixed 

* I have been unable to get richtextfield to appear on the frontend of the site, I can view it in django admin, I have reseached this issue online and I can not find an issue with my setup.

[Return to README.md](README.md)



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
* Subscribe email working as expected


### Product Search

        As a shopper I can search for products using the search form so that I can find the products I'm specifically looking for

**Expected**

* A search result page should open
* Empty search gives a error message

**Outcome**

* Search result page works as expected
* Empty search gives a error message


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
* Low or no stock badges diplaying as expected
* Pagination working as expected 
* Back to top button working as expected
* Edit and delete button working as expected

### Product Detail

                As a shopper I can see the products details page so that I can see the rating, price, short and description
                As a shopper I can select the quantity of a product so that I can buy more 
                As a shopper I can add an umbrella to the shopping bag so that I can keep track of what I am spending
                As a logged-in shopper I can save selected products to my wishlist for later purchase
                As a shopper I can see ratings and reviews so that I can read the opinions of other shoppers
                As a logged-in shopper I can leave a rating and reviews so that I can share my experience with others


**Expected**
I
* The name of the product, the price, the catagory the product is in, the rating of product, a description and the product image displays
* A badge appears under the price to advise the user if the product is low in stock or out of stock
* A quanity selector so the user can change the quanity
* An add to cart button display and is disabled if the product is out of stock
* An add to wishlist icon displays, users need to be logged in for this functionality to work, a modal will display if the user selects the button and is not logged in.
* Toast messages display advising the user of any actions completed on this page either if they have added an item to the cart or added or removed an item from the wishlist. The success toast message 

**Outcome**

* Product information displays as expected
* Low or no stock badges diplaying as expected
* Quanity selector works as expected
* The add to cart button works as expected
* The wishlist works as expected
* Toast messages display as expected

### Product detail - reviews

                As a shopper I can see ratings and reviews so that I can read the opinions of other shoppers
                As a logged-in shopper I can leave a rating and reviews so that I can share my experience with others

**Expected**

* Review section displays a list of reviews for a product if available 
* Registered users can rate and review a product
* Registered users can only review a prodcut once
* Registered users can edit and delete their review
* When a producted is rated, the rating will update with the average rating across all reviews

**Outcome**
All review fucntionality working as expected











##### Back to [top](#table-of-contents)

## Validator Testing

## Validator Testing

### HTML

All HTML pages were run though the [html-checker](https://validator.w3.org/nu/). 

Due to the django templating language code used in the HTML files and pages with login required, these pages could not be copy and pasted into the validator. To test the validation on the files, open the page to validate, right click and view page source. Paste the raw html code into the validator as this will be only the HTML rendered code.




##### Back to [top](#table-of-contents)

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

##### Back to [top](#table-of-contents)

## Unfixed 

[Return to README.md](README.md)



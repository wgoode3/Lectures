# Week 2 Day 5
## Responsive Web Design and Bootstrap
<img src="https://en.bmstu.wiki/index.php?title=Bootstrap_(front-end_framework)&mobileaction=toggle_view_mobile#/media/File:Bootstrap.png" alt="Bootstrap" width="200px">

## Responsive Web Design

<details>
  <summary>What is Responsive Web Design?</summary>
  A technique for building a website so that it can be functional and look good on any type of hardware: phone, tablet, laptop, or desktop. Rather than designing a version of the site for each, design one that works for all of them.
</details>

## Techniques

* Use responsive units

| Unit | Description                                                  |
|:-----|:-------------------------------------------------------------|
| px   | the number of pixels in the viewing device                   |
| em   | relative to the font size of the parent element              |
| rem  | relative to the font size of the root element                |
| vw   | 1% of the viewport's width                                   |
| vh   | 1% of the viewport's height                                  |
| vmin | 1% of the smaller dimension of the viewport (height or width)|
| vmax | 1% of the larger dimension of the viewport (height or width) |
| %    | 1% of the containing element                                 |

* Use Media Queries

Allows us to specify alternative css based on the size of the display.

```css
@media only screen and (max-width: 480px) {
    body { 
    	background: green; 
    }
}
@media only screen and (min-width: 481px) {
    body { 
    	background: red; 
    }
}
@media only screen and (min-width: 1024px) {
    body { 
    	background: yellow; 
    }
}
```

* Use a Grid System

There are many that exist, we will demonstrate the one built into Bootstrap shortly.

## Bootstrap

Bootstrap is the most popular CSS Framework. It was released by Twitter back in 2011 and is free to use in all of your projects. 

```Bootstrap is the second most-starred project on GitHub, with more than 121,725 stars and 57,617 forks.``` 
-[Wikipedia](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework))

### Getting Started

We can incorporate Bootstrap into our projects just like we did with jQuery, either linking to a CDN, or linking to the downloaded code in our project.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Bootstrap Demo</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
</head>
<body>
    <h1>Bootstrap Demo</h1>
</body>
</html>

``` 

In this case we will be using CDN links. Notice that Bootstrap also includes JavaScript libraries.

### Classes and ```container```

The first thing to note is that Bootstrap provides us with a number of really cool classes that we can use in out code. The first one we'll be using is called ```container```. The ```container``` class is like a wrapper around our code, and it will adjust its size based on the screen size.

```html
<body>
    <div class="container">
        <h1>Bootstrap Demo</h1>
    </div>
</body>
```

Next we can draw attention to our ```<h1>``` tag by wrapping it in the ```jumbotron``` class.

```html
<body>
    <div class="container">
        <div class="jumbotron">
            <h1>Bootstrap Demo</h1>
        </div>
    </div>
</body>
```

### Bootstrap Grid

Let's introduce the Bootstrap grid. Bootstrap uses a grid with 12 columns, meaning if we specify a ```<div>``` to take up all 12 it will be full width. 

```html
<div class="row">
    <div class="col-sm-3">.col-sm-3</div>
    <div class="col-sm-3">.col-sm-3</div>
    <div class="col-sm-3">.col-sm-3</div>
    <div class="col-sm-3">.col-sm-3</div>
</div>
```

This example will create 4 equal width columns.

```html
<div class="row">
    <div class="col-sm-4">.col-sm-4</div>
    <div class="col-sm-8">.col-sm-8</div>
</div>
```

This example will create 2 columns, one taking 1/3 of the width and the other taking 2/3 of the width.

Note the ```sm``` in the above class name. This is the size of screen at which it will break and form single full width columns. We can also have ```lg``` and ```md``` as well and these will break at different screen widths.

We can use this to our advantage as well.

```html
<div class="row">
    <div class="card col-lg-3 col-md-4 col-sm-6">Content</div>
    <div class="card col-lg-3 col-md-4 col-sm-6">Content</div>
    <div class="card col-lg-3 col-md-4 col-sm-6">Content</div>
    <div class="card col-lg-3 col-md-4 col-sm-6">Content</div>
</div>
```

The above code will be 4, 3, 2, or 1 ```div```s wide based on the display width.

A breakdown of the column classes and the breakpoint width for each.

| class   | width    |
|:--------|:---------|
| col-    | <576px   |
| col-sm- | >=576px  |
| col-md- | >=768px  |
| col-lg- | >=992px  |
| col-xl- | >=1200px |

### Bootstrap Forms

There are also classes that can be used for forms.

```html
<form action="/process" method="post">
    <div class="form-group">
        <label for="name">Your name:</label>
        <input type="text" name="name" id="name" class="form-control">
    </div>
    <div class="form-group">
        <label for="email">Your email:</label>
        <input type="text" name="email" id="email" class="form-control">
    </div>
</form>
```

The ```form-group``` class applies proper form spacing. The ```form-control``` class styles the input.

### Buttons

We can also style buttons for our form. The ```.btn``` class styles the sizes and appearance of the button. ```btn-success``` gives additional style to the button specifically it makes the button green.

```html
<input type="submit" value="Sign Up!" class="btn btn-success">
```

Other colors can be applied similarly.

| class         | color     |
|---------------|-----------|
| none          | grey      |
| btn-primary   | blue      |
| btn-secondary | grey      |
| btn-success   | green     |
| btn-info      | blue      |
| btn-warning   | yellow    |
| btn-danger    | red       |
| btn-dark      | black     |
| btn-light     | white     |
| btn-link      | blue link |

You can also change the size with classes like: ```btn-lg```, ```btn-sm```.

### Alerts

You may also need to display messages to users on the site and alerts are perfect for this.

```html
<div class="alert alert-success alert-dismissable">
    <button type="button" class="close" data-dismiss="alert">&times;</button>
    Welcome to the site!
</div>
```

This is a dismissable alert, it uses JavaScript so that when a user clicks on the "X" it hides the alert. There are many different classes of ```alert``` similar to the classes available with buttons as we see above.

### Tables

Bootstrap can make your table look nice.

```html
<table class="table table-striped">
    <tr>
        <td>Product</td>
        <td>Price</td>
        <td>Action</td>
    </tr>
    <tr>
        <td>Dojo t-shirt</td>
        <td>$15.99</td>
        <td><a href="/buy/1">Buy</a></td>
    </tr>
    <tr>
        <td>Dojo Algorithm Book</td>
        <td>$34.99</td>
        <td><a href="/buy/2">Buy</a></td>
    </tr>
</table>
```

### Other classes to look up

There are a bunch of really cool things you can do in bootstrap, check out the following:

* Modal
* Navbar
* Dropdown
* Carousel

Useful bootstrap resources:

* https://getbootstrap.com/ - where to get bootstrap
* https://www.w3schools.com/bootstrap4/ - a great tutorial

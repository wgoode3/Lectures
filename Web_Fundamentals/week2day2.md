# Week 2 Day 2
## jQuery
![jQuery](https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/JQuery_logo.svg/1280px-JQuery_logo.svg.png "jQuery")

### What is a JavaScript library?

what is a library in general?

fairly analogous to that
library: collection of books :: JavaScript Library : collection of JavaScript

basically a bunch of handy methods that someone wrote for us

why is this useful?

avoid reinventing the wheel
code already pretty optimized
supports the javascript engines used by Chrome, Firefox, Safari, etc. 
helps DRY up our code? <-- maybe too early to bring up


### What is the DOM?

Document Object Model 

### How do I use it?

First we must link to it in our html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Examle</title>
    <meta charset="UTF-8">
    <script type="text/javascript" src='https://code.jquery.com/jquery-3.1.1.min.js'></script>
</head>
<!-- and so on -->
```

or we can download the jquery-3.1.1.min.js script and link to it in our project's /js folder

```html
<!DOCTYPE html>
<html>
<head>
    <title>Examle</title>
    <meta charset="UTF-8">
    <script type="text/javascript" src='/js/jquery-3.1.1.min.js'></script>
</head>
<!-- and so on -->
```
### $(document).ready()

```javascript
// inside script.js
$(document).ready(function(){
    console.log("jQuery is ready");
});
```

What does this do? Is it necessary?

### Selectors and Events
you can select html tags, ids, classes, any combination of the above
selectors should feel similar to css selectors

```javascript
$(p).append(" <i>hello</i>");
$("#some_id").text("New text");
$(".some_class").css("background-color", "red");
```

events, wait for something to happen

```javascript
$(button).click(function(){
    console.log("the button has been clicked");
});

$(".logo").hover(
    function(){
        $(this).css("width", "200px";
    },
    function(){
        $(this).css("width", "100px";
    }
});
```
and then trigger an anonymous function that we call a callback function.

### getters and setters

```javascript
$("#name").val("Shelly");

$("#registerButton").click(function(){
    var name = $("#name").val();
    console.log(`the name is ${name}`);
});
```

can use a method like ```.val()``` to both set a value or access the value.

# Week 2 Day 3
## jQuery Part II
<img src="https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/JQuery_logo.svg/1280px-JQuery_logo.svg.png" alt="jQuery" width="500px">

### Callbacks revisited
A callback is just a function that we pass as a variable into another function. The function we pass it into can call the callback function. This can be a handy way to to pass data from one function to another function as well.

<details>
  <summary>Why is a callback function called a callback function?</summary>
  Because the function into which it is being passed as an argument calls it... back.
</details><br>

```javascript
function acceptsCallback(callback){
  return callback();
}

console.log(acceptsCallback(function(){
  return "I'm being called by the function acceptsCallback";
}));

// this will print "I am coming from your callback function!"


function acceptsCallback2(callback){
  return callback("It's dangerous to go alone, take this data!");
}

console.log(acceptsCallback2(function(data){
  return data;
}));

// this will print "It's dangerous to go alone, take this data!"
```

### The DOM review

<details>
  <summary>Is the DOM exactly equal to our HTML code?</summary>
  No. But it is generated from our HTML code.
</details><br>

```html
<table border=1>
	<tr><th>Test</th></tr>
	<tr><td>Data</td></tr>
</table>
```
<details>
  <summary>Does the above table have &lt;tbody&gt; tags?</summary>
  Yes. The browser will automatically generate a &lt;tbody&gt; for us even if we didn't write it. You can style it with CSS and everything.
</details><br>

<details>
  <summary>How else could the DOM differ from out HTML? (Hint: what have we been learning this week)</summary>
  It can contain HTML generated from JavaScript.
</details>

### Static vs Dynamic

### What is ```$(this)``` ?

### Why would we use ```.on()``` ?

### Debugging

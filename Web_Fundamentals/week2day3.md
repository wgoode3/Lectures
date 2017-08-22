# Week 2 Day 3
## jQuery Part II
<img src="https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/JQuery_logo.svg/1280px-JQuery_logo.svg.png" alt="jQuery" width="500px">

### Callbacks revisited
A callback is just a function that we pass as a variable into another function. The function we pass it into can call the callback function. This can be a handy way to to pass data from one function to another function as well.

<details>
  <summary>Why is a callback function called a callback function?</summary>
  Because the function into which it is being passed as an argument calls it... back.
</details>

```javascript
function acceptsCallback(callback){
  return callback();
}

console.log(acceptsCallback(function(){
  return "I am coming from your callback function!"
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

### The DOM revisited

### Static vs Dynamic

### What is ```$(this)``` ?

### Why would we use ```.on()``` ?

### Debugging

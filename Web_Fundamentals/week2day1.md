# Week 2 Day 1

## Lecture:

<details> 
	<summary>Where does javascript run? </summary>
	In our browsers... 
	<summary>If you could provide js code directly to a cpu would it run?</summary>
	No... we must first convert it into machine code / bytecode before it runs, this is done by the javascript engine
	<summary>Examples of JS engines</summary>
	* V8
	* JavaScriptCore
	* Chakra
	* Spider monkey
	* Squirrel fish

	They are written in C/C++ and have the goal of translating our js code into something a cpu can actually run.

	In other words: JavaScript must be parsed before it can be run.

</details>

### How do we declare variables?
```javascript
var x = 3;

function test(){
		var y = 4;
}

if(true){
		var z = 5;
}

for(var i = 0; i < 1; i++){
}

console.log(x, y, z, i);
```

<details> 
	<summary>Can we access x, y, and/or z?</summary>
	Variables declaration is function scoped... that means it can get into a loop or a conditional, but not into a function.
	<summary>Loops? <br>What types are there?</summary>
	* for
	* for/in
	* while
	* do/while
</details>

### How does a for loop work?	

```javascript
for (var i = 0; i < 5; i++){	
}

// 1) declares a variable i and sets it to some number (var i = 0)
// 2) continues running as long as this condition (i < 5)
// 3) on each iteration do this (i++, short for i = i + 1)
```

#### T-Diagram

| Iteration  | var i | i < 5 |
|:----------:|:-----:|:-----:|
| 1          | 0     | false |
| 2          | 1     | false |
| 3          | 2     | false |
| 4          | 3     | false |
| 5          | 4     | false |
| 6          | 5     | true  |

		
### How do functions work?

```javascript
function test(){
	// do something
}

var test2 = function(){
	// do something else
}
```

### What does return do?

```javascript
// What does this return?
function test(){
	return "this";
	return "that";
}
```		

#### return vs console.log() vs alert()

```javascript
function returnSomething(){
	return "Something";
}

function returnNothing(){
}

console.log(returnSomething());
console.log(returnNothing());

// What do these console log and why?

alert("hello");

// What does alert do?

```	
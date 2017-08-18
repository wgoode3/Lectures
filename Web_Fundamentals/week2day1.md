# Week 2 Day 1

## Lecture:

### Introductory questions

<details> 
	<summary><h4>Where does javascript run?</h4></summary>
	<br>In our browsers... 
</details><br>

<details>
	<summary><h4>If you could provide js code directly to a cpu would it run?</h4></summary>
	<br><p>No... we must first convert it into machine code / bytecode before it runs, this is done by the javascript engine</p>
	<h3>Examples of JS engines</h3>
	<ul>
		<li>JavaScriptCore</li>
		<li>V8</li>
		<li>Chakra</li>
		<li>Spider Monkey</li>
		<li>Squirrel Fish</li>
	</ul>
	<p>They are written in C/C++ and have the goal of translating our js code into something a cpu can actually run.<br>In other words: JavaScript must be parsed before it can be run.</p>
</details><br>

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
</details><br>

<details>
	<summary>Loops? What types are there?</summary> 
	<ul>
		<li>for</li>
		<li>while</li>
		<li>for/in</li>
		<li>do/while</li>
	</ul>
	<p>Don't worry about those last two, we'll talk about them in the future</p>
</details><br>

### How does a for loop work?	

```javascript
for (var i = 0; i < 5; i++){	
}
```
<details>
	<summary>var i = 0</summary>
	declares a variable i and sets it to some number
</details><br>

<details>
	<summary>i < 5</summary>
	continues running as long as this condition
</details><br>

<details>
	<summary>i++</summary>
	on each iteration do this <br><code>i++ is shorthand for i = i + 1</code>
</details><br>

<details>
	<summary>T-Diagram</summary>
	<table>
		<tr><th>Iteration</th><th>var i</th><th>i < 5</th></tr>
		<tr><td>1</td><td>0</td><td>true</td></tr>
		<tr><td>2</td><td>1</td><td>true</td></tr>
		<tr><td>3</td><td>2</td><td>true</td></tr>
		<tr><td>4</td><td>3</td><td>true</td></tr>
		<tr><td>5</td><td>4</td><td>true</td></tr>
		<tr><td>6</td><td>5</td><td>false</td></tr>
	</table>
</details><br>
		
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

### return vs console.log() vs alert()

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
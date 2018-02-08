/* We declare a function called `reverse` that takes one parameter `arr` */
function reverse(arr){
	/* We instantiate a for loop with `i` starting at 0 and running to */
	/* array length divided by two, and increasing by 1 every iteration */
	for(var i=0; i < arr.length/2; i++){
		/* We declare a variable called `temp` and set it equal to the value */
		/* of `arr` at `arr.length - 1 - i` */
		var temp = arr[arr.length-1-i];
		/* We set the value of the array at `arr.length - 1 - i` to the */
		/* value at `i` */
		arr[arr.length-1-i] = arr[i];
		/* We set the value of the array at `i` to `temp` */
		arr[i] = temp;
	}
	/* After the for loop executes, we return the array `arr` */
	return arr;
}

/* We declare a variable `result` and set it equal to the function reverse */
/* being called with the parameter `arr` equal to [1,2,3,4,5,6] */
var result = reverse([1,2,3,4,5])
/* We console log the variable `result` */
console.log(result);
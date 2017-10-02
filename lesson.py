'''
hypothetical python intro
'''

# let's recap some javascript
# algorith example


function removeDuplicates(array){
	for(var i=1; i<array.length; i++){
		if(array[i] == array[i-1]){
			for(var j=i; j<array.length; j++){
				array[j] == array[j+1];
			}
			array.pop();
			i--;
		}
	}
	return array;
}

# let's get rid of the ugly curly brackets!

function removeDuplicates(array)
	for(var i=1; i<array.length; i++)
		if(array[i] == array[i-1])
			for(var j=i; j<array.length; j++)
				array[j] == array[j+1];
			array.pop();
			i--;
	return array;

# those parenthesis are next

function removeDuplicates(array)
	for var i=1; i<array.length; i++ 
		if array[i] == array[i-1] 
			for var j=i; j<array.length; j++ 
				array[j] == array[j+1];
			array.pop();
			i--;
	return array;

# we don't like semicolons now and we like colons instead

function removeDuplicates(array):
	for var i=1; i<array.length; i++: 
		if array[i] == array[i-1]:
			for var j=i; j<array.length; j++:
				array[j] == array[j+1]:
			array.pop()
			i--
	return array

# let's declare a function with def

def removeDuplicates(array):
	for var i=1; i<array.length; i++: 
		if array[i] == array[i-1]:
			for var j=i; j<array.length; j++:
				array[j] == array[j+1]:
			array.pop()
			i--
	return array

# and rewrite the for loops

def removeDuplicates(array):
	for i in range(1,len(array)): 
		if array[i] == array[i-1]:
			for j in range(i,len(array)):
				array[j] == array[j+1]:
			array.pop()
			i -= 1
	return array
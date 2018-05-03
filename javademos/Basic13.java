import java.util.Arrays;

public class Basic13 {
	public static void main(String[] args){
		// print 1 to 255
		// for ( int i = 1; i<256; i++){
		// 	System.out.println(i);
		// }

		// print odds 1 to 255
		// for (int i = 1; i < 256; i += 2){
		// 	System.out.println(i);
		// }
		// print ints and sum 0 to 255	
			// int sum = 0;
			// for( int i= 0; i <= 255; i++){
			// 	sum+= i;
			// 	System.out.println(i + " " + sum);

			// }

		// iterate and print array
		int[] arr = {12,6,33,-5,16,22,-936};
		// for(Integer val:arr){
		// 	System.out.println(val);
		// }
		// System.out.println(arr);
		// find and print max

		// int max = arr[0];
		// for(int x : arr){
		// 	if(x > max){
		// 		max = x;
		// 	}
		// }
		// System.out.println(max);
 
		// get and print average

		// float sum= 0;
		// float length= arr.length;
		// for (int i= 0; i<length; i++){
		// 	sum += arr[i];
		// }
		// float avg= sum/ length;
		// System.out.println(avg);

		// array with odds

		// int[] odds = new int[128];
		// for(int f = 0, v = 1; f < 128; f++, v+=2 ){
		// 	odds[f] = v;
		// }
		// System.out.println(Arrays.toString(odds));

		// square the values
		// int length = arr.length;
		// for (int i = 0; i<length; i++){
		// 	arr[i] = arr[i]*arr[i];

		// }
		// System.out.println(Arrays.toString(arr));
		// greater than y
		// int y = 7;
		// int count = 0;

		// for (int i =0; i  < arr.length; i++ ){
		// 	if(arr[i] > y){
		// 	count++;
		// 	}	
		// }
		// System.out.println(count);

		// zero out negative values
		for (int i = 0; i < arr.length; i++){
			if(arr[i] < 0){
				arr[i] = 0;
			}
		}
		System.out.println(Arrays.toString(arr));

		// min, max, and average

		// shift array values

		// swap string for array negative values

		// sigma

		// convert farenheit to celcius

		// greater than second

	}
}
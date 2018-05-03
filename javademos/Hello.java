import java.util.ArrayList;
import java.util.Arrays;

public class Hello {
	public static void main(String[] args) {
		String msg = "the message";
		int[] array = {10,11,12,13,14,15,16,17,18,19};
		ArrayList<String> test = new ArrayList<String>();
		for ( int i = 0; i < 10; i++ ){
			System.out.println(array[i]);
			test.add(array[i] + " : " + i);
		}
		System.out.println(Arrays.toString(array));
		System.out.println(test);
	}
}
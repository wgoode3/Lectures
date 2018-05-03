public class Person {
	protected String name;
	private int age;
	protected String personality;

	public Person(String name, int age){
		this.name = name;
		this.age = age;
		this.personality = "cool";
	}

	public Person(String name, int age, String personality){
		this.name = name;
		this.age = age;
		this.personality = personality;
	}

	public void sayHello(){
		System.out.println(this.name + " says hello.");
	}

	public void sayHello(String msg){
		System.out.println(this.name + " says " + msg + ".");
	}

}
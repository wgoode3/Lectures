public class PersonTest {
	public static void main(String[] args){
		Person bob = new Person("Bob", 21);
		bob.sayHello();
		bob.sayHello("I am Stanley");
		bob.personality = "angry";
		System.out.println(bob.personality);

		Wizard megumin = new Wizard("Megumin", 18, "infj", 50);
		megumin.sayHello();
		megumin.explosion();
		megumin.explosion();
		megumin.numberOfWizards();
		Wizard gandolf = new Wizard("Gandalf", 9999, "old", 1000);
		megumin.numberOfWizards();
	}
}